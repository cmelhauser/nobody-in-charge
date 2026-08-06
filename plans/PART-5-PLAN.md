# Part Five: How Groups Die

Chapters 19 to 22, roughly 12,000 words.

Master plan: `../BOOK-PLAN.md`. Companions: `PART-1-PLAN.md` to `PART-4-PLAN.md`. Technical
apparatus: `../appendix/APPENDIX.md`. Computation: `../model/part5_runs.py`, cached in
`../research/part5.json`, verified in notebook section 14.

**Written 2 August 2026, after Parts One to Four were drafted and after the runs were made.**
This is the only part whose plan was written with its numbers already in hand, which is why it
is shorter and more specific than the others. It is also the part where the simulation does the
most work and therefore the part where the sensitivity discipline matters most.

---

## 1. What Part Five is for

Part One showed a movement dying and could not say why with any precision, because the record is
thin and curated. Parts Two to Four built the apparatus. Part Five turns the apparatus on the
question Part One could not answer: what does a group's death actually look like, from inside and
from the outside, and would anyone notice in time.

The answer the model gives is uncomfortable and it is the spine of the part.

**Referral loss is the most closure-prone failure, and conditioning can hide part of its
decline.** The corrected trajectory does not support the earlier claim of no internal warning:
among viable groups, membership falls from 22.07 at year five to 16.47 at year ten and 11.39 at
year twenty. Established practice remains high and even rises among the small selected remnant,
but room size provides a visible warning. The part therefore treats selection as a threat to
interpretation, not as evidence that decline is wholly invisible from inside.

---

## 2. What the runs establish

4,800 runs, 400 seeds per condition, thirty-year horizon. Notebook section 14.

**The three fingerprints, at year 10 and year 30.** Quality is established-member practice
conditional on endpoint viability, defined as more than five members.

| Failure mode | Viable, y10 | Members if viable, y10 | Quality y10 | Viable, y30 | Quality y30 |
|---|---|---|---|---|---|
| nothing wrong | 0.9975 | 29.40 | 0.302 | 0.985 | 0.265 |
| invisible: pure attraction loss | 0.9925 | 12.99 | 0.295 | 0.985 | 0.259 |
| unreferred: no exogenous inflow | 0.660 | 16.47 | 0.348 | 0.0275 | 0.364 |
| unwelcoming: both Tradition 3 paths lost | 0.905 | 15.70 | 0.360 | 0.5475 | 0.321 |

Three distinct shapes, and they fail in different organs:

- **Invisible** groups, defined by pure loss of the Tradition 11 attraction path with its
  governance path intact, shrink without closing in the 400 runs.
- **Unreferred** groups shrink sharply and close in 89.5 per cent of runs by year thirty.
  Their conditional practice looks high because only eleven viable runs remain.
- **Unwelcoming** groups lose both Tradition 3 resource governance and inverse-practice
  dropout protection. They close in 25 per cent of runs and remain viable in 54.75 per cent.

**The Tradition 3 sweep.** At full adherence the thirty-year mean is 17.80 and endpoint
viability is 98.5 per cent. Losing both Tradition 3 paths lowers the mean to 6.755, existence
to 75.0 per cent and viability to 54.75 per cent. The separate factorial shows resolved losses
through both resource governance and dropout friction, plus a non-additive interaction.

**Composition is unresolved.** Against even founders, the paired final-membership contrast is
0.293 for concentrated practice with a 95 per cent interval of -0.898 to 1.483, and -0.348 for
split practice with an interval of -1.472 to 0.777. No equivalence margin was specified, so
these intervals do not establish equality or irrelevance.

---

## 3. Chapter plan

### Chapter 19. You Cannot Close the Door
*Target 2,000 words of main text.*

Tradition 3 is the only Tradition that removes an option rather than adding one. A group cannot
refuse admission, so the released model does not encode the mechanism as a closed-door arrival
ban. It uses two separate paths: resource governance and dropout friction that is strongest at
low practice. Low practice is not tenure, so the chapter must not call this a newcomer-only path.

The chapter's spine is the sweep, read as a price list. And its sting is that the price is paid
in several currencies: membership, existence, viability, closure and practice among the
remaining viable groups. The conditional practice comparison cannot substitute for the
membership and closure series.

**Must state.** That the survival figures at T3 = 0.75 and T3 = 1.00 overlap and must not be read
as a peak at three quarters.

### Chapter 20. Three Ways to Starve
*Target 2,500 words.*

The table above, in prose, with the mechanism for each. The organising claim is that the three
failure modes have different trajectories and mechanisms. Conditional practice can mask the
severity of referral loss, but the corrected room-size trajectory also provides visible warning.

**Must state.** That quality is conditional on survival, that this is why the unreferred row
looks good, and that the conditioning is doing real work rather than being a footnote.

### Chapter 21. The Healthy-Looking Corpse
*Target 3,000 words. The strongest chapter in the part.*

Take the unreferred trajectory alone and follow it year by year. At year 5, 97.0 per cent are
viable, with viable groups averaging 22.07 members and established practice 0.348. At year 10,
66.0 per cent are viable, averaging 16.47 and 0.348. At year 20, 17.25 per cent are viable,
averaging 11.39 and 0.355. At year 30, only 2.75 per cent are viable; their practice estimate is
0.364 with a wide interval because it comes from eleven runs.

The unconditional mean falls to 0.51 and 89.5 per cent of groups close. The selected practice
series looks strong, but the viable-room membership series declines too. The earlier claim that
no surviving group looks ill is withdrawn.

Then back to Part One. This is what the Washingtonian record looks like: societies that were
flourishing in the accounts right up to the point where there are no more accounts. The chapter
should be careful here, because it is offering a mechanism for an absence of evidence, which is
the most seductive and least testable kind of argument in the book.

**Must state.** That this is a selection effect, that the book relies on it here and warns
against it elsewhere, and that the difference is whether the conditioning is reported.

### Chapter 22. What You Cannot Engineer
*Target 2,500 words. The weakest, and the one needing an acquisition.*

The question is whether a group could be improved by arranging who is in it: seeding a new
meeting with strong members, or spreading experience evenly, or concentrating it.

The model comparison is paired and unresolved. Founder states affect every state-dependent
channel, not only two paths, and the confidence intervals cross zero. With no prespecified
equivalence margin, the result cannot establish that composition does not matter.

What carries the chapter is the outside literature, and **that is the acquisition this part
needs**: Carrell, Sacerdote and West on what happens when peer groups are optimally engineered
from previously observed peer effects. It is cited in `../BOOK-PLAN.md` and has never been read.
Without it the chapter is a null result and an apology. With it, the chapter is about a real and
replicated finding that engineering peer composition backfires, and the model's null becomes a
minor corroboration rather than the argument.

~~**Do not draft Chapter 22 until Carrell, Sacerdote and West is in hand.**~~ **Obtained and read
2 August 2026** and the chapter was rewritten from 762 words to 1,297 the same day. Their own
model predicted a gain of 0.053 grade points for the students they set out to help; the measured
treatment effect was minus 0.061, and the mechanism was homophily, the students re-sorting inside
the squadrons that had been built for them. The chapter now leads with that and uses the model's
null as the minor corroboration it is. **Part Five has no outstanding acquisitions.**

---

## 4. Definition of done, per chapter

As Parts Three and Four, plus:

1. Every stochastic figure at 400 seeds with an interval, from `research/part5.json` and not
   carried by hand.
   Expanded robustness comes from more perturbation points in the sensitivity suite, not a
   change in modeled group size or in this trajectory cache's seed count.
2. **Every quality figure states whether it conditions on survival**, because in this part the
   conditioning is the finding rather than a caveat.
3. `python3 ../tools/check_chapter.py <file>` and `python3 ../tools/check_book.py` clear.
4. Appendix updated in the same session if the model is touched. It was not touched: every run
   here uses the model as it stands, and `part5_runs.py` duplicates three lines of `simulate()`
   for the composition experiment rather than changing its signature, because eleven other
   scripts reference it and a signature change would invalidate their caches.

---

## 5. Risks

**The selection effect is a finding and a threat at once.** Conditioning on viability produces
a high practice series while most groups close. It does not erase the decline in viable-room
membership, so Chapter 21 must present both and must not revive the stronger invisibility claim.

**Explaining an absence.** Applying the healthy-looking-corpse mechanism to the Washingtonian
record explains why there is no record of decline. An explanation of missing evidence cannot be
checked against the missing evidence. State it as a candidate mechanism, not as a finding.

**The composition contrast is unresolved, not an equality result.** See section 3.

**Nothing here is validated against a real group.** Threat 2 in appendix A7 applies to this part
more than to any other, because Part Five is the only place where the model's *trajectories*,
rather than endpoint contrasts, are the object of interest. Endpoint orderings and
trajectories have different robustness records and must be reported with their design and
conditioning; neither receives a blanket sensitivity claim.

**A second copy of this part's figures now exists, added 5 August 2026.**
`reference/PRIMER-steps-and-traditions.md` restates the four decline conditions at year
thirty and the whole Tradition 3 sweep, under Traditions 3 and 11. It is derived, it asserts
nothing and no checker reads it, so a corrected figure here has to be carried there in the
same session. The specific risk for this part is that the primer's plain-English layer
states the referral-versus-attraction result, whose wording matters most. Under the corrected
mean-one capability model, referral loss is worse than pure attraction loss on existence,
endpoint viability and mean final membership in the base architecture and all four tested
variants. The expanded parameter screens still report strict orderings, ties and reversals
separately for each outcome. A plain restatement must name its outcome and design rather than
turning either finite audit into a universal claim.

---

## 6. Release-gate corrections, opened 6 August 2026

Outcome reporting will separate endpoint existence, endpoint viability, final membership, first crossing below the viability threshold, recovery after crossing, and permanent closure. \(N=0\) remains absorbing; \(0<N\leq5\) is an outcome threshold, not an absorbing model state. “Steady state,” “survives forever,” and similar language is prohibited unless mathematically established.

The Tradition Eleven headline will use the clean attraction-only contrast, with the mixed governance-plus-attraction intervention reported separately. Tradition Three will likewise separate the governance and dropout-friction paths and will use the low-practice label rather than “newcomer” where tenure is not measured.

Composition effects will be reported as paired but unresolved unless a design identifies recruitment selection separately from incumbent response. Required simulation histories and event fields must make first-passage and recovery claims auditable.
