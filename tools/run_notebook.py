"""Execute a verification notebook end to end, in one process, and write the real outputs
back into the file: model/book-calculations.ipynb by default, the paper's notebook with
--paper, or any notebook given by path.

This exists because for a long time the notebook was maintained cell by cell and never run
as a whole, and a cell that referenced an undefined name sat broken and unnoticed. Running it
is now a one-liner that takes a few seconds.

Exit status is non-zero if any cell raises or any assertion fails, so this can be used as a
gate. Run it before calling any chapter done, alongside tools/check_chapter.py and
tools/check_book.py. --no-write executes without touching the file.

Run:  python3 tools/run_notebook.py [--no-write] [--paper | path/to/notebook.ipynb]
"""
import json, os, sys, io, contextlib, traceback, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK_NB = os.path.join(ROOT, 'model', 'book-calculations.ipynb')
PAPER_NB = os.path.join(ROOT, 'paper', 'anonymity-as-an-aggregation-condition.ipynb')


def main(notebook=BOOK_NB, write=True):
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
    if write and not errs:
        for i, c in enumerate(nb['cells']):
            if c['cell_type'] != 'code':
                continue
            o = outs.get(i, '')
            c['outputs'] = [{'output_type': 'stream', 'name': 'stdout', 'text': [o]}] if o else []
            c['execution_count'] = None
        json.dump(nb, open(notebook, 'w'), indent=1)
        print('outputs written back')
    ok = not errs and not fails and not blank
    print('CLEAN' if ok else 'NOT CLEAN')
    return 0 if ok else 1


if __name__ == '__main__':
    from tool_help import help_requested
    help_requested(__doc__)
    args = sys.argv[1:]
    write = '--no-write' not in args
    args = [arg for arg in args if arg != '--no-write']
    if '--paper' in args:
        notebook = PAPER_NB
        args.remove('--paper')
    elif args:
        notebook = args[0] if os.path.isabs(args[0]) else os.path.join(ROOT, args[0])
    else:
        notebook = BOOK_NB
    sys.exit(main(notebook=notebook, write=write))
