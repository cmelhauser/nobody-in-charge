# Agent instructions

The authoritative workspace is the current Git checkout. Treat the repository root as `.` and
use only repository-relative paths in tracked files, commands, notebooks, manifests, and
handoffs.

Before changing the project, read `CLAUDE.md`, `HANDOFF.md`,
`plans/RELEASE-GATE-PLAN.md`, and `AGENT_VERIFY.md`. Resume from the checkpoint in
`HANDOFF.md`; preserve completed caches and the deferred-source boundary. Run
`python3 tools/check_portability.py` before committing.
