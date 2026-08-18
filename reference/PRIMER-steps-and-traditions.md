---
title: "What the Model Says About the Twelve Steps and the Twelve Traditions"
subtitle: "A reference primer for *Nobody in Charge*"
author:
  - "Human Author: Christopher Melhauser"
  - "AI Writing Collaborator: theonlymuffinbot"
  - "Models: Anthropic Claude Opus 5; OpenAI GPT-5.6 Sol/Terra"
date: "6 August 2026"
---

Released to the public domain under The Unlicense. See the repository's attribution and license
notices. The AI writing collaboration used a mix of Anthropic Claude Opus 5 and OpenAI GPT-5.6
Sol and Terra models.

## How to read this

This is a reference document, not a chapter. It gives one short finding for each
Step and each Tradition, and it exists so that a reader who wants to know what the
model says about a particular item does not have to reconstruct it from six chapters.
Everything here is drawn from the manuscript and is reproducible from
`model/book-calculations.ipynb`. Nothing here is new.

Every entry comes in three parts. **Technical** states the result and its provenance.
**What was assumed** says, in the same plain language as the rest, which numbers in that
row somebody chose rather than measured, and what would follow if the choice were wrong.
**In plain terms** says what the result would mean to somebody sitting in a room, and
says so without arithmetic. The third part is an interpretation of the first and is
softer than it. Where the plain reading would carry further than the technical one
supports, the entry says where it stops.

The middle part is there because the arithmetic in this document is exact and its inputs
are not. Every figure in Part Four is a correct calculation on two tables that one person
wrote down from reading, and a reader who sees only the technical line can easily mistake
the precision of the calculation for the precision of the inputs. Reading the assumption
beside the result is the intended use of this primer.

Three different instruments produce the findings below, and they are not
interchangeable. Every entry says which one it used.

**Algebra.** Exact calculation on two fixed matrices. The consumption matrix S is
twelve Steps by eight group resources. The governance matrix G is twelve Traditions
by the same eight resources. Their product

> B = S G'

gives the demand each Step places on resources each Tradition governs. These figures
carry no sampling error. They are also no better than the two matrices, both of which
one person built, and the largest outstanding item in the whole project is a second
reader marking which of the ninety-six governance cells are non-zero.

**Deliberation.** Closed-form results from Golub and Jackson's 2010 theorem on naive
learning. These concern how a room's consensus tracks the truth as the room grows.
They are exact and they involve no simulation.

**Simulation.** Monte Carlo runs of the group model. Every figure quoted here comes
from at least 400 seeds and carries an interval.

---

## Five standing cautions

**One. The coupling is not used by the simulation.**

*Technical.* B = S G' is a derived object. No entry of it was chosen and no entry of
it feeds a run. It is a description of the two matrices, and it inherits every
judgement in them.

*In plain terms.* The table matching Steps to Traditions was not built by watching
groups. It falls out of two lists somebody wrote down: what each Step needs from other
people, and what each Tradition looks after. If those two lists are wrong, everything
in Part Four is wrong with them, and no amount of computing will reveal it.

**Two. At full adherence the governance matrix cancels exactly.**

*Technical.* It is column-normalised, so when every Tradition is at 1.0 the governance
quality of every resource is identically 1. Thirty-five of the model's 118 registered
sensitivity values cannot affect a fully adherent group at all. The count is not the total
number of authored choices in the model.

*In plain terms.* In a group doing everything right, the Traditions do not show up in
the numbers, because there is nothing left for them to fix. Everything the model says
about individual Traditions is a statement about groups falling short somewhere, which
is every real group. The Traditions are visible only in the breach.

**Three. Sensitivity screens bound claims; they do not make them universal.**

*Technical.* The project uses global, targeted, screening and structural designs with
different estimands and power. A claim can receive strict support, tie, reverse, or remain
unresolved. The corrected audit reports those categories separately and does not turn
finite parameter ranges or five-seed screens into statements that a result holds for every
possible model. Mortality, endpoint viability and final membership are separate outcomes.

*In plain terms.* Repeated tests can make a model result more or less credible inside the
model, but they cannot make it a law about every specification or a forecast about AA.
Read each simulation statement with its outcome, comparison, range and uncertainty. A
direction that repeats is stronger than one that reverses, and an unresolved comparison
is not evidence of no effect.

**Four. The degradation figures rank one outcome at one point.**

*Technical.* Where a Tradition entry quotes a membership loss, the design is: all
twelve Traditions at 0.85, then one Tradition alone lowered to 0.50, twenty-year
horizon, 400 paired replications under common random numbers, reference membership 13.10
with a cross-seed standard deviation of 5.67. Tradition 3 and Tradition 11 remain mixed
adherence rows here; their mechanism-specific paths are separated in the release factorials.

*In plain terms.* That column answers one question: if a group let this Tradition slide
while holding the others steady, how many fewer people would be in the room in twenty
years. It is not a measure of how much a Tradition matters. It says nothing at all
about whether the group's decisions are any good, which is where Traditions 2, 9 and 12
do most of their work. A Tradition can score near zero here and still be carrying one
of the book's three headline results. One of them does.

**Five. Three different things were assumed, and they are not equally well tested.**

*Technical.* Every entry below rests on three separable authored choices. First, the list
of resources: the model says a group supplies eight things and no others. Second, the
pattern: which of the 96 cells in each matrix are non-zero. Third, the magnitudes: how
large each non-zero cell is, on a scale from 0 to 1 with no unit outside this model. The
robustness designs reach these unequally. Plus or minus thirty per cent jitter and the
randomized-matrix draws test magnitudes. The 64 resource-list variants test the list by
deleting one resource, merging a pair, or deleting two, and they establish that the Part
Four verdicts are not an artifact of any single column. They cannot test whether a
resource should have been *split*, or whether a ninth resource is missing, because both
require fresh judgement rather than an operation on the existing columns. Nothing tests
the pattern of zeros against an outside source, which is why a second reader marking the
non-zero cells is the largest outstanding item in the project.

*In plain terms.* There are three ways these tables could be wrong, and they are not
equally guarded. The magnitudes have been shaken hard and most results survive. The list
of eight has been tested by removing entries and combining them, and the headline
findings hold. What has not been tested at all is the possibility that the list is
missing something, or that one of the eight is really two things wearing one name. No
computation can find that, because the test would have to come from outside the tables,
and everything here is inside them. When a result below looks surprisingly clean,
the honest question is not whether the arithmetic is right, which it is, but whether the
eight columns were the right eight.

---

# Part One. The Twelve Steps

Each entry gives the derived group-dependence coefficient beta, which is the Step's
row sum in S normalised by the largest row sum, and the Step's principal supplier,
which is the Tradition governing the largest share of what that Step consumes. The
index-mate is the Tradition carrying the same number, and its rank among the twelve is
the whole of Part Four's argument in one column.

## Step One, admitting powerlessness

*Technical.* beta = 1.00, the joint maximum. Principal supplier Tradition 3 at 1.22,
with Tradition 1 second at 0.99. Its largest consumption is identification, others in
the room who name themselves as alcoholic, at the matrix maximum of 1.0, followed by
admission at 0.8. It carries the highest top speed of any Step, 0.30 per week, and the
lowest exposure to the maintenance gate, 0.05. Its index-mate, Tradition 1, ranks
second at 0.99 against the winner's 1.22, the closest any index-mate comes. Under the
sixty-four resource-list variants Step One regains its index-mate in fifteen of them,
more than any other Step. *Algebra, plus the simulation's parameter table.*

*What was assumed.* Five of the eight resources were given non-zero entries:
identification at 1.0, admission at 0.8, visible proof at 0.3, continuity at 0.2 and
gentle pressure at 0.1. The 1.0 is a ceiling rather than a measurement; it says only
that nothing in the table needs identification more than this Step does. Two further
numbers are assumed outside the matrix: a top speed of 0.30 per week, the fastest of
the twelve, and an exposure to the maintenance gate of 0.05, the lowest of the twelve.
That 0.05 is not a judgement about Step One specifically. Gate exposure was laid out as
a straight line from 0.05 at Step One to 1.00 at Step Twelve, so every Step's value on
that dial follows from its position rather than from anything observed about it.

The reading behind the row is that what an arrival needs is other people naming
themselves the same way, and a door that opened without asking anything first. Nobody
measured that. Reverse the two largest entries, so that admission outranks
identification, and Tradition 3 would win this row more clearly rather than less, so
the headline result here is not sensitive to that particular judgement. What the row
does depend on is the claim that identification is a distinct thing a group supplies,
rather than an aspect of admission. The resource-list test can merge those two columns,
and does, and Step One is among the fifteen variants where the index pairing comes
back.

*In plain terms.* This is the Step you cannot take by yourself, and it is tied with the
twelfth for depending most on other people. What it needs is not advice. It is other
people in the room saying the same thing about themselves, and a door that opened
without asking anything first. It is also the fastest Step to move and the one least
affected by how much you already have to lose, which is the model's way of saying that
an arrival has nothing yet to protect. It is the one place where the obvious pairing
nearly works, and it is the Step most likely to pair with its own Tradition if somebody
redrew the list of what groups supply.

## Step Two, coming to believe

*Technical.* beta = 0.71. Principal supplier Tradition 11 at 0.82, with Tradition 5
second at 0.72. Its dominant input is visible proof that recovery happens, at 1.0. The
index-mate, Tradition 2, ranks seventh at 0.13. *Algebra.*

*What was assumed.* Four non-zero entries: visible proof at 1.0, identification at 0.4,
continuity at 0.2 and counsel at 0.1. Top speed 0.25 per week, gate exposure 0.136 from
the straight line. The substantive assumption is the one large number. Coming to
believe was coded as an evidential matter, so the thing it consumes most is other
people visibly getting better, and it was coded as needing almost no counsel, 0.1,
which is the model saying that this Step is not achieved by being talked to.

That is a reading of the Step, and a contestable one. A tradition of interpretation
holds that Step Two is largely a matter of being persuaded, argued with, or taught, in
which case counsel should be large and proof small. Had it been coded that way the
principal supplier would move from Tradition 11 to Tradition 2, and the primer's
plain-language claim that a group's best argument for itself is the condition of its
members would not follow. The claim is downstream of the coding, not evidence for
it.

*In plain terms.* The model treats coming to believe as an evidential matter rather
than a persuasive one. What the Step consumes is people visibly getting better in front
of you. That is why the Tradition supplying it is attraction rather than promotion:
nobody is talked into this, they watch it happen and draw the obvious conclusion. If
the model is right about Step Two, then a group's most important argument for itself is
the condition of the people in it.

## Step Three, the decision

*Technical.* beta = 0.29, near the bottom. Principal supplier Tradition 2 at 0.31, with
Tradition 1 second at 0.27. Row sum 0.70, so it asks little of the group in absolute
terms. Index-mate Tradition 3 ranks seventh at 0.01, the smallest non-zero index-mate
entry in the matrix. *Algebra.*

*What was assumed.* Four small non-zero entries: counsel at 0.3, visible proof at 0.2,
continuity at 0.1 and gentle pressure at 0.1, giving the second smallest row sum in the
table at 0.70. Top speed 0.25 per week, gate exposure 0.223. Every number here is
small, and that smallness is itself the assumption: the decision was coded as something
a person does, with a group nearby rather than involved.

This matters more than the individual cells, because the starkest number against the
index-pairing idea anywhere in the matrix, Tradition 3 ranking seventh at 0.01, is
partly a consequence of the row being small in total. A row that asks little of a group
gives every Tradition little, and rank is then decided by fine differences. The finding
survives the magnitude jitter, so it is not fragile in that sense. But a reader should
know that the dramatic phrasing rests on a row the author deliberately made
quiet.

*In plain terms.* The decision asks less of a group than almost any other Step. What it
does draw on is counsel: somebody to talk it over with. The Tradition sharing its
number contributes essentially nothing to it, and that is the starkest single number
against the pairing idea anywhere in the matrix.

## Step Four, the inventory

*Technical.* beta = 0.33. Principal supplier Tradition 2 at 0.35, with Tradition 1 tied
at 0.35 to the second decimal and behind by four parts in a thousand, the narrowest
top-two margin in the matrix. Its largest consumption is gentle pressure at 0.4 and
counsel at 0.3. The index-mate, Tradition 4, has an entry of exactly zero, because
Tradition 4 governs no resource any Step consumes. That zero is arithmetic and not
evidence: no multiplicative perturbation can move it. The threshold test that can reach
it finds that a uniform governance strength of 0.438 would be needed for the index-mate
to win, against a mean live entry in the governance matrix of 0.374. *Algebra.*

*What was assumed.* Three non-zero entries: gentle pressure at 0.4, counsel at 0.3 and
identification at 0.1. Top speed 0.18 per week, among the slowest, and gate exposure
0.309. The reading is that an inventory needs mild expectation that you will actually
do it and somebody to ask about how, and needs nothing else from a group.

The index-mate's exact zero is not an assumption about Step Four at all. It follows
from a decision made in the other table, that Tradition 4 governs no resource any Step
consumes. No perturbation of Step Four's own row can move it, because zero times
anything is zero. This is the clearest case in the primer of a result that looks like a
finding and is really a restatement of an input, which is why the entry says so rather
than counting it.

*In plain terms.* The inventory needs two things from a group: mild expectation that
you will actually do it, and somebody to ask about how. Tradition 4 supplies neither,
and it supplies nothing to any other Step either, because it is one of the five
Traditions in the model that guard rather than provide. So the pairing fails here for a
boring reason rather than an interesting one, and the primer says so rather than
counting it as a discovery.

## Step Five, telling someone

*Technical.* beta = 0.71. Principal supplier Tradition 12 at 1.08, with Tradition 1
second at 0.65, a margin of 0.43, the second widest in the matrix. Step Five is the only
Step that consumes confidentiality at the matrix maximum of 1.0, and Tradition 12 is the
Tradition that governs confidentiality at 1.0. Its robustness is asymmetric: it survives
99.5 per cent of draws at plus or minus thirty per cent jitter, with a 95 per cent
Wilson interval of [99.1, 99.7] on 2,000 draws, and only 17.5 per cent [15.9, 19.2] when
every non-zero magnitude is replaced at random. Its index-mate, Tradition 5, ranks fifth
at 0.12. *Algebra.*

*What was assumed.* Five non-zero entries, one of them decisive: confidentiality at
1.0, counsel at 0.3, continuity at 0.2, identification at 0.1 and gentle pressure at
0.1. Top speed 0.22 per week, gate exposure 0.395. Two separate judgements produce the
cleanest match in the book, and they were made in two different tables: that Step Five
is the only Step needing confidentiality at full strength, and that Tradition 12
supplies confidentiality at full strength.

The entry's own robustness numbers are the honest measure of that. Holding the pattern
of which cells are non-zero and jittering the magnitudes by thirty per cent, the match
survives 99.5 per cent of the time. Replacing every non-zero magnitude at random, so
that only the pattern remains, it survives 17.5 per cent of the time. The gap between
those two figures is not noise. It is the size of the authored judgement, stated
numerically, and it is the reason this entry is described as a judgement argued for
rather than a result computed.

*In plain terms.* Telling someone requires that it stay told. Step Five is the only Step
that needs confidentiality at full strength, and anonymity is the only Tradition that
supplies it at full strength. That is the cleanest match in the book, and it is also
the clearest illustration of what these matches rest on. If you accept my numbers it is
near certain. If you accept only the pattern of which Tradition touches what, and let
the strengths fall where they may, it mostly disappears. The pairing is a judgement
argued for, not a result computed, and the difference between ninety-nine and seventeen
is exactly the size of the judgement.

## Step Six, becoming willing

*Technical.* beta = 0.25. Principal supplier Tradition 1 at 0.25, with Tradition 2
second at 0.24, a margin of 0.01 and the narrowest of any row except Step Four's, which
is a tie. Row sum 0.60. Index-mate Tradition 6 is a structural zero and ranks ninth. Its
threshold is 0.417, the lowest of all twelve. *Algebra.*

*What was assumed.* Three non-zero entries: gentle pressure at 0.3, counsel at 0.2 and
visible proof at 0.1, giving a row sum of 0.60. Top speed 0.20 per week, gate exposure
0.482. As with Step Three the assumption is mostly the smallness.

The technical line reports that the top two Traditions are separated by 0.01, which is
below any precision the inputs can support. That is worth stating plainly: where the
margin between two Traditions is smaller than the rounding in the table that produced
it, the primer should be read as saying the model has no opinion, and not as saying
Tradition 1 narrowly wins. The entry is phrased that way deliberately.

*In plain terms.* Becoming willing barely needs a group at all: a little pressure, a
little counsel, and that is most of it. The two Traditions at the top are so close that
the model has no real opinion about which one carries it. Of all twelve Steps this is
the one where the pairing comes nearest to being recoverable, and it still needs its own
Tradition to look after its needs more attentively than a typical entry in the whole
matrix.

## Step Seven, asking

*Technical.* beta = 0.17, the minimum. Row sum 0.40, the smallest in S. Principal
supplier Tradition 1 at 0.17. The ratio of the most group-dependent Step to this one is
6.0. Index-mate Tradition 7 is a structural zero and ranks tenth. Setting a uniform
governance strength at the mean live entry of 0.374 for all twelve Steps at once, Step
Seven's index-mate loses by the narrowest margin of the twelve, 0.02. *Algebra.*

*What was assumed.* Three non-zero entries: gentle pressure at 0.2, visible proof at
0.1 and counsel at 0.1, giving the smallest row sum in the whole table at 0.40. Top
speed 0.20 per week, gate exposure 0.568.

The six-to-one ratio between the most group-dependent Step and this one is therefore an
assumption's shadow rather than a discovery. It is arithmetic on a row the author made
the smallest, because the reading was that asking is the most private thing in the
programme. The ratio is worth quoting because it makes the reading explicit and
falsifiable: anyone who thinks Step Seven needs more from a room than Step Four does
has a specific disagreement with a specific number, which is the most this kind of
table can offer.

*In plain terms.* This is the most private Step in the programme. If you asked how much
of each Step happens in a room rather than in a person, Step Seven gives the smallest
answer, by a factor of six against the largest. That is not a claim that it is easy, or
minor, or that it happens without the rest. It is a claim about how much of it other
people can supply, and the answer the model gives is: almost none of it.

## Step Eight, listing the harms

*Technical.* beta = 0.33. Principal supplier Tradition 2 at 0.43, with Tradition 1
second at 0.29. Its largest consumption is counsel at 0.4. The index-mate, Tradition 8,
ranks fourth at 0.07, the best rank achieved by any index-mate other than Step One's.
*Algebra.*

*What was assumed.* Three non-zero entries: counsel at 0.4, gentle pressure at 0.3 and
confidentiality at 0.1. Top speed 0.18 per week, gate exposure 0.655. The reading is
that making the list is mostly a matter of having somebody to ask, with some
expectation that it gets done and a little need for discretion.

The single interesting assumption is the small confidentiality entry. It is the reason
Tradition 8 reaches fourth here, its best rank anywhere, rather than disappearing.
Remove that 0.1 and the index-mate's showing gets worse. The primer's claim that the
pairing is not absurd anywhere therefore rests, in this row, on a judgement about a
tenth of a unit.

*In plain terms.* Making the list is mostly a matter of having somebody to ask, which
is why the group conscience supplies it. Its own numbered Tradition does better here
than in most rows and still comes fourth, which is the pattern across the whole table:
the pairing is not absurd anywhere, and it wins nowhere.

## Step Nine, amends

*Technical.* beta = 0.62. Principal supplier Tradition 2 at 0.90, with Tradition 1 at
0.48, a margin of 0.42 and the third widest in the matrix behind Step Ten's 0.51 and
Step Five's 0.43. Step Nine consumes counsel at 0.9, the largest entry in S other than
the four entries at 1.0. It carries the lowest top speed of any Step, 0.15 per week.
Disabling the twelfth Step lowers mean Step Nine practice by 0.0055 in the 400-seed
paired experiment, but the 95 per cent interval is -0.0015 to 0.0125 and includes zero.
The same intervention does produce resolved decreases in membership, established
practice and maintenance capacity. Index-mate Tradition 9 is a structural zero and
ranks eleventh. *Algebra and simulation.*

*What was assumed.* Four non-zero entries: counsel at 0.9, confidentiality at 0.3,
gentle pressure at 0.2 and continuity at 0.1. The 0.9 is the largest entry in the table
that is not one of the four maxima. Top speed 0.15 per week, the slowest of the twelve,
and gate exposure 0.741.

Two of those numbers were chosen to say something the author believed and did not
measure: that amends is the Step most needing somebody to talk it through with, and the
one that moves slowest. Both are readings of the practice rather than observations of
it, and the plain-language sentence about not doing this one quickly is a restatement
of the assumed speed, not a finding about it. The finding in this entry is the separate
simulation result about switching off the twelfth Step, which does not depend on Step
Nine's own row.

*In plain terms.* Amends is the Step that most needs counsel, and it is the slowest
Step to move, which between them describe something people already know: you do not do
this one quickly and you do not do it without asking. The finding worth carrying is not
about Step Nine's own needs. Switch off the twelfth Step, so nobody in the group is
carrying the message to anyone, and the group ends smaller with lower maintenance
capacity. The isolated Step Nine change is too imprecise to call. The model therefore
supports a group-level service pathway here, not the earlier claim of a large resolved
spillover into Step Nine itself.

## Step Ten, the daily inventory

*Technical.* beta = 0.62. Principal supplier Tradition 1 at 0.94, with Tradition 2
second at 0.43, a margin of 0.51, the widest in the matrix. Its largest consumptions are
gentle pressure at 0.7 and week-to-week continuity at 0.5, which between them are the
two resources Tradition 1 supplies most heavily. Index-mate Tradition 10 is a structural
zero and ranks twelfth, the worst rank in the table. *Algebra.*

*What was assumed.* Four non-zero entries: gentle pressure at 0.7, continuity at 0.5,
counsel at 0.2 and confidentiality at 0.1. Top speed 0.25 per week, gate exposure
0.827. The reading is that a daily inventory is a habit, and that habits are held in
place by the meeting happening again and by other people mildly expecting you at it.

The widest margin in the matrix, 0.51 in Tradition 1's favour, is produced by that
reading meeting a matching one in the other table, where Tradition 1 was given the two
largest shares of exactly those two resources: 60 per cent of gentle pressure and 50
per cent of continuity. The two tables were written by the same person, so agreement
between them is not independent corroboration. This row is the clearest place in the
primer where a striking number comes from one judgement appearing twice.

*In plain terms.* Daily inventory is a habit, and habits need the two things a group
supplies steadily rather than dramatically: the meeting happening again next week, and
other people mildly expecting you at it. That is the whole of what the model means by
unity here, and it is a duller thing than the word suggests. Step Ten also has the worst
showing of any Step for the pairing idea. Its own numbered Tradition comes dead last of
twelve.

## Step Eleven, the conscious contact

*Technical.* beta = 0.33. Principal supplier Tradition 1 at 0.47, with Tradition 2
second at 0.21. Index-mate Tradition 11 ranks fourth at 0.11. With Steps Ten and Twelve
it forms the maintenance capacity term: the model computes a member's capacity to hold
what they have as a Hill function of the mean of Steps Ten, Eleven and Twelve, and that
capacity multiplies the growth of every Step, weighted by an exposure rising from 0.05
at Step One to 1.00 at Step Twelve. *Algebra and the simulation's structure.*

*What was assumed.* Four non-zero entries: gentle pressure at 0.4, continuity at 0.2,
visible proof at 0.1 and counsel at 0.1. Top speed 0.20 per week, gate exposure 0.914.
The row itself is unremarkable and was meant to be.

The consequential assumption about this Step is structural and lives outside its row.
The model computes maintenance capacity from the mean of Steps Ten, Eleven and Twelve,
and that grouping was chosen rather than derived: three Steps were nominated as the
maintenance Steps and the other nine were not. The straight-line gate exposure then
decides how much that capacity matters to each Step, from 0.05 at Step One to 1.00 at
Step Twelve. Both the choice of which three, and the straightness of that line, are
modelling conveniences. The plain-language claim that the last three Steps stop the
first nine leaking away is a description of that construction, and would be false in a
model that nominated a different three.

*In plain terms.* Its own row is unremarkable. Its importance is structural: along with
Ten and Twelve it is what the model calls maintenance, the capacity to keep hold of what
has already been gained. Those three set a multiplier on everything else, weighted so
that it barely touches Step One and fully governs Step Twelve. In plainer language, the
last three Steps are what stop the first nine leaking away, and the more practice a
modeled member has accumulated, the more there is to maintain. The model records no
tenure, so this state comparison cannot be translated into newcomer and veteran cohorts.

## Step Twelve, carrying it

*Technical.* beta = 1.00, the joint maximum, and the Step that consumes seven of the
eight resources. Principal supplier Tradition 5 at 1.25, with Tradition 3 second at
1.10. It is the only consumer of the recipient resource, which is the only one of the
eight defined by a ratio of member states: low-practice members per high-practice
potential helper. It records no tenure, sponsorship or matching, and lower helper count
increases rather than reduces the ratio. Three simulation
results at 400 paired seeds, thirty years, full adherence. Setting the twelfth Step's
growth rate to zero lowers endpoint membership from 17.80 plus or minus 0.88 to 12.48
plus or minus 0.35; the paired loss is 5.33 [4.44, 6.21]. Endpoint viability is
394 of 400 in both conditions. In the corrected clean ablation, forcing only recipient
capacity to one raises final membership by 1.03 members with paired 95 per cent
interval [-0.26, 2.31], so the effect is unresolved. Index-mate Tradition 12 ranks sixth
at 0.12, and this
is the fragile row of Part Four: the top two are 1.25 and 1.10, a margin of 0.15, and
the Step Twelve to Tradition 5 assignment survives only 67.3 per cent [65.3, 69.4] of
draws at plus or minus thirty per cent jitter. *Algebra and simulation.*

*What was assumed.* Seven of the eight resources are non-zero, the most of any Step:
recipient opportunity at 1.0, continuity at 0.6, gentle pressure at 0.3, admission at
0.2, and identification, visible proof and counsel at 0.1 each. Top speed 0.22 per
week, gate exposure 1.00, the maximum, again by position on the straight line.

The recipient resource carries the weight here and is the most heavily assumed object
in the model. It is the only one of the eight defined as a ratio of member states,
low-practice members per high-practice potential helper, and that definition has a
consequence the author did not choose but must own: a group with fewer experienced
members has a *higher* ratio and therefore looks richer in this resource, not poorer.
It records no tenure, no sponsorship, and no matching between a particular helper and a
particular newcomer. Whether that ratio is a reasonable stand-in for the opportunity to
be useful is a hypothesis, and it is the hypothesis on which the thirty per cent
membership result rests. The row is also the fragile one in Part Four for a separate
reason: the top two Traditions are 1.25 and 1.10, and the assignment to Tradition 5
survives only 67.3 per cent of magnitude draws.

*In plain terms.* Carrying the message is not a reward collected at the end inside this
model. Turn its growth off and the group loses about thirty per cent of mean endpoint
membership, while the estimated viability fraction is unchanged. The experiment ends at
thirty modeled years and does not establish that either condition stays there indefinitely.
The recipient calculation is a hypothesis about
opportunity per potential helper, not evidence about how real sponsorship matches form.
The clean comparison is too imprecise to say that removing the modeled limit improves
the group. The earlier stronger conclusion came from an intervention that also changed
Step weights and beta.

---

## What the Step rows say taken together

*Technical.* Group-dependence is highest at the two ends, 1.00 at Step One and Step
Twelve, and lowest in the middle, 0.17 at Step Seven, with a mean of 0.53. That the
entry Step and the service Step depend most on other people is a consequence of the
resource assignment rather than an input to it. Beta is a within-model dependence
index that blends autonomous and resource-supported peer growth. The code does not
implement a reciprocal member-to-group weight, so no one-to-six transmission ratio
follows. The ordering claim, that a Step cannot be skipped, is a limiting case: writing the
stage as a constant-elasticity-of-substitution aggregator, strict ordering holds for
every substitution parameter rho less than or equal to zero. The current simulation
is only a proxy-averaging demonstration: it supplies the regressors and loadings
without error and adds noise to the output. More output proxies improve resolution
in that exercise, but it does not validate a latent-variable estimator or a required
instrument count.

*In plain terms.* The Steps form a U. The first and the last are things you cannot do
alone. The middle ones are largely yours to do, with a group nearby rather than
involved. Nobody designed that shape and it was not put in by hand; it comes out of
asking, for each Step in turn, what it needs from other people.

The second point is about the rule that you cannot skip a Step. That has always been
stated as a piece of folk wisdom, take it or leave it. The model shows it is not a
separate belief at all. It is one setting of a dial that runs continuously from "each
Step strictly requires the one before" to "the Steps substitute freely for each other",
and the folk rule is everything on one half of that dial rather than a single extreme
point. Which means it is the kind of claim that could be measured. The calculation here
makes the estimand explicit and shows that averaging noisy outputs can improve precision
under oracle information. It does not establish a sufficient sample size or measurement
design for real data, where inputs are latent and group attention is endogenous.

---

# Part Two. The Twelve Traditions

Each entry gives the Tradition's load, which is its column sum in B and therefore the
total demand all twelve Steps place on resources it governs, how many of the eight
resources it governs, and its membership loss in the degradation comparison described
in caution four. Losses whose 95 per cent interval includes zero are marked
unresolved: seven of the twelve comparisons resolve and five do not. The T3 and T11
entries instead lead with the more informative 400-seed path-split factorials.

## Tradition 1, unity

*Technical.* Load 6.52, the largest, governing all eight resources and the only
Tradition to do so. Principal supplier for four Steps and runner-up for six, so it is
in the top two for ten of the twelve. Degrading it alone costs 1.65 members
[0.99, 2.30], third largest. Its primacy survives 75.4 per cent [73.5, 77.2] of fully
structural draws, against 40.6 per cent for the index-pairing claim. It is not the most
diffuse Tradition by concentration: singleness of purpose scores marginally lower at
0.197 against unity's 0.204. Its load is carried by two resources: continuity at 1.89
and gentle pressure at 1.86 are 57.5 per cent of the total, and transferring either one
to Tradition 5 makes Tradition 5 the leader. Six of eight such transfers cannot flip it
and two can. *Algebra, with simulation for the degradation figure.*

*In plain terms.* Unity is not one of the things a group supplies. It is the condition
of everything a group supplies, which is why it is the only Tradition touching all eight
and why it is in the top two for ten of the twelve Steps. But look at what that
actually consists of, and most of it is two unglamorous things: the meeting keeps
happening, and people notice whether you are at it. Take those two away and unity drops
to third place. So the model's "unity" is closer to reliability and mild social
expectation than to fellow feeling, and a group worried about its unity would do better
to check whether it has cancelled a meeting than to check whether everyone is getting
on.

## Tradition 2, the group conscience

*Technical.* Load 3.89, second largest, governing four resources, with counsel at 0.69
of its load and the highest concentration of any Tradition at 0.520. Principal supplier
for four Steps and runner-up for four more. Degrading it alone costs 0.48 members
[-0.14, 1.10], an unresolved contrast. In the deliberation model it is one of three Traditions keeping maximum
influence falling toward one over N, which is the Golub and Jackson condition for a
consensus converging on the truth. A single member holding 0.35 of every row floors the
group's error at 0.279 however large the group grows, against a flat error falling as
one over the square root of N. Five per cent of every row leaves the error 1.84 times
the flat benchmark at a thousand members, and the factor grows without bound. *Algebra,
deliberation and simulation.*

*In plain terms.* In the simulation, the group conscience is mostly what supplies
counsel: it is the Tradition behind there being somebody to ask. Its real work is
somewhere the membership numbers cannot see it. It is what keeps a room deciding by
adding up what everybody thinks rather than by deferring to one person, and the theorem
behind that is unforgiving. A group that leans on one member is permanently worse at
being right, and it does not matter how big the group gets, because the leaning does not
dilute. Nor does the room have to be dominated for this to bite. A member who holds five
per cent of everyone's attention, which is not much and would not look like a problem
from inside, nearly doubles how wrong a large group ends up. The damage starts long
before anybody would call it a problem.

*The objection AA itself raises.* The fellowship's 1953 commentary on this Tradition
describes a group's committee as sharply limited, unable in any sense to govern or
direct, and then says where the influence actually is: with elder statesmen, former
officeholders it calls the real and permanent leadership, who become the voice of the
group conscience and to whom a perplexed group inevitably turns. They hold no office, so
nothing rotates them out. Three such members holding a tenth of the attention between
them cost a group of ten almost nothing, one per cent, and cost a group of a thousand a
factor of 2.08 on error, with their share settling at 0.034 against a flat benchmark of
0.001. Widening the rotation does not touch it, because the concentration is not in the
rotation. This is a claim about a described practice and not about the Tradition, which
still satisfies the condition; but a group following AA's own commentary faithfully will
build the thing the condition forbids. *Deliberation model.*

## Tradition 3, the open door

*Technical.* Raw semantic load 2.69, governing four resources, with admission at 0.37
of that raw load. In the 400-seed paired factorial, the baseline ends at mean N 17.80
[16.92, 18.68]. Friction loss alone costs 2.96 members [1.85, 4.08]; governance loss
alone costs 6.03 [5.04, 7.01]; combined loss costs 11.05 [10.03, 12.06]. The interaction
is -2.06 [-3.41, -0.70], so the two contrasts must not be added. Combined loss closes
25.0 per cent of groups [21.0, 29.5] and leaves 54.8 per cent endpoint-viable
[49.9, 59.6].
Because the Tradition removes the group's power to refuse admission, Tradition 3 does
not appear in the default arrival rate. It has two other paths: it governs four resource
columns and it reduces an inverse-practice-weighted dropout friction. The latter is largest
for members whose practice is near zero; it measures neither tenure nor demographic
newness. The corrected factorial reports governance loss, friction loss, their combination
and their interaction separately. Older combined sweeps cannot be described as retention
only. *Algebra and simulation.*

*In plain terms.* In the default model a group cannot decide who turns up, but it can
affect what people receive and whether low-practice members stay. Those are two distinct
mechanisms, and the old description collapsed them into one. The model records practice,
not arrival date, so a room's low-practice fraction must not be translated into a count of
newcomers. Testing demographic newness would require tenure or cohort data the model does
not have.

## Tradition 4, autonomy

*Technical.* Load 0.00. Its row in the governance matrix is identically zero: it governs
no resource any Step consumes. It is one of the five protective Traditions and enters
the simulation only as a multiplier, paired with Tradition 7, on the effective adherence
of everything else. Degrading it alone costs 0.88 members [0.26, 1.50], identical to
Tradition 7's to the last digit because the two enter the same term symmetrically. That
identity is an artefact of the model's construction, not a finding about the Traditions.
*Algebra and simulation.*

*In plain terms.* Autonomy hands the Steps nothing directly. Its whole job in the model
is keeping the other Traditions from being overridden from outside, and it does that
jointly with self-support. The two share a number because the model treats them as a
pair, not because anybody discovered they were equally important. What *is* derived here
is only that autonomy supplies nothing; how it should act instead was assumed, and the
multiplier is the simplest assumption that gives it any role at all.

## Tradition 5, singleness of purpose

*Technical.* Load 3.88, a hair behind the group conscience, governing six resources, the
second broadest. Principal supplier for Step Twelve and runner-up for Step Two.
Degrading it alone costs 0.96 members [0.35, 1.57]. Transferring unity's governance of
continuity or of gentle pressure to singleness of purpose makes it the leader, which is
the strongest form of the objection that later AA literature substituted unity for
single-purposedness. Six of the eight possible transfers cannot flip it and two can.
*Algebra and simulation.*

*In plain terms.* Singleness of purpose is unity's only real rival for the most
load-bearing Tradition, and the whole contest comes down to who owns two things: the
meeting continuing to happen, and the pull of other people expecting you there. If those
belong to unity, unity leads. If they belong to the group having one job, single purpose
leads. That is a real question about how AA works and the model cannot settle it. What
the model can do is say that this, and nothing else in the matrix, is where the answer
would change.

## Tradition 6, no endorsement

*Technical.* Load 0.00, a protective Tradition with an empty governance row. Enters the
simulation as a multiplier, paired with Tradition 10, on the effective adherence of
singleness of purpose. Degrading it alone costs 0.23 members [-0.24, 0.69],
**unresolved**: the comparison cannot distinguish its effect from zero at 400 paired
replications. Identical to Tradition 10's figure for the same structural reason as the
Tradition 4 and 7 pair. *Algebra and simulation.*

*In plain terms.* Refusing endorsements supplies nothing to any Step. Its job is
protecting the group's single purpose from being diluted, alongside Tradition 10. The
simulation cannot tell its effect apart from nothing at all, and the correct reading of
that is that the simulation has nothing to say about it, not that it does nothing. An
instrument that cannot resolve a thing is silent about it, not against it.

## Tradition 7, self-support

*Technical.* Load 0.00, protective, empty row. Paired with Tradition 4 as a multiplier
guarding against outside override. Degrading it alone costs 0.88 members [0.26, 1.50],
identical to Tradition 4's by construction. Money enters the simulation elsewhere,
through a solvency term scaling the continuity resource: a group whose established
members cannot cover the rent supplies continuity at 0.45 rather than 1.0. That
mechanism is not attributed to Tradition 7 in the governance matrix. *Algebra and
simulation.*

*In plain terms.* Passing the basket looks after nothing directly in the matrix, and yet
money is unmistakably in the model somewhere else: a group that cannot pay its rent
supplies week-to-week continuity at less than half strength, and continuity is one of
the two things holding unity up. So the practical content of self-support is that the
meeting keeps happening. The matrix does not give Tradition 7 credit for that, and a
reader could reasonably say it should. This is one of the places a second person
building the governance table would most likely disagree with the first.

## Tradition 8, non-professional

*Technical.* Load 1.11, the smallest non-zero load, governing four resources with
confidentiality the largest at 0.41 of the total. Principal supplier for no Step and
runner-up for none. Degrading it alone changes membership by -0.20 members
[-0.71, 0.31], **unresolved**.
*Algebra and simulation.*

*In plain terms.* This is the Tradition the model can say least about. It touches four
things lightly, leads on none of them, and its cost in members cannot be told apart from
zero. Stating that plainly is better than dressing it up. Keeping AA unpaid may matter a
great deal for reasons this model was never built to see, and the honest report is that
the instrument did not detect anything rather than that there is nothing there.

## Tradition 9, no hierarchy

*Technical.* Load 0.00, protective, empty row. Degrading it alone costs 0.02 members
[-0.41, 0.46], **unresolved**. In the deliberation model, rotation of service works only
if the rotating pool scales with the group. A fixed pool floors maximum influence at
roughly the officeholder's share divided by the pool size, while the flat benchmark
keeps falling as one over N, so the gap grows without limit: a pool of twelve sits at
2.1 times the flat benchmark at fifty members and 23.9 times at eight hundred. The pool
needed to stay within a factor of two of flat is 26 per cent of the group at every size
tested from fifty to eight hundred. The 26 per cent depends on the parameter choices;
the divergence does not. *Algebra, deliberation and simulation.*

*In plain terms.* This is the sharpest warning against reading the membership column as
importance. On that column Tradition 9 does nothing measurable, and it carries one of
the three headline results in the book.

Rotation is where the model knows something AA does not say. The long form of this
Tradition says rotating leadership is best, and the 1953 commentary warns against
entrenched power, but neither says how many people. The model says the answer is a
fraction of the group and not a headcount, and that the difference is not a matter of
degree. A group of fifty rotating twelve people through its service positions is fine. A
group of eight hundred rotating twelve is a permanent oligarchy, whoever those twelve are
and whatever anybody intends, and from inside it looks exactly like the healthy small
group did. Roughly a quarter of the group needs to be in the pool. Treat the quarter as
an order of magnitude rather than a target, and treat the underlying question as the
durable one: if this group doubled, would the same people still be running it?

*And a limit on that advice, from AA's own commentary.* The quarter is necessary and it
is not sufficient. The same 1953 text that recommends rotation says the rotating
positions carry no governing authority, and locates real influence in elder statesmen who
hold no position at all. A group rotating a quarter of itself but deferring to three such
members sits at 2.5 times the flat benchmark at fifty, 9.2 at two hundred and fifty, and
34.2 at a thousand. A service roster cannot detect this, because a roster records offices
and nothing records deference. The second question a group would have to ask is: when
something difficult comes up, how many different people does this room turn to, and is
that number growing as the room does?

## Tradition 10, no outside issues

*Technical.* Load 0.00, protective, empty row. Paired with Tradition 6 as a multiplier
on singleness of purpose. Degrading it alone costs 0.23 members [-0.24, 0.69],
**unresolved**, identical to Tradition 6's by construction. Part One's historical
material bears on it more than the model does: the Washingtonians had a written analogue
of this Tradition in print within two years of founding. *Algebra and simulation.*

*In plain terms.* Staying out of outside controversies supplies nothing directly and
protects single purpose. The model cannot resolve its effect. The history is the more
interesting evidence here, and it cuts against the easy story: the Washingtonians wrote
down their own version of this rule almost immediately, circulated it in a manual and a
newspaper, and dissolved anyway. Whatever preserved AA, it was not this rule on its own,
because the other movement had it too.

## Tradition 11, attraction rather than promotion

*Technical.* Raw semantic load 2.69, governing four resources, with visible proof of
recovery at 0.49 of that raw load. Principal supplier for Step Two. Tradition 11 has two
paths. Its attraction path multiplies inflow from members' Step Twelve practice; its
governance row affects four resource columns. In the 400-seed paired factorial, pure
attraction loss costs 5.42 members [4.52, 6.33], governance loss costs 2.29
[1.21, 3.36], and combined loss costs 5.88 [4.97, 6.79]. The interaction is 1.83
[0.76, 2.90]. None of the three conditions closes a group in these runs, and each leaves
about 98 per cent endpoint-viable. Older tables that set the Tradition itself to zero are
mixed interventions, not pure attraction tests. *Algebra and simulation.*

*In plain terms.* Attraction and resource governance are different jobs in this model.
Removing attraction makes the thirty-year group smaller without producing closure in these
runs; removing governance also matters. Removing both is not the sum of removing each. No
finite simulation establishes that a remnant lasts forever, and the outstanding comparison
with referral loss must be reported on closure, endpoint viability and size separately.

## Tradition 12, anonymity

*Technical.* Load 2.62, governing five resources, with confidentiality at 0.57 of its
load. Principal supplier for Step Five and the Tradition governing confidentiality at the
matrix maximum of 1.0. Degrading it alone costs 0.99 members [0.41, 1.58]. It is also one
of two Traditions guarding the effective adherence of the group conscience, entering that
term symmetrically with Tradition 9. Because the two enter identically there, the entire
difference between their measured losses, 0.99 against 0.02, is associated with Tradition 12's own
governance row. In the deliberation model it is the third of the three holding maximum
influence near one over N. *Algebra, deliberation and simulation.*

*In plain terms.* Anonymity does two separate jobs and they are easy to run together.
The first is ordinary and immediate: it is what makes confidentiality available, and
confidentiality is what the fifth Step needs and cannot do without. The second is
structural and invisible from inside the room: by keeping anybody from becoming a name,
it stops the group's decisions concentrating on one person, which is the condition for
those decisions being reliable at all. Tradition 9 shares the second job and not the
first, which is exactly why anonymity scores higher in the membership comparison and why
that higher score says nothing about the part that matters most.

That two-job reading was arrived at from the model and has since been found in the
source. AA's 1953 commentary on this Tradition tells the two as separate lessons learned
at different times: first that a member's name and story had to be confidential, after
members repeated each other's stories and trust broke; and later, once national publicity
arrived, that anonymity had to be absolute at press, radio, film and television, so that
no self-appointed member could present himself as a messiah representing AA. The first is
confidentiality. The second is the structural job. Nobody had to reconcile them because
the fellowship never treated them as one thing.

Maxwell wrote in 1950 that anonymity had "sheer survival value" and could not say why.
This is the why, and the point worth keeping is that it is two whys rather than one. The
Washingtonians, for what it is worth, took the opposite position on this deliberately and
with an argument, which is what makes the comparison a comparison between two written
codes rather than between rules and no rules.

---

## What the Tradition rows say taken together

*Technical.* The twelve split into two tiers, and the split is a property of the
governance matrix rather than a reading of the text. Seven Traditions govern at least one
resource some Step consumes. Five, namely 4, 6, 7, 9 and 10, govern none, so they supply
nothing to any Step and appear in the simulation only as multipliers on the adherence of
the Traditions they guard. That multiplier form is an assumption. The index-pairing
conjecture fails on all twelve counts, and five of the twelve are arithmetic: those five
Traditions have empty rows, so no sparsity-preserving perturbation can move the
index-mate entry off zero. At every jitter level the proportion of draws in which pairing
fails on all twelve equals the proportion in which it fails on the seven that could have
gone either way, to the last draw. A threshold test that can reach the five finds them
failing by margins comparable to the seven, with thresholds from 0.417 to 0.627 against a
mean live governance entry of 0.374. Pairing fails on all twelve in 85.5 per cent
[83.9, 87.0] of draws at plus or minus thirty per cent jitter and 40.6 per cent
[38.5, 42.8] when every magnitude is randomised.

*In plain terms.* The author-coded governance table places the Traditions in two kinds;
the model did not discover the division independently. Seven of them hand the group
something it needs. Five hand over nothing and instead stop something from going wrong:
they are guards rather than suppliers. That is a transparent property of one person's
coding and an invitation for independent readers to disagree, not a result computation
can validate.

The pairing idea, that the first Step goes with the first Tradition and so on down, is
wrong everywhere. But the honest version of that result is more careful than the
headline. Five of the twelve failures are wrong for a boring reason: those Traditions
supply nothing to anybody, so of course they do not supply their own Step. Those five are
arithmetic, not evidence, and a separate test had to be built to say anything real about
them. It was built, and they fail like the others. What the whole result rests on is
whether the strengths in the two tables are roughly right. If they are, the pairing is
dead. If a reader accepts only the pattern of which Tradition touches what and rejects
every magnitude, it becomes a coin flip. So Part Four argues for its numbers rather than
hiding behind a robustness percentage, and this is the one part of the book that works
that way.

---

## What this primer does not say

**It does not rank the Traditions by importance.** The degradation column measures
membership at twenty years in a one-factor sweep from 0.85 to 0.50. Seven of the twelve
contrasts resolve and five do not. Traditions 2, 9 and 12 carry the book's central
argument, and three of the five unresolved rows are protective Traditions whose
simulation role is an assumption rather than a derivation.

**It does not establish that Traditions 2, 9 and 12 are what prevents the three
obstructions.** The appendix shows the three obstructions behave as the theorem says. The
step from there to the claim that these three Traditions are what prevents them is a
reading of three sentences, and it is the book's central claim. Nobody has a method for
testing it. In plainer terms: the mathematics says what a group has to avoid, and the
Traditions look very much like instructions for avoiding exactly those things, but
"looks very much like" is a judgement and no computation upgrades it.

**It does not validate the two matrices.** Both were built by one person. The eight
resources are that person's list and no source proposes it. A second reader marking the
ninety-six governance cells is the largest outstanding item in the project and no further
computation substitutes for it. Flipping four of fifty-six enabling cells at random
leaves Part Four's claims standing 86 per cent of the time; flipping sixteen leaves them
at a coin flip. In plainer terms: one disagreement here and there is survivable, wholesale
disagreement is not, and only a second reader can say which this would be.

**Nothing here is calibrated to AA data**, because none exists at the required
resolution. Inflow, dropout and churn were originally set to target about forty-five
members with an experienced core near nine. After mean-centring the lognormal capability
draw, 400 runs deliver 17.80 plus or minus 0.88 members overall; among the 394 viable
endpoints the experienced count above 0.5 is 1.25 plus or minus 0.20. The calibration
fails. It is disclosed rather than repaired after seeing the result.

---

## A follow-up: asking the same questions about a different fellowship

Everything above is about one fellowship. The model was built around AA's twelve Steps
and twelve Traditions, and it takes those two lists as its two inputs. A fair question is
whether any of it reaches further. In August 2026 that question was asked directly, about
Recovery Dharma, a peer-led Buddhist recovery fellowship whose program book is published
free under a Creative Commons licence.

The specific question was whether the model shows the twelve Steps simplified into the
Dharma. It does not, and the reasons are worth stating here because they mark the edge of
what this primer covers.

**The dates run the wrong way.** The Eightfold Path is roughly two and a half thousand
years older than the twelve Steps. Nothing can be a simplification of a document written
long after it. Recovery Dharma presents its program as an application of early Buddhist
teaching, not as a rewriting of AA.

**Counting does not support the word either.** Recovery Dharma sets out thirty-five
enumerated items across seven lists: three jewels, four Noble Truths, eight path factors,
five precepts, four heart practices, four foundations of mindfulness, and seven
commitments in a section called The Practice. AA, as this model codes it, is twenty-four
items across two lists. The comparison that makes simplification look true sets the eight
path factors against the twelve Steps. That is one list against one list.

**There is a group conscience, and it is the sangha.** A first pass at this said there
was no Traditions equivalent at all. That was wrong, and the correction is worth stating
because it turned into the best finding here. Every Recovery Dharma meeting opens with
members affirming that they trust in the wisdom of the Buddha, the Dharma and the Sangha,
where the Sangha is the community itself. AA locates ultimate authority in a group
conscience. Recovery Dharma locates trust in a sangha. That is the same move.

**What is missing is not the authority but the procedure.** There is no charter setting
out numbered provisions. The fellowship's whole governance commitment is one undivided
act of trust, rather than twelve separate rules a group could keep or drop one at a
time. Searching the whole book turns up no "group conscience", no "consensus",
no "business meeting", no "rotation" and no "bylaws". The jobs the Traditions do are
real, but several of them sit inside a suggested meeting script that each meeting is
invited to edit. Confidentiality sits in the closing. Self-support is the basket passed
near the end. The facilitator says plainly that they hold no authority.

**And the fellowship exists because of the failure this book is about.** Recovery Dharma
split in 2019 from an earlier Buddhist recovery program that had been built around a
single named teacher. That program fractured, in the words of one of its own former
officers, over inequities among its leaders, and people were harmed. The people who
rebuilt it, including the predecessor's executive director, made the first commitment of
the new fellowship the one every meeting now reads aloud: it is peer-led and follows no
one leader or teacher. Nobody involved had heard of this model or of the mathematics
behind it. They arrived at Traditions Two and Nine on their own, eighty-four years after
AA, by watching what happened without them. It is one case and it is the fellowship's own
account of itself, so it corroborates and cannot confirm. Chapter Twenty-Four is where
the book uses it and says so.

**The deepest difference is the sequence, and it is the one the model can see clearly.**
Two of the model's central ideas depend on the Steps being worked in order. Growth on each
Step is gated by the Step before it. That gate is why the practice which brings in new
members, Step Twelve, is also the most expensive one to reach, and why a group's ability
to grow lags its ability to hold people. Recovery Dharma's path is grouped under three
headings and practiced at the same time rather than in order. Take away the sequence and
there is no longer any reason for the member-attracting practice to be the costly one. So
those two ideas simply do not carry across.

None of this changes a single figure above. What it changes is the scope a reader should
give them. This model is not about recovery groups in general. It is about groups that
have a numbered sequence of practices and a fixed written charter. Recovery Dharma has
neither, and a model with one Step matrix and one Tradition matrix has nowhere to put a
fellowship built that way.

Two cautions, in the spirit of the section above. Nothing here compares the two
fellowships for effectiveness, and nothing in this project could. Nothing here is advice
about which room anyone should walk into. The full comparison, with the page references
and the arithmetic, is appendix section A12, and it is written to stand alone.

**A second reading, from the other end.** The model assumes that most people arrive
because a member brought them, rather than finding the group on their own. That is one of
the hundred and eighteen chosen numbers and it had never been checked against anything.
In August 2026 the twenty-nine personal stories in the 1939 first edition of *Alcoholics
Anonymous* were read for exactly this. They support the assumption for that fellowship at
that time: the recurring shape is a recovered drinker turning up in person, often several
of them, and in one case about twenty men visiting a single man in hospital. Only one
story describes somebody reached without a visit, by letter and a copy of the book, and
the fellowship presents that as an experiment it was unsure of, recording that it had
begun to think the book inadequate without personal contact.

Set beside Recovery Dharma, where almost everybody arrived through a website, a free
book, a flier, a therapist or a chaplain, the two readings bound the assumption rather
than confirm it. How a fellowship recruits is a fact about that fellowship and that
period, not about mutual-aid groups in general, and the model should be read as speaking
about AA in its founding decades. Appendix section A13 carries the census and its
limits, of which the largest is that the stories were selected to persuade and everyone
in them recovered.

---

## Where every figure comes from

The five headings below are the book's canonical reference headings, in the order
`tools/check_chapter.py` requires of a chapter. The primer is exempt from that rule,
because it is an appendix rather than a chapter and the checker skips its structural
block entirely. It keeps the convention anyway, and the exemption is the reason a reader
should not assume anything enforced it.

The separately supplied corpus under `research/staged/` is reserved for the next
iteration. None of those remaining items is evidence for this primer merely because a
local file exists.

**Read in full:**

Golub, B. and M. O. Jackson (2010). "Naive Learning in Social Networks and the Wisdom
of Crowds." *American Economic Journal: Microeconomics* 2(1): 112-149. The vanishing
influence condition and the three obstructions. Read at source.

Maxwell, M. A. (1950). "The Washingtonian Movement." *Quarterly Journal of Studies on
Alcohol* 11: 410-452. The claim that anonymity has "sheer survival value". Read in full
from the project's retyped reproduction, not at journal source. The original project PDF
and text are stored in the Maxwell subdirectory of `research/incorporated/`; four
demonstrable transcription errors are listed in `research/SOURCES.md`.

Grosh, A. B. comp. (1842). *Washingtonian Pocket Companion.* Second edition. Utica,
N.Y.: B. S. Merrell. The Washingtonians' own manual, used here for the written
analogues of Traditions 4, 7, 9 and 10 and for their deliberate opposite position on
anonymity. Read at source; saved in `research/`.

Recovery Dharma Global (2023). *Recovery Dharma.* Second edition. Recovery Dharma Inc.
CC BY-NC-SA 4.0. The only source for the follow-up section above. Read: the front matter,
the whole of Section I, the whole of Section II with its fourteen personal recovery
stories, and the glossary, meeting format and dedication of merit. Only the meditations
and inquiry questions were not read. The 2019 split is reported in the stories by people
who held office in the predecessor organization, whose founder is named in that source
and is deliberately not named here. Saved in
`research/incorporated/RecoveryDharma_2023/`.

**Cited at a remove:**

Nothing. Every source named here was read at source. The primer restates findings from
chapters that do cite at a remove, and those removes are recorded in the chapters rather
than repeated here.

**Internal, and reproducible from this repository:**

`model/aa_group_model.py`, matrices S and GOV, the effective-adherence function, and
the arrival and dropout expressions.

`model/book-calculations.ipynb`. Section 2 for the influence weights and consensus
errors behind every deliberation figure; 3 for the twelve-Tradition degradation
comparison; 10 for the apparatus, including the derived group-dependence table; 11 and
11b for the coupling, the principal suppliers and the perturbation designs; 11c for the
threshold test; 11d for the load column and the reassignment test; 13 for the service
results behind Step Twelve; 14 for the Part Five failure modes; 17 for the resource-list
test; 18 for the sparsity perturbation.

`research/tradition_paired.json`, the 400-replication paired degradation runs, produced
by `model/tradition_paired.py`. `research/part5.json`, 4,800 runs behind the Tradition 3
sweep and the three failure modes. `research/ch15_service.json`, the three service
configurations. `research/core_thresholds.json`, the two membership thresholds and the
calibration figures. `research/resource_list.json`, the sixty-four resource-list
variants. `research/oat_full.json`, the 944 registered multi-level perturbation points.
`research/structural.json`, the four structural variants.

`appendix/APPENDIX.md`, sections A2 for the effective-adherence specification, A4 for
the seed counts and estimands, A5.4 and A7.1 for the perturbation designs and what they
cannot reach, A8 for the threshold, reassignment and sparsity-pricing tests, A5.2 for the
degradation ranking, A7.3 for the structural variants and A7.6 for the resource-list
test. Part Two's sensitivity analysis is the section titled
"Part Two: sensitivity of the mapping between the theorem and the Traditions", which is
numbered A8 and shares that number with the reproduction section at the end of the file.

Manuscript chapters 8, 9, 10, 12, 13, 15, 16, 17, 18, 19 and 20, whose Machinery
sections carry the full designs and estimands for every figure quoted above.

**What was not read:**

The AA literature was said here to gesture at a parallel between the Steps and the
Traditions. That was written without having read it. *Twelve Steps and Twelve Traditions*
was read in full on 10 August 2026, and no Tradition chapter refers to the Step of its own
number, while the word "Tradition" does not appear in any Step chapter at all. So the
conjecture is refuted as a thing people believe rather than as a thing somebody
published, and I cannot say how strongly the literature gestures.

No study of AA group culture, which is why the behavioural description behind
Tradition 3's retention mechanism is illustration rather than evidence.

The literature on skill depreciation rates in adults, which would say whether six per
cent a week is the right order of magnitude for anything comparable. It is the most
easily improved number in the model and it has not been tried.

From Recovery Dharma, only the selected meditations and the inquiry questions, which are
practice material rather than description. The fourteen personal stories were read after
a first pass had skipped them, and skipping them was the reason that pass got the
governance question wrong.

Anything independent about the 2019 split. The account above rests entirely on the
successor fellowship's own literature, written by people who left the predecessor. No
press coverage and no statement from the other side was sought. That is a one-sided
record and the book's use of it inherits the weakness.

The research literature on Buddhist and mindfulness-based recovery programs, which was
not searched at all. The follow-up section compares program documents and one
fellowship's account of its own history, and knows nothing about either fellowship's
outcomes.
