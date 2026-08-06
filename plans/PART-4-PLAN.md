# Part Four: How the Two Halves Connect

Chapters 16 to 18, roughly 11,000 words.

Master plan: `../BOOK-PLAN.md`. Companions: `PART-1-PLAN.md`, `PART-2-PLAN.md`,
`PART-3-PLAN.md`. Technical apparatus: `../appendix/APPENDIX.md`.

---

## 1. What Part Four is for

Parts Two and Three are two separate arguments that happen to be about the same
institution. Part Two says a group deciding by discussion is reliable only if no member
holds a fixed share of attention, and that three Traditions secure that. Part Three says a
person is twelve perishable quantities, gated, unevenly dependent on a group.

Part Four is where they meet. The joint is the two matrices: what each step needs from a
group, and which Traditions govern the supply of each thing needed. Everything in this part
descends from those matrices, which makes it the most judgemental part of the book and the
part where the sourcing and sensitivity discipline has to be tightest.

> **This section said the opposite when it was first written on 2 August 2026, and the
> correction is the most important thing in this plan.** The original text read: "The
> magnitudes in those matrices do not carry the argument... What carries the argument is the
> pattern of which cells are empty." That is true of the *survival* claims and false of the
> *coupling* claims, and Part Four is entirely about the coupling. Running the structural
> test on the coupling, which the plan itself listed as still to compute, falsified it within
> the hour.

**The magnitudes carry Part Four, and this has to be said out loud in the chapters.**

Two facts that look similar and are not:

**The survival claims are structural.** Replace every non-zero entry of both matrices with a
random number, keeping only which cells are empty, and the ordering claim still holds in 100
per cent of draws. Parts One and Three may be defended as resting on structure rather than
on my judgement about magnitudes.

**The coupling claims are not.** The same structural randomisation leaves index-pairing
failing on all twelve in only **40.6 per cent** of draws, which is less often than it holds.
The Step 5 inversion survives in 17.5 per cent, the Step 12 inversion in 27.6, and unity's
primacy in 75.4. The degradation is smooth rather than sudden:

| Design | T1 most load-bearing | Index-pairing wrong on all 12 | Step 5 to T12 | Step 12 to T5 |
|---|---|---|---|---|
| jitter ±15% | 100.0% | 98.8% | 100.0% | 89.7% |
| jitter ±30% | 100.0% | 85.5% | 99.5% | 67.3% |
| jitter ±50% | 98.0% | 72.5% | 88.7% | 52.9% |
| jitter ±75% | 86.8% | 65.2% | 71.5% | 43.8% |
| structural, sparsity only | 75.4% | 40.6% | 17.5% | 27.6% |

**What Part Four may therefore claim.** That index-pairing fails, and that the failure is
robust to *modest* disagreement about the magnitudes: a reader who would have written 0.7
where I wrote 0.9 gets the same answer. It is not robust to *wholesale* disagreement. A
reader who thinks the matrices are essentially arbitrary should not be persuaded, and the
chapters must say so rather than borrowing the preface's structural defence, which was
established for a different claim.

This is not fatal. It relocates the argument's foundation from the sparsity pattern to the
judgements about magnitude, which means the defence of Part Four is the *derivation* of those
judgements, chapter by chapter, and not a robustness statistic. That is a harder chapter to
write and a more honest one.

**Still true and worth keeping.** The governance matrix is exactly cancelled at full
adherence, which is algebra; and it carries under 4 per cent of total effect in the Morris
screen even at partial adherence. Those are statements about the *simulation*, not about the
coupling, and they survive.

---

## 2. Chapter plan

### Chapter 16. The Pairing That Isn't
~~*Target 4,000 words.*~~ **Drafted 2 August 2026, 2,001 words of main text.** Shorter than
planned because the plan's step 3, "report the result", turned out to need step 3a: report how
much of the result is arithmetic. Five of the twelve counts are trivial, the chapter says so in
its fourth paragraph, and notebook section 11b proves the five contribute nothing to any
robustness figure at any level. What was planned as the strongest chapter in Part Four is still
the strongest and is a smaller claim than the plan expected.

The natural conjecture is that Step *i* is served by Tradition *i*. Twelve steps, twelve
Traditions, published side by side for seventy years. It fails on all twelve counts.

The chapter's argument:

1. State the conjecture fairly. It is not stupid; the numbering invites it, and AA
   literature sometimes gestures at it.
2. Derive the coupling from first principles: B = S G', where S records what each step
   consumes and G what each Tradition governs. Neither matrix was built with pairing in
   mind, which is what makes the test meaningful.
3. Report the result: no step's principal supplier is its own index-mate.
3a. **And immediately report that five of the twelve are arithmetic.** T4, T6, T7, T9 and T10
   have identically zero rows in G, so steps 4, 6, 7, 9 and 10 have index-mate entries of
   exactly zero. No sparsity-preserving perturbation can change that. Verified in notebook
   11b: at every level the "all twelve" proportion equals the "all seven non-trivial"
   proportion exactly.
4. **Report the two inversions that make the point vivid.** Step 5, telling another human
   being, is chiefly served by Tradition 12, anonymity, by way of confidentiality. Step 12,
   carrying the message, is chiefly served by Tradition 5, singleness of purpose, by way of
   the recipient resource. The two most quotable pairings in the programme are swapped.
5. Report the robustness honestly and *unequally*. Over 2,000 draws at plus or minus 30 per
   cent on every matrix entry, index-pairing fails on all twelve in 85.5 per cent of draws.
   But the Step 5 inversion holds at 99.5 per cent and the Step 12 inversion at only 67.3,
   because Tradition 3 is a close competitor for the recipient resource. **Chapter 16 must
   not present the twelve counts as equally secure.** See appendix A5.4.
6. **And report the degradation curve, not one level.** The claim weakens smoothly as the
   permitted disagreement widens, and disappears under structural randomisation. The chapter
   should give the whole curve and let the reader decide how much disagreement with my
   matrices they think is reasonable. A single robustness percentage at a level I chose is
   exactly the kind of number this book has been wrong about before.

**What the chapter must not do.** It must not treat the two-tier split, that five Traditions
govern no consumed resource, as surviving 100 per cent of draws in any meaningful sense. The
perturbation is multiplicative, so a zero row stays zero by construction. That is a fact
about the derivation and stating it as robustness would be a straightforward overclaim.

**The Machinery.** The coupling matrix in full; the load per Tradition with unity at 6.52
against a mean near 3; the 2,000-draw robustness table with all four rows; the explicit
statement that the perturbation cannot move structural zeros.

**Risk.** This is the chapter most likely to read as numerology. The defence is that the
matrices were built by asking what each step requires and what each Tradition governs, months
before anyone tested pairing, and that the test could have come out the other way.

---

### Chapter 17. ~~What a Step Needs From a Room~~ What a Tradition Carries
~~*Target 3,500 words.*~~ **Drafted 2 August 2026, 1,685 words of main text, and retitled.**
The planned title still described the rescoped-away version. The chapter reads the coupling
column-wise, reports unity at 6.52 against a next-highest of 3.89, and spends its hardest
section answering the conflation objection below.

**Rescoped, and the reason is a real collision.** The master plan gave this chapter the
resource derivation and the group-dependence coefficients. Chapter 12 has since spent both:
it owns the eight resources, the derived coefficients, and the claim that the group is most
necessary at the two ends and least in the middle. This chapter cannot introduce material
the reader met three chapters ago.

What is left for it, and it is enough, is the other half of the coupling. Chapter 16 asks
which Tradition serves each step. This chapter asks the transpose: what each Tradition is
carrying, across all twelve steps at once.

Tradition 1, common welfare first, comes out as the most load-bearing Tradition in the
derived coupling, at 6.52 against a next-highest of 3.89. It holds that position in 100 per
cent of draws at plus or minus 30 per cent, and **75.4 per cent under full structural
randomisation**, which is the highest of any Part Four claim on that test. It is the firmest
result in this part, and "firmest" now means three quarters rather than certainty.

The chapter has to answer the obvious objection, which is that this is an artefact of unity
governing many resources rather than governing any of them strongly. The honest answer is
that this is *partly* true and is the interesting part: unity is load-bearing precisely
because it is diffuse. It is the only Tradition that supplies something to nearly every
resource, which makes it the one whose failure degrades everything at once rather than
degrading one thing badly.

Connect forward to Part Five: a group losing unity does not present with a specific
symptom.

**ANSWERED 2 August 2026, and the answer is a test rather than a reading.** Transferring
unity's governance of one resource to singleness of purpose, wholesale, one resource at a time,
flips the lead for two of the eight and not for the other six. The two are continuity and
pressure. So the finding is conditional on the judgement that unity rather than singleness of
purpose governs whether the group persists and whether it exerts expectations, and on nothing
else in the matrix. Appendix A5.4c, notebook 11d. **What is still not settled** is what Wilson
says in *AA Comes of Age* pp. 97-98, which Kurtz names as decisive and which this project does
not acquire. The chapter says so in its own notes.

**A historical objection that must be answered before this chapter is written.** Kurtz's
note 16 to his Chapter Five records that in some later AA literature the concept properly
conveyed by *single-purposed* was obfuscated by substituting *unity* as its supposed exact
equivalent, and that after Wilson's death AA itself at times fell into this. This chapter's
central finding is that Tradition 1, unity, is the most load-bearing in the derived coupling
at 6.52, with Tradition 5, single purpose, third at 3.88. **If the two terms were
historically conflated, the finding may be an artefact of how I read the Traditions when
building the governance matrix rather than a result about them.** Check Wilson's own
discussion of the First Tradition in *AA Comes of Age* pp. 97-98, which Kurtz cites as
clarifying the distinction, before drafting. This is exactly the kind of thing the book has
been wrong about before.

~~**Still to compute.** Whether the primacy of unity survives the structural test.~~
**Computed 2 August 2026: 75.4 per cent.** Notebook section 11. Unity's primacy is the only
coupling claim that survives structural randomisation at better than even odds, which makes
this chapter the most defensible in Part Four and is a reason to consider promoting it ahead
of Chapter 16 in the reading order, though not in the writing order.

---

### Chapter 18. Two Kinds of Rule
~~*Target 3,500 words.*~~ **Drafted 2 August 2026, 2,090 words of main text, and it produced
the most useful new instrument in Part Four.**

Five Traditions govern no resource that any step consumes: 4, 6, 7, 9, 10. Autonomy, no
endorsement, self-support, no hierarchy, no outside issues. In the model they act only as
multipliers on the Traditions they guard.

The claim is that this split was *derived* rather than imposed: it falls out of asking which
Traditions supply anything a step needs, and the answer divides them into enabling and
protective without anyone deciding it should.

**The honesty problem here is acute and specific.** The split cannot be tested by the
perturbation designs used elsewhere, because multiplicative perturbation cannot turn a zero
into a non-zero. Any claim that it "survives" perturbation is vacuous.

> **Partly solved 2 August 2026, and the solution is the threshold test.** Invert the question:
> ask what uniform strength a Tradition would need across its own Step's consumed resources
> before index-pairing held. One division per Step, exact, and able in principle to make any
> index-mate the principal supplier including the five with empty rows. Every threshold exceeds
> both the mean and the median live entry of the governance matrix, and at the mean live
> strength no index-mate wins. This is the only design in Part Four that could have overturned
> the five protective counts, and it does not. Appendix A5.4b, notebook 11c. **It prices the
> zeros; it does not test whether they belong there.**

The remaining and unsolved test is
whether a differently-minded person, asked to build the governance matrix from the Traditions
themselves, would place zeros in the same rows. That is not a computation. It is a question
for the reader passes, and the chapter puts it to the reader directly.

**What the chapter can legitimately claim.** That the split is coherent: the five protective
Traditions are exactly the ones phrased as prohibitions or limits rather than as practices,
and the seven enabling ones are exactly the ones that describe something a group does. That
is an observation about the text of the Traditions, checkable by anyone, and independent of
the model.

---

## 3. Definition of done, per chapter

Unchanged from Part Three, plus the appendix standard now in `../CLAUDE.md`:

1. Drafted with the four-part Machinery.
2. Every number added to `../model/book-calculations.ipynb` with an assertion, and the
   notebook re-run clean.
3. **Any figure from a stochastic run needs at least 400 seeds and a stated interval.**
   Part Four's figures are mostly deterministic matrix algebra, which is easier, but the
   chapter must say which is which.
   The release gate keeps that seed rule while expanding sensitivity perturbation coverage;
   the model's room capacity remains 60.
4. `python3 ../tools/check_chapter.py <file>` returns no FAIL.
5. Cross-checked for repetition against neighbouring chapters.
6. `../appendix/APPENDIX.md` updated in the same session if the model is touched.

---

## 4. Sequence

1. ~~**Chapter 16 first.**~~ **Done 2 August 2026.** The coupling is now introduced and
   notebook section 11b has been added beside section 11.
2. ~~**Chapter 18 second.**~~ **Done, and the sequencing paid.** Writing it second is what
   produced the threshold test, which then repaired a claim in Chapter 16. Had it been written
   third the repair would have arrived after both other chapters were settled.
3. ~~**Chapter 17 last.**~~ **Done.**

**Part Four is complete in draft.** Reading order: the plan's earlier note that Chapter 17
might be promoted ahead of Chapter 16 still stands, since unity's primacy is the only claim in
the part that survives structural randomisation at better than even odds, at 75.4 per cent. It
has not been promoted, because Chapter 17 opens by reading a table Chapter 16 introduces.

---

## 5. Risks

**Numerology.** Part Four computes a twelve-by-twelve coupling between two lists of twelve
things and reports patterns in it. That is a shape which has embarrassed better arguments.
The defences are that both matrices were built for other reasons, that the coupling is
derived rather than fitted, and that the results are reported with their robustness
unequal rather than uniformly strong.

**Vacuous robustness.** Twice now, a claim about the matrices has been stated as surviving
perturbation when the perturbation could not have disturbed it. Check, for every robustness
figure in this part, whether the design could in principle have produced a different answer.

**The single-source problem in reverse.** Part One rested too long on one paper. Part Four
rests on two matrices built by one person with no domain qualification. There is no external
check available and the chapters should say so plainly rather than compensating with
confidence.

**The reader passes matter more here than anywhere.** An AA member reading Chapter 18 can
say in five minutes whether the two-tier split reads as natural or as forced. Nothing in the
apparatus substitutes for that.

**A new copy of Part Four's figures now exists outside Part Four, added 5 August 2026.**
`reference/PRIMER-steps-and-traditions.md` restates the coupling table, the loads, the
thresholds and every robustness proportion this part reports, once per Step and once per
Tradition. It is a derived document that asserts nothing, no checker reads it, and it is
therefore a second place for these numbers to go stale. If a figure in Chapters 16, 17 or 18
moves, it has to move there in the same session. `CLAUDE.md` carries the rule.

**The primer also restates them in plain English, and that layer is the exposed one.** Each
entry has a technical statement and an interpretation of it. The interpretation is not
asserted anywhere and nothing checks that it still matches the statement above it. Part
Four's claims are the ones most easily overstated in plain language, because the honest
version of the index-pairing result is a good deal more careful than the headline: five of
the twelve counts are arithmetic rather than evidence, and the whole result rests on
magnitudes that are judgement. Any plain-English restatement that loses either of those has
made this part's central claim stronger than the chapters allow.

---

## 6. Release-gate corrections, opened 6 August 2026

The computational architecture will distinguish:

- semantic overlap \(B=S G^{\mathsf T}\);
- normalized executable coupling \(C=S_{\mathrm{norm}}G_{W}^{\mathsf T}\);
- the state-update map; and
- trajectory-level finite-difference effects.

Competition ranks will be tie-aware, structurally absent cells will be authored as such rather than numerically imputed, and the global interaction summary will report the 17 relevant cells rather than treating all 35 screen cells as substantively defined.

Tradition Three and Tradition Eleven will each be decomposed into paired \(2\times2\) mechanism checks. This round will also add an executable release checker for cache provenance, notebook execution, citation coverage, structural-null handling, and propagated headline values.
