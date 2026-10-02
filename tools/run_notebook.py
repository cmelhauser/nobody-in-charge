"""Execute a verification notebook end to end, in one process, and write the real outputs
back into the file: model/book-calculations.ipynb by default, the paper's notebook with
--paper, or any notebook given by path.

This exists because for a long time the notebook was maintained cell by cell and never run
as a whole, and a cell that referenced an undefined name sat broken and unnoticed. Running it
is now a one-liner that takes a few seconds.

Exit status is non-zero if any cell raises or any assertion fails, so this can be used as a
gate. Run it before calling any chapter done, alongside tools/check_chapter.py and
tools/check_book.py. --no-write executes without touching the file.

--check executes without touching the file and also fails if the outputs stored in it are not
the ones a fresh run prints. `tools/check_book.py` reads the stored outputs, and on 1 October
2026 the paper notebook's still said the paper prints 451 decimals, ten days after the paper's
count moved to 460 and then 461, because nothing compared them. Text must match exactly and
numbers to a relative 1e-9, since the stored outputs come from one machine and the comparison
runs on others, and a float printed to sixteen digits can differ in its last.

Run:  python3 tools/run_notebook.py [--no-write | --check] [--paper | path/to/notebook.ipynb]
"""
import json, os, sys, io, contextlib, traceback, time, re, math
from itertools import zip_longest

NUMBER = re.compile(r'-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK_NB = os.path.join(ROOT, 'model', 'book-calculations.ipynb')
PAPER_NB = os.path.join(ROOT, 'paper', 'anonymity-as-an-aggregation-condition.ipynb')


def same_output(stored, fresh):
    """Equal text, with every number equal to a relative 1e-9."""
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
            if x != y and not math.isclose(float(x), float(y), rel_tol=1e-9, abs_tol=1e-12):
                return False
    return True


def stale_cells(nb, outs):
    """(cell, first differing stored line, fresh line) for each code cell that is stale."""
    stale = []
    for i, c in enumerate(nb['cells']):
        if c['cell_type'] != 'code':
            continue
        stored = ''.join(''.join(o.get('text', '')) for o in c.get('outputs', []))
        fresh = outs.get(i, '')
        if not same_output(stored, fresh):
            pairs = zip_longest(stored.splitlines(), fresh.splitlines(), fillvalue='')
            first = next(((a, b) for a, b in pairs if not same_output(a, b)), ('', ''))
            stale.append((i, *first))
    return stale


def main(notebook=BOOK_NB, write=True, check=False):
    notebook = os.path.abspath(notebook)
    nb = json.load(open(notebook))
    cwd = os.getcwd()
    os.chdir(os.path.dirname(notebook))
    g = {'__name__': '__main__'}
    outs, errs = {}, []
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
    fails = g.get('FAILURES', [])
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
    stale = stale_cells(nb, outs) if check else []
    for i, was, now in stale:
        print(f'\nCELL {i} STORES STALE OUTPUT:\n    stored: {was}\n    fresh:  {now}')
    if stale:
        print('\nrun it without --check to write the fresh outputs back, and commit them')
    if write and not check and not errs:
        for i, c in enumerate(nb['cells']):
            if c['cell_type'] != 'code':
                continue
            o = outs.get(i, '')
            c['outputs'] = [{'output_type': 'stream', 'name': 'stdout', 'text': [o]}] if o else []
            c['execution_count'] = None
        json.dump(nb, open(notebook, 'w'), indent=1)
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
