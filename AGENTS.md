# Agent instructions

Entry point for any agent working on this repository: Cursor, Codex, Claude, or a human. Read
this file first. `CLAUDE.md` is the long form of the same rules and is authoritative where the
two overlap; nothing here contradicts it.

## What this project is

A finished book-length research project. A 25-chapter manuscript, an academic paper, a technical
appendix, a Steps-and-Traditions primer, an executable agent-based model, nineteen analysis
scripts, eighteen hash-linked result caches, two verification notebooks, and six checkers:
`check_book.py`, `check_chapter.py`, `check_portability.py`, `check_release.py`,
`check_pdfs.py`, and `build_corpus.py --check`. Every count here is countable from the tree, and
the cache count is the gate's own required list in `tools/check_release.py`.

It argues that three of Alcoholics Anonymous's Twelve Traditions implement a formal condition,
proved by Golub and Jackson in 2010, for when a group that decides by discussion can be trusted
to be right. It is unpublished. The Human Author is Christopher Melhauser
(`christopher.melhauser@gmail.com`); the AI Writing Collaborator is theonlymuffinbot
(`theonlymuffinbot@outlook.com`), using a mix of Anthropic Claude Opus 5 and OpenAI GPT-5.6 Sol
and Terra models. See `ATTRIBUTION.md` and `LICENSE`.

**The release gate is closed and every checker passes.** Treat the current state as correct until
a checker says otherwise. Your job is almost certainly not to re-derive anything.

## Ground rules

1. **Do not edit `model/aa_group_model.py`.** It is frozen at SHA-256
   `c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952`. Every cache records that
   hash and `tools/check_release.py` fails closed if it changes. If you believe there is a genuine
   defect, say so and stop; do not fix it silently.
2. **Do not edit an analysis script under `model/` whose cache exists.** Caches record the script
   hash too. Editing the script invalidates the cache and the gate fails. Regenerating the Sobol
   design alone costs about four hours.
3. **Do not restart a completed analysis.** All eighteen caches are complete and hash-current.
4. **Do not commit a source document.** No PDF or extracted text belongs in git. See below.
5. **Do not weaken a checker to make it pass.** The checkers have caught real errors, including a
   misprinted number that had survived every human read. If one fails, the finding is usually
   real.
6. **Nothing in this project may be written as advice about an individual's recovery.**
7. **Do not edit `model/elicitation_compare.py`.** It is a preregistered analysis, written before
   any respondent form came back. If it genuinely needs a change, make it, record it in
   `research/progress-log.md`, and report the original and revised analysis both.
8. **Do not restore the wording "this project does not acquire AA copyright material."** It was
   removed on 10 August 2026 as a category error. Reading a copyrighted work and holding one are
   different acts and the rule is about holding: read what is lawfully readable, hold nothing,
   quote nothing at length, record the provenance.

## Authority order

When two things disagree, believe them in this order:

1. `model/aa_group_model.py` for executable semantics
2. hash-linked JSON caches in `research/` whose model and script hashes match
3. generated `research/RELEASE-GATE-RESULTS.md` and `research/ROBUSTNESS-RESULTS.md`
4. the executed notebooks
5. appendix, paper, primer, manuscript, plans, README, PDFs

A PDF or a Markdown table never overrides a cache.

## Where to look

| You want | Read |
|---|---|
| current status, reproduction sequence | `README.md` |
| what remains, and why | `HANDOFF.md` |
| the full rules, statistical and editorial | `CLAUDE.md` |
| how to verify the release independently | `AGENT_VERIFY.md` |
| what each source supports, and its read status | `research/SOURCES.md` |
| what changed and why, chronologically | `research/progress-log.md` |
| the elicitation round and what to send | `research/elicitation/`, and section 9 of `HANDOFF.md` |

## The synchronisation rule, which is the one that bites

A change to the model or to any published number must be propagated **in the same session** to
the caches, both notebooks, the manuscript, the appendix, the paper, the primer, the ledgers, the
plans, the README, the progress log, `HANDOFF.md`, `AGENT_VERIFY.md`, and all three PDFs. A
half-propagated change is worse than none, because the checkers will pass on the layer you fixed
and the contradiction will sit in the layer you did not.

## Sources

Every source lives in `research/incorporated/<ShortAuthor>_<Year>/`. **The documents themselves
are git-ignored and must stay that way**: this repository is public and several sources are in
copyright. What is committed is the record, a citation, rights, provenance URL, SHA-256, summary,
and a vocabulary-only verification index.

Citation checking does not need the documents. Add or repair a source with
`python3 tools/build_corpus.py`, never by hand; `--check` audits without changing anything.

Eleven of the 31 sources are **record only**: no document exists at any time, which is a stronger
condition than git-ignored. Each carries `"record_only": true` in its metadata. Seven of those eleven
have no verification index because no text was retained to build one from. Neither is drift
and neither should be reported as a missing source.

A directory's leading token must be at least three characters, distinctive, and unique across the
corpus, because `tools/check_book.py` identifies a source in prose by that token.

## Tests

`python3 -m pytest` after `pip install -r requirements-dev.txt`. No source document is needed.

The coverage gate is 100 per cent of `model/aa_group_model.py` and is enforced by `.coveragerc`.
**Never edit that file to make a test pass**: its SHA-256 is the release identity, and
`tests/test_release_invariants.py` pins the digest along with capacity 60, viability 5, and the
118-value decomposition. If a test there fails, find out whether the model was changed on
purpose and run the synchronization rule before touching anything.

`tools/` and the analysis scripts sit outside the coverage gate on purpose; they are batch jobs,
covered instead by `tests/test_tools_integration.py`, which runs each for real. Slow work behind
`NIC_SLOW_TESTS=1`.

CI has three jobs. `lint` runs ruff, actionlint and shellcheck, and asserts that the canonical
model takes no lint waiver. `checks` needs pip and nothing else and gates every push: the suite,
the model hash, corpus drift, portability, the book checks, and `check_release.py
--skip-artifacts`, which is 131 of the 136 release checks. `documents` renders the PDFs, checks
them with `check_pdfs.py`, and runs the full gate, on `main` only, because it needs pandoc,
tectonic and a font, and every environmental failure this repository has had came from those
three fetches. **Do not move a check into `documents` that does not need a rendered PDF.** The
whole point of the split is that a CTAN timeout must not stop the release checks running.

## Branches, tags and releases

`RELEASING.md` is the authority. The short version:

- **Never commit to `main`.** Branch, open a pull request, let CI run. Prefixes: `model/`,
  `fix/`, `docs/`, `ci/`, `source/`.
- `lint` and `checks` run on pull requests; `documents` renders the PDFs and runs only on
  `main`, so **a green pull request is not a green release**. Run `tools/run_ci_locally.sh`
  before merging, which covers all three.
- **Never create a tag to mark work finished.** A tag asserts six conditions listed in
  `RELEASING.md`, including the full gate with no `--skip-artifacts`. Asserting them without
  checking is worse than not tagging.
- Versions are semantic, mapped to what can change here: MAJOR is a changed model hash or a
  reversed conclusion, MINOR is new evidence or analysis, PATCH is corrections and tooling.
  Below 1.0 until the elicitation round closes.
- A GitHub Release is a publication, and this repository is public. **Do not publish one
  unless the Human Author asks.** `v0.9.0` is currently tagged and published this way, as a
  pre-release with the three PDFs attached; that does not authorize the next one.

## Lint

`ruff check .`, narrow by design and configured in `ruff.toml`. **Never let it edit a file
under `model/`**: those record their SHA-256 in the caches they produced and a reformat
invalidates hours of computation. They carry per-rule waivers.
`model/aa_group_model.py` takes none and CI asserts it with `--isolated`.

## Before you commit

```bash
python3 tools/check_portability.py
```

`tools/run_ci_locally.sh` runs all three CI jobs here, which is the cheapest way to find out whether a
push will go red.

Before claiming a release, run the full sequence in `README.md` and close with `AGENT_VERIFY.md`.

## What is still outstanding

One item could change a conclusion: the elicitation round. Part Four rests on a twelve-by-eight
matrix one person wrote down, and no computation can test its pattern of empty cells because every
check holds that pattern fixed. The packet to send is `research/elicitation/`. Send
`1-respondent-form.pdf`. **Never send `4-collator-notes.pdf`**, which names the answer the exercise
exists to elicit.

Five more qualify a conclusion rather than change one: three need a copyrighted book bought or
borrowed, two are scholarly loose ends. `HANDOFF.md` section 10 is the complete list and the only
place they are recorded; do not treat any shorter list, including this paragraph, as the full
account. Three items were closed on 17 August 2026 by checking whether the publisher gives them
away, which it did.

## House style, if you touch prose

No em dashes in the author's voice; punctuation inside quotations is preserved as the source has
it. Plain-language equations in the manuscript, LaTeX in the paper. No subheadings or tables in a
chapter's narrative; tables belong in the chapter's Machinery section. Every stochastic number
carries its estimand, seed count, horizon, pairing, and interval. An interval crossing zero is
"unresolved", never "no effect".
