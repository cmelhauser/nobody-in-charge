# Changelog

Versioning is explained in `RELEASING.md`. In short: MAJOR means the canonical model hash
changed or a conclusion was reversed, MINOR means new evidence or analysis, PATCH means
corrections and tooling. It stays below 1.0 while the elicitation round is open.

Every entry records the model SHA-256 it was produced with, because every cache in the
repository is keyed to that hash and a number quoted without it cannot be traced.

`research/progress-log.md` is the working record and is far longer. This file exists so that
someone who wants to know what changed between two tags does not have to read it.

## [Unreleased]

### Changed

- Continuous integration now splits `unit-tests` from `checkers`, so version-independent
  checkers run once on Python 3.12 instead of once per matrix cell. Pull requests test on
  3.12 only; `main` still runs 3.11, 3.12 and 3.13. The lint job uses `shellcheck-py` from
  pip rather than an apt package.
- Five held sources that had been read only in part are now read in full: the three American
  Temperance Union documents, Gough's 1869 autobiography, and the meditations and inquiry
  questions of *Recovery Dharma*. Nothing in the manuscript changes. `research/SOURCES.md`
  records what the full reading found, including the Sons of Temperance's own 1848 count of
  members who broke the pledge, verified against the page image.
- Appendix A12, the primer's Recovery Dharma entry and Chapters 1 and 2 now state the read scope
  `research/SOURCES.md` records, and the book and primer PDFs are rebuilt. Chapter 2's list of
  unread sources also named Krout, Harrison, Marsh and Eddy, all long since read at source.
- The seven papers held on 13 September 2026 are read, six in full and one in part, and what they
  bear on is applied. Chapter 12 sets the decay rate of six per cent a week against the two
  skill-depreciation papers, which find rates one to two orders of magnitude slower for skill, and
  states how much of the book rides on it; Chapters 1 and 24 note that large downward moves of it
  reverse the referral-versus-attraction ordering in the one-at-a-time screen. Chapter 13 adds
  Cunha, Heckman and Schennach's sign-changing estimate as an analogy, and Chapters 2 and 15 use
  Lembke. The paper, primer, appendix A11 and `research/PARAMETERS.md` follow, and the book, paper
  and primer PDFs are rebuilt. The canonical model is unchanged.

### Added

- Seven open-access papers held git-ignored: five the paper cites (Angrist 2014,
  Cunha and Heckman 2007, Cunha, Heckman and Schennach 2010, Hu and Schennach 2008, Lembke n.d.)
  and two from the skill-depreciation literature Chapter 12 has not consulted (Dinerstein,
  Megalokonomou and Yannelis; Cohen, Johnston and Lindner). The corpus holds 40 sources.

- Copies of six sources that were record only, held git-ignored at the Human Author's direction:
  P-17, SMF-132 and the short-form Concepts, byte-identical to the files read in August; the
  *Twelve Steps and Twelve Traditions* and the 2001 Big Book, assembled from aa.org's
  per-chapter PDFs; and the Kurtz talk in the Human Author's own transcription.
- `ServiceManual_2024`, the 2024-26 *A.A. Service Manual* with Bill W.'s full Twelve Concepts,
  which AAWS posts free. Its Concept IV essay holds no rule on the size of a rotating pool,
  which closes the Concept 4 item in `HANDOFF.md` section 10.
- `WorkingManuscript_1939`: Hazelden's 2010 facsimile of the annotated 1939 multilith, read on
  every page and held as a git-ignored reading copy at the Human Author's direction, with a
  written account of the edits and where they bear on the manuscript. It changes no model
  number, cache or release check. It implies a correction to Chapter 4 and a recount in
  Appendix A13, both recorded in `HANDOFF.md` section 10 and neither yet made.
- `tools/build_note.py`, which typesets that account to
  `build/WorkingManuscript_1939-edits-and-suggested-uses.pdf` with the primer's typography. The
  PDF is a reading copy, not a release artifact, and the release gate does not check it.
- `tools/check_docs.py`, which re-derives the counts this repository states about itself and
  fails when prose disagrees with the tree: CI jobs, checkers, corpus size and record-only
  status, analysis scripts, chapters, relative links, the model hash, and the rendered page
  counts. It exists because the 24 August 2026 sweep found that every stale claim in the
  documentation was a count a tool could have checked and nothing did.

### Fixed

- Three attributions to Cunha, Heckman and Schennach: the book's rho is their phi, Chapter 12's
  "multiplicative production of a stage" is a CES in their papers, and Chapter 13's "and solve it"
  overstated their claim. Chapter 14 also credited them with a depreciation structure their
  technology does not have; it is Ben-Porath's.
- `tools/build_book.py`, the preface and the appendix still named the Human Author, so a rebuild
  put the name back into a book that had been anonymized by hand. All three now say the book is by
  an anonymous author, and the committed PDFs are rebuilt from source.
- The record of the `lint` job, `check_pdfs.py` and `BigBook_2001`, none of which had been
  propagated into the documents that count them. Totals were right and enumerations were short.
- `HANDOFF.md` built the primer with a bare `pandoc` call, which `README.md` says is not the
  release artifact; it now calls `tools/build_primer.py`.
- `CITATION.cff` carried no version and a release date preceding the tag.

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
- `tools/run_ci_locally.sh`, added to mirror the CI workflow on a local machine
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

**Published**

As a GitHub [pre-release](https://github.com/cmelhauser/nobody-in-charge/releases/tag/v0.9.0)
on 23 August 2026, with the three rendered PDFs attached, verified byte-identical to the files
at this tag.

**Open**

The elicitation round, and the items in section 10 of `HANDOFF.md`.

[Unreleased]: https://github.com/cmelhauser/nobody-in-charge/compare/v0.9.0...HEAD
[0.9.0]: https://github.com/cmelhauser/nobody-in-charge/releases/tag/v0.9.0
