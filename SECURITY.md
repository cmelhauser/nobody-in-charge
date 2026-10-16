# Security and sensitive-content policy

This is a research repository. It has no running service, no user accounts and no credentials, so the
things worth reporting are about content rather than code.

## What to report

- A secret or key committed by mistake.
- A source document committed by mistake. No source document is meant to be tracked: every file under
  `research/incorporated/` and `research/staged/` that is a PDF, text, DjVu or EPUB file is git-ignored on
  purpose, and the rights position of each source is in its `metadata.json`.
- Personal information about a living person, or anything that identifies an early or current member of a
  fellowship beyond the initials the project uses.
- The name the project has undertaken not to print (see `CLAUDE.md`, "Source boundary"). If you find it,
  say where (file and line) and do not repeat it in the report.
- A flaw in a check, workflow or pinned download that would let a wrong result pass or let untrusted code run.

## How to report

Issues are disabled on this repository. Write to the Human Author at the address in `ATTRIBUTION.md`,
with the file path and, if you can, the commit. Please do not open a public pull request that repeats
the sensitive content. You will get a reply, and a fix goes through the normal pull-request flow described
in `CONTRIBUTING.md`; history is not rewritten without a reason, because every hash in a published citation
would change.

## Supported versions

Only the latest commit on `main` and the latest tag are maintained.

## Known exposure

`research/progress-log.md` and `research/SOURCES.md` record one: a 2025 NIH author manuscript
(Fatimah, Hunter and Bornovalova) was committed in the first import of 6 August 2026 and removed on
10 August 2026 (`39725c9`). It remains in git history. Nothing else that is in copyright is in the history.
