# Project instructions

Read this file, `plans/RELEASE-GATE-PLAN.md`, and `AGENT_VERIFY.md` before changing the
project. Work directly in this repository. Do not delete source material or caches without
explicit user authorization. Preserve unrelated user work.

The authoritative workspace is the Git checkout containing this file. Treat its root as `.`.
All tracked paths, commands, notebook loaders, generated manifests, and handoff instructions
must be repository-relative or derived at runtime from `__file__`, `Path.cwd()`, or Git. Never
commit a user home directory, workspace root, or other host-specific absolute path. Non-Git
copies are reference copies only and are not release authorities.

## Authority and current state

The source hierarchy is:

1. `model/aa_group_model.py` for executable semantics;
2. hash-linked analysis scripts and complete caches for numerical results;
3. manuscript, paper, appendix, primer, plans, and ledgers for interpretation;
4. generated Markdown and PDFs.

Do not make prose agree with a stale cache or make a cache agree with prose by hand. The current
canonical model SHA-256 is
`c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952`.

The modeled room capacity remains 60. Confirmatory stochastic claims use 400 seeds, paired by
common random numbers where possible. The expanded robustness round increases parameter draws,
perturbation distances, structural variants, trajectories, horizons, and integration-step
checks. It does not increase room size or replace the 400-seed confirmatory rule with 1,000
seeds.

## Model language that must remain exact

- `B = S @ GOV.T` is semantic overlap, not executable coupling.
- `C = Snorm @ GOVW.T` is the normalized no-capacity linear map, not a trajectory effect.
- State-dependent resource maps and simulated finite differences are separate objects.
- Tradition 3 has resource-governance and inverse-practice dropout-friction paths.
- Tradition 11 has resource-governance and attraction paths.
- Ordinary changes in T3 or T11 adherence move both paths and are mixed interventions.
- The recipient resource is low-practice opportunity per high-practice potential helper.
  Low and high practice are not tenure cohorts.
- Capability uses a mean-one lognormal draw. `het_sd` changes dispersion, not average
  capability by construction.
- Zero membership is absorbing closure. Existence is `N > 0`; endpoint viability is `N > 5`;
  first crossing, recovery, final membership, and closure are different estimands.
- The constructed practice scale is cardinal only inside this model and has no validated
  clinical or individual unit.
- The Chapter 13 rho exercise is proxy averaging under oracle-known inputs and loadings. It is
  not validation of a latent-variable estimator and does not establish a required instrument
  count.
- Founding composition changes all state-dependent channels. Its paired contrasts are
  unresolved without a prespecified equivalence margin.
- Chapter 14's old frozen-environment high state, separatrix, and hysteresis are retired
  diagnostics. In corrected endpoint environments, high and low starts separate in only 7 of
  400 cases.

## Statistical rules

Every confirmatory stochastic statement must give the estimand, conditioning rule, seed count,
horizon, integration step, pairing, and interval. Use Wilson intervals for one-condition binary
fractions and paired intervals or paired tests for contrasts. A common-random-number design is
more efficient; it is not fewer replications.

Three- and five-seed parameter-point designs are screens. Report strict support, ties, and
reversals separately. Do not call parameter points independent replications of the stochastic
model. Do not use absence of an OAT effect as evidence that a parameter is irrelevant. A
multiplicative screen cannot move a structural zero.

The release designs are:

- 1,002 global draws across 12.5%, 25%, and 50% amplitudes;
- 1,000 tiered draws and 1,000 randomized-matrix draws;
- 944 multi-level OAT points over 118 registered values;
- 20 Morris trajectories;
- a 1,024-row Sobol base design on eight post-Morris leaders;
- 10,000 structural simulations;
- 400-seed principal T3, T11, recipient, service, trajectory, and composition contrasts;
- 200-seed integration-step and horizon checks.

The 118-value decomposition is 22 scalar defaults, 12 step speeds, 49 nonzero `S` cells, and
35 nonzero `GOV` cells. Call these registered sensitivity values, not all parameters or all
choices. Use competition rank `1 + count(values greater than the indexed value)` and preserve
ties.

## Synchronization rule

Any change to the model or a public number must be propagated in the same work session to every
affected layer:

- analysis scripts and caches;
- both notebooks;
- manuscript chapters and preface;
- `appendix/APPENDIX.md`;
- `paper/anonymity-as-an-aggregation-condition.tex`;
- `reference/PRIMER-steps-and-traditions.md`, including its plain-language paragraph;
- `research/PARAMETERS.md`, `research/SOURCES.md`, and claim registers;
- `README.md`, all applicable plans, `research/progress-log.md`, and `AGENT_VERIFY.md`;
- the book, paper, and primer PDFs.

Search the whole repository for retired values and phrases. The release checker supplements
that search; it does not replace reading the surrounding claim.

## Source boundary

The staged corpus was worked through on 9 August 2026 and is now mostly incorporated. Four items
moved to `research/incorporated/`: the three American Temperance Union documents and the source
record for AA pamphlet P-17. Maxwell (1950) and Golub and Jackson (2010) were already there.

Three copyrighted works were read and catalogued on 10 August 2026, bringing the corpus to 26
sources: `TwelveAndTwelve_1953`, `Rohr_2011` and `KurtzTalk_c1984`. All three are record only.

`RecoveryDharma_2023` was added on 16 August 2026, bringing the corpus to 27. Sections I and II were
read in full; only the meditations and inquiry questions were not. It supports appendix A12 and four
paragraphs of Chapter 24. It is held on the ordinary footing, git-ignored with a hash and an index.
Its CC BY-NC-SA 4.0 licence is the one licence in the corpus that would permit committing the
document; it is git-ignored anyway, because the rule is uniform.

Two rules attach to it. **The founder of the predecessor organization it split from is named in that
source and is named nowhere in this project.** The structural claim does not need the name and
nothing here can adjudicate an allegation about a living person. And a first pass on that source
concluded the fellowship had no group-conscience analogue, which was wrong: the sangha is one, and
the error came from skipping Section II. Do not restore the earlier claim.

Both journal articles, Pagano et al. (2004) and Greenfield and Tonigan (2013), were obtained by
hand on 10 August 2026 and read in full; they are under `research/incorporated/`. The staged
corpus is therefore fully incorporated, and what is left under `research/staged/` is the
acquisition report and metadata, which are provenance rather than evidence. The rule still applies
to anything acquired in future: file presence does not make a source read.

**No source document is committed, and this repository is public.** Every source lives in
`research/incorporated/<ShortAuthor>_<Year>/`. `.gitignore` excludes every `.pdf`, `.txt`,
`.djvu` and `.epub` under `research/incorporated/` and `research/staged/`. What is committed is
the record: `citation.md`, `metadata.json` with rights, provenance URL and SHA-256,
`source_summary.md`, and a vocabulary-only verification index. Documents are local working files.

Do not commit a source document, and do not add a source by hand. Run
`python3 tools/build_corpus.py`, which normalizes the layout and rebuilds any index whose stored
SHA-256 no longer matches its file. `--check` reports drift without changing anything.

Citation checking does not depend on the documents. Each index records the source's vocabulary
and, because a vocabulary set has no word order, which registered subjects the document contains,
decided against the real text at build time. With no documents present, every citation-subject
pair still verifies. If a re-acquired file's hash differs from the record, the index is stale and
must be rebuilt rather than trusted.

**Seven sources are held as record only, with no document at any time.** This is a distinct
category from the git-ignored documents, and a verifier should not report either as a missing
source. AAWS pamphlet P-17 and Kurtz (1991) are copyrighted works the project chose never to
store. DeGroot (1974) and the April 1946 *A.A. Grapevine* article were consulted on 10 August 2026
from scans whose posting authorization is unverified, and the project's own rights review directs
that they be cited and quoted within limits rather than archived. Each record keeps the citation,
the rights position, the hash of the scan consulted, and the passages verified from it.

Three more were added on 10 August 2026 on the same footing: AAWS *Twelve Steps and Twelve
Traditions* (1953), Rohr (2011), and the Kurtz talk of about 1984. Rohr carries a stronger
provenance objection than any other source, recorded in full in its `metadata.json`: the copy
consulted was an unauthorized posting of a current in-print title. It was not retained, its
bibliographic record was confirmed independently of it, and both claims drawn from it are absence
claims. Any Rohr citation must be confirmed against a lawfully obtained edition before release.

**Reading a copyrighted work and holding one are different acts, and the project rule is about
holding.** Several chapters formerly said "this project does not acquire AA copyright material"
and treated that as a reason not to read it. That was a category error and it cost the argument
evidence: the 1953 commentary turned out to contain the book's own thesis in Wilson's words, the
strongest objection to it, and the disproof of the index-pairing conjecture. The rule now reads:
read what is lawfully readable, hold nothing, quote nothing at length, and record the provenance.
Do not restore the old wording anywhere.

Do not restore a document to any of those four. Adding a source of any kind means running
`python3 tools/build_corpus.py`, and a directory's leading token must be at least three characters
and distinctive, because `check_book.py` identifies a source in prose by that token. "AA" is not
usable; "Grapevine", "BigBook" and "ATU" are.

The current authority for read status, provenance, and claim support is `research/SOURCES.md`.

Verify quotations against an original page image when available. OCR and retyped texts are
search aids. Distinguish read in full, abstract-only, cited at a remove, referenced but not
reproduced, and not obtained.

## Manuscript conventions

- No em dashes in the author's prose. Preserve punctuation inside quotations.
- Use plain-language equations in manuscript Markdown; the paper remains LaTeX.
- No subheadings or tables in a chapter's narrative. Use horizontal rules between narrative
  sections; tables belong in The Machinery.
- Every chapter ends with The Machinery and its reference-status headings, in this order, using
  the ones that apply: Read in full; Cited at a remove; Referenced but not reproduced; Internal,
  and reproducible from this repository; What was not read. A heading with nothing under it is
  omitted rather than filled with a placeholder, which is why most chapters carry four of the
  five. The order is fixed; the set is not.
- A number from a stochastic run carries its uncertainty and design. Deterministic algebra is
  labeled deterministic.
- Nothing in the project may be written as advice about an individual's recovery.

## Reproduction

Run from the repository root:

```bash
python3 -m pytest
python3 tools/run_notebook.py
python3 tools/check_book.py
python3 tools/check_chapter.py reference/PRIMER-steps-and-traditions.md
python3 tools/check_portability.py
python3 tools/check_release.py
python3 tools/build_book.py
python3 tools/build_primer.py
```

## Tests and CI

`python3 -m pytest` runs the suite. It needs `requirements-dev.txt` and nothing else, and it
does not need any source document: every source under `research/incorporated/` is git-ignored
and the citation checker works from the committed verification indexes.

The coverage gate is **100 per cent of `model/aa_group_model.py`** and is enforced by
`.coveragerc` with `fail_under = 100`. That file is the canonical model, is hash-frozen, and
is pure computation, so it is worth testing exhaustively. The scripts under `tools/` and the
analysis scripts under `model/` are deliberately outside the gate: they are batch jobs and
entry points that write hash-linked caches and render PDFs. They are covered by
`tests/test_tools_integration.py`, which runs each one for real, and by the release gate.

**`model/aa_group_model.py` must never be edited to make a test pass.** Its SHA-256 is the
release identity. `tests/test_release_invariants.py` pins the digest, room capacity 60, the
viability threshold 5, and the 22 + 12 + 49 + 35 = 118 decomposition, so a change fails the
build rather than being noticed by a reader.

GitHub Actions runs two jobs, defined in `.github/workflows/ci.yml`. `checks` is fast and
gates every push and pull request. `release-gate` installs pandoc and tectonic, rebuilds the
book and the primer, asserts zero overfull boxes, and runs `check_release.py`; it rebuilds
rather than trusting the committed PDFs because a fresh clone gives every file the same
checkout timestamp.

The standalone primer is rebuilt by `python3 tools/build_primer.py`, which holds its typography so
the Markdown stays free of LaTeX; the paper is rebuilt from its LaTeX source. All three PDFs use one
inch margins and must render with zero overfull boxes. `build_book.py` and `build_primer.py` both
report the overfull count, and a nonzero count means text is sitting outside the type block.
Render and visually inspect all three PDFs. Confirm that each artifact is newer than every
source that feeds it, has no clipping or broken tables, and contains no retired language.

## Release discipline

Do not claim steady state, indefinite persistence, universal sensitivity, causal composition
effects, or path-specific T3/T11 effects from mixed interventions. Do not describe an interval
crossing zero as no effect. Do not retune the failed 45-member and 9-experienced-member targets
after seeing the correction. Do not approve release until every required cache is complete and
hash-current, both notebooks execute cleanly, all checkers pass, and an independent verifier can
return the documented release verdict using `AGENT_VERIFY.md`.
