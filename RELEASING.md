# Branches, tags and releases

This is a research repository, not a library. Nobody depends on an API here; what a version
number has to describe is the state of an argument and the numbers behind it. The scheme below
is built around that, and around the one fact this project already treats as an identity: the
SHA-256 of `model/aa_group_model.py`.

---

## Branches

`main` is the only long-lived branch and takes no direct commits. Everything arrives through a
pull request from a short-lived topic branch, named for what it is for:

| Prefix | For |
|---|---|
| `model/` | the canonical model, an analysis script, or a cache |
| `fix/` | a defect in prose, code, or a checker |
| `docs/` | documentation, plans, ledgers, the progress log |
| `ci/` | the workflow, tooling, lint, tests |
| `source/` | adding or re-reading a corpus source |

A `model/` branch is the serious one. Changing `model/aa_group_model.py` changes the release
identity, invalidates every cache that records it, and obliges the synchronisation rule in
`CLAUDE.md` across every layer. Do not open one casually.

Delete the branch on merge. `git remote prune origin` afterwards.

---

## Versions

Semantic versioning, with the three levels mapped to what can actually change here.

**MAJOR** — the canonical model hash changes, or a published conclusion is reversed or
withdrawn. These are the changes that invalidate caches and every number downstream of them. A
reader who has cited this work needs to know.

**MINOR** — new evidence, analysis, chapters, appendix sections, or sources. Conclusions are
extended, qualified or sharpened, not reversed.

**PATCH** — corrections, typography, tooling, lint, documentation. Nothing a reader would cite
differently.

### Why this is pre-1.0

It stays below 1.0 while the elicitation round is open. Part Four rests on a twelve-by-eight
matrix one person wrote down, and no computation can test its pattern of empty cells, because
every check holds that pattern fixed. Until a second reader has marked those cells
independently, the central claim has not been checked by anyone but its author.

**1.0.0 means that item is closed, not that the prose is finished.** See section 10 of
`HANDOFF.md` for what remains.

---

## What a release requires

A tag asserts that the repository was in a releasable state at that commit. It is a claim, so
it has to be earned. All of these, in this order:

1. `tools/run_ci_locally.sh` clean, all four jobs.
2. `python3 tools/check_release.py` with **no** `--skip-artifacts`. The seven artifact
   checks are the point of a release; skipping them is for a fresh clone, never for a tag.
3. `python3 tools/check_pdfs.py` clean, with poppler present so the ink measurement runs
   rather than skips.
4. `python3 tools/check_docs.py` clean **after rebuilding the PDFs**, so the page-count claims
   are confirmed against a fresh build rather than against the committed artifacts.
5. Both notebooks execute cleanly.
6. CI green on `main` at that commit, including the `documents` job.
7. An independent verifier can return the documented verdict using `AGENT_VERIFY.md`.

Then tag. **Annotated, never lightweight**, because the message is where the state is recorded:

```bash
git tag -a v0.9.0 -m "..."     # see CHANGELOG.md for what the message should carry
git push origin v0.9.0
```

The message records the model SHA-256, the gate counts, and the corpus size. A tag whose
message does not say which model produced it is not much use, since that hash is what every
cache is keyed to.

Pushing a tag runs `.github/workflows/release.yml`, which re-runs the full gate and the PDF
checks against the tagged tree. It cannot make a bad tag good, but it records publicly whether
the claim held.

---

## GitHub Releases

A tag is a mark in the history. A GitHub Release is a publication, with a page and a feed, and
this repository is public. **Do not publish one without the Human Author asking for it.**
Tagging is the routine act; publishing is not.

If one is published, attach the three rendered PDFs, since a reader wanting the book should not
have to build a TeX toolchain to read it.

`v0.9.0` was published this way on 23 August 2026, at the Human Author's request, as a
[pre-release](https://github.com/cmelhauser/nobody-in-charge/releases/tag/v0.9.0): marked
pre-release because the repository is below 1.0, not because the publication itself was
provisional. All three PDFs are attached and were verified byte-identical to the files at the
tagged commit after upload. This is the only GitHub Release to date; the rule above still
governs the next one.

---

## For agents

- Never commit to `main`. Branch, open a pull request, let CI run.
- `lint`, `unit-tests` and `checkers` run on pull requests. `documents` does not, so **a green pull request is
  not a green release**; run `tools/run_ci_locally.sh` before merging.
- Never create a tag to mark work finished. A tag asserts the seven conditions above, and
  asserting them without checking is worse than not tagging.
- If the model hash changes, that is a MAJOR release and the synchronisation rule in
  `CLAUDE.md` applies to every layer before anything is tagged.
