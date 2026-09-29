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

- Iannaccone (1992), "Sacrifice and Stigma", is confirmed as read at source, reread on 29 September
  2026 at the Human Author's request. The record had disagreed with itself: Chapter 12 called it
  read, Chapter 2 listed it as cited at a remove, and `research/SOURCES.md` recorded no status.
  - Chapter 2's use of it holds: the screening argument is the paper's own, and the chapter's entry
    moves to "Read in full" with one short quotation checked against the page image.
  - Chapters 12 and 15 credited the paper with the saturation form of the participatory resources.
    It supplies the premise, group quality strictly concave in members' average participation and
    group size, and its worked example is linear; the capped c / (c + k) form is this book's. Both
    chapters now say so, and the paper's reference gains its read status.
  - The only full text found online is a JSTOR download reposted on a third party's archive without
    verified authorization, so the source is catalogued as record only, like DeGroot (1974), with
    the hash of the copy consulted. The corpus holds 45 sources, six of them record only.
  - The book's draft date moves to 29 September 2026 because its text changed.

- The paper's title page is dated September 2026, since its text last changed on 28 September.
  Making that change turned up five stale statements the 28 September sweep missed, because they
  were worded as "has not read" or "remains" rather than "not obtained". The paper's abstract and
  Chapter 1 said the project had not read the service document that estimates AA's membership;
  SMF-132 was read on 17 August 2026, so both now give the real reason no present count is stated:
  AA keeps no membership lists and the table read stops at 2020. Chapter 4's notes opened by saying
  the chapter rests on a work not yet obtained, which Kurtz ceased to be on 2 August. The paper and
  appendix A9 still described `research/staged/` as holding unread articles or a next-round corpus;
  both articles were read on 10 August and what remains there is provenance. The release gate's
  label for its check of that directory is reworded to match, with the condition unchanged.

- The working manuscript's seven remaining suggested uses are drafted, one commit each so that any
  can be dropped:
  - Chapter 5, the 1939 Foreword and the Foundation page;
  - Chapters 7 and 9, how the first book was settled;
  - Chapter 18, the protective tier's precursors;
  - Chapter 15, helping and its cost;
  - Chapter 19, the membership rule;
  - Chapter 22, the founders' answer to the composition question;
  - Chapters 24 and 21, the 1939 meeting sizes, as a check on the room capacity and not on the
    endpoint.

  Each is an illustration rather than a test of the model, and every quotation was checked against
  the page images. Chapters 21 and 24 now record that SMF-132 was read and is held.
- Five background papers the paper cites are read in full at PubMed Central: Banks et al. (2017),
  Gorman et al. (2006), Kelly, Humphreys and Ferri (2020), Rynes and Tonigan (2012) and Witkiewitz
  and Marlatt (2007).
  - `research/SOURCES.md`, Chapter 14's references and the paper's bibliography record them as
    read, and Banks et al. (2014) as cited at a remove.
  - Four citations gain a subtitle or an issue number, checked against Crossref.
  - The summaries supplied in place of the articles were not filed, and no copy is held.
  - Four statements the reading found out of step with their sources are corrected, at the Human
    Author's direction:
    - the paper's summary of the Cochrane review;
    - its account of the mechanism literature, which now reports Rynes and Tonigan (2012) as a
      dissent;
    - its description of Gorman et al. (2006);
    - Chapter 14's account of the warrant for its older strand.
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

- Copies of two papers the paper cites and had read but could not hold, bringing the corpus to 44:
  Banks et al. (2017) and Rynes and Tonigan (2012), both NIH author manuscripts read at PubMed
  Central on 14 September 2026. The record then said every scripted route refuses, which was half
  right: the PDF routes do refuse, and PMC's serves a proof-of-work interstitial this project does
  not attempt, but the deposited full text is served by the NCBI E-utilities API. Three of the five
  papers in that position return metadata only and still need a copy saved by hand. No read status
  or claim changes.
- Two sources that bracket the decay rate, held git-ignored and read in full on 22 September 2026,
  bringing the corpus to 42: Edgren, Baretta and Inauen (2025) on habit decay in daily life, open
  access under CC BY 4.0, and Kaskutas, Bond and Avalos (2009) on seven-year trajectories of AA
  attendance, as the NIH author manuscript. Neither is held as a PDF, because the publisher and
  PubMed Central download routes are behind bot checks this project does not attempt; the held copy
  of each is the deposited full text rendered to plain text.
  - Chapter 12 now says the rate is bracketed rather than merely untested: deliberate habit
    degradation settles in a median of 9 to 10 days, an order of magnitude faster, while measuring
    the opposite case; skill depreciation is one to two orders of magnitude slower; and
    participation in AA itself falls away over years without abstinence following it down.
  - The paper's limitation item, appendix A11 item 9, the primer's "what was not read" entry and
    `research/PARAMETERS.md` follow it. Chapter 24 adds the design consequence: a study testing the
    ordering must record practice rather than attendance, because attendance fell away in three of
    the four AA trajectories while abstinence did not follow it down. No model value or released
    number changes.
- `research/DECAY-RATE-LITERATURE-SCAN.md`, the search behind that reading, which `HANDOFF.md` had
  carried as unsearched since the skill papers were read.
- `research/elicitation/5-invitation-email.md`, the message to send a prospective respondent: three
  subject lines, the email, a short version for a message, the longer version for someone who asks
  what they are contributing to, answers to the questions respondents actually ask, a nudge and a
  thank-you. It describes neither the argument nor which rows the book leaves empty, and it adds
  the one instruction the packet lacked, that respondents should not compare notes until every form
  is back. `0-start-here` lists it, and `build.sh` now falls back to tectonic where xelatex is
  absent.
- `model/decay_reversal.py` and `research/decay_reversal.json`: the same design at 10, 15 and 20
  per cent lower decay, 400 paired seeds per cell, 3,600 runs, model `c3823f72`. It locates the
  membership reversal `decay_ordering.json` left unlocated: the ordering holds at 10 and 15 per
  cent lower, at 10.92 members [10.18, 11.66] and 6.35 [5.03, 7.68], and is reversed at 20 per
  cent lower, at -2.79 [-4.77, -0.81], while endpoint viability and existence are reversed in no
  paired run at any of the three. The two caches are read as one seven-level series, which a test
  enforces by comparing the scripts with the docstring and the level list removed. Registered in
  the release gate, now 148 checks, 142 of them under `--skip-artifacts`, in both notebooks and in
  `research/ROBUSTNESS-RESULTS.md`; Chapters 1, 4, 12 and 24, appendix A7.5 and A11, the paper, the
  primer and `research/PARAMETERS.md` report it. No released number changes.
- `model/decay_ordering.py` and `research/decay_ordering.json`: the referral-versus-attraction
  ordering at the default decay rate and at 25, 50 and 75 per cent lower, 400 paired seeds per
  cell, 4,800 runs, model `c3823f72`. It confirms the one-at-a-time screen's membership reversals
  and finds the ordering still holds on endpoint viability and existence at 25 per cent lower.
  Registered in the release gate, now 142 checks, 136 of them run under `--skip-artifacts`, in both
  notebooks and in `research/ROBUSTNESS-RESULTS.md`; Chapters 1, 4, 12 and 24, appendix A7 and
  A11, the paper, the primer and `research/PARAMETERS.md` report it. No released number changes.
- Tests that compare generated files with what generates them: both notebooks are executed, their
  code and `research/ROBUSTNESS-RESULTS.md` are compared with their generators, and three cells of
  `research/decay_ordering.json` are recomputed from its script. Continuous integration had never
  executed the notebooks.
- Seven open-access papers held git-ignored: five the paper cites (Angrist 2014,
  Cunha and Heckman 2007, Cunha, Heckman and Schennach 2010, Hu and Schennach 2008, Lembke n.d.)
  and two from the skill-depreciation literature Chapter 12 has not consulted (Dinerstein,
  Megalokonomou and Yannelis; Cohen, Johnston and Lindner), bringing the corpus to 40 sources.

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

- `--help` now prints each tool's usage and exits. Only the argparse tool answered it before; the
  other sixteen ran, and several wrote files. `tools/run_ci_locally.sh` also answers `--help` and
  refuses an unknown job, which used to run nothing and still print "local CI clear". The
  docstrings `--help` shows were checked against the code, and six were wrong or incomplete. A
  test runs every tool with `--help` and fails if the tree changes.
- The README built the paper with `latexmk -pdf` from the repository root, which writes the PDF to
  the root and leaves `paper/`'s untouched; it now builds as `CLAUDE.md`, the handoff and CI do.
  The P-17 README still said the pamphlet was not held, the corpus README described every source
  as a PDF with text, the staged package's agent instructions pointed at a directory that no
  longer exists, and `AGENT_VERIFY.md` and one CI comment described `check_docs.py` as checking
  counts only. All are corrected. Test coverage of the canonical model remains 100 per cent.

- The drift found by hand between 24 and 29 September 2026 is now caught by tools, each check made
  to fail on the actual defect before being trusted:
  - `check_chapter.py` fails on an entry marked read in full or at source that sits under any
    other reference heading; on the pre-sweep chapters it flags all six misfiled entries.
  - `build_corpus.py --check` fails when a record-only source holds a document, or a summary opens
    "Record only" for a source that is not; it flags the Kurtz talk's summary as it stood.
  - `check_docs.py` fails when the paper's `\date` month is older than its last change, and when
    `HANDOFF.md` is dated before the newest progress-log entry, which is the handoff's own rule.
    It runs 25 checks.
  - A test keeps the paper's reference list in first-author and year order.
- Rebuilding no longer dirties the tree. TeX stamps the clock into every PDF and the model-choice
  inventory stamped it into `created_utc`, so each local CI run left four committed files modified
  with nothing in them changed. `tools/source_date.py` gives each build a fixed timestamp from the
  date its document declares, and all three PDFs now rebuild byte-identically; the inventory keeps
  its stamp while its content is unchanged.
- `check_book.py` pooled nothing across directories that share a token, such as the three ATU
  reports and the two Big Book editions: each overwrote the one before, so a citation was checked
  against whichever sorted last. They are now pooled. No current citation was affected.

- A sweep before the elicitation round found twenty-odd statements the tree had outgrown, none
  caught by a checker because each was a reference status or a sentence rather than a count.
  - Five chapter references read in full were still filed under "Cited at a remove": Blair and
    Fehlandt in Chapter 2, the April 1946 *Grapevine* article in Chapter 5, Greenfield and Tonigan
    in Chapters 13 and 24, and Pagano et al. in Chapter 15. Each now sits under "Read in full".
  - Chapter 12 still said the lapse literature was never searched, and Chapters 16 and 25 that the
    Twelve Concepts and the service manual had never been opened. Chapter 16 now reports a search
    of both held texts, which finds no sentence pairing a Step with the same-numbered Tradition.
  - The paper listed Pagano et al. (2004) as unread and at a remove, called the *Twelve Steps and
    Twelve Traditions* a record with no document, said the service pamphlets were unobtained, and
    listed the lapse literature as unread.
  - Appendix A13's reference list said the 2001 Big Book was not held and its census not
    attempted, which A13.7 has done since 17 August.
  - The summaries for the Kurtz talk and the *Twelve Steps and Twelve Traditions* still said
    "Record only. No document is stored at any time", and `research/SOURCES.md` still said no copy
    of the latter was held and counted twenty-eight sources holding a document where there are
    thirty-nine.
  - `CLAUDE.md` and `HANDOFF.md` described a heading rule the chapter checker contradicts: three
    reference headings are required in every chapter, and nine carry "Nothing.". Both now state
    the rule the checker enforces.
  - `AGENT_VERIFY.md` quoted the no-documents citation check at 18 indexed sources; rerun with all
    64 documents set aside, it is 55 pairs across 38. `HANDOFF.md` was dated 15 September, which by
    its own rule marked it stale against the progress log. `AGENTS.md` still listed working
    manuscript corrections as outstanding, and the release-gate plan dated a 148-check gate to 9
    August.

  - The paper's reference list had six entries out of alphabetical order, one of them Edgren,
    placed before Eddy on 22 September. It is now sorted by first author and then year, with no
    entry's text changed.

  The book's draft date moves to 28 September 2026 because its text changed. The comparison
  script's SHA-256 is recorded in `HANDOFF.md` section 9 at the start of the round.

- The book and the primer dated themselves from the clock. Both builders took the printed date
  from `date.today()`, and continuous integration rebuilds both on every push to `main`, so the
  date recorded when a machine last ran pandoc rather than when the text last changed; a rebuild
  that changed nothing still moved it. Both are now declared, `DRAFT_DATE` in
  `tools/build_book.py` and `REVISED_DATE` in `tools/build_primer.py`, and `tools/check_docs.py`
  enforces each in both directions: the rendered artifact must carry the declared date, and the
  declared date must not be older than the newest commit touching the sources the document is made
  from. The builders themselves are not among those sources, because tidying an assembler is not
  changing the text. The primer's clock-derived date had been a deliberate fix for a hard-coded
  date that went stale unnoticed; what was missing then was a checker, which now exists.
  `check_docs.py` runs 23 checks. The comparison against Git is skipped, and says so, in a shallow
  clone, which is what continuous integration checks out: there the only commit is a merge GitHub
  synthesises on the day the job runs, so every source appears to have changed that day. It runs
  wherever the history is whole, including `tools/run_ci_locally.sh`, and ignores merge commits,
  which record when branches met rather than when the text changed.

- The published Git history is rewritten to remove what the personal-information pass found in it:
  the withheld name, host paths from the initial import, four source documents, and a second
  personal email address in commit metadata.
  - Every current file and every commit message is unchanged.
  - Every commit hash has changed, so a clone made earlier must be re-cloned.
  - `v0.9.0` now points at the rewritten commit, and its release assets are unchanged.
- The surname of the founder this project never names was in the committed vocabularies of two
  verification indexes, `RecoveryDharma_2023` and `Rohr_2011`, because `tools/check_book.py`
  enforced the rule over a fixed list of prose files. The changes:
  - The digests moved to `tools/withheld.py`, whose test also catches possessives and compounds.
  - `tools/build_corpus.py` leaves a withheld word out of every index, and `--check` reports one.
  - `check_book.py` scans every tracked text file, and `tools/check_pdfs.py` scans the text of
    each rendered PDF.
  - Each index lost that one word and nothing else.
- Ben-Porath (1967) was recorded in `research/SOURCES.md` with no read status and listed by
  Chapter 14 as cited at a remove, while Chapter 12 said it was read at source. The Human Author
  confirmed Chapter 12; the ledger, Chapter 14 and the paper's bibliography now agree.
- `tools/check_release.py --skip-artifacts` counted its own skip notice as a passed check, and
  the gate's comment, `CLAUDE.md`, `AGENT_VERIFY.md` and both workflows said the flag omits seven
  checks. It omits six, whether each of the three rendered PDFs exists and is newer than its
  sources, and now reports them as skipped: 136 passed and 6 skipped, where it printed 137 passed.
- Appendix A13 counted twenty-nine personal stories in the 1939 edition; its contents page lists
  thirty. A13, the primer and the source records now say thirty, and A13 says its census covers the
  twenty-six stories the automatic split recovered. No census figure changes.
- Chapter 4 said the 1939 comment round softened "you must" to "we ought". The working manuscript
  shows a change of speaker from "you" to "we" that mostly keeps the modal, and the paragraph now
  says so, with each quotation checked against the page images.
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
