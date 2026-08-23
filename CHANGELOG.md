# Changelog

Versioning is explained in `RELEASING.md`. In short: MAJOR means the canonical model hash
changed or a conclusion was reversed, MINOR means new evidence or analysis, PATCH means
corrections and tooling. It stays below 1.0 while the elicitation round is open.

Every entry records the model SHA-256 it was produced with, because every cache in the
repository is keyed to that hash and a number quoted without it cannot be traced.

`research/progress-log.md` is the working record and is far longer. This file exists so that
someone who wants to know what changed between two tags does not have to read it.

## [Unreleased]

## [0.9.0] - 2026-08-18

First tagged state. The manuscript, paper, appendix and primer are complete and every checker
passes; the version is below 1.0 because the elicitation round is open, not because the prose
is unfinished.

Canonical model SHA-256:
`c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952`

**State at this tag**

- 25 manuscript chapters, an academic paper, a technical appendix, a Steps-and-Traditions primer
- 31 corpus sources, 11 held as record only, no source document committed
- 18 hash-linked result caches, complete and matching the current model and script hashes
- 136 release-gate checks passing; 100 tests on Python 3.11, 3.12 and 3.13; 100 per cent
  coverage of the canonical model
- Three PDFs rendering with zero overfull boxes, all fonts embedded

**Added in the run-up to this tag**

- Continuous integration, split so that the checks that need no network run on every push:
  `lint`, `checks` and `documents`
- `tools/check_pdfs.py`, which checks the rendered result rather than the build log
- `tools/run_ci_locally.sh`, which runs all three CI jobs on a local machine
- `check_withheld_names` in `tools/check_book.py`, enforcing by digest that a living person
  named in a source is named nowhere in this project
- Appendix A12, Recovery Dharma read against the model, and A13, the arrival census on the
  1939 and 2001 editions of the Big Book
- Three sources previously carried as unobtainable, read at source after checking whether the
  publisher gives them away: SMF-132, the Twelve Concepts, and *Tricycle* on the 2019 schism

**Corrected**

- The appendix named the founder of a predecessor organisation, against a rule stated in two
  places. The name is gone and a checker now enforces its absence
- Chapter 10's rotation claim narrowed: the Twelve Concepts do hold a proportionality
  principle, but between voting weight and responsibility, not pool and group
- The Rohr provenance objection closed: the Human Author holds a lawful copy

**Open**

The elicitation round, and the items in section 10 of `HANDOFF.md`.

[Unreleased]: https://github.com/cmelhauser/nobody-in-charge/compare/v0.9.0...HEAD
[0.9.0]: https://github.com/cmelhauser/nobody-in-charge/releases/tag/v0.9.0
