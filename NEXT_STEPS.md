# Next steps

What remains to be done, in the order it should be done, as of 26 October 2026. Nothing here blocks
the release state: every checker passes, both notebooks execute, the three PDFs render with zero
overfull boxes, and continuous integration is green. `HANDOFF.md` section 10 is the detailed list
with the evidence for each item and `research/progress-log.md` is the dated record; this file is the
short, forward-looking version, and the two must agree. When an item is done, delete it here and
move its record to the progress log and `CHANGELOG.md`.

## 1. Needs the Human Author

| # | Step | Why it matters | Where it is described |
|---|---|---|---|
| 1 | **Send the elicitation round.** Two or three respondents fill in `research/elicitation/1-respondent-form.pdf`. Never send `4-collator-notes.pdf`. | The only open item that could change a conclusion: Part Four rests on a twelve-by-eight matrix one person wrote down, and no computation can test its pattern of empty cells. Returned forms are filed under anonymous codes (R01, R02, ...); the code-to-person mapping stays outside the repository. | `HANDOFF.md` section 9; `research/elicitation/5-invitation-email.md` |
| 2 | **Install the four CI fonts**, then rebuild the book and primer, run CI, and compare with the runner. | Local PDF builds use different TeX Gyre Pagella files from CI's pinned ones, so the book and primer are not byte-reproducible across machines. | the install-CI-fonts guide the Human Author keeps in their Downloads folder; `tools/check_fonts.py` |
| 3 | **Decide whether to add the Chapter 24 survey item** drafted in section 3 below. | Chapter 10 no longer promises it; the draft says what it would ask and what would count against the book. | Section 3 |
| 4 | **Obtain *Alcoholics Anonymous Comes of Age*, pages 97 to 98.** | Kurtz names it as the passage that settles the unity versus singleness-of-purpose question Chapter 17 depends on. | `HANDOFF.md` section 10, item 2 |
| 5 | **Lawful copies** for the six record-only sources; **photographs** of pages 22 and 23 of the 1939 working manuscript; copies and read statuses for the nine background citations. | Each moves a record-only source onto the ordinary footing. None changes a conclusion. | `HANDOFF.md` section 10, items 3 to 6 |

## 2. Waiting on an outside event

| Step | Trigger | What to do |
|---|---|---|
| Confirm the pinned pandoc 3.10.2 and tectonic 0.17.0 on the new runner image | GitHub moves `ubuntu-latest` to Ubuntu 26.04 (announced for 19 October 2026; the runner was still 24.04 on 23 October) | Dispatch the workflow: `gh workflow run ci.yml --ref main`, read the "Operating System" lines in the log, and fix the pins in `ci.yml` and `release.yml` together if a step fails. |
| Raise a pinned GitHub Action | Dependabot opens a monthly pull request | Read the release notes, dispatch the workflow on the branch, then merge. |
| Rights holder objects to the Fatimah et al. (2025) text in git history | A complaint | Rewrite history with `git filter-repo` and file a GitHub Support request to clear `refs/pull/*`. The rewrite was prepared and verified once and discarded. `SECURITY.md` and `research/SOURCES.md` describe the exposure. |

## 3. Draft for the author's decision: a Chapter 24 survey item

Chapter 10 used to promise that Chapter 24's survey would ask how many people a room turns to on a
hard question. Chapter 24 has no such item and Chapter 10 now says so. If the author wants it, this
is a draft to place after item Two in `manuscript/ch24-what-would-settle-it.md`. It is not in the
manuscript, because adding a preregistered item is the author's decision.

> **Two (b). Whom the room turns to.** Chapter Eight's elder-statesman family and Chapter Ten's
> rotation pool both turn on how much of the room's attention a few people hold when a hard
> question comes up, and no one has counted. The measurement is a one-page anonymous survey at the
> same meetings as item Two. Each regular attendee names up to three people they would go to with
> a hard question. From the nominations, compute the share held by the most-named person, and the
> number of people it takes to cover half of all nominations, and set both against the group's
> size, age and whether it has split.
>
> What would tell against the book: shares close to one over the headcount in groups that rotate
> little, or large shares that bear no relation to whether a group holds together. The first would
> mean the model's elder-statesman problem does not arise; the second, that attention concentration
> is not the mechanism. The analysis, including the concentration measure, is fixed before any form
> is collected. The obstacle is the one that item Two already has: the unit is a meeting.

## 4. Standing notes: left undone on purpose

None changes a conclusion; each is also in `HANDOFF.md` section 10 or the progress log.

- The `model/*.py` analysis scripts keep stale docstring pointers and a few unit slips, because
  editing a script invalidates the cache that records its SHA-256. They are recorded in
  `model/ERRATA.md`; correct them in the same commit as any rerun.
- The public `research/elicitation/4-collator-notes.pdf` names the answer the exercise elicits. It
  was left public by decision on 16 October 2026 because Chapter 18 states the same rows.
- Dependabot watches GitHub Actions only. The `requirements-dev.txt` versions are deliberate floors.
- The optional pre-commit hooks (`.pre-commit-config.yaml`) are a subset of CI.

## 5. If the model or a public number changes

Run the synchronization rule in `CLAUDE.md`: analysis scripts and caches, both notebooks, the
chapters and preface, the appendix, the paper, the primer (including the "What was assumed" block of
every entry that quotes a changed value), the research ledgers, the plans, the README, the progress
log, `AGENT_VERIFY.md`, and the three PDFs. `tools/check_release.py` supplements the search; it does
not replace reading the surrounding claim.
