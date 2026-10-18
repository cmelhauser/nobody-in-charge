# Contributing

This is a single-author research project with an AI writing collaborator (see `ATTRIBUTION.md`). Pull
requests are welcome for corrections, and every one is read by the Human Author before it is merged. Issues
are disabled.

## The flow

`main` is protected: nothing is committed to it directly and it cannot be force-pushed or deleted.
Work on a branch named for what it is for (`docs/`, `fix/`, `ci/`, `model/`), run the local gate, and open
a pull request.

```bash
git checkout -b fix/what-this-is
tools/run_ci_locally.sh
gh pr create --fill
```

`tools/run_ci_locally.sh` runs the same four jobs as CI. The `documents` job runs only after a merge, so
the local run is what closes that gap. Python 3.11 or newer is required; `requirements-dev.txt` is all the
tests need.

## What must not change

- `model/aa_group_model.py` is hash-frozen and is the release identity. It is never edited to make a test
  pass. A change to the model is a different project state and is propagated through every layer listed in
  `CLAUDE.md` ("Synchronization rule").
- No source document is ever committed. Run `python3 tools/build_corpus.py`; do not add a source by hand.
- No claim is made about an individual's recovery, and the project is not affiliated with any fellowship.
- Numbers come from a cache or a notebook, with the design, seed count and interval stated, and prose is
  made to agree with them, not the reverse.

## Style

No em dashes in the author's prose. Chapters have no subheadings or tables in their narrative; tables belong
in The Machinery. `CLAUDE.md` is the full statement of the conventions and `RELEASING.md` of branches,
versions and tags.

## Code

Python under `tools/` and `tests/` must pass `ruff check .` with no `noqa` comments, carry a docstring on
every module, class and function, and keep `tools/` and the canonical model at 100 per cent test coverage
(`python3 -m pytest` enforces it). The analysis scripts under `model/` are frozen: each records its SHA-256
in the cache it produced, so a linter, formatter or comment edit there invalidates hours of computation. Do
not let a tool touch them.
