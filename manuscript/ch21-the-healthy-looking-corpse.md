# Chapter Twenty-One
## The Healthy-Looking Corpse

Take the unreferred group on its own and follow it for thirty years.

At year five, every group still exists and 97.0 per cent remain viable above five members. The viable groups average 22.1 members and their established members sit at 0.348 on the practice scale, above a healthy group's 0.322.

At year ten, 94.8 per cent still exist but only 66.0 per cent remain viable. The viable groups average 16.5 members, at 0.348, still above a healthy group's 0.302.

At year twenty, 42.5 per cent still exist and 17.3 per cent remain viable. The viable subset averages 11.4 members, at 0.355, above a healthy group's 0.273.

At year thirty, 10.5 per cent still exist and 2.75 per cent remain viable. The eleven viable groups average 12.3 members, at 0.364, above a healthy group's 0.265.

Read those columns down. Membership falls from 22 to 12 while established practice stays high. The practice reading looks healthy; the room count does not.

Now read the existence column down. One hundred per cent. Ninety-five. Forty-three. Eleven. The viable column falls faster still.

Almost nine in ten groups are closed. The selected survivors look strong on practice, but they look small. The earlier chapter title overstates what the corrected model shows.

---

I want to be careful about what is and is not surprising here.

The arithmetic is not surprising. If a process kills groups outright rather than degrading them, then obviously the groups that remain are undegraded, and the average over survivors will not move much. Anybody would predict that on a moment's thought. It is the same reason the average height of people in a room does not change when you remove the ones who left.

What survives correction is a narrower divergence. The unconditional membership series, which counts a closed group as zero, falls from 30.4 members at year two to 0.51 at year thirty, a 98 per cent collapse. Membership among viable groups falls from 30.4 to 12.3, which is also severe. Established practice among that selected subset remains high and ends above the healthy comparison.

One process. Three estimands. Existence, viability and membership all say catastrophe; conditional practice does not. All are correctly computed from the same runs.

---

Which of the two numbers can anybody actually see?

A member sees one group. Their own. They can see its room count and its practice culture, but they cannot see the groups that have already closed. In the corrected runs their own shrinking room is a warning; the apparently strong practice of those left is the misleading signal.

A group secretary sees the same thing with better records.

An area committee sees more, and this is the first level at which the unconditional series is visible at all, because an area committee knows how many groups it had last year and how many it has now. Whether it *notices* is a different question, since a group that stops meeting is usually explained by something specific: the church wanted the room back, the man who chaired it moved away, the Tuesday group merged with the Thursday one. Every death has a proximate cause and the proximate causes are all true.

The full closure rate is legible only at a level of aggregation above the individual group, and only if somebody there counts births and closures separately over a long enough series. The within-group decline is legible sooner through attendance. The two levels answer different questions.

That is a demanding set of conditions and it is worth saying plainly that AA meets more of them than most voluntary organisations, because it has counted its groups for decades and publishes the counts.

---

Here is where this connects back, and where I have to be most careful in the whole book.

Part One asks why the Washingtonians vanished and finds a record that is thin in a specific way. There is an enormous amount of material about the movement flourishing and very little about it declining. Maxwell's account of the fade is largely an account of the *cause* dissolving into the temperance movement, and Krout's is about the movement's structural weaknesses, and neither has much to say about what it looked like in a room in Baltimore in 1847, because nobody wrote that down.

The standard reading of that silence is that the movement collapsed quickly and its members had better things to do than document it.

This model offers a narrower reading. If the Washingtonians were in the unreferred condition permanently, the societies that had stopped existing were not there to describe themselves, and the practice quality of selected survivors could remain high. But the corrected simulation also predicts visibly shrinking rooms. It therefore cannot explain the historical silence by invisibility alone.

The process can bias the record toward functioning survivors, but it does leave a membership trace inside them. The earlier categorical explanation of the thin record is retired.

---

That is an attractive argument and its attractiveness is the problem with it.

It explains an absence of evidence. Arguments that explain absences of evidence are the most flattering and least testable kind, because the thing they predict is the thing already observed, and no further observation can bear on them. I could construct three other mechanisms that predict exactly the same silence and I would not be able to choose between them.

There is also a specific reason to distrust it here. The claim requires that individual Washingtonian societies were dying while the survivors looked healthy, and the evidence that survivors looked healthy is exactly the evidence a curated record would produce anyway, since the movement's own publications had every reason to print accounts of societies doing well. Chapter Two shows Marsh curating that record in precisely this direction. So the observation the mechanism explains is also an observation the curation explains, and the two are not distinguishable from what survives.

What the model contributes is therefore narrower than it first appeared. It does not show that the Washingtonians died this way. It shows that conditioning on surviving organisations can preserve a healthy-looking practice measure while closures accumulate, and that absence of decline narratives is not evidence of absence. It does not show that surviving societies would have missed their falling attendance.

---

One further thing follows, and it is the most practical claim in Part Five.

If a fellowship wants an early warning of this failure, practice quality alone is inadequate. Individual groups can track attendance, while the fellowship has to count group births and closures over a long enough window that changing rates are separable from noise.

Those measurements are complements. A room can see itself shrinking; only the wider fellowship can see how often rooms disappear.

The next chapter takes the opposite question, which is whether anything about the composition of a room can be arranged to make it better, and finds that the model says no and could hardly have said otherwise.

---

## The Machinery

### 1. What the model says

Nothing in this chapter is a new mechanism. It is the unreferred condition from the previous chapter, read as a time series rather than as an endpoint, and split into its conditional and unconditional forms.

The reason the estimands diverge is structural and worth stating. Setting exogenous inflow to zero makes arrivals strictly proportional to current twelfth-step practice. Zero is absorbing. The corrected outcome distribution contains mass at closure, a set of extant but nonviable groups, and a small viable tail; it should not be reduced to a binary alive/dead label.

Conditioning is what makes the practice mean incomplete. The mean among eleven viable endpoints says nothing about the 358 closed runs or the thirty-one extant runs at one to five members.

### 2. The technical version

400 paired seeds, thirty-year horizon, dt of half a week, membership and practice sampled yearly. `model/part5_runs.py`, cached in `research/part5.json`. Existence is N > 0, viability N > 5, and closure N = 0. Proportions use Wilson intervals; means use 95 per cent half-widths.

The unreferred condition, both views:

| Year | Exists | Viable | Members, all runs | Members, viable runs | Established practice, viable runs |
|---|---|---|---|---|---|
| 2 | 1.000 | 1.000 | 30.38 ± 0.70 | 30.38 ± 0.70 | 0.3585 ± 0.0049 |
| 5 | 1.000 | 0.970 | 21.55 ± 1.01 | 22.07 ± 1.00 | 0.3479 ± 0.0058 |
| 10 | 0.9475 | 0.660 | 11.68 ± 1.02 | 16.47 ± 1.18 | 0.3475 ± 0.0084 |
| 20 | 0.425 | 0.1725 | 2.50 ± 0.48 | 11.39 ± 1.37 | 0.3547 ± 0.0206 |
| 30 | 0.105 | 0.0275 | 0.51 ± 0.23 | 12.27 ± 3.81 | 0.3642 ± 0.0443 |

For comparison, viable baseline groups average 29.40 members and 0.3016 established practice at year ten, and 18.00 members and 0.2648 at year thirty; viability is 98.5 per cent at the endpoint.

**The quality comparison still has the misleading sign.** At years ten, twenty and thirty the viable unreferred subset is respectively 0.046, 0.081 and 0.099 above viable baseline groups. But its membership is lower at every one of those horizons, so practice is not the only dimension a member can perceive.

**Why the late conditional estimates are imprecise.** The viable subset falls from 264 runs at year ten to eleven at year thirty. The membership half-width expands to 3.81 and the practice half-width to 0.044. The final conditional mean is a description of eleven selected runs, not a stable population estimate.

**The selection is the remaining finding and it is also a threat.** Every conditional figure is labeled and both existence and viability appear beside it. Dropping either column would turn a selected-subset comparison into a population claim.

**What is not shown.** Whether real groups die bimodally. The bimodality follows from the absence of an additive inflow term, which is a modelling choice justified in Chapter One by the historical claim that no referral system existed in 1840. If a real unreferred group has any floor at all, however small, the process is no longer absorbing and the shape of this chapter changes.

### 3. Notes on sources

**The historical application is a candidate mechanism and not a finding, and the chapter says so twice.** I want it recorded here as well. The argument is that the thinness of the Washingtonian decline record is consistent with a failure mode that leaves no trace in surviving institutions. It is consistent with several other explanations, including the one Chapter Two documents at length, which is that the record was curated by a man with an interest in what the movement should have been. The two explanations predict the same silence and nothing in the surviving material distinguishes them.

**The claim about AA's group counts is now specific, and the series has still not been obtained.** The document is service material SMF-132, *Estimated Worldwide A.A. Individual and Group Membership*, published by the General Service Office as a table of groups and members by year. That is the right instrument for the test this chapter proposes and it is named here so a future session does not have to find it again. It was located on 2 August 2026 and not read: it is distributed as a PDF under an AA World Services content-use policy permitting a single printed copy, and this project does not acquire AAWS publications on the book's behalf. Two further limitations would remain even with it in hand. The series is worldwide rather than regional, so the natural experiment the chapter proposes, a region whose referral pipeline changed sharply, would need finer data than SMF-132 carries. And a count of groups is not a count of group deaths, since the total moves with births as well.

**Nothing here is validated.** The trajectories are model output and have never been compared against a real group. The expanded sensitivity suite measures dependence on authored choices; it does not validate the durations, the absolute group sizes or the historical application.

### 4. References

**Read in full:**

Maxwell, M. A. (1950). "The Washingtonian Movement." *Quarterly Journal of Studies on Alcohol* 11: 410-452. Saved under `research/incorporated/Maxwell_1950/`; see Chapter One for the note on the retyped copy. Used here only for the character of the decline record, which is discussed at length in Chapter Two.

Krout, J. A. (1925). *The Origins of Prohibition.* New York: Alfred A. Knopf, chapter IX. Saved in `research/`. Used here for the same purpose.

**Cited at a remove:**

Nothing.

**Internal, and reproducible from this repository:**

`model/part5_runs.py`, `research/part5.json`, `model/book-calculations.ipynb` section 14. `appendix/APPENDIX.md` A4 for the selection threat, A7.1 for what no design covers, A11 threat 2 for the absence of external validation.

**What was not read:**

SMF-132, discussed above. I have not obtained it. Also not read: any survival analysis of voluntary associations that would say whether bimodal group mortality is a real phenomenon or an artefact of this model's inflow structure. The chapter's central mechanism therefore has no empirical corroboration of any kind, and a reader should weigh it as an argument about a model rather than a claim about the world.
