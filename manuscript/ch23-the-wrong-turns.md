# Chapter Twenty-Three
## The Wrong Turns

This chapter is a list of everything I got wrong.

Not everything I am unsure about, which is Chapter Twenty-Four, and not everything the method cannot reach, which is Chapter Twenty-Five. This is the record of specific, identifiable errors that were in the work and are no longer, together with what each one took to find.

I am including it for a reason that is not modesty. The errors sort themselves into three kinds, and the three kinds were caught by three completely different instruments. That pattern is the most useful thing this book has to say about how to do work of this sort, and it would be invisible if I reported only the corrected version.

---

The first kind is a **modelling error**, and the distinguishing feature is that no amount of reading would have found it.

I built the model with a single equilibrium. Members' practice grew toward one attractor and, whatever you did to the group, it approached that attractor from wherever it started. This is a very natural thing to build and it makes collapse mathematically impossible, which I did not notice until I tried to simulate a group dying and found I could not. I added a Hill-function gate because the relapse literature motivates nonlinear dynamics. The release audit then found that the corrected model's actual endpoint environments rarely support the typical-member bistability I claimed for that gate. Chapter Fourteen now records both corrections.

I had the protective Traditions entering as multipliers that compounded. A group at uniform 0.8 adherence collapsed in every parameterisation I tried, which seemed like a finding until I worked out why: a twenty per cent shortfall passing through four or five multiplications comes out closer to fifty. The adherence terms are averaged within brackets now and applied once each, and Chapter Five's Machinery says so.

I had the recipient resource proportional to the raw number of newcomers, so that a room full of newcomers with nobody to help them registered as a room rich in the thing twelfth-step work consumes. It is now low-practice members per high-practice potential helper. That is still a proxy, not a newcomer or sponsorship measure, because the model stores neither tenure nor matching.

I had newcomer dependence bolted on as a term I inserted by hand, rather than falling out of what each step consumes. The eight-resource derivation replaced it, and the derived version is what Part Four is built on.

I keyed dropout to the mean across all twelve steps, which makes a member who has done Step One and nothing else look identical to a member who has done nothing at all. It is keyed to early-step practice now, which is why Chapter Nineteen's friction term is strongest at low practice. The model records no tenure, so it cannot identify newcomers or veterans.

I calibrated the baseline on a ten-year horizon and then reported thirty-year results from it, so the model was tuned to a group that had not yet finished settling.

I wrote a noise-floor check that used the same seeds on both sides of the comparison, so it measured nothing and reported zero, which looked like a very clean result.

And I quoted Monte Carlo figures to three significant figures from ten seeds. That error was real, but its first repair exposed another. The ten-seed referral-starved result of 0.20 viable and 2.9 members became 0.360 and 9.9 at four hundred seeds under the old model. Then the release audit found that individual capability had been drawn from an uncentred lognormal distribution, silently raising its mean above one. With the distribution corrected to mean one, the four-hundred-seed result is 0.0275 endpoint viability, 0.105 existence, 0.895 closure and 0.51 mean membership. The first change was sampling error; the second was a modelling error. Both are retained here because collapsing them into one correction would hide what each check found.

Every one of those was invisible until something was computed. Reading more history would not have touched any of them.

---

The second kind is a **research error**, and the distinguishing feature is the mirror image: no amount of computation would have found it.

I had the index-pairing conjecture in my head as something worth testing because there are twelve Steps and twelve Traditions. That is not an error, but the way I first framed the result was: I described the failure of index-pairing as a finding on twelve independent counts, when five of the twelve follow from a single prior fact about the governance matrix. Chapter Sixteen now says so and Chapter Eighteen repairs part of it.

I had Hawkins losing two wives, from a secondary site. Maxwell's account has his wife supporting him through withdrawal. She was there the whole time.

I had a Worcester statistic attributed to Maxwell that is not in Maxwell at all. He has better-documented equivalents from Cincinnati, Brattleboro and Vermont, and the Vermont figure is more dramatic than the one I had been using.

I treated Gough's account of his 1845 relapse as defensive, until I read it and found the sentence *I have fallen*.

I attributed the 1858 libel trial to the 1845 relapse. It arose from a dispute about prohibition enforcement, thirteen years later and about something else.

I cited Crothers's 1911 book for the founding rationale of the Sons of Temperance. He does not mention the Sons anywhere. That material is Eddy's, and the misattribution was caught by a checking script on its first run rather than by me.

I said the Washingtonians had no rule against outside issues and therefore no way to decline the temperance movement's turn to legislation. They had two, in print, within two years of founding. Their own manual contains them and I had not read their own manual.

I said Maxwell was precise about all three founding dates. He gives two and then says the pledge was signed the next day.

I said the period's vocabulary distinguished at least eight grades of drinker. Maxwell lists ten.

I said the Traditions were a set of rules. Wilson's own framing sentence says a code of traditions could never become rule or law.

I said the Traditions were adopted at a 1950 international convention. Kurtz dates the adoption to June 1950 and does not connect it to that gathering.

Every one of those became visible the moment a primary source was in front of me, and not one minute before.

---

The third kind is an **institutional error**, and I did not catch it at all.

I built a scenario in which an AA group closes its doors to newcomers. A reader with experience of the fellowship pointed out that Tradition Three makes this impossible: there is no membership decision to close off, because the Tradition removes it. Whatever an unwelcoming group does, it does after the person is already a member. A second correction to the same chapter came later and from anticipating the same reader: I had been using "closed" for that culture, and a closed meeting is a formal and entirely ordinary category in the fellowship, meaning one restricted to people with a desire to stop drinking.

That correction produced Chapter Nineteen, which is now a chapter about retention rather than admission, and it produced a structural test in the appendix showing that the alternative reading makes zero adherence equivalent to a group that admits nobody and dies in every run. The corrected version is better than the original in a way I could not have reached by myself, because the thing I was missing was not in any document.

---

Three kinds, three instruments, and the instruments do not substitute for each other.

The model errors were found by simulation. Specifically, by trying to make the model do something and failing, which is a different activity from checking that it runs.

The research errors were found by reading primary sources at length. Not by checking citations, which would have caught the Crothers misattribution and none of the others, but by reading whole documents and noticing that they did not say what I had them saying.

The institutional error was found by a person with standing I do not have.

If I had done only the first, I would have a well-tested model of a fellowship that does not exist. If I had done only the second, I would have a well-sourced history with a broken model underneath it. If I had done only the third, I would have neither.

---

There is a fourth category that I want to name separately, because it appeared late and it changed how I work.

Several of the errors above were caught by assertions rather than by me. The practice is simple: every number printed in the book is also written into a notebook cell with an assertion that it equals what the computation produces. The point is not that the assertions verify the numbers. It is that writing an assertion forces you to state the relationship you think holds, and stating it is what exposes the ones that do not.

Five errors in this book were caught that way, and every one was a claimed relationship rather than a modelling fault. I wrote that a range of thresholds sat inside another range; it did not, it extended below it at both ends. I wrote that a Tradition stripped of two resources fell to fourth place; it fell to third. I wrote a constant as 0.2769 when it was 0.2269. In each case the sentence was in a draft, the assertion failed on its first run, and the sentence was corrected before anyone read it.

An assertion detects drift, not error. It cannot tell you that a number is wrong, only that it has changed. But an assertion about a *relationship*, of the form "this range contains that one" or "these two figures are equal", is a different instrument, and it catches the thing you were sure of.

---

The last correction is the one I like least, and it is the most recent.

The single most robust comparison in the simulation is between a group starved of referrals and one that has lost only its attraction path. Earlier drafts said that comparison survived 236 quarter-step perturbations and four architectural changes. Those numbers belonged to the retired capability-inflated model and to a narrower sensitivity design.

I never said what worse meant.

The release audit retested five architectures at 400 paired seeds per condition: the base model, a flat step gate, Tradition Three moved to admission, capacity supplied by all members, and unsaturated resource counts. In the corrected model the referral-loss condition has lower existence, lower endpoint viability and lower mean final membership than pure attraction loss in all five. The former three-of-four size reversal does not reproduce. Parameter screens still report strict, tied and reversed draws separately, because agreement across five architectures is evidence over those architectures, not a universal theorem.

That correction is the argument for this whole chapter. A result can change because the model changed, because the estimand changed, or because the earlier audit sampled too narrowly. Keeping the old structural conclusion after changing the capability distribution would have been as misleading as never testing the architecture at all.

---

## The Machinery

### 1. What the model says

Nothing new. This chapter is about the model's history rather than its output, and every figure in it is quoted from the chapter where it belongs.

One structural observation is worth making here because it does not fit anywhere else. Of the nine modelling errors listed above, seven were errors in which the model was **too well behaved**: a single equilibrium so collapse was impossible, a resource that grew without a constraint, a dropout hazard that could not distinguish a beginner from a newcomer, a noise floor of zero. Only two, the compounding multipliers and the ten-seed sampling, made the model behave worse than it should.

That asymmetry is not an accident and it is a hazard worth naming. A model that misbehaves gets debugged, because it is annoying. A model that behaves smoothly is finished. Every one of the seven survived until something specific was demanded of it that it could not do.

### 2. The technical version

The corrections, with what found each one and where the corrected version lives.

| Error | Found by | Now in |
|---|---|---|
| Single equilibrium, collapse impossible | trying to simulate a death | Ch 14, appendix A2 |
| Adherence compounding multiplicatively | a group at 0.8 collapsing everywhere | Ch 5 Machinery, A2 |
| Recipient resource on raw newcomer count | Worcester not reproducing | Ch 1 Machinery |
| Newcomer dependence inserted by hand | the eight-resource derivation | Part Four |
| Dropout keyed to the twelve-step mean | Ch 19's retention question | A2 |
| Baseline calibrated on ten years, reported at thirty | horizon study | A3 |
| Noise floor using the same seeds twice | reading the check | A4 |
| Three significant figures from ten seeds | recomputing at 400 | Ch 1, 2, 4, 14, preface, A4 |
| Uncentred lognormal capability changed both mean and dispersion | release-gate distribution audit | Ch 4, Ch 12, appendix |
| Semantic overlap published as executable coupling | source-to-code trace | Parts Three and Four, paper, appendix |
| Recipient ablation changed several mechanisms | one-mechanism override | Ch 15, primer, appendix |
| T3 and T11 interventions mixed two paths | paired two-by-two factorials | Ch 19, Ch 20, paper |
| Endpoint viability described as survival or death | event-history audit | Ch 1, Ch 2, Part Five, paper |
| One-draw recovery exercise and overclaimed estimator | 25 then 400 replications, claim narrowed | Ch 13 |
| Frozen Chapter 14 environment came from the retired model | re-estimating 400 endpoint environments | Ch 14, paper |
| Composition null narrated as equality | paired intervals and estimand review | Ch 22, paper |
| Exact ties broken by ordinal ranking | competition-rank audit | Ch 16, primer, paper |
| Public notebooks and caches lacked complete dependency identity | release checker and notebook rebuild | both notebooks, all current caches |
| Index-pairing as twelve independent counts | the trivial-count decomposition | Ch 16, Ch 18 |
| Hawkins's two wives | Maxwell, read in full | Ch 1 |
| A Worcester statistic not in Maxwell | Maxwell, read in full | Ch 1 |
| Gough's 1845 account read as defensive | Gough, read at source | Ch 3 |
| The 1858 trial attributed to the 1845 relapse | Gough, read at source | Ch 3 |
| Crothers cited for the Sons of Temperance | the sources checker, first run | Ch 2 |
| The Washingtonians had no rule on outside issues | Grosh 1842, read at source | Ch 1, Ch 2 |
| Maxwell precise about three founding dates | Maxwell, read from a saved copy | Ch 1 |
| Eight grades of drinker | the same | Ch 1 |
| The Traditions described as rules | Kurtz, quoting Wilson | Ch 5 |
| Adoption at a 1950 convention | Kurtz | Ch 5 |
| A group closing its doors | a reader who had been in the rooms | Ch 19, A9 |
| Threshold range containment | a notebook assertion | Ch 18 |
| A rank stated as fourth | a notebook assertion | Ch 17 |
| A constant transcribed as 0.2769 | a notebook assertion | Ch 22 |
| "Worse" undefined in the book's strongest claim | structural variants, appendix A9 | preface, Ch 1, Ch 4, A9 |

The table no longer has the tidy count this chapter once reported. The release-gate audit added
distributional, semantic, estimand and reproducibility errors that cross the earlier categories.
That loss of neatness is itself accurate: code inspection, simulation, source reading,
institutional review and cross-artifact verification caught different classes of failure.

**A count I am not going to give.** How long each error was in the manuscript before it was caught. The progress log carries no dates, so any such claim would be unverifiable, and this project has already written two duration claims it could not support.

### 3. Notes on sources

**This chapter is sourced entirely from `research/progress-log.md`**, which is the running record of corrections, and every entry above is traceable to an entry there. Where the log and my memory disagree, the log wins, and it has won twice.

**Two claims about this project's own history were themselves wrong** and were removed rather than corrected, because there was nothing to correct them to. One asserted a number of shared phrases between two chapters that appears nowhere in the log. One asserted that an error had stood for months, which the log cannot support because it is undated. Both were written by me about my own work, which is the least reliable kind of testimony in this book and the kind a reader can least easily check.

**The institutional correction is reported at one remove and cannot be otherwise.** It came from a reader rather than a document. I have recorded what was said and what it changed, and there is nothing to cite.

### 4. References

**Read in full:**

Nothing new to this chapter. Every source named above is cited in the chapter where the correction landed.

**Cited at a remove:**

Nothing.

**Internal, and reproducible from this repository:**

`research/progress-log.md` for every entry in the table. `model/book-calculations.ipynb` for the assertions that caught three of them. `appendix/APPENDIX.md` A4 for the small-sample errors, A7.3 for the structural variants that split the final claim. `tools/check_book.py` for the sources check that caught the Crothers misattribution.

**What was not read:**

Nothing applicable; this chapter reads only its own project.
