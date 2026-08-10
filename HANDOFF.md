# Project handoff

**Written:** 2026-08-10
**Canonical project:** the Git checkout containing this file; its repository root is `.`
**Status:** Release-complete. Every checker passes, both notebooks execute clean, all three PDFs
are built and visually inspected, the source corpus is normalized, and the repository is
published and in sync with `origin/main`.

Nothing here is blocked on engineering. What remains is listed in section 7 and is either a
scientific limitation that cannot be closed by more computation, or a task that needs a human to
do something outside this repository.

---

## 1. Decisions that must not change

- The modeled room capacity is **60**.
- Confirmatory stochastic analyses use **400 paired seeds**.
- Expanded robustness comes from more draws, distances, variants, trajectories, horizons, and
  integration steps. Not from 1,000 modeled members and not from a blanket 1,000-seed rule.
- The executable model is frozen at
  `c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952`.

Every interpretation decision in `CLAUDE.md` still holds: semantic overlap is not executable
coupling, the recipient resource is opportunity per high-practice potential helper rather than a
tenure cohort, T3 and T11 each have two separable paths, existence and endpoint viability and
closure are different outcomes, and the practice scale is cardinal only inside the model.

Do not restart a completed analysis. Every cache in `research/` is complete and hash-linked to
the frozen model; the Sobol design alone costs about four hours to regenerate.

## 2. What the project now contains

A 25-chapter manuscript in six parts, plus preface and introduction, at 262 pages. A 32-page
paper. A 17-page primer. A technical appendix. The executable model and twenty analysis scripts.
Eighteen hash-linked caches. Two verification notebooks. Seven checkers and builders.

## 3. Verification state

| Command | Result |
|---|---|
| `tools/check_release.py` | 136 checks passed, 0 failed |
| `tools/check_book.py` | 0 failures, 39 warnings |
| `tools/check_chapter.py` on the primer | all clear, 9 long-sentence warnings |
| `tools/check_portability.py` | clear |
| `tools/build_corpus.py --check` | 0 corpus problems |
| `tools/run_notebook.py` | CLEAN, 8 cells, 71 assertions |
| `tools/run_notebook.py --paper` | CLEAN, 10 cells, 95 assertions |
| PDFs | 262 / 32 / 17 pages, 0 blank, 0 margin overflow, no undefined references |

The 39 repetition warnings are overlapping n-grams of one phrase, the registered-set
decomposition, restated in the preface and Chapter 12 because both need it. They are intentional.

The reproduction sequence is in `README.md` and is complete: it now includes
`inventory_model_choices.py` and `summarize_release_gate.py`, whose outputs the release check
requires and which were previously omitted, so a fresh clone could not regenerate everything the
gate demands.

## 4. The two notebooks are different artifacts

The paper notebook used to be byte-identical to the book notebook apart from its title. That
satisfied the release gate mechanically while verifying nothing specific to the paper, and the
release plan's section 3.4 had asked for it to be a real verification or explicitly retired.

It is now a real verification. Beyond everything the book notebook does, it re-derives the paper's
headline tables from the caches and requires every decimal the paper prints, 420 of them, to be
reachable from the model source, a hash-linked cache, or a derivation shown in the notebook. That
is the paper's equivalent of the figure check `check_book.py` performs for the chapters.

If the two notebooks are ever identical again, that is a regression.

## 5. Source corpus

Every source is a directory under `research/incorporated/<ShortAuthor>_<Year>/` holding
`citation.md`, `metadata.json` with rights and provenance URL and per-file SHA-256,
`source_summary.md`, and a vocabulary-only verification index.

**No source document is committed.** This repository is public, several sources are in copyright,
and the public-domain ones are large scans that are not project outputs. `.gitignore` excludes
every `.pdf`, `.txt`, `.djvu` and `.epub` under `research/`. Documents are local working files.
Normalize and rebuild with `python3 tools/build_corpus.py`; audit with `--check`.

Citation checking does not depend on the documents. Each index records the source's vocabulary
and, because a vocabulary set has no word order, which registered subjects the document contains,
decided against the real text at build time and stamped with that file's SHA-256. This was tested
by moving every document out of the tree: all 55 citation-subject pairs still verified.

**Nothing is staged and unread any more.** Both journal articles were obtained by hand on
10 August 2026 and read in full: Pagano et al. (2004) and Greenfield and Tonigan (2013), each now
under `research/incorporated/`. What remains under `research/staged/` is the acquisition report and
metadata, which are provenance rather than evidence.

**Seven sources are held as record only, with no document at any time.** This is a distinct
category from the git-ignored documents, and a verifier should not report either as a missing
source. AAWS pamphlet P-17 and Kurtz (1991) are copyrighted works the project chose never to
store. DeGroot (1974) and the April 1946 *A.A. Grapevine* article were consulted on 10 August 2026
from scans whose posting authorization is unverified, and the project's own rights review directs
that they be cited and quoted within limits rather than archived. Three more were added on
10 August 2026: AAWS *Twelve Steps and Twelve Traditions* (1953), Rohr (2011) and the Kurtz talk
of about 1984. Each record keeps the citation, the rights position, the hash of the copy
consulted, and the passages verified from it.

Rohr (2011) carries the corpus's strongest provenance objection, recorded in its `metadata.json`:
the copy consulted was an unauthorized posting of a current in-print title. It was not retained,
its bibliographic record was confirmed independently, and both claims drawn from it are absence
claims. Confirm any Rohr citation against a lawfully obtained edition before release.

The corpus holds 26 sources. Six arrived on 10 August 2026 after the rest of this file was
written: the April 1946 *A.A. Grapevine* article, which settled a citation problem Chapter 5 had
recorded as unresolvable; DeGroot (1974), which supplies a corpus record for the updating rule
Part Two rests on; the 1939 Big Book text in a 1999 reprint, held but not yet used as claim
support; and, later the same day, three copyrighted works read but never held.

Those three are the substantive change of that day and a reader of this file should know what
they did. *Twelve Steps and Twelve Traditions* (1953) supplied Chapter 8 with the book's own
thesis in Wilson's words and, three pages away, the best objection anyone has made to it: the
elder statesmen, a permanent non-rotating advisory class the commentary endorses, which is exactly
what the aggregation condition forbids. It also disproved the index-pairing conjecture directly,
no Tradition chapter citing its own-numbered Step and no Step chapter using the word Tradition at
all, and corroborated Chapter 17's unity assignment. Rohr (2011) supplied a named holder of the
protective reading of anonymity. The Kurtz talk supplied Chapter 25's closing counterweight.

The model gained the elder-statesman family, `model/part2_influence.py` sections 5b and 5c. The
frozen model was not touched.

## 6. Repository and credentials

`main` is published at `github.com/cmelhauser/nobody-in-charge` and the working tree is clean.
Pushes from an analysis sandbox use a repository-scoped SSH deploy key with write access, stored
as `.git-deploy-key` in the project folder and git-ignored. If it is ever exposed, delete the
deploy key on GitHub and generate a new pair; nothing account-wide is involved.

**History was rewritten once, on 10 August 2026, and force-pushed.** Untracking the copyrighted
Maxwell article and the AA pamphlet stopped them being distributed going forward but left them
reachable at older commits in a public repository. Four blobs were purged from every commit with
`git filter-repo`: the Maxwell PDF and text, and the P-17 PDF and OCR. Every record file survived.
A fresh clone confirms none of the four is reachable, and the commit count is unchanged at twelve.

Two things are worth knowing before doing this again. A checkpoint reference under `refs/codex/`,
which is a bare tree rather than a commit, kept the old blobs alive after the rewrite, and
`git log --name-only` does not traverse a tree reference, so the first verification wrongly
reported success; the check that works is `git rev-list --objects --all`. And GitHub keeps
unreachable objects for a period after a force-push, so an object may still be retrievable by its
exact SHA for a while; ask GitHub Support to run garbage collection if that matters.

A pre-rewrite bundle of the complete history is at `nobody-in-charge-pre-rewrite.bundle` in the
project folder, git-ignored. It is the rollback path. Delete it when you are satisfied.

## 7. What actually remains

**Needs a person, not a computation.** Both remaining items are outside the repository.

1. **The elicitation round.** This is the only outstanding item that could change a conclusion. Part Four rests on a twelve-by-eight matrix one person built, and no
   further computation can test it. The instrument exists and is waiting:
   `research/GOVERNANCE-MATRIX-ELICITATION.md` is a form for a naive second reader, and
   `model/elicitation_compare.py` was written before any form came back, so the analysis is fixed
   in advance. It reports whether a respondent leaves the same five governance rows empty; if they
   leave four or six, Chapter 18 is wrong and says so. This is the highest-value outstanding item
   and it is blocked on recruiting readers.
2. **A representational limitation Greenfield and Tonigan (2013) exposed, which no sensitivity
   analysis here can reach.** The model gives each step one practice level. Their factor analysis
   separates behavioural from spiritual step-work, with different predictors, different time paths,
   and only the spiritual component predicting abstinence. Every perturbation design in this
   project varies the values of the dials; none varies the decision to have one dial per step.
   Testing that would mean a second model, not another screen. Chapter 12 states the objection.

**Unresolved scientific limitations, which are not defects.** No parameter is fitted to
longitudinal AA data and the original calibration fails at 17.80 members and 1.25 experienced
against targets of 45 and 9, un-retuned. The mapping from Traditions to the theorem's assumptions
is a reading of three sentences. Part Four degrades smoothly with disagreement about magnitudes
and is largely gone under structural randomization, where index-pairing fails on all twelve in
40.6 per cent of draws. The recipient and both founder-composition contrasts are unresolved rather
than null. Chapter 14's separation is rare, 7 of 400 endpoint environments. Two Sobol factors sit
at or below the Monte Carlo noise floor and the practice first-order column is withheld. Every
horizon is finite and membership is still moving at 100 years.

## 8. If you change anything

Read `CLAUDE.md` first. Its synchronization rule is the one that matters: a change to the model or
to any public number must be propagated in the same session to the caches, both notebooks, the
manuscript, the appendix, the paper, the primer, the ledgers, the plans, the README, the progress
log, this file, `AGENT_VERIFY.md`, and all three PDFs. Then run the full sequence in `README.md`
and close with `AGENT_VERIFY.md`.
