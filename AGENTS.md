# Agent instructions

The authoritative workspace is the current Git checkout. Treat the repository root as `.` and
use only repository-relative paths in tracked files, commands, notebooks, manifests, and
handoffs.

Before changing the project, read `CLAUDE.md`, `HANDOFF.md`, `plans/RELEASE-GATE-PLAN.md`, and
`AGENT_VERIFY.md`. `README.md` carries the current status and the reproduction sequence.

The release gate is closed and every checker passes. Do not reopen it casually: preserve the
completed caches, which are hash-linked to the frozen model and cost hours to regenerate, and
preserve the source boundary as `research/SOURCES.md` currently states it.

No source document is committed. Sources live in `research/incorporated/<ShortAuthor>_<Year>/`
as records only, and `.gitignore` keeps the documents out. Add or repair a source with
`python3 tools/build_corpus.py`, never by hand.

Run `python3 tools/check_portability.py` before committing, and the full sequence in `README.md`
before claiming a release.
