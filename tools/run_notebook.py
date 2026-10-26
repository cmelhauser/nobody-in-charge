"""Execute a verification notebook end to end and write the real outputs back into it.

The notebook runs in one process, cell by cell, with a shared namespace: the book's
model/book-calculations.ipynb by default, the paper's notebook with --paper, or any
notebook given by path (relative paths are taken from the repository root).

This exists because for a long time the notebook was maintained cell by cell and never run
as a whole, and a cell that referenced an undefined name sat broken and unnoticed. Running it
is now a one-liner that takes a few seconds.

Exit status is non-zero if any cell raises or any assertion fails, so this can be used as a
gate. Run it before calling any chapter done, alongside tools/check_chapter.py and
tools/check_book.py. --no-write executes without touching the file.

--check executes without touching the file and also fails if the outputs stored in it are not
the ones a fresh run prints. `tools/check_book.py` reads the stored outputs, and on 1 October
2026 the paper notebook's still said the paper prints 451 decimals, ten days after the paper's
count moved to 460 and then 461, because nothing compared them.

The comparison asks for agreement to the precision printed, which is the standard
`AGENT_VERIFY.md` sets for reproduction on another machine. Text must match exactly, and so must
a whole number, since those are counts. A decimal may differ by one unit in its last printed
place, and a float printed at full length by a relative 1e-9. The stored outputs come from one
machine and the tests run on others, and that is not hypothetical: the DeGroot example's third
round averages to 5.74275, which a last-bit difference in a matrix product prints as 5.7428 on
one machine and 5.7427 on another.

Reads the notebook and, when it is allowed to write, rewrites that one file in place with
each code cell's stdout as its stored output. Cells run with the working directory set to the
notebook's own directory, and it is restored afterwards. Nothing is written when a cell
raised, so a broken notebook never overwrites good stored outputs.

Exit status: 0 when the run is CLEAN (no cell raised, no recorded assertion failure, no code
cell without output, and under --check no stale stored output), 1 otherwise.

Run:  python3 tools/run_notebook.py [--no-write | --check] [--paper | path/to/notebook.ipynb]
"""
import contextlib
import io
import json
import math
import os
import re
import sys
import time
import traceback
from itertools import zip_longest
from typing import Any

NUMBER = re.compile(r'-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK_NB = os.path.join(ROOT, 'model', 'book-calculations.ipynb')
PAPER_NB = os.path.join(ROOT, 'paper', 'anonymity-as-an-aggregation-condition.ipynb')


def same_number(x: str, y: str) -> bool:
    """Return True if two printed numbers (given as strings) agree to the precision printed.

    Whole numbers must match exactly, since they are counts. Otherwise a decimal may differ by
    one unit in its last printed place (the longer of the two spellings sets the place), and
    anything else, such as a float printed at full length, by a relative 1e-9.
    """
    if x == y:
        return True
    if not any(mark in x + y for mark in '.eE'):
        return False
    places = max(len(s.split('.')[1]) if '.' in s and not set('eE') & set(s) else 0
                 for s in (x, y))
    a, b = float(x), float(y)
    if places and abs(a - b) <= 10.0 ** -places * 1.000001:
        return True
    return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-12)


def same_output(stored: str, fresh: str) -> bool:
    """Return True if two outputs are equal text, with every number equal per same_number.

    Numbers are masked out and the remaining text compared first, so a changed word or a
    different count of numbers on a line is never excused by the numeric tolerance.
    """
    if stored == fresh:
        return True
    old, new = stored.splitlines(), fresh.splitlines()
    if len(old) != len(new):
        return False
    for a, b in zip(old, new, strict=True):
        # NUL cannot occur in printed output, so equal masks mean equally many numbers.
        if NUMBER.sub('\0', a) != NUMBER.sub('\0', b):
            return False
        for x, y in zip(NUMBER.findall(a), NUMBER.findall(b), strict=True):
            if not same_number(x, y):
                return False
    return True


def stale_lines(nb: dict[str, Any], outs: dict[int, str]) -> list[tuple[int, str, str]]:
    """Return (cell index, stored line, fresh line) for every line a fresh run prints differently.

    `nb` is the parsed notebook and `outs` maps cell index to the stdout the run just produced.
    Cells whose stored and fresh outputs agree under same_output contribute nothing.
    """
    stale = []
    for i, c in enumerate(nb['cells']):
        if c['cell_type'] != 'code':
            continue
        stored = ''.join(''.join(o.get('text', '')) for o in c.get('outputs', []))
        fresh = outs.get(i, '')
        if not same_output(stored, fresh):
            pairs = zip_longest(stored.splitlines(), fresh.splitlines(), fillvalue='')
            stale += [(i, a, b) for a, b in pairs if not same_output(a, b)]
    return stale


def main(notebook: str = BOOK_NB, write: bool = True, check: bool = False) -> int:
    """Execute `notebook`, report problems, optionally write outputs back; return 0 or 1.

    All code cells run in one shared namespace (`g`), in order, so a later cell can use an
    earlier one's names, as in Jupyter. A cell that raises is recorded and the run goes on,
    so one run lists every broken cell. `write=False` (--no-write) or `check=True` (--check)
    leaves the file untouched; `check` also compares the stored outputs with the fresh ones.
    Outputs are only written back when no cell raised, and an assertion failure alone (a
    recorded FAILURES entry) still writes them, so the failure is visible in the file.
    """
    notebook = os.path.abspath(notebook)
    with open(notebook, encoding="utf-8") as fh:
        nb = json.load(fh)
    cwd = os.getcwd()
    os.chdir(os.path.dirname(notebook))
    g: dict[str, Any] = {'__name__': '__main__'}
    outs: dict[int, str] = {}
    errs: list[tuple[int, str]] = []
    t0 = time.time()
    try:
        for i, c in enumerate(nb['cells']):
            if c['cell_type'] != 'code':
                continue
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    exec(compile(''.join(c['source']), f'cell{i}', 'exec'), g)
                outs[i] = buf.getvalue()
            except Exception:
                outs[i] = buf.getvalue()
                errs.append((i, traceback.format_exc()[-900:]))
    finally:
        os.chdir(cwd)
    fails: list[Any] = g.get('FAILURES', [])
    nchk = sum(o.count('  OK ') + o.count('  FAIL') for o in outs.values())
    print(f'{len(outs)} code cells run in {time.time()-t0:.1f}s, {nchk} assertions')
    for i, tb in errs:
        print(f'\nCELL {i} RAISED:\n{tb}')
    if fails:
        print(f'\n{len(fails)} ASSERTION FAILURES:')
        for f in fails:
            print('   ', f)
    blank = [i for i, o in outs.items() if not o.strip()]
    if blank:
        print(f'\ncells producing NO output: {blank}')
    stale = stale_lines(nb, outs) if check else []
    for i, was, now in stale:
        print(f'\nCELL {i} STORES STALE OUTPUT:\n    stored: {was}\n    fresh:  {now}')
    if stale:
        print(f'\n{len(stale)} stale line(s); run it without --check to write the fresh outputs '
              'back, and commit them')
    if write and not check and not errs:
        for i, c in enumerate(nb['cells']):
            if c['cell_type'] != 'code':
                continue
            o = outs.get(i, '')
            c['outputs'] = [{'output_type': 'stream', 'name': 'stdout', 'text': [o]}] if o else []
            c['execution_count'] = None
        with open(notebook, 'w', encoding='utf-8') as fh:
            json.dump(nb, fh, indent=1)
        print('outputs written back')
    ok = not errs and not fails and not blank and not stale
    print('CLEAN' if ok else 'NOT CLEAN')
    return 0 if ok else 1


if __name__ == '__main__':
    from tool_help import help_requested
    help_requested(__doc__)
    args = sys.argv[1:]
    write = '--no-write' not in args
    check = '--check' in args
    args = [arg for arg in args if arg not in ('--no-write', '--check')]
    if '--paper' in args:
        notebook = PAPER_NB
        args.remove('--paper')
    elif args:
        notebook = args[0] if os.path.isabs(args[0]) else os.path.join(ROOT, args[0])
    else:
        notebook = BOOK_NB
    sys.exit(main(notebook=notebook, write=write, check=check))
