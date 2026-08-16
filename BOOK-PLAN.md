# Book Plan (master)

## *Nobody in Charge*
### How a Fellowship of Drunks Solved a Problem in Mathematics Without Knowing It

Human Author: Christopher Melhauser (christopher.melhauser@gmail.com). AI Writing Collaborator:
theonlymuffinbot (theonlymuffinbot@outlook.com), using a mix of Anthropic Claude Opus 5 and OpenAI
GPT-5.6 Sol and Terra models. Unpublished and written for its own sake.
Audience: the general reader who has never thought about how AA is governed. See
`ATTRIBUTION.md` and `LICENSE`.

Supersedes all earlier plans. Part-level detail lives in `plans/PART-1-PLAN.md` and
`plans/PART-2-PLAN.md`. `README.md` is the index and current status.

---

## 1. The thesis, as it now stands

**It narrowed once, and the narrowing is load-bearing.**

The original conception was that nobody had noticed AA's governance rules
implement a formal condition for reliable group decision-making. That is not
right. Milton Maxwell, a sociologist at State College of Washington, published a
study in 1950 comparing the Washingtonians with AA and concluded that AA's
advantages were exclusively alcoholic membership, singleness of purpose, a definite
programme, anonymity, and what he called hazard-avoiding traditions. He said
anonymity has *sheer survival value*. He reached it through Gough's relapse. He
named keeping authority in principles rather than offices, and rotating
leadership, as a functional group.

So the honest thesis is:

> A sociologist identified the mechanism in 1950 and had no way to prove it. This
> book supplies the proof, and three things he could not have had: that Traditions
> 2, 9 and 12 satisfy a published criterion for when group deliberation converges
> on truth; that rotation only works if the rotating pool scales with the group;
> and that the natural assumption pairing Step *i* with Tradition *i* is wrong on
> all twelve counts.
>
> **Part Four, drafted 2 August 2026, qualifies the third claim and then partly restores it.**
> Five of the twelve counts are invisible to the multiplicative perturbations used everywhere
> else, because five Traditions have identically empty rows and multiplying a zero leaves a
> zero. Chapter 16 reports that and treats the five as arithmetic. Chapter 18 then supplies a
> design that can reach them, asking what strength a Tradition would need before index-pairing
> held, and finds the five failing by margins comparable to the seven. The settled statement is
> that index-pairing fails on all twelve, that five of them cannot be tested by multiplying, and
> that the test which can reach them finds no difference worth the name.
>
> **The third of those is weaker than the other two and the plans now say so.** It rests on
> the magnitudes in two hand-built matrices rather than on their structure. It survives
> modest disagreement about those magnitudes and not wholesale disagreement. See
> `plans/PART-4-PLAN.md` section 1.

That is a smaller claim than "nobody noticed" and a far more defensible one. It
also gives Part One a proper ending, which the original plan lacked.

**The first of those three now has a historical test attached to it, and it passed.** The
selection of Traditions 2, 9 and 12 comes from the theorem, not from history. But if the
Washingtonians had prescribed rotation of the chair, or advised societies against giving
members' names to the press, the book's use of them as the control case would collapse. The
movement's own manual, the *Washingtonian Pocket Companion* of 1842, obtained 2 August 2026,
prescribes neither and takes the opposite position on the second in terms. It does contain
written analogues of four other Traditions, which is why the comparison in Part One has been
rewritten as one code against another rather than as rules against none.

---

## 2. Structure

Six parts, 25 chapters, roughly 80,000 words.

| Part | Chapters | Subject | Research needed |
|---|---|---|---|
| I | 1 to 6 | Two fellowships, 1840 and 1935 | **Blocked on acquisitions** |
| II | 7 to 11 | The group: the condition and its failure modes | **None. Complete.** |
| III | 12 to 15 | The individual: steps as a technology | One literature check |
| IV | 16 to 18 | How the two halves connect | None |
| V | 19 to 22 | How groups die | None |
| VI | 23 to 25 | What we do not know | None |

**Seventeen of twenty-five chapters need no new research.** The burden sits almost
entirely in Part One.

---

### Part I. Two Fellowships (drafted, ~21,000 words)

| Ch | Title | Status |
|----|-------|--------|
| 1 | Chase's Tavern | Solid |
| 2 | The Fade | Solid |
| 3 | The Man Who Was the Movement | Solid |
| 4 | Akron, 1935 | Provisional |
| 5 | Twelve Points to Assure Our Future | Provisional |
| 6 | The Sociologist | Solid on Maxwell |

Full detail, including what is needed from the author, in `plans/PART-1-PLAN.md`.

---

### Part II. The Group (drafted, ~12,200 words)

| Ch | Title | Status |
|----|-------|--------|
| 7 | How a Room Decides | Drafted |
| 8 | The Condition | Drafted |
| 9 | Confident and Wrong | Drafted |
| 10 | Rotation Has to Be Wide | Drafted |
| 11 | What the Washingtonians Lacked | Drafted |

Consolidated from six chapters to five: the original "Three Ways It Breaks" and
"Confident and Wrong" were the same chapter. Full detail in `plans/PART-2-PLAN.md`.

---

### Part III. The Individual (~14,000 words)

| Ch | Title | Content | Status |
|----|-------|---------|--------|
| 12 | Twelve Dials | The person as a state vector. Leaks, gates, order. | Drafted |
| 13 | Can You Skip a Step? | Everyone says no; nobody has checked. The CES reduction makes it one estimable number whose sign is the answer. | Drafted |
| 14 | The Leaky Bucket | Maintenance (Steps 10, 11, 12); an externally plausible nonlinear mechanism whose earlier typical-member threshold result fails in the corrected model environment. | Corrected draft |
| 15 | Helping Is Not the Reward | Pagano's 40 per cent against 22 per cent. Step 12 as a group-level service pathway: removing it lowers membership and maintenance, while its isolated Step 9 spillover is unresolved. | Corrected draft |

Full detail in `plans/PART-3-PLAN.md`.

~~**One outstanding check.** Chapter 13 will assert that nobody has tested whether members
work the steps in order.~~ **Done.** The search found that the standard instrument records
a *sum* of steps completed, which discards order by construction, so the question has not
been declined but made unaskable. Chapter 13 was narrowed around that and around Greenfield
and Tonigan's two-factor finding, which cuts against the strict chain.

**A note carried back from Chapter 14.** The old frozen-environment threshold used constants
from the retired capability-inflated model. With the corrected mean-one capability draw, a
high/low-start test separates in only 7 of 400 full-adherence endpoint environments and
collapses to one low state in the mean environment. The external literature makes nonlinear
relapse dynamics worth testing; this simulation does not establish typical-member
bistability, a separatrix, or hysteresis in its released baseline.

---

### Part IV. How the Two Halves Connect (~11,000 words)

| Ch | Title | Content |
|----|-------|---------|
| 16 | The Pairing That Isn't | The natural index-pairing conjecture, tested and rejected on all twelve steps. The two inversions: Step 5 is served by Tradition 12, Step 12 by Tradition 5. |
| 17 | What a Step Needs From a Room | **Rescoped.** Chapter 12 has already spent the resource derivation and the group-dependence coefficients, so this chapter cannot be the introduction to them. It becomes the chapter on what the coupling says about *Traditions* rather than about steps: why unity is the most load-bearing at 6.52 against a next-highest of 3.89, and why being diffuse rather than strong is what makes it so. |
| 18 | Two Kinds of Rule | Enabling and protective traditions, derived rather than asserted. Five of the twelve give members nothing directly. Note that this claim cannot be tested by multiplicative perturbation and must not be reported as surviving it. |

---

### Part V. How Groups Die (~12,000 words)

| Ch | Title | Content |
|----|-------|---------|
| 19 | You Cannot Close the Door | Tradition 3 as a binding constraint. A group cannot refuse admission, so what can actually go wrong? |
| 20 | Three Ways to Starve | Invisible, unreferred, unwelcoming. Three fingerprints. |
| 21 | The Healthy-Looking Corpse | Quality holds while the group dies. Then back to 1848 and the fade. |
| 22 | What You Cannot Engineer | Carrell, Sacerdote and West. Why you cannot arrange the right mix of newcomers. |

---

### Part VI. What We Do Not Know (~10,000 words)

| Ch | Title | Content |
|----|-------|---------|
| 23 | The Wrong Turns | Every structural error made building this, and what each correction revealed. |
| 24 | What Would Settle It | The measurement agenda: rotation breadth against longevity, step order against completion, the demographic signature. |
| 25 | What a Model Cannot Tell You | The ethical close. Nothing here can assess anyone's recovery. |

**Chapter 23 has grown and should be split.** The error count is no longer nine.
There are roughly fourteen, and they fall into two kinds that teach different
lessons:

*Model errors* (found by simulation): the single-equilibrium proof that made
collapse impossible; adherence compounding multiplicatively; the recipient
resource proportional to raw newcomer count; newcomer dependence bolted on as a
hand-inserted term; protective traditions unable to register at all; dropout keyed
to the mean across all twelve steps; a baseline calibrated on a ten-year horizon
that decayed by thirty; a noise-floor check that used the same seeds twice and
proved nothing; Monte Carlo figures quoted to three decimals the simulation did
not support.

*Research errors* (found by reading sources): the index-pairing assumed from two
numbered lists; Hawkins's two wives, taken from a secondary site; a Worcester
statistic that is not in the source I attributed it to; treating Gough's 1845
account as defensive when he wrote *I have fallen*; attributing the 1858 libel
trial to the 1845 relapse when it arose from a dispute about prohibition
enforcement.

And one *institutional* error, caught in review rather than by me: building a
scenario in which an AA group closes its doors, which Tradition 3 makes
impossible.

The lesson differs by category. The model errors were invisible until tested. The
research errors were invisible until the primary source was read. The
institutional error was invisible to anyone who had not been in the rooms. That
three-way split is the chapter.

---

## 3. Conventions

**Every chapter ends with a section called The Machinery**, in four parts: what
the model says about the chapter, the technical version, notes on how far the
sources can be trusted, and the references. Part 2 is skippable by construction.
All six drafted chapters conform.

**No em-dashes** in the author's prose. Quoted primary material keeps its
punctuation. Verified across all files.

**References separate what was read from what was not.** Every reference list is
divided into read in full, cited at one or more removes, and still to obtain.

**Every chapter is checked mechanically before it is called done.** Run
`python3 check_chapter.py <file>` from the outputs directory. It enforces all of
the above and fails the chapter if any is broken. Each rule exists because a
chapter broke it once:

| Rule | Broken by |
|---|---|
| Chapter headings `# Chapter <Word>` then `## <Title>` | convention |
| Machinery present with exactly the four named parts | convention |
| No `###` subheadings in the main text; separate sections with `---` | ch03, ch08 |
| No tables in the main text; figures live in Machinery, prose in the narrative | ch08 |
| No LaTeX anywhere; plain-text symbols, display equations as `>` blockquotes | ch03, ch04, ch08 |
| No em-dashes in the author's prose | ch01 to ch03 |
| References separate "read in full" from material cited at a remove | convention |
| An explicit statement of what was **not** read | ch08 |
| Flesch-Kincaid under 10; no sentences over 45 words | ch06 at 11.0 |

The last two are warnings rather than failures, since a chapter can legitimately
have nothing unread (ch08) or run harder than average.

**Run it after any revision, not just on new chapters.** The ch08 tidy-up
introduced no errors but the ch03 normalisation did, and the checker caught it.

**Every computed figure is reproducible and regression-tested.**
`model/book-calculations.ipynb` regenerates every number quoted in the book, organised by
chapter, and asserts each against the value printed. If a cell fails, either the model
changed or a chapter is wrong. Run it after any change to `model/aa_group_model.py` and before
calling any chapter done. It currently reports all figures matching.

**Sources are archived.** `research/SOURCES.md` records provenance for everything cited,
split into obtained-and-read, obtained-and-partly-read, and not-obtained. Since 9 August 2026
each source is a directory under `research/incorporated/<ShortAuthor>_<Year>/`, and no source
document is committed: what is published is the citation, the rights position, the provenance
URL, the SHA-256 and a vocabulary-only verification index. Gough (1869), the primary source for
Chapter 3, is at `research/incorporated/Gough_1869/` with its chapter offsets recorded in
`SOURCES.md`; the document itself is a local working file.

**Claims are tracked.** `research/part1-claim-register.md` grades every load-bearing claim
in Part One as primary, scholarly, at-a-remove, or inference.
`research/progress-log.md` records corrections as they are made.

---

## 4. Risks

**The authority problem is the serious one.** A book confers far more weight than
a working paper, and the model has never been tested against a real group.
Someone in early recovery could take "here is the mathematics of how this works"
much harder than the evidence supports. The response is structural: Part VI is a
sixth of the book, Chapter 23 sits where a reader will reach it, every predictive
claim in Parts III to V stays conditional, and Chapter 25 exists solely to say
what the book cannot do.

**Copyright.** The Steps and Traditions are AAWS copyright. Paraphrase
throughout, as the paper does. The 1939 first edition appears to be public domain
in the US, unrenewed, with facsimiles in print, but that should be checked against
Copyright Office renewal records before any text is quoted.

**Partisan sources.** Most accessible Washingtonian material is written by AA
members to illustrate why the Traditions matter. Handled by preferring Maxwell,
naming him as sympathetic to AA, and flagging tertiary sources as tertiary.

**Register.** The book has to be readable by someone with no mathematics and
satisfying to someone with plenty. The Machinery structure is the mechanism.
Chapter 8 is where it either works or fails.

---

## 5. What is actually blocking what

| Blocked | On | Who |
|---|---|---|
| ~~Chapter 5's rewrite~~ | **Done 2 Aug 2026.** Rewritten on Kurtz; fifteen of sixteen claims read directly. | Done |
| Chapter 4's funding narrative | Rockefeller Archive Center, or accepting AA's histories at a remove | You, and optional |
| Chapter 2 verification | Blumberg 1980 | You. **Largely relieved** by Marsh 1866, Blair 1888 and Grosh 1842. |
| Chapter 1 completeness | Alexander 1988 | You. **Partly relieved** by Grosh 1842 on the women's societies. |
| Chapter 6's 1944 material | A Mann biography, or Kurtz reread for the NCEA sequence | Me, in part |
| Chapter 3 definitiveness | AAS Gough scrapbook | You, and optional |
| Chapter 13 | Step-ordering literature search | Me |
| **Everything else** | **Nothing** | **Me** |

**Parts II, IV, V and VI can be written now, in full, with no acquisitions.** Parts II and III
are done. That leaves ten chapters and roughly 33,000 words with nothing blocking them.

**The *Washingtonian Pocket Companion*, obtained 2 August 2026, changed what Part One
argues.** The comparison is no longer between a fellowship that wrote rules and one that did
not. The Washingtonians had written analogues of Traditions 4, 7 in part, 9 between societies,
and 10, in print within two years of founding. They had no analogue of Tradition 2 and took the
opposite position to Tradition 12 deliberately. The thesis of section 1 is unchanged and better
supported; the framing in Chapters 1 and 2 has been rewritten, and one claim in Chapter 2 was
falsified outright.

---

## 6. Recommended order from here

1. **Part II, starting with Chapter 8.** It is the hardest translation problem in
   the book and everything depends on it. If plain-language Golub and Jackson
   works at book length, write the rest; if not, stop and rethink.
2. **Part V**, which is the model's strongest and most falsifiable material and
   pairs naturally with Part One's fade.
3. **Part IV**, short and self-contained.
4. **Part III**, after the step-ordering literature check.
5. **Part VI**, last, because it has to account for everything before it.
6. ~~**Chapters 4 and 5 rewritten**, whenever Kurtz arrives.~~ **Both done 2 Aug 2026.** Chapter 4's founding narrative and board room scene and the whole of Chapter 5 are now built on Kurtz. What remains at a remove in Part One is Chapter 4's funding narrative after December 1937 and Chapter 6's 1944 material.
7. **Introduction**, written last, once the thesis has stopped moving.

**Superseded 9 August 2026. The book is complete.** All six parts are drafted: 25 chapters plus
the preface and the introduction, assembled by `tools/build_book.py` into a 260-page PDF. Part Six
and the introduction, described below as outstanding, were written. Chapter 22 is no longer
provisional: it stands at about 2,300 words and cites Carrell, Sacerdote and West, whose three
figures are registered as source figures in `tools/check_book.py`.

The paragraph below is kept as the record of where the project stood on 2 August 2026.

> **Parts One to Five are drafted as of 2 August 2026.** What remains is Part Six (three chapters)
> and the introduction, neither blocked on anything. One drafted chapter is provisional: Chapter 22
> is 762 words against a planned 2,500 and waits on Carrell, Sacerdote and West.

---

## 7. What the finished book contains, added 5 August 2026

The book ends in three appendices rather than one, and the plan should say so because two of
them did not exist when the structure above was written.

1. **The technical appendix**, `appendix/APPENDIX.md`. Unchanged in role: the document a
   referee reads first.

2. **The primer**, `reference/PRIMER-steps-and-traditions.md`. One finding for each of the
   twelve Steps and each of the twelve Traditions, in two layers, a technical statement and a
   plain-English reading of it. It exists because the book's per-item findings are spread
   across eleven chapters and a reader who wants to know what the model says about, say,
   Tradition 9 has no way to find out short of reading Part Two entire.

   **It is derived and it asserts nothing.** Every figure in it is copied from a chapter
   Machinery, the notebook or a cached JSON. That makes it the one document in the project
   that can go wrong without any instrument noticing, since `check_book.py` reads chapters and
   the notebook asserts chapter figures. Auditing it on the day it was written, against the
   model source rather than against the chapters it was copied from, found one real error: it
   cited Maxwell 1950 as 11(3): 410-451 where every other file in the project and the saved
   text itself say 11: 410-452.

   **The plain layer is the part to watch.** It is an interpretation of the technical layer
   sitting directly above it, it is not asserted anywhere, and nothing checks that the two
   still agree. Four places in the first draft carried the interpretation further than the
   technical statement supports and are marked in the progress log.

3. **The working paper**, converted from `paper/anonymity-as-an-aggregation-condition.tex` by
   pandoc at build time. The LaTeX remains the source of truth for the paper and its own PDF
   remains its authoritative rendering.

**The build is a script now**, `tools/build_book.py`. It had been a description in the
progress log, which meant the book could not be rebuilt from the repository alone. The
reconstruction was verified by rebuilding the previous book and diffing: it reproduces the
2 August build line for line apart from the date and the appendices added here.

---

## 8. Release-gate correction round, opened 6 August 2026

plans/RELEASE-GATE-PLAN.md is now the controlling plan for the final audit and correction round. Its release criteria supersede earlier statements in this file that the project was “fully audited,” universally checked, or release-ready.

The approved model semantics for this round are:

- raw \(B=S G^{\mathsf T}\) remains a semantic overlap matrix, not an executable transition operator;
- executable coupling, the state map, and trajectory finite differences are reported as distinct objects;
- Tradition Three and Tradition Eleven each retain two plausible mechanisms and are separated with paired \(2\times2\) designs;
- the recipient statistic is an opportunity-per-potential-helper proxy, labelled low- versus high-practice, with a clean resource-override ablation;
- zero membership is permanently closed, while existence, endpoint viability, final membership, first passage, recovery, and closure are separate estimands; and
- lognormal heterogeneity is mean-centred so its scale parameter does not silently change average capability.

All affected caches, notebooks, appendix tables, manuscript claims, paper claims, primer wording, source ledgers, and generated PDFs must be regenerated or revised before the release status can be restored.

The robustness expansion distinguishes modeled group size, confirmatory replication and
perturbation coverage. Room capacity remains 60 and ordinary stochastic claims retain the
400-seed minimum. Sensitivity coverage expands to roughly one thousand independent
perturbation points per major design: 1,002 global draws, 1,000 tiered draws, 1,000
randomized-matrix draws, 944 multi-level one-at-a-time points, 20 Morris trajectories and a
1,024-row Sobol base design. The three- and five-seed evaluations inside those screens remain
screens and must be labeled accordingly.
