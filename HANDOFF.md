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

A 25-chapter manuscript in six parts, plus preface and introduction, at 261 pages. A 32-page
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
| PDFs | 261 / 32 / 17 pages, 0 blank, 0 margin overflow, no undefined references |

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

AA pamphlet P-17 is cited but has no document here at all, by decision. Keep the citation, the
aa.org URL and the file hash; do not restore the PDF or its OCR.

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

**Needs a person, not a computation.**

1. **The elicitation round.** Part Four rests on a twelve-by-eight matrix one person built, and no
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
