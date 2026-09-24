# Progress Log

Running record of what has been verified, corrected, and found. Updated as work proceeds.

Part One sessions are below. Part Two begins at the end.

---

## Session 2

### Step 1 complete: Gough read at source

Downloaded the full 1869 autobiography (176,000 words) and read Chapters X and
XIII directly rather than inferring from chapter titles.

**Chapter Three was substantially wrong and has been rewritten.** The earlier
draft claimed Gough framed the 1845 episode defensively, as a charge to rebut
rather than a relapse to own. His own statement of 22 September 1845 says *I have
fallen*, accepts blame for going with a stranger and for the brandy, submits to
his church's judgment, and tells doubters he does not blame them for
disbelieving. The error ran in the direction of making the argument easier, which
is the direction errors usually run.

**What replaced it is stronger.** Gough relapsed twice and documented both, so the
chapter now rests on nothing about his character:

- **April 1843.** Tells two friends, re-signs the pledge, burns his appointment
  book, is talked into attending the Monday meeting, and the room receives him
  with what the *Cataract and Washingtonian* called the true spirit of
  Washingtonian sympathy, kindness and charity. Ten days, handled internally.
- **September 1845.** His church appoints an examining committee. The
  congregation formally votes to instruct it to inquire thoroughly. The committee
  spends over a month attempting to verify a sick man's account of a week he
  cannot remember, travelling to New York and interviewing the proprietor of the
  Croton Hotel. Then a press war. Then, thirteen years later, the Court of
  Exchequer.

Same man, same illness, twenty-nine months apart. The difference is entirely in
the institutional response, and the variable that changed is that his name had
become an asset.

**Unresolved conflict found.** The sceptical case against Gough holds that there
were no soda shops on Chatham Street. Gough's own statement says there are two or
three such establishments in that vicinity and that he believes he could identify
the shop. These are in direct contradiction. Only the 1845 newspapers or the
American Antiquarian Society scrapbook will settle it.

### Step 2 complete: model number audit

Every figure quoted in Part One regenerated from the current model in one session.

**Verified exactly:** all decline scenarios (full adherence survival 1.00 at 45.0
members; attraction lost 1.00 at 13.4; referrals lost 0.20 at 2.9; both lost 0.00;
gatekeeping 0.90 at 30.7), the established core at 9.0, all maximum influence
weights (flat 0.100 to 0.002 across N=10 to 500; dominant flat at 0.350; clique at
0.167), and the rotation floor at 0.0307 for a pool of 12 in a group of 400.

**One real error found and fixed.** The consensus-accuracy figures were Monte
Carlo estimates quoted to three decimals, and they moved between runs by more than
the last digit implied. They have been replaced with the exact closed form: if
members receive the truth plus independent noise of standard deviation sigma, the
consensus is normally distributed about the truth with standard deviation
sigma times the norm of the influence vector, so mean absolute error is that times
the square root of two over pi. Under flat weighting this is exactly
sigma * sqrt(2/pi) / sqrt(N).

Corrected values now in Chapter Three: flat 0.252 at N=10 falling to 0.036 at
N=500; dominant member 0.328 falling only to 0.280; clique 0.275 to 0.231;
rotation over a fixed pool of twelve 0.253 to 0.087.

**Note for the paper.** The same Monte Carlo figures appear in
`anonymity-as-an-aggregation-condition.docx` and its PDF. They should be replaced
with the analytic values there too.

### Step 3 partial: post-1950 scholarship

Two findings that change the acquisition list.

**Blumberg, L. U., with Pittman, W. L. (1991). *Beware the First Drink! The
Washingtonian Temperance Movement and Alcoholics Anonymous.* Seattle: Glenn Abbey
Books.** This is a book-length modern treatment of precisely the comparison Part
One is built on, and I had not identified it. It now ranks alongside Kurtz as a
required acquisition. Blumberg also published "The significance of the alcohol
prohibitionists for the Washingtonian Temperance Societies, with special reference
to Paterson and Newark, New Jersey," *Journal of Studies on Alcohol* 41 (1980):
37-77, which is a local study of exactly the political-entanglement question
Chapter Two treats as unsupported.

**Alexander, R. M. (1988). "'We Are Engaged as a Band of Sisters': Class and
Domesticity in the Washingtonian Temperance Movement, 1840-1850." *Journal of
American History* 75(3): 763-785.** A major-journal treatment of a dimension Part
One currently omits entirely.

**Consequent gap, now flagged in Chapter One.** Part One tells the movement as six
working men and their imitators. The Martha Washington Societies formed from May
1841, with women in leadership roles for the first time in American temperance;
juvenile auxiliaries followed; and freed Black Americans organised separate
societies. This is both a coverage gap and an argument gap: a movement generating
auxiliaries for non-alcoholic women and children had a porous boundary by design,
which is Chapter Two's absorption thesis appearing earlier than currently placed.

**Also identified:** Dannenbaum, *Drink and Disorder: Temperance Reform in
Cincinnati from the Washingtonian Revival to the WCTU* (Illinois, 1984); Blocker,
*American Temperance Movements: Cycles of Reform* (1989); Blumberg, "The ideology
of a therapeutic social movement: Alcoholics Anonymous," *JSA* 38 (1977).

### Step 3 complete: the timing objection tested and answered

The strongest objection to Part One was that the comparison is confounded by
chronology: the Washingtonians were absorbed because temperance was the dominant
reform cause of the 1840s and was standing by to absorb them, whereas AA arrived
in 1935 with temperance discredited and nothing waiting to capture it. On that
reading Tradition 10 is a scar rather than a shield.

**The objection is testable and it fails.** Something did try to capture AA, in
1944, and AA initially said yes.

Marty Mann, an AA member sponsored by Bill Wilson, founded the National Committee
for Education on Alcoholism in April 1944, with offices at Yale, sponsored by the
Yale group around E. M. Jellinek. The *Grapevine* endorsed it enthusiastically.
Wilson wrote a piece supporting the arrangement in October 1944. The names of both
AA co-founders appeared on the committee's letterhead. Mann broke her anonymity
and toured as its public face. Then the committee solicited funds, and the
solicitation reached AA members.

Wilson and Smith withdrew. Mann agreed to stop identifying publicly as an AA
member. The conclusion drawn, in AA's own words, was that total non-affiliation
was the only answer. Twelve Points to Assure Our Future appeared eighteen months
later.

**Why this strengthens rather than merely survives the objection.** The structural
situation was identical to the Washingtonians'. In both cases a fellowship of
recovered drinkers proved to be excellent evidence for a larger cause; in both
cases that cause was the dominant reform movement of its day with real
institutional resources; in both cases the fellowship's most prominent members
found the larger cause more interesting than the parish work and drifted toward
it. Hawkins and Gough toward general temperance advocacy, Mann toward public
health education. The difference is that AA had eleven years of wreckage to read,
wrote the rules eighteen months after the incident, and then held to them,
including Wilson declining a Yale honorary doctorate in 1954 on the explicit
grounds that accepting would encourage big shots and power seekers.

Three weaker objections are now also named in Chapter Six and not fully answered:
the disease concept and medical alliance; the referral stream, which the model
itself treats as decisive and which the book arguably under-weights; and
survivorship bias, whose only real defence is that Part Two does not depend on
Part One.

---

## Standing status

| Ch | Source status |
|----|---------------|
| 1 | Solid on Maxwell. Coverage gap flagged (women, Black societies). |
| 2 | Solid on Maxwell. Needs Blumberg 1980 on the political question. |
| 3 | **Now first-hand.** Gough read at source for both relapses. |
| 4 | Provisional. Needs Kurtz. |
| 5 | Provisional. Needs Kurtz. |
| 6 | Solid on Maxwell. 1944 NCEA episode second-hand, needs verification. |

### Step 4 complete: paper corrected, claim register built

**Paper corrected.** The Monte Carlo accuracy figures in
`anonymity-as-an-aggregation-condition.docx` and its PDF have been replaced with
the closed-form values, and the table caption now gives the derivation. The claim
that error declines "approximately as N^(-1/2)" under flat weighting has been
strengthened to "exactly", since that is what the algebra gives. Both files
rebuilt and verified.

**Claim register built** (`part1-claim-register.md`). Every load-bearing factual
claim in Part One, with source and status: primary read directly, scholarly read
directly, reported at a remove, or my own inference.

The register makes the shape of the problem exact:

| Chapter | Primary or scholarly | At a remove |
|---|---|---|
| 1 | 22 of 27 | 5 |
| 2 | 13 of 17 | 4 |
| 3 | 14 of 20 | 6 |
| 4 | **0 of 14** | 14 |
| 5 | 2 of 6 | 4 |
| 6 | 9 of 17 | 8 |

Chapter Four currently has no claim sourced to a document I have read. Kurtz would
move roughly twenty-six claims from "at a remove" to "scholarly, read directly"
in a single reading.

### Acquisition attempt: unsuccessful

Kurtz's *Not-God* is held by the Internet Archive under lending restriction
(identifiers `notgodhistoryofa0000kurt` and `notgodhistoryofa00kurt`) and is not
available as full text. Search-inside returned nothing. Blumberg and Pittman's
*Beware the First Drink!* does not appear in the Archive at all.

Neither is obtainable by the means available to me. Both require a library, a
purchase, or an Internet Archive borrowing account. This is the binding constraint
on finishing Part One, and no amount of further searching will remove it.

---

## Next actions

1. Acquire (requires a library or purchase, not further searching): Kurtz; Blumberg and Pittman 1991; Alexander 1988; Blumberg 1980;
   *Pass It On* p. 320 or an independent account of the 1944 NCEA episode.
2. Read Gough chapters XXVII to XXIX (the libel trial) at source; the text is
   already downloaded and the chapter offsets are known.
3. Incorporate the Martha Washington Societies and the Black Washingtonian
   societies into Chapter One rather than merely flagging them.
4. Reader passes: one historian, one AA member.


---

## Part Two

### Chapters 7, 8 and 9 drafted

Written out of order, per the plan: Chapter 8 first as the hardest translation
problem, then Chapter 9, then Chapter 7 as the ramp once it was clear what it had
to ramp into.

| Ch | Title | Words | FK | Status |
|----|-------|-------|----|--------|
| 7 | How a Room Decides | 2,327 | 7.4 | Drafted, checked |
| 8 | The Condition | 3,109 | 6.7 | Drafted, checked |
| 9 | Confident and Wrong | 2,424 | 7.1 | Drafted, checked |

**One result I had not computed before writing Chapter 9.** Golub and Jackson's
third obstruction, imbalance, turns out to be far worse than the other two. Five
members whom everyone listens to, and who listen mainly to each other, hold *all*
of the group's influence in the limit. Everyone else holds approximately zero. So
a meeting of two hundred and fifty structured that way decides exactly as well as
a meeting of five: error 0.357, which is the square root of two over pi divided by
the square root of five. The two hundred and forty-five others are talking and are
not in the room as far as the decision is concerned.

The practical form: the dangerous question about a group's core is not whether it
is respected, but whether it listens.

**A checker bug found by accident.** The LaTeX normalisation two sessions ago
stripped the dollar delimiters but left the commands, so Chapters 3 and 8 carried
thirty-three orphaned fragments that the checker passed because it only looked for
dollar signs. Both cleaned; the checker now fails on bare LaTeX commands. This is
the second time the check has caught something introduced during tidying rather
than during drafting.

**Repetition control.** Cross-checking flagged one verbatim eight-word phrase
carried from Chapter 8 into Chapter 9, and a Tradition 2 paraphrase shared between
Chapters 7 and 8. Both varied. Chapter 3's Machinery was also carrying the full
four-regime comparison tables, which are now Chapter 9's job; trimmed to the
flat-versus-dominant contrast the Gough argument actually needs, with a forward
pointer.

### Chapter 10 drafted, and it corrected a claim I had been repeating

**The stale claim.** I had been saying, in the Part Two plan, that rotating twelve
people in a group of four hundred puts maximum influence "nearer the clique regime
than the flat one". Computing it properly shows otherwise: 0.031 against a flat
benchmark of 0.0025 and a caucus at 0.167. It sits between them and is closer to
flat on both influence and error. Corrected in the plan; it had not reached any
drafted chapter.

**The result that replaces it is better.** A fixed rotation pool produces a
*floor*, not a decline. Pool twelve gives 0.041 at N=50, 0.032 at N=200, 0.031 at
N=400, 0.030 at N=800. It converges while the flat benchmark keeps halving, so the
ratio runs 2.1, 6.4, 12.3, 23.9. The group grows and throws away the benefit of
growing.

**And a clean testable rule fell out.** The pool needed to come within a factor of
two of an evenly weighted room is about **twenty-six per cent of the group**, at
every size from fifty to eight hundred. A proportion, not a headcount. That makes
the prediction checkable against any group's service roster: count how many
different people have held any position in recent years, divide by the group size.

### Chapter 11 drafted: Part Two complete

The chapter's job was to apply Part Two's three failure modes to the Washingtonians
rather than recap them, and doing so produced the strongest new claim in Part Two.

**The Washingtonians had the worst of the three, structurally.** Their meetings were
flat: everyone testified, attention ran in every direction. But the movement *grew*
through touring speakers, and a lecture is not a meeting. Attention runs one way.
Five thousand people listen to Hawkins; Hawkins listens to nobody. That is Golub and
Jackson's imbalance condition, which Chapter Nine showed captures effectively all of
a group's influence in the closed set.

So the prominent-agent problem was downstream, not causal. Gough's 1843 relapse
produced nothing and his 1845 relapse produced a national controversy; the variable
that changed was the weight the growth mechanism had placed on him.

**And the contrast with AA is structural rather than moral.** Facing the same
scaling problem in 1937, AA was refused the money for missionaries and wrote a book
instead, published with no author's name on it. A book confers no influence weight
on anybody, because there is nobody there to confer it on. Two movements, same
problem, opposite instruments.

### Sync review of Parts One and Two

Eleven chapters, 33,139 words, all passing the checker.

**Repetition found and fixed.** Twenty-one shared ten-word phrases between Chapters
9 and 11, both carrying a Gough passage. Chapter 9 trimmed to a brief pointer, since
Chapter 11 is the proper home for the synthesis. Also one shared formulation between
Chapters 8 and 10 about how the Traditions were compiled, varied.

**Cross-part references all resolve.** No chapter cites an undrafted chapter except
as a deliberate forward pointer into Parts III to VI.

**Reading levels run 6.6 to 11.0.** Chapter 6 remains the hardest in the book and is
still a candidate for a simplifying pass. Part Two runs 6.6 to 9.1, which is easier
than Part One, as intended for the formal material.


---

## Sensitivity analysis

Ran global perturbation at three levels (12.5, 25 and 50 per cent) over all 118
hand-chosen parameters, 30 draws each, plus a one-at-a-time sweep on the 21 scalars.

**The parameter count was wrong.** Earlier plans said "roughly 28". The real figure is
118 chosen by hand: 21 scalars, 12 step speeds, 55 non-zero cells in the consumption
matrix, 30 in the governance matrix. Understated by a factor of four in a book whose
credibility rests on being straight about exactly this.

**Robust:** full adherence persists (97 / 90 / 73 per cent across levels). Losing
referrals is worse than losing attraction (100 / 100 / 87). The ordering is the
strongest thing the simulation says.

**Not robust:** the specific claim that a referral-starved group dies four times in five
held in only 73 per cent of draws at the mildest perturbation and 50 at the largest, with
the range covering zero to one at every level. It fails at the gentlest shake. Softened
in four chapters, with a robustness note beside the table in Chapter One.

**The one-at-a-time sweep explains why.** Three parameters, each moved alone by a
quarter, take the outcome from certain death to certain survival: the decay rate, the
gating exponent, and how strongly early practice protects against dropout. The result is
a knife-edge, not an estimate. Seven other parameters have no effect on it whatever.

**A claim that needed restating rather than softening.** The quality-holds-during-decline
prediction was reported at 78 per cent, which was conditional on the starved group
surviving. Unconditionally it is about 47 per cent, because half the perturbed runs kill
the group outright. Both numbers are now given, in the preface and in PARAMETERS.md,
because the conditional figure alone would mislead.

**Still to do:** move the sensitivity code out of a throwaway script and into
`../model/book-calculations.ipynb` as its own section. At present the analysis that
underwrites the preface is not reproducible from the repository, which is the fragility
this whole exercise exists to remove.


---

## Part Three: literature search on step ordering

Done, and it improves Chapter 13 by narrowing it.

**The claim survives but changes shape.** Step ordering has not been tested, and the
reason is more interesting than neglect: the standard measurement construct is the *sum of
steps completed*, which discards order by construction. The question has not been asked
because the instruments cannot express it.

**A finding that must be confronted.** Greenfield and Tonigan (2013), following 130 new AA
affiliates over nine months, found a two-factor structure in step work: behavioural and
spiritual. The factors have different predictors, opposite time trends, and different
outcome relationships, and only the spiritual factor prospectively predicted percent days
abstinent. That is indirect evidence against a strict twelve-link chain, and it arrives
before any modelling. Chapter 13 must present it rather than route around it.

**And it corroborates the identification argument.** More participants endorsed step work
on the indirect measure than the direct one for nine of twelve steps. Which instrument you
use changes what you conclude, which is precisely the measurement-error problem the
chapter's design section addresses.

**Still to check:** Carroll (1993) on step adherence; whether any treatment-manual
literature has tested sequence effects experimentally.


### Chapter 13 drafted

Written first in Part Three, per the plan, because the literature search that gates it was
the one outstanding research task.

**The chapter got narrower and better.** It can no longer claim virgin territory. Its
argument now runs: the ordering question has never been asked because the standard
instrument records a *sum* of steps completed, which discards order by construction; and
the one study that examined the structure of step work found two factors rather than one
chain, which is reason to doubt the strict version before any modelling. The contribution
is making the question askable.

**The threshold is at zero, not at minus infinity.** Worth stating because it widens the
chain hypothesis considerably: strict ordering holds for every rho less than or equal to
zero, so the chain does not require perfect complementarity, only the absence of
substitutability. Output with the prior step at zero is 0.0000 at rho = -100, -4, -1 and 0,
then 0.2167 at +0.3 and 0.4803 at +0.9.

**The three-proxy requirement now has a sharper justification.** Single-proxy recovery is
tolerable far from the boundary (-3.45 for a true -4.0) and unreliable near it (-0.10 for a
true 0.0, +0.35 for a true +0.5). It fails exactly where the question is decided.

**Checker bug found and fixed.** The regex testing for a statement of what was not read
did not match "at one remove", only "at a remove" or "at one or more removes". Chapter 13
tripped it despite having four such statements. Pattern widened.

**Outstanding for this chapter:** the Greenfield and Tonigan paper is read via abstract
only and should be obtained; Carroll (1993) on step adherence has not been consulted and is
the likeliest place for a prior treatment of sequencing.


### Chapter 14 drafted, and it falsified a figure carried in four other files

2,679 words, FK 6.9, passes the checker, 44 figures asserted in the notebook, zero shared
seven-word phrases with any other chapter's main text.

**The fragility figure was wrong, and wrong in the direction that flatters.** Every plan
and the preface said a five per cent change in the decay rate removes the bistability.
Computed properly it is **2.79 per cent**, and the failure is not the one described.
Bistability does not dissolve by the two states merging. Above `delta0` = 0.0617 the
*healthy* equilibrium ceases to exist, so a typical member cannot hold a daily practice
from any starting position in a fully adherent group. Below baseline the healthy state
simply strengthens, reaching 0.5569 at minus twenty per cent against 0.3205 at baseline.
The fragility is one-sided. Corrected in ch00-preface, PART-3-PLAN, PARAMETERS.md and the
orientation files.

**A result the plan did not anticipate, and it is now the chapter's best claim.** Member
heterogeneity does not soften the individual threshold, it hides it. Individual critical
decay rates across 2,000 members span a factor of four: tenth percentile 0.0307, median
0.0605, ninetieth 0.1236. Each member has a hard edge; the edges sit in different places.
So the population curve is smooth at every point (0.507 of members hold a healthy state at
baseline, 0.448 at plus ten per cent, 0.111 at double), and the full group simulation
survives ten seeds of ten across the entire range from minus thirty to plus fifty per cent
with maintenance sliding 0.3376 to 0.0132.

Each member has a cliff and the room has a slope. A group perceives itself through an
average of step functions, and averaging destroys exactly the information that would tell
the room somebody has already gone. That is a second, independent way a deliberating group
can fail, and it has nothing to do with influence weights, so it complements Part Two
rather than repeating it.

**The collapse profile is back to front and I had not predicted it.** In the collapsed
attractor Step 1 sits at 0.758 against a healthy 0.766, essentially untouched, while Step 8
falls 0.459 to 0.056 and the three daily steps go to zero. What survives is the knowledge
that one is an alcoholic; what goes is everything that knowledge was meant to lead to. This
was not put in by hand. It falls out of the gate weighting, which was chosen so that a
newcomer with nothing to maintain is not penalised for failing to maintain it. It yields a
testable prediction: acceptance items should barely move during a slide, daily-practice
items should move first and most.

**Hysteresis is sharp.** Total withdrawal of the group for eleven weeks is fully
recoverable; twelve weeks is not, with the same group and five years to work with. The
eleven and a half weeks is worthless as a number for the same reason as everything else
here. The asymmetry is not.

**A source claim in the plan did not survive checking.** The plan said Hufford and
colleagues found a cusp catastrophe outperformed "linear and logistic" specifications. The
published abstract says linear models only, and the comparison statistics are not in the
abstract. The stronger word is removed. The warrant is also thinner than the plan implied:
two preliminary studies, 51 inpatients and 43 outpatients, six months. Citation details for
Hufford et al. (2003), Witkiewitz and Marlatt (2007) and Hunter-Reel et al. (2009) are now
verified and recorded in SOURCES.md under a new "obtained as abstract only" heading.

**A second, unrelated error found while propagating.** The preface said the model has
**238** numbers chosen by hand. Nothing in the model is 238. Counted from the code the
figure is 118 chosen by hand out of 226 cells, which is what PARAMETERS.md and README have
said all along. Corrected in the preface.

**And PARAMETERS.md's own breakdown was wrong in four of six rows**, although its headline
total of 118 was right, which is presumably why it went unnoticed. It said 21 continuous
scalars, 55 non-zero cells in S and 30 in GOV. Counted from `aa_group_model.py`: 22, 49 and
35. Both wrong sets happen to sum to 118. Corrected, with a note recording the recount.

**A bug in my own notebook code, caught by the checker's discipline rather than by
reading.** The Chapter 14 `settle` helper originally passed group inputs by mutating module
globals. Run in a fresh kernel it was correct; run after a restart with restored state it
silently ignored the override and reported that a member who left the group for six months
was unaffected. Seven assertions failed and that is the only reason it was found. Rewritten
to pass group inputs explicitly. Worth remembering: a helper that reads its inputs from
globals will pass every test that runs it in one order.

**Notebook.** Section 8 added, five code cells. Whole notebook re-run: 104 assertions, zero
failures. One pre-existing cell, the paired tradition-comparison simulation in section 3,
was not re-executed this session because it runs longer than the tooling available here
allows in a single call. It contains no assertions, so it cannot affect the regression
result, but its stored output is from an earlier session.

**Still to do on this chapter:** obtain the Hufford full text; the fit statistics would
either strengthen the shape claim or weaken it, and at present the chapter rests on an
abstract.


### Whole-book consistency pass

Ran after Chapter 14, over every chapter, both plans, the preface and the research files.
Four things were wrong. Three of them had been wrong for several sessions.

**Every figure in every chapter now traces to the notebook.** Extracted all decimal figures
from ch00 to ch14 and matched them against notebook source and output. Five did not match
on a string comparison and all five are benign: two matrix literals written `.30` in code
and `0.30` in print, two roundings in the Chapter 10 pool table (0.1178 to 0.118, 0.0156 to
0.016), and one prose rounding in Chapter 14 (0.459 to 0.46). Nothing unaccounted for.

**Cross-references all resolve.** The only forward pointers into undrafted material are two
into Chapter 12, both deliberate, and both now recorded in the Part Three plan as
obligations Chapter 12 must discharge.

**Error 1: the sensitivity table mixed two definitions of survival.** Each draw records the
fraction of three seeds that survived, so a claim can be scored on every seed or on any
seed. The full-adherence row was scored on every seed. The attraction row was scored on any
seed and printed in the same table under the same heading. On a common standard the
attraction row is 100 / 97 / **63**, not 100 / 100 / 83. At the largest perturbation a group
that has lost attraction is therefore *less* likely to survive in every seed than a fully
adherent one, which is the opposite of what the row implied. The ordering claim is
unaffected, since it is a paired within-draw comparison, and still holds in 87 per cent.
PARAMETERS.md now gives both standards and says which was wrong.

**Error 2: "seven parameters have no effect" was four.** Recomputed from `sens3.json`:
`k_ident`, `lam_exog`, `cost` and `contrib` are flat at zero. `hill_k`, `k_recip` and
`drop0` were wrongly included; they move the outcome to 0.33 at *both* ends, which is a flat
response, not no response.

**Error 3: a figure with no code behind it.** PARAMETERS.md claimed the matrices were tested
"by perturbing every entry by thirty per cent across two thousand draws", with index-pairing
rejected in 85.5 per cent. No such test exists in this repository. `sensitivity_tiered.py`
perturbs at plus or minus fifty per cent over thirty draws and scores survival, not
index-pairing, and neither saved JSON contains a 2,000-draw run. Nothing drafted rests on
it, but **Chapter 16 is entirely about index-pairing** and would. Flagged in PARAMETERS.md
with instructions either to re-run and record it or drop it. The supported version of the
same idea is the structural test, which does hold at 100 per cent over thirty draws.

**Error 4, minor: Chapter 5 said Traditions 4 and 7 were "the two largest effects".** They
tie with unity at 5.5 members lost and are separated only by a smaller standard error.
Reworded to say they are the only two that clear significance, with the tie noted. Chapter 6
also said the ordering held "in every one of thirty perturbed parameterisations" without
naming the level; it holds in every draw at the two milder levels and in 87 per cent at the
largest, and now says so.

**The sensitivity section is now reproducible.** This was the outstanding item from the
session that ran the sweeps: the analysis underwriting the preface was carried as
hand-typed numbers. Notebook section 7 now derives every figure from `research/sens3.json`
and `research/tiered.json`, so the same class of transcription error cannot recur silently.
That is how errors 1 and 2 were found.

**Notebook state.** 138 assertions, zero failures. Every cell re-executed this session
except the paired tradition comparison in section 3, which exceeds the per-command time
limit available here; it was recomputed separately in blocks and reproduces its stored
output exactly, figure for figure.

**Files.** The three retired orientation stubs (PROJECT-INSTRUCTIONS, START-HERE,
FOLDER-INSTRUCTIONS) are deleted. CLAUDE.md is the only instructions file and README.md the
only status file. The claude.ai Project has been emptied.

**Repetition sweep across all pairs of chapters.** Shared eight-word phrases in main text
fell from 28 to 18. Three were the author's own prose repeated and were varied: the famous
speakers sentence shared by Chapters 1 and 2, the eleven-years-of-letters sentence shared by
Chapters 5 and 8, and the total-abstinence clause shared by Chapters 2 and 6. The remaining
18 are all legitimate: the Maxwell quotation, the statement of the Golub and Jackson
condition, a journal title, and the book's own thesis sentence deliberately echoed between
the preface and Chapter 2.

**Two standing warnings, neither new and neither introduced this session.** Chapter 6 is
still the hardest chapter in the book at FK 11.1, above the checker's threshold, and is
still a candidate for a simplifying pass. Several chapters carry sentences over 45 words.
Both are warnings rather than failures and have been consciously accepted before.

**Next session: Chapter 12, Twelve Dials.** Not overdue; it is third in the sequence by
design, for the same reason Chapter 7 was written third in Part Two. Its spec in the Part
Three plan now records the two forward pointers it has to discharge, from the preface and
from Chapter 14's references, and what Chapters 13 and 14 have already spent so it does not
re-derive them.


### Targeted sensitivity, all 118 parameters

The one-at-a-time sweep had never been run over the whole model. It covered **21 of the
118**: the continuous scalars, minus room capacity, scored on a single outcome. Ninety-seven
parameters had never been varied alone, including all twelve step speeds and every cell of
both matrices. `model/sensitivity_oat_full.py` now does all of them, at plus and minus
twenty-five per cent, over three scenarios and four outcomes. 236 perturbations, raw results
in `research/oat_full.json`, notebook section 9.

**The headline claim came out much stronger.** Losing referrals is at least as damaging as
losing attraction in **all 236** perturbations, without exception. Global perturbation
already put it at 100 / 100 / 87 per cent, but targeted perturbation is the harder test: a
claim can survive random jitter by averaging while still resting on one number. This one
rests on no number in the model. Stated in Chapters 1, 4 and 6 and in the preface.

**Full-adherence persistence survived 235 of 236.** The single exception is member
heterogeneity at minus twenty-five per cent, dropping survival to 0.67. That is the
parameter PARAMETERS.md already names as the least defensible in the model, so the sweep
found the weak point where the audit predicted it.

**The fragile claim is more fragile than the preface said.** Three parameters give a full
zero-to-one swing in referral-starved survival, which is what the preface reports and is
correct. But 53 of 118 move the outcome off the floor at all, and only 65 leave it alone.
The preface now says so.

**The governance matrix cannot affect a fully adherent group, and this is algebra.** All 35
of its cells produce exactly zero change in every outcome. `GOVW` is column-normalised, so
governance quality is GOVW' times Te, which equals one for every resource whenever every
tradition is at 1.0, whatever the entries are. Under partial adherence a twenty-five per
cent change in one cell moves the normalised weight by about one per cent and still moves no
outcome. The preface argued from the weaker randomisation test that the model rests on the
matrices' structure rather than their magnitudes; for this matrix it is now provable, and
the preface says it.

**A consequence worth recording.** Any sweep that perturbs governance entries and scores a
*fully adherent* group is testing nothing. The uniform global sweep does exactly that in its
full-adherence rows, which are therefore effectively over 83 parameters rather than 118. The
attraction and referral rows are unaffected. Flagged in PARAMETERS.md section 4c.

**Two things the sweep says about Part Three.** No single parameter moved by a quarter
drives *group* maintenance to zero, while Chapter 14's *individual* threshold is knife-edge
at 2.79 per cent in the decay rate. That is the same individual-versus-group distinction
reached a second way. And the step-ordering exponent `p_gate` is the single strongest
influence on maintenance in the whole model, swinging it by three times baseline. Chapter 13
makes the *sign* of the related substitution parameter its whole subject; the *magnitude* of
the ordering exponent matters at least as much and nobody has measured either. Worth a line
in Chapter 12.

**Chapter 6 is no longer the checker's problem child.** It was the one chapter above the FK
threshold, at 11.1, flagged as a candidate for simplification in two previous sessions.
Splitting nine long sentences brings it to 9.9 with no loss of content. Every chapter now
passes with no FK warning.


### Chapter 12 drafted: Part Three is one chapter from complete

2,012 words, FK 7.7, passes the checker, and **zero shared seven-word phrases with any other
chapter's main text**, which is the cleanest any chapter has come out of that check.

**Both forward pointers discharged.** The preface promised the model would be "described
properly in Chapter Twelve" and Chapter 14's references parked Ben-Porath here. Both are now
delivered, and the book has no unresolved forward pointer into undrafted material.

**The spine is the distinction between "I did Step Four" and "Step Four is at 0.8".** One is
about the past and permanent, the other about now and perishable. If the second is the right
description then everything else follows: practice decays, order matters, and the group's
contribution varies by step. That framing avoided the model-tour problem the plan warned
about, because each property arrives as a consequence rather than as a feature.

**A claim I had not expected the chapter to be able to make.** The derived group-dependence
coefficients say the group is most necessary at the two ends and least in the middle. Steps
1 and 12 sit at the maximum, Step 7 at a sixth of it, a spread of six to one. That is a
statement about what a meeting is for, and it fell out of the resource assignment rather
than being put in. Confidence is in the shape, not the coefficients, and the chapter says so.

**The sweep gave Chapter 13 a better argument than Chapter 13 makes for itself.** Of all 118
parameters, the step-ordering exponent has the single largest influence on outcomes,
swinging group maintenance by three times its baseline. The strictness of the ordering is the
most consequential number in the apparatus and nobody has measured it. Chapter 12 says this
where it will be read; Chapter 13 argues only about the sign of the related substitution
parameter.

**Repetition caught and fixed during drafting.** The first draft shared 23 seven-word phrases
with the preface, because I had written both in one session and reached for the same
formulations about the matrices and about the absence of data. All varied; the preface keeps
the canonical statement of the structural defence and Chapter 12 defers to it explicitly.

**Notebook.** Section 10 added, asserting the depreciation parameters, the eight resources,
the derived coefficients and the parameter inventory. The inventory is now asserted in one
place because the preface, both plans and PARAMETERS.md all quote it and it has drifted
twice. Whole notebook: **172 assertions, zero failures.**

**Next: Chapter 15, Helping Is Not the Reward**, which completes Part Three. The recipient
resource is the one group resource no drafted chapter has used, so it is genuinely new
material rather than a recombination.


### Numerical audit: the decline table was wrong, and ten seeds is why

The index-pairing figure resolved first, and in the book's favour. The 85.5 per cent was
real; the code lived only in `paper/anonymity-as-an-aggregation-condition.ipynb`, which is
why nothing in the book's repository could regenerate it. Ported to notebook section 11 and
it reproduces to the decimal. Two corrections fell out of porting it. The two-tier split
does not "survive 100 per cent of draws" in any meaningful sense, because multiplicative
perturbation leaves a zero row zero; that is a fact about the derivation, not a robustness
result. And the twelve counts are not equally firm: the Step 5 inversion holds at 99.5 per
cent, the Step 12 inversion at only 67.3, because Tradition 3 is a close competitor. Chapter
16 must not present all twelve as equally secure.

**Then the serious finding.** The cross-run standard deviation of final membership is about
15 members against a mean near 42, a coefficient of variation of 0.36. The decline table in
Chapters One, Two and Four was computed from **ten seeds**. Ten seeds gives a standard error
near 5 on the mean and quantises a survival fraction to tenths. Recomputed at 400 seeds:

| quantity | book | 400 seeds | 95% interval |
|---|---|---|---|
| full adherence, mean N | 45.0 | 41.7 | plus or minus 1.5 |
| **referrals lost, survival** | **0.20** | **0.360** | **0.314 to 0.408** |
| **referrals lost, mean N** | **2.9** | **9.9** | **plus or minus 1.6** |
| gatekeeping, survival | 0.90 | 0.940 | 0.912 to 0.959 |
| gatekeeping, mean N | 30.7 | 27.5 | plus or minus 1.7 |

Six of nine entries fell outside the interval the larger sample allows. The referral-starved
row was not imprecise, it was wrong: the book said a starved group dies in four runs out of
five at an average size of 2.9, and the truth is closer to two in three at an average size
of 9.9. This is a sampling error and is independent of the separate finding that the
quantity is not robust to perturbation anyway. Corrected in Chapters 1, 2 and 4, the
preface, PARAMETERS.md and the notebook, and every figure now carries an interval.

**A selection effect that had been reported as a finding.** Practice among survivors is
*higher* in every declining scenario than in the healthy one: 0.354 at full adherence, 0.372
under referral starvation, 0.400 under gatekeeping. That is not resilience. Only 144 of 400
starved runs survived and the survivors are the runs that were doing well already. Chapter 2
now says so beside the table.

**What the model got right.** The integration step is not a source of error: a factor of
eight in dt moves the answer by a fifth of one standard error. That is a clean verification
and worth having. The horizon is converged for practice and maintenance by thirty years and
only marginally so for membership, which drifts down slowly out to a hundred years; stated
in the appendix rather than glossed.

**New: `appendix/APPENDIX.md`.** Full model specification, numerical verification, Monte
Carlo error budget, all five sensitivity designs, results and what they license, provenance
of every parameter class, and seven threats to validity stated plainly. Written to the
standard a dissertation committee would referee. CLAUDE.md now carries that standard as six
numbered rules and a 400-seed minimum, so future chapters are held to it.

**Still outstanding, and named in the appendix rather than hidden.** No design run so far
can see interactions: the global sweeps confound them all together and the one-at-a-time
sweep is a star around the nominal point that cannot see them at all. A Morris
elementary-effects screen over all 118 factors, followed by Sobol indices on the important
subset, is the standard remedy and has not been run. No claim in the book currently depends
on an interaction, so nothing is asserted beyond what is supported, but the gap is real and
appendix A5.5 says so.

Notebook: **182 assertions, zero failures.**


### Morris screen, and two more small-sample errors

**Priority 1 done: the Morris elementary-effects screen over all 118 factors.** Ten
trajectories, four levels, 1,190 model evaluations, five seeds each under common random
numbers, at 0.85 adherence rather than 1.0 so the governance matrix is live rather than
cancelled. `model/morris_screen.py`, raw results in `research/morris.json`, notebook
section 12, appendix A4.6 and A5.5.

**The one-at-a-time ranking was not an artefact.** The same five factors dominate under
Morris as under the targeted sweep: the ordering exponent, the decay rate, churn,
heterogeneity and dropout protection. For membership all five have sigma/mu* below one,
meaning their effects are largely additive. That answers the standard objection to a star
design, which is that it generalises from one point in parameter space.

**The governance matrix is nearly inert even where it is not cancelled.** Thirty-five of
118 factors, thirty per cent of the model by count, carrying 3.6 per cent of total mu* for
membership and 4.1 per cent for practice, at partial adherence where the full-adherence
identity does not apply. The median governance factor moves membership by a third of one
member. This is strictly stronger than the algebraic result and is the firmest version of
the structural claim the preface makes.

**Interactions exist but are secondary.** Every factor with sigma/mu* above one sits outside
the top five. No claim in the book rests on an interaction. The resolution limit was
measured rather than assumed, using the near-inert governance factors as an empirical null:
1.41 members and 0.011 practice units at the 95th percentile.

**Then the retroactive Machinery audit found two more small-sample errors, both of the same
kind as the decline table.**

Chapter 14's decay-rate sweep was ten seeds. At 400, six of eight maintenance figures were
outside the interval and the ten-seed curve had two reversals that were pure noise. The
corrected curve is strictly monotone and survival falls to 0.927 at the top of the range
rather than staying at 1.00. Nothing qualitative changed, which is why it is worth
reporting rather than quietly restating.

Chapter 13's recovery exercise was **one simulated dataset**, at one seed, reported to three
significant figures, with a conclusion drawn from it. Over 25 replications per cell the
conclusion does not survive. The estimator is close to unbiased with one proxy or three;
bias never exceeds 0.21. What three proxies buy is precision, roughly halving the standard
deviation. At a true rho of exactly zero the sign is near a coin flip whatever the design,
because an unbiased estimator sitting on a boundary must land either side. The chapter's
design requirement has been rewritten from "one measure returns the wrong sign" to a
statement about resolution: one proxy leaves an indeterminate band of about plus or minus
0.3 around zero, three proxies about 0.15. That is a better argument and it is the one the
evidence supports.

**Three errors, one cause.** The decline table, the Chapter 14 sweep and the Chapter 13
estimator all reported statistics computed from samples too small to support the digits
printed. None was a modelling error. All three were invisible until the sample was
enlarged. Appendix A3.3b states this once, in general terms, so it is not learned a fourth
time.

**Machinery audit result.** Chapters 3, 7, 8, 9, 10 and 11 quote figures that are exact
algebra, not Monte Carlo, and say so; they need no intervals and have none. Chapters 5 and 6
already stated replication counts and standard errors. Chapters 1, 2, 4, 13 and 14 have all
been corrected in this session. Every simulation figure in the book now carries a sample
size and an interval.

**Still outstanding, and it is the only quantitative gap left.** Sobol first-order and
total-order indices on the top eight factors, to separate interaction from non-linearity
where Morris cannot. About 1,300 further evaluations. Nothing in the book depends on it;
appendix A5.5 and threat 5 in A7 both name it.

Notebook: **182 assertions, zero failures**, every cell executed.


### Two primary sources acquired, and both changed the argument

Part One rested almost entirely on one 1950 paper. Two of the sources Maxwell cites are out
of copyright and digitised, and reading them at source took under two hours between them.

**Marsh, *Temperance Recollections* (1866).** Marsh was Corresponding Secretary of the
American Temperance Union for thirty years and edited the Annual Reports the whole decline
chronology rests on, so this is a participant document. Saved as
`research/marsh-1866-temperance-recollections.txt` with offsets in SOURCES.md. Four claims
moved from at-a-remove to first-hand: the Beecher letter of 21 January 1845 now quoted in
full; the absorption thesis in Marsh's own words, the movement's fruits *gathered into new
organizations*; the Connecticut convention at which the Washingtonians resolved for
prohibition, with Marsh's parenthesis *for a great change had come over the Washingtonians in
this matter*; and Marsh's own exclusion from the Sons of Temperance for not being a reformed
man, which bears on Chapter 2's costly-screening argument.

**The Beecher letter names a mechanism the model cannot represent.** Beecher does not say
the Washingtonians failed or were absorbed. He says their *thunder is worn out* and *the
novelty of the common-place narrative is used up*. That is a resource depleting through use,
and not one of the model's eight group resources behaves that way. Nothing in the apparatus
can get stale. Chapter 2 now states this as a second limitation beside the missing-competitor
one, and notes that AA has run the same format for ninety years without exhausting it, which
is evidence the effect is weaker than Beecher thought but not an explanation of why.

**The political-entanglement claim is partly unblocked.** It was waiting on Blumberg 1980.
Marsh supplies a participant's evidence that the Washingtonians came round to prohibition
rather than resisting it, which reframes the charge: taking a position was the price of
staying in the room, and having no rule against it they had no way to decline.

**Krout, *The Origins of Prohibition* (1925).** The first scholarly history of American
temperance, written twenty-five years before Maxwell and independent of him. Chapter IX read
in full. Saved as `research/krout-1925-origins-of-prohibition.txt`.

**It contains this book's thesis, stated in 1925.** Krout reports two fundamental weaknesses
contemporaries saw in the movement. The first: there was no connection between societies,
because centralised control was considered too great an infringement on the rights of the
individual society, so systematic organisation was impossible, uniformity was never attained,
and **chance largely determined the formulation of principles**. That is Tradition 4 without
Traditions 1, 2 and 5 to hold it, described by a historian who had never heard of AA. It is
the sharpest formulation of the argument I have found anywhere and Chapter 2 now quotes it.

**And it corrects Chapter 1 by addition.** Krout has Mitchell proposing that meetings be
limited to members narrating their own experience, with the Baltimore society admitting **no
outside speakers unless they came to relate their experience as reformed men**. That is a
deliberate restriction on who may address the room, adopted in the first year, and it is
functionally a Tradition, close kin to singleness of purpose. The chapter had the closed
meetings, which governed who could enter and ended in November 1840, but not this, which
governed who could speak and did not end. So the comparison is no longer "they had no rules
and AA had twelve". They had at least one good one. What they lacked was any means of
transmitting it as a rule: Krout says the standard for other societies was thereby set, and
the mechanism is imitation. A practice that spreads by imitation survives only while it is
visibly working.

**One error of my own, caught and fixed within the session.** I first wrote that Chapter 1
had missed the dues, fee and officers. It had not; they are in the main text at line 38. Only
the speaking rule was new. Corrected before the chapter was saved, but worth recording,
because the failure mode is the same one the sourcing discipline exists to prevent: asserting
a gap without checking.

**A source conflict created rather than resolved.** Marsh's founding account, taken from the
Maryland State Temperance Society's eleventh annual report, names the preacher as Elder Knapp
and has four of the six attend. Maxwell has Matthew Hale Smith and one delegate. Both are
retrospective and descend from different Baltimore informants. Recorded in Chapter 1's notes
on sources; not resolved. Marsh adds that the sermon account was *afterward denied by some
who preferred that the movement should be considered an immediate impulse from Heaven*, which
is a founding myth visible under construction.

**Claim register updated.** Chapter 1 now 23 of 28 sourced primary or scholarly, Chapter 2
now 17 of 20, up from 22 of 27 and 13 of 17.

**The lesson for the remaining acquisition list.** Every source Maxwell cites from the 1840s
to the 1920s is out of copyright and several are digitised. Eddy 1887, Blair 1888 and
Fehlandt 1904 are all still cited through Maxwell and are all likely obtainable the same way.
That is a cheap route from solid to well-sourced and it needs no library. What still needs a
library is Kurtz, Blumberg, Alexander, and the *Washingtonian Pocket Companion* of 1842,
which is the single most valuable outstanding item because it is the movement's own statement
of its organising principles and therefore the direct counterpart to the Traditions. It is
not in the Internet Archive under any search tried.


### Chapter 15 drafted: Part Three complete

1,586 words, FK 8.4, passes the checker, four shared seven-word phrases with the rest of the
book and all four are the ordering claim or the referral channel, both of which are supposed
to recur. **Parts One, Two and Three are now complete in draft: preface plus fifteen
chapters, about 50,600 words.**

**The result the chapter turns on.** Disabling the twelfth step's growth entirely, at 400
seeds, costs 66 per cent of membership and degrades **Step 9 by 28 per cent**. Step 9 has no
direct dependence on service; it degrades because it sits downstream of a maintenance
capacity of which Steps 10 to 12 are the average. That is what load-bearing means, and it is
a sharper demonstration than "service is important", which nobody disputes.

**And the group does not die.** Survival is 400 of 400 without any service practice at all.
The result is a stable group at a third of the size and a sixth less practice, which looks
like a small quiet meeting that has been going for years rather than like a failure. Worth
having, because it means the model does not predict that service-less groups collapse, only
that they shrink and flatten.

**The recipient constraint binds.** Removing the twelfth step's dependence on having somebody
to help raises membership 8.7 per cent and service practice a fifth, z = 3.4. So in the
ordinary configuration the shortage of newcomers is limiting what established members can
practise. That is the recipient problem stated as a measured quantity rather than an
intuition, and it sets up Part Five.

**Sourcing is the weak point and the chapter says so.** Pagano et al. (2004) is read via
abstract, and **the forty and twenty-two per cent figures come from a 2011 Case Western press
release describing Pagano's own review of her earlier work, not from the paper's tables**.
That is a weak place to take two numbers from and the chapter states it in the notes on
sources rather than burying it. Riessman (1965) is cited for the name of the helper therapy
principle and not read at source; it is behind a subscription. Both are now on the
acquisition list with full citations.

**The observational limitation is stated as mine to raise, not theirs to answer.** Project
MATCH randomised treatment, not helping. Somebody well enough to sponsor is by that fact
somebody already doing better, and nothing in the design rules that out.


### Part Four planned, and planning it found a collision

`plans/PART-4-PLAN.md` written. Sequence is 16, then 18, then 17, because Chapter 18's
honesty problem is the one most likely to force a change in how the whole part is framed and
it is better to find that out before writing the middle chapter.

**The collision.** The master plan gave Chapter 17 the resource derivation and the
group-dependence coefficients. Chapter 12 has since spent both. Chapter 17 has been rescoped
to the transpose of Chapter 16: Chapter 16 asks which Tradition serves each step, Chapter 17
asks what each Tradition carries across all twelve. Unity at 6.52 against a next-highest of
3.89 is the material, and the interesting answer to the obvious objection is that unity is
load-bearing *because* it is diffuse. Both BOOK-PLAN.md and the part plan now record this.

**Two warnings written into the plan.** First, Part Four computes a twelve-by-twelve coupling
between two lists of twelve things and reports patterns in it, which is a shape that has
embarrassed better arguments; the defence is that both matrices were built for other reasons
and the test could have failed. Second, and concretely, **check every robustness figure in
this part for whether the design could in principle have produced a different answer.** Two
claims about the matrices have already been stated as surviving perturbation when the
perturbation could not have disturbed them.


### Full-book reconciliation

- Checker: all sixteen files, no FAIL, no readability warning.
- Notebook: **205 assertions, zero failures**, every code cell executed and stored.
- Figures: two decimals in the whole manuscript not literally present in the notebook, both
  benign roundings (0.1178 to 0.118, 0.459 to 0.46).
- Cross-references: **zero forward pointers into undrafted material.** Chapter 12 discharged
  the last two.
- Repetition: 21 shared eight-word phrases across all chapter pairs, clustering on the
  Maxwell quotation and the statement of the Golub and Jackson condition. Both are supposed
  to recur.
- Status files: README, BOOK-PLAN, CLAUDE.md, SOURCES.md, the claim register and the part
  plans all reconciled in this session.


### Audit of the project's claims about itself

The instructions and the appendix carry statements about what has gone wrong before, and
those statements are used to justify the rules. They had not been checked. Three were wrong.

**"Thirteen shared phrases between chapters 6 and 11."** In CLAUDE.md for several sessions
and used to justify the repetition check. It appears nowhere in this log. The recorded
figure is twenty-one shared ten-word phrases between chapters **9 and 11**. Corrected, and
the sentence now cites the two instances this log actually records.

**"The decline table was wrong for months."** Written by me on 2 August 2026 in two places
in CLAUDE.md. It cannot be supported: **this log carries no dates at all**, so nothing here
establishes how long anything was true. Replaced with what is verifiable, which is which
chapters carried it.

**"Two errors that had survived several sessions"** in README.md. Same problem, same fix.

**A rule added to CLAUDE.md**, because this is the third instance of the same failure mode
today, after the chapter 1 draft that claimed the chapter had missed the Washingtonians'
dues when they were in its main text: if you are about to say that something in this project
went wrong, or was caught, or has been true for some length of time, grep this log and quote
it, or do not say it.

**And a limitation of the safeguard, now stated in appendix A3.3b.** All three small-sample
errors *were* asserted in the notebook and *were* passing. The assertion re-ran the same
ten-seed computation and compared it to itself, so it verified reproducibility and said
nothing about accuracy. An assertion detects drift, not error. The 400-seed minimum is a
different kind of rule, not a strengthening of the assertion rule, and the two do different
jobs.

**Consider dating entries in this log.** Every claim about how long something persisted is
currently unverifiable. It would cost nothing to add a date line per session and would make
the project's account of itself checkable in the way the rest of the book aims to be.


### The Part Four plan was falsified within the hour of being written

The plan listed one item as "still to compute": whether unity's primacy survives the
*structural* test as distinct from the magnitude test. Running it falsified the plan's own
framing, which had said in its opening section that "the magnitudes in those matrices do not
carry the argument" and that "what carries the argument is the pattern of which cells are
empty".

**That is true of the survival claims and false of the coupling claims, and Part Four is
entirely about the coupling.**

Structural randomisation, replacing every non-zero entry with a uniform draw and keeping only
the sparsity pattern, 2,000 draws:

| Claim | at ±30% jitter | structural |
|---|---|---|
| T1 most load-bearing | 100.0% | **75.4%** |
| Index-pairing wrong on all twelve | 85.5% | **40.6%** |
| Step 5's principal supplier is T12 | 99.5% | **17.5%** |
| Step 12's principal supplier is T5 | 67.3% | **27.6%** |

Index-pairing fails on all twelve in 40.6 per cent of structurally randomised draws, which is
less often than it holds. The two vivid inversions that Chapter 16 was going to lead with
survive in 17.5 and 27.6 per cent.

**The degradation is smooth, not a cliff**, which is the useful part. At ±15 per cent the
claims are essentially intact; at ±50 they are weakened; at ±75 they are marginal; structural
randomisation removes them. The full curve is in notebook section 11 and Chapter 16 should
print all of it rather than one level, because a single robustness percentage at a level I
chose is exactly the kind of number this project has been wrong about before.

**What this does and does not do to the book.** It does not overturn index-pairing, which
still fails at the actual matrices and fails robustly to the kind of disagreement a
reasonable second opinion would produce. It does remove the defence Part Four was going to
borrow from the preface. The honest position is that Part Four rests on the magnitudes, that
those magnitudes are judgement, and that the chapters have to argue for them one at a time
rather than pointing at a percentage. The third of the book's three headline claims is
therefore weaker than the other two, and README.md, BOOK-PLAN.md, PARAMETERS.md, appendix
A5.4 and the Part Four plan all now say so.

**The general point, which is the same one as the assertion limitation above.** A robustness
test only tests what the design can vary. The ±30 per cent design cannot vary the magnitudes
by enough to matter, so reporting it alone made a magnitude-dependent claim look structural.
Both of today's methodological findings are the same shape: *check what the test could in
principle have found before quoting what it found.* That is now rule 4 in CLAUDE.md.

**Notebook at the close of this session: 225 assertions, zero failures, every code cell
executed and stored.** The earlier figures of 182 and 205 in entries above were correct when
written and are left as written rather than back-edited, since this log is a record of what
was true when, not a status page. README.md carries the current number.


### A second checker, and it caught a misattribution on its first run

`check_chapter.py` checks one file against the house style. Every error found today lived
*between* files, where it could not see. `tools/check_book.py` now checks the seven things
that went wrong: figure traceability, sample sizes and intervals, cross-pair repetition,
forward references, status drift between README and reality, unverifiable duration claims,
and citations against saved full texts.

**The sources check found a real misattribution within minutes of being written.** Chapter 2
cited Crothers 1911 for the founding rationale of the Sons of Temperance. **Crothers does not
mention the Sons anywhere.** That material is Eddy 1887. The citation had been carried since
the chapter was drafted and no human reading would have caught it, because the claim is
plausible and the source is real; only comparing the claim against the text finds it.

**Tuning it was as instructive as writing it.** The first run gave twelve failures, nine of
them false. Chapters quoting exact algebra were flagged for missing intervals; the Eddy
citation was flagged because the scan spells Mitchell three different ways; the rule text in
CLAUDE.md forbidding duration claims was flagged as making one. All three exemptions are now
in the code with a comment saying which passage earned them, and CLAUDE.md carries the
principle: **when a check fires falsely, fix the check, not the prose.** A checker that cries
wolf gets ignored, which is the same failure as an assertion that cannot fail.

### Eddy 1887 and Crothers 1911 read at source

Supplied by the author. Both are now in `research/` with full provenance in SOURCES.md.

**Eddy gives the Sons of Temperance founding as a document rather than a summary.** The call
of Thursday 29 September 1842, sent to some forty prominent Washingtonians, sixteen
attending, and the terms in the call itself: initiation one dollar, dues six and a quarter
cents a week, four dollars a week in sickness, thirty dollars for a funeral. Chapter 2 had
the screening and the price in outline and now has them in the founders' own words, and the
funeral benefit is new. Set against Krout's figures for the Washingtonians, twenty-five cents
to join and twelve and a half cents a month, the Sons cost four times as much to enter and
twice as much to stay, and paid out. That is Iannaccone's costly screening with a club good
attached, documented rather than inferred.

**Eddy also supplies Mitchell on the liquor traffic at one remove instead of two**, quoting
Dr Jewett from personal knowledge: no pledge against manufacture or sale, sellers admitted to
membership, and an admission that Mitchell had bought liquor at the bar for others after
signing. And his verdict that the movement was not irreligious and not a failure, having
stopped because it reached the limit of the means it employed, which is close to Beecher's
diagnosis from the other direction.

**Crothers corrected a citation rather than supporting one**, and what he does supply is
better than what he was cited for. He puts five million pledges between 1840 and 1845 and
then concedes that of those, *a certain unknown number* remained abstainers for life. A
sympathetic physician writing seventy years later, with every professional reason to want a
figure, says he has not got one; that is Chapter One's demolition of the statistics reached
independently and much earlier. He also traces a line of descent nobody else in the sources
does: the lodging houses for men who had broken their pledges became the beginning of the
hospital system of cure, and one opened in Boston in 1857 became the Washingtonian Home. So
the movement's residue went two ways, into the fraternal orders and into medicine, and only
the first is usually told.

**State of the checks.** `check_chapter.py` clear on all sixteen files. `check_book.py`: zero
failures, fifteen warnings, all of them shared phrases that are quotations or the statement
of the theorem. Notebook 225 assertions, zero failures.

### Four more sources supplied, and the founding scene is now first-hand

Harrison 1860, Hawkins 1862, Blair 1888 and Fehlandt 1904, all supplied by the author as
PDFs and extracted to text. With Marsh, Krout, Eddy and Crothers earlier the same day, that
is **eight sources moved from at-a-remove to read-at-source**, and Part One's Washingtonian
half no longer rests on one 1950 paper.

**Harrison 1860 is the origin of the founding scene**, the text Maxwell quotes and every
retelling descends from. Reading it directly corrected three things in Chapter 1.

*The preacher is not named.* Harrison, the earliest account, says only that a clergyman
preaching in the city had given public notice of a discourse on temperance. Maxwell supplies
Matthew Hale Smith; Marsh, from the Maryland report, supplies Elder Knapp. The earliest
source is silent and the two later ones disagree, which is the signature of a gap being
filled twice. **The chapter now leaves him unnamed.**

*Four went, not one.* Harrison and Marsh's source both say four of the six were sent.
Only Maxwell has a single delegate. Two against one, and the chapter follows the two.

*The pledge was written on the Monday morning*, not on the Sunday walk. What happened on the
walk was the agreement to draft one and sign it next day.

**And a calibration on Harrison's reliability**, which is worth as much as the corrections:
he dates the tavern evening to "Friday evening, the second of April, 1840". The second of
April 1840 was a Thursday. He is the origin of the scene and he is loose about detail, which
is a reason to keep the dialogue as reported speech rather than promoting it to fact.

**Hawkins 1862 gives his own account of 12 June 1840 verbatim**, and it contains something
the circulating version drops. Everyone tells this story as the daughter's reproach breaking
him. His own telling has the daughter break him and then *his wife carry him*: "But my wife
supported me. She said, 'Hold on, hold on.'" Also *I suffered all the horrors of the pit that
day*, which is a man describing unmedicated withdrawal in 1840 with no other vocabulary for
it. Both are now quoted in Chapter 1.

**A second date conflict, recorded not resolved.** Maxwell has Hawkins signing 14 June 1840.
Hawkins says the crisis was the 12th, that he felt better the next day, and that he signed on
the Monday. The 12th was a Friday, so his Monday is the 15th; the 14th was a Sunday. Chapter
1 now says the middle of June and does not pick.

**An edition warning that has to travel with the citation.** The Hawkins acquired is the 1862
Briggs and Richards printing, sixth thousand. Maxwell cites the earlier Jewett printing. The
two have not been collated, so Chapter 1 cites what was actually read and says which it is.
Added to the acquisition list as a low-priority item.

**Blair 1888 is much sharper read whole than as the clause the book was quoting.** "Maudlin
insanity" is not a stray insult; it is the end of an indictment. Blair allows a hundred and
fifty thousand reformed men saved, asks what that is among so many, and then charges the
Washingtonians' opposition to legal restraint with demoralising public sentiment and so with
the four hundred and fifty thousand *who fell and perished*. He is a United States senator
and the author of a proposed prohibition amendment, so he is a hostile witness with a
legislative motive, which is exactly why the passage is useful. Chapter 2 now quotes it at
length: being neutral on the traffic did not go quietly out of fashion, it became in the eyes
of the men who inherited the cause a moral failure with a body count. He also recites the six
hundred thousand figure Chapter 1 shows cannot be supported, which is a reminder that a
number can outlive its evidence and be picked up on both sides of an argument.

**Fehlandt 1904 is useful as the received view Maxwell was correcting**, not as evidence:
*By 1843, however, interest began to wane, and soon Washingtonianism had spent its force.*
Maxwell's regional evidence shows that is both too early and too uniform, and the
disagreement is the point.

**Claim register.** Chapter 1 now 30 of 32 sourced primary or scholarly, up from 22 of 27
this morning; Chapter 2 now 24 of 26, up from 13 of 17. Two conflicts are recorded and
unresolved, which is the honest state rather than a defect.

**The checker knows all nine texts.** `tools/check_book.py` matches every citation to
Harrison, Hawkins, Marsh, Gough, Eddy, Blair, Fehlandt, Crothers and Krout against the saved
full text, with tolerance for optical character recognition noise. Zero failures.

**Where the burden now sits.** Part One's Washingtonian chapters are well sourced. Its AA
chapters are not: Chapter 4 still has no claim sourced to a document read at source, and
Kurtz is the only thing that fixes it. That asymmetry is now the largest single weakness in
the book.

### The strongest external evidence in the book arrived, and it was not on the list

Fatimah, Hunter and Bornovalova (2025), "Modeling the Dynamics of Addiction Relapse Via the
Double-Well Potential System", *Journal of Psychopathology and Clinical Science* 134(1):
69-80. Supplied by the author. Read in full from the NIH author manuscript, saved as
`research/fatimah-2025-double-well-relapse.txt`.

**It supersedes Hufford (2003) as Chapter 14's empirical warrant, and the upgrade is large.**
When Chapter 14 was drafted, the shape rested on two preliminary samples of 51 and 43
patients, a cusp catastrophe model, and an abstract I had not been able to get behind. It now
rests on a double-well potential model fitted to timeline followback data from 139 adults
leaving residential treatment, validated against outcomes, with person-specific parameters.

Three things in it bear directly on the chapter.

**The two wells are fitted, not assumed.** Their steepness and tilt parameters predicted life
satisfaction and criminal behaviour at long follow-up **over and above proportion of days used
and time to first use**, which are the field's standard metrics. A description that adds
predictive power beyond the usual measures is doing more than redescribing them.

**Their separation energy is Chapter 14's separatrix, and it is asymmetric.** They define the
relapse process by the disturbance required to move from abstinence to relapse and, as a
separate quantity, from relapse back to abstinence. Two different energies, one each way.
That is the hysteresis the chapter argues for, reached by fitting curves to real drinking
histories rather than by building a mechanism.

**And they find significant between-subject variance in steepness and relapse risk**,
predictable from demographics, baseline psychopathology and treatment history. That is the
empirical counterpart of `het_sd`, the parameter PARAMETERS.md calls the least defensible in
the model, chosen because it converted individual cliffs into a group slope. Somebody has now
measured something like it and found it is really there. **The value 0.55 remains unsupported
by anything**; what has changed is that the qualitative assumption behind it is no longer only
a modelling convenience.

**Four limits, written into the chapter because the temptation to over-read this is real.**
Their object is substance use behaviour; the model's bistability sits in maintenance capacity,
and nobody has fitted a double well to step practice. Their model is descriptive and this one
generative: they fit a landscape to behaviour, this model derives one from a claimed
mechanism, and a different mechanism producing the same landscape would fit their data
equally well, so the paper supports the shape and is silent on the mechanism. Their sample is
criminal-justice-involved and largely polydrug, not an AA meeting, and their own limitations
section notes the retrospective timeline followback gives weekly rather than daily resolution
over long windows. And **non-use was the predominant stable state across their participants**,
so the two wells are not of equal depth for most people, which qualifies the dramatic reading
of the chapter.

**What has not changed.** None of this locates anybody's threshold. The chapter's second
half, that the shape is claimed and the location is not, stands exactly as written, and the
2.79 per cent fragility in the decay rate is untouched.

**A checker false positive, fixed in the checker.** The `figures` check read the DOI
`10.1037/abn0000960` as an untraceable decimal. Identifiers are now stripped before figures
are extracted, with a comment saying why. Third exemption added under the standing rule that
a check firing falsely is fixed in the check rather than worked around in the prose.

**Propagated to:** Chapter 14 main text and Machinery, `research/SOURCES.md`,
`research/PARAMETERS.md` section 2, `appendix/APPENDIX.md` A6, README's blocked table, and
`tools/check_book.py`, which now matches ten source texts.

### Kurtz acquired, and it changed the opening of Chapter 2

Supplied by the author as an epub. Converted to PDF, read in full, ~185,500 words, expanded
1991 edition.

**Copyright handling, and it follows a precedent this project already set.** *Not-God* carries
an all-rights-reserved notice. The nine plain-text sources in `research/` are public domain
1860 to 1925 plus one NIH public-access manuscript; Kurtz is neither. The full text is
therefore **not** stored in the repository, exactly as Maxwell 1950 is read in full and not
stored. What is stored is `kurtz-1991-verification-index.json`, a vocabulary index with no
running text, so `tools/check_book.py` can still confirm a cited subject appears in the work.
The checker now reads any `*-verification-index.json` alongside the full texts and reports 39
citation-subject pairs against 11 sources.

**The find that mattered most.** Chapter 2 opened by calling the standard account of the
Washingtonians' death a story you hear in meeting rooms, treating it as folk history. Kurtz
tracks it to a document. Bill Wilson published his reading of Washingtonian history in the
*A.A. Grapevine* of August 1945, prompted by a member's article the month before, crediting
the movement with about a hundred thousand alcoholics helping each other stay sober and
listing four flaws that killed it. **The article ran eight months before the Twelve Traditions
were published**, and Kurtz says Wilson was explicitly conscious of seeking support for the
Traditions he was then formulating.

The four flaws map onto Traditions Eleven, Ten, Five and Ten. So the story is not folk memory
that happens to align with the Traditions; it is a case made for the Traditions by the man
drafting them, in the fellowship's own magazine, while he was drafting them. Between 1945 and
1976 the *Grapevine* carried twelve separate articles on the Washingtonians. Chapter 2 now
opens with this, and it is a considerably stronger version of the argument the chapter was
already making about curated records.

**A disclosure that should have been in the book already.** Kurtz describes Maxwell, the
book's principal scholarly source on the Washingtonians, as *currently an A.A. trustee*. That
does not impeach the 1950 paper, which predates the trusteeship and contradicts AA's own
published account repeatedly. It does mean the book cannot call him a disinterested outsider.
Recorded in SOURCES.md under Maxwell so it travels with every citation.

**A warning for Part Four, and it may cost a chapter its finding.** Kurtz's note 16 to his
Chapter Five records that in some later AA literature the concept properly conveyed by
*single-purposed* was obfuscated by substituting *unity* as its supposed exact equivalent, and
that after Wilson's death AA itself at times fell into this. Chapter 17 is planned around
Tradition 1, unity, coming out most load-bearing at 6.52 with Tradition 5, single purpose,
third at 3.88. **If the two terms were historically conflated, that finding may be an artefact
of how I read the Traditions when building the governance matrix.** Written into
`plans/PART-4-PLAN.md` as something to settle before the chapter is drafted, with the pointer
Kurtz gives to Wilson's own discussion of the First Tradition.

**Chapter 4's founding narrative is now first-hand**: the failed Akron proxy fight of early
May 1935, Wilson pacing the Mayflower lobby on Saturday 11 May with the bar filling at one end
and the church directory at the other, *God, I am going to get drunk* and the panic that
followed, and Dr Bob's last drink and restitution rounds on 10 June. Kurtz also names **four**
founding moments rather than one, and the chapter now says the June date is the enshrined one
rather than the only one. Claim register: Chapter 4 moves from 0 of 14 sourced to 4 of 15.

**What Kurtz did not fix.** The Rockefeller and Amos material, the Scott question and the
funding narrative still reach Chapter 4 through AA's copyrighted histories. Chapter 5 has not
been reworked at all. The chapter is no longer a well-corroborated outline and is not yet
uniformly first-hand.

**Outstanding upload.** A Maxwell PDF was announced mid-session but did not arrive in the
workspace. Worth re-sending: Maxwell is the most-cited source in Part One and no Maxwell
citation has ever been machine-verified against its text.

### The Washingtonian Pocket Companion arrived, and it was worth the wait

Supplied by the author as HathiTrust plain text plus the scanned page images: Grosh, A. B.,
comp. (1842), *Washingtonian Pocket Companion*, second edition, Utica, B. S. Merrell. Harvard
copy, digitised by Google. Public domain, so both the text and the 22.8 MB PDF are saved in
`research/`. About 33,400 words, of which the first fifteen pages are prose and the rest is a
hymnal.

Chapter 1 had listed this as the one document that would most sharpen or most damage the
book's central comparison, on the grounds that it is the movement's own statement of its
organising principles and therefore the direct counterpart to the Twelve Traditions. That was
the right prediction and it came true in both directions in the same fifteen pages.

**What it damaged.** Chapter 2 said the Washingtonians had no rule against outside issues and
so had no way to decline the temperance movement's turn to legislation, and that AA a century
later wrote a rule and could point at it. That is false. They had two: a clause in the
definition of principles barring anything inimical to any political party or religious
denomination from the movement's periodicals, lectures, meetings and proceedings, and Article
3 of the model constitution, which forbids sectarian sentiments and party politics in any
lecture, speech, singing or doing of a society. A mass convention at Utica adopted a
declaration of principles and a constitution for all societies on 22 February 1842, published
it in the *Utica Washingtonian* of 25 February, and reprinted it in October because of demand.
All of that is three years before the Connecticut delegates marched to the State House.

Chapter 1 lost a sentence too: that what the Washingtonians lacked was any means of
transmitting a practice *as* a rule. A manual in its second edition, a convention, a newspaper
and reprints run off to meet demand is a transmission mechanism, and a better one than AA had
in 1946.

**Both corrections are in the main text, not buried in the Machinery.** Chapter 2 now argues
that the Washingtonian rule failed for two reasons that are not absence. Scope: Article 3
binds what may be introduced into the doings of *a society*, and the Connecticut resolutions
were passed at a convention of delegates, a venue the article does not reach and which existed
because the societies were subordinate to none. And standing: a rule barring politics from the
meeting cannot help a movement whose identity is already a position on the political question.
I have been careful here. Grosh's moral-suasion creed is about how to treat sellers and
drinkers, not about statute, and the log should record that I did not claim otherwise; what I
claimed is that contemporaries read it as a position on statute, which is exactly what Blair is
doing when he calls it maudlin insanity.

**What it sharpened, and it is the strongest thing Part One now has.** Read as a list, the
definition of principles contains written analogues of four Traditions. Each society
independent: Tradition 4. Funds under the direct control of its members: half of Tradition 7.
Subordinate to none: the between-society half of Tradition 9. Nothing political or sectarian in
the publications and meetings: Tradition 10. And the reasoning given is a diagnosis rather than
piety. The old societies were arranged county under state under national, hierarchies have
employed agents, agents have views, and a local member finds his name on positions he never
took. They identified the mechanism this book attributes to Tradition 9 and legislated against
it, in 1842.

What they did not have is not silence. On anonymity the manual takes the opposite position
with an argument: names are called out, entered by the secretary and called back over the
room, and "Publicity and freedom are preferable to private solicitations, whisperings, and
secresy in giving the names." On leadership there is no rotation and no doctrine of service,
and the president may order a transgressing member to sit down. On singleness of purpose the
manual is expansive rather than silent: Washingtonianism embraces all classes, sexes, ages and
conditions, and aims to cure as well as prevent, so the porous boundary Maxwell identifies as
the cause of absorption was doctrine, printed and sold, rather than drift.

So the comparison Part One makes is no longer rules against no rules. It is one written code
against another, and the three the book will argue are load-bearing are exactly the three
missing. **I have said in Chapter 1 why a reader should be suspicious of that and what the
fair test is.** The selection of Traditions 2, 9 and 12 comes from the theorem in Part Two and
not from this history, so the honest test is what the *Pocket Companion* could have contained
and does not: had it prescribed rotation of the chair, or advised societies against giving
members' names to newspapers, the book would be in serious trouble and the chapter would have
had to say so.

**Limits, stated in the chapter and here.** One compiler, one edition, from Utica rather than
Baltimore, and prescriptive rather than descriptive. Its own section on differences between
societies is the evidence that practice varied, and I have not established how widely the
model constitution was adopted. That section is also the reason to trust the rest: a manual
willing to record how much its societies disagree is not concealing much.

**Bookkeeping.** Twelve new claims in the register, all primary, nine in Chapter 1 and three
in Chapter 2. One falsified. The register's summary table was recomputed from its own rows
rather than carried forward, and four of the six chapter counts had drifted by one or two; the
counting rule is now stated in the file. `SOURCES.md` has a full entry with a page-and-offset
table, and the offsets in it were verified against the saved text rather than estimated, after
a first pass in which every one of them was wrong by between two hundred and three thousand
seven hundred characters. `check_book.py` reports 0 failures. Chapter 1 is 4,075 words and
Chapter 2 4,617; the book is 56,930.

**Repetition, and a note on how it was handled.** The first draft of these two sections quoted
the same passages of Grosh in both chapters and `check_book.py` reported twenty-seven new
shared seven-word phrases. That is the checker doing its job on real duplication rather than
firing falsely, so the prose was fixed and not the checker: each passage is now quoted in full
in one chapter and referred to in the other. Fifteen warnings remain, which is the count from
before this session.

**Two changes to `tools/check_book.py`, both made because a legitimate passage tripped it.**
Grosh was added to the saved-source table, and four subjects were added with it: pocket
companion, publicity and freedom, utica, and reformed inebriates. Kept specific rather than
generic, because a subject like "sectarian" appears near several source names and would
manufacture pairs the check cannot adjudicate. That produced two failures and neither was a
misattribution: a references list where Krout's entry adjoined a mention of the *Pocket
Companion*, and a passage where Grosh is discussed in one sentence and Blair quoted in the
next. The flat four-hundred-character window was the problem, so the window now ends at
whichever comes first, the start of another saved source's name or the end of the second
sentence. Pair count falls from 42 to 30 and the check was regression-tested by reinserting
the original Crothers misattribution, which it still catches. Twelve saved sources now, eleven
full texts and one vocabulary index.

**Maxwell arrived later the same day, and every citation to it has now been checked.**


### Maxwell 1950 catalogued, and checked against the book for the first time

Supplied by the author. Originally saved as `maxwell-1950-the-washingtonian-movement.pdf`
and `.txt`; moved without content changes to `research/incorporated/Maxwell_1950/` on
6 August 2026.
Thirteen saved sources now, and `check_book.py` reports 47 citation-subject pairs, up from 30.

**The copy is a transcription, not a scan, and the file this project previously described as
"a scan of the original journal article" was not one.** Running footers read "CHIPS on the
WEB". Four transcription errors are demonstrable from internal evidence: the movement's rise
dated to "the early 1940's", "confirmed" set as "conformed" in at least two places, "from" as
"form", and Brattleboro as "Battleboro". So the machine check is against a retyping and not
against the *Quarterly Journal of Studies on Alcohol*. That is one remove. It is shorter than
no check at all, and both Chapter 1's notes and `SOURCES.md` now say so. Page references taken
from this copy are worthless: it paginates as 29 sheets, not as pp. 410-452.

**Three corrections to Chapter 1, all in the direction of claiming less.** The chapter said
Maxwell was precise about all three founding dates; he gives 2 and 5 April and then says the
pledge would be signed "the next day", so 6 April is arithmetic. The chapter said the period's
vocabulary distinguished "at least eight grades of drinker"; Maxwell lists ten, and they are
now named. And the chapter rounded Jellinek's figure to "about fourteen per cent across the
whole decade"; it is 14.3 per cent, ages fifteen and over, from a base of 4.9 gallons, between
1840 and 1850.

**Everything else in the chapter checked out**, including every figure that had been carried
from a secondary reading: the pledge text, the six founders and trades, the fee of twenty-five
cents and dues of 12.5 cents, two-thirds of 300 at eight months, the parade of about 1,000
reformed and 5,000 others before 40,000 spectators, the motto, 23,340 signatures, Pittsburgh's
10,000, Cincinnati's 900 of 8,000, Vermont's 518 of 42,273, Hawkins on 14 June 1840 and at
Annapolis in February 1841, the descent of the 600,000 figure from the 1843 ATU Report, Marsh's
revisions, Jellinek's nine words, the "sheer survival value" passage and the five-point
comparison.

**One more checker exemption, added deliberately.** The `figures` check flagged 14.3 and 4.9,
correctly by its own rule, since neither is in the notebook. Neither is a model output. A
`SOURCE_FIGURES` table now holds them with the source named beside each, so an exemption in
the checker can be audited the same way a number in the notebook can. The comment says not to
turn it into a blanket rule for numbers with a citation nearby.

**A copyright decision that should be reviewed.** Maxwell 1950 is not public domain. The file
is stored because it was supplied for this folder and the folder is private. That is a
departure from the Kurtz treatment, where the full text was deliberately not stored and a
vocabulary-only index was built instead. Recorded in `SOURCES.md`; reversible in one session.


### Chapter 5 rewritten on Kurtz, and it is no longer the weak chapter

Part One's weakest chapter is now its second best sourced: fifteen of sixteen claims read
directly, against three of six before. The one exception is the Holmström application, which is
mine and is labelled as an interpretation. Two claims were dropped rather than carried.

**The correction that matters most is one word.** The chapter called the Traditions rules, four
times. Wilson's own framing, circulated before publication and quoted by Kurtz, is that

> a code of traditions could not, of course, ever become rule or law [,] but might serve as a
> guide for our Trustees, Headquarters people, and especially for groups with growing pains

That is not modesty and it is not a quibble. A rule needs an authority to enforce it, and the
whole problem of 1941 to 1945 was that creating such an authority would stop the experience
arriving. The chapter now says what he said. It also strengthens Part Four: what the Traditions
are, formally, is a guide addressed to trustees, headquarters staff and groups in trouble, and
not a body of law addressed to members.

**The chapter's thesis turned out to be Wilson's first sentence.** The chapter had argued, as
my own reading, that the Traditions were recorded rather than designed. The April 1946
publication opens: "Nobody invented Alcoholics Anonymous. It grew. Trial and error has produced
a rich experience." That claim moves from I to S in the register.

**Kurtz's statement of the 1941 to 1945 problem is this book's Tradition 9 argument, made by
AA's historian with no theorem in front of him:** how to share effectively the rapidly
accumulating wisdom of experience without establishing a central authority, the very existence
of which might stifle further experience and greater wisdom. Quoted in the chapter and flagged
forward to Part Two.

**Five specific corrections.**

- The chapter opened on 1944. Kurtz puts the repetition of questions and Wilson's decision to
  codify in 1945.
- It said the Traditions were formally adopted at the first international convention of 1950.
  Kurtz says officially adopted June 1950 and separately describes the Cleveland gathering as
  the fifteenth anniversary convention. He does not connect them. Claim dropped.
- It said the 1938 trust agreement required an alcoholic trustee to resign on drinking and that
  this was invoked within months. Not in Kurtz; it had come from a secondary account. Dropped.
- Maxwell dates the Traditions to 1947 and 1948; Kurtz to April 1946. The chapter follows Kurtz
  and explains why, and notes that Maxwell's dates fit the elaborating editorials and the 1947
  booklet he was actually reading.
- Kurtz cites the April 1946 publication twice with different issue numbers and pages. One is a
  slip. Recorded rather than silently resolved.

**New material, and the best-documented scene in the chapter.** The 1937 Towns offer: an office,
a drawing account, a healthy slice of the profits, and the invitation to become a lay therapist,
perfectly ethical. Wilson bowled over, then the silence at Clinton Street, then the group's
answer that what we've got won't run on ethics only. Kurtz's gloss is that this was the first
time Wilson heard the voice of what he later called the group conscience. Two Traditions arrive
in one room in five minutes, and the founder is on the losing side of both, which is the best
available evidence against the view that he composed them.

**Chapter 4 was corrected in the same pass, and it was in the wrong order.** It had Amos's Akron
visit and his fifty-thousand-dollar recommendation first, with Scott's question arriving
afterwards to stop it. Kurtz has Scott asking at the December 1937 meeting itself, immediately
after Wilson's appeal, with Amos sent to Akron afterwards. So the objection preceded the
investigation. Kurtz also records two incompatible memories of the refusal, Wilson's and
Henrietta Seiberling's, and the chapter now carries both and says which is the more flattering.
Chapter 4 moves from four of fifteen claims read directly to seven of eighteen.

**Bookkeeping.** ch4 is 3,336 words and ch5 4,158, whole-file. The book is 59,472. The claim
register's summary table now excludes dropped claims from the counts and says so, and dropped
rows are left struck through so a future session can see what was removed. `check_chapter.py`
all clear, `check_book.py` 0 failures and 15 warnings, notebook untouched at 225 assertions.
No model figure changed in this session, in either direction.


### Chapter 16 drafted, and it deflated its own headline

Part Four is open. Chapter 16, *The Pairing That Isn't*, is drafted at 2,001 words of main
text, and the useful thing in it is not the result but the arithmetic underneath the result.

**The finding that changes what the book may claim.** The book's third headline result is that
index-pairing, the natural conjecture that Step *i* is served by Tradition *i*, fails on all
twelve counts. It does. But five of those twelve are arithmetic. Traditions 4, 6, 7, 9 and 10
have identically zero rows in the governance matrix, so Steps 4, 6, 7, 9 and 10 have index-mate
entries of exactly zero, and index-pairing cannot hold for them under any perturbation that
preserves sparsity, which both of the book's perturbation designs do. Index-pairing fails for
those five the way a horse fails to win a race it did not enter.

I checked the consequence rather than asserting it, and it is exact. At every level of
disagreement, the proportion of draws in which index-pairing fails on all twelve equals the
proportion in which it fails on the seven that could have gone either way, to the last draw:
98.75 and 98.75 at plus or minus 15 per cent, 85.50 and 85.50 at 30, 72.45 and 72.45 at 50,
65.15 and 65.15 at 75, 40.60 and 40.60 structurally. **Every robustness figure Part Four
reports is carried by seven steps.** Notebook section 11b, added for this.

Propagated the same session to README, BOOK-PLAN, PART-4-PLAN, PARAMETERS.md and appendix
A5.4, all of which stated "all twelve" without the qualification.

**A second fragility, and it cuts the other way.** The identity of a Step's principal supplier
is often decided by a hair: Step 4's top two are separated by less than a hundredth, Step 6's
by one hundredth, Steps 3 and 7 by four. Change the numbers slightly and the winner changes for
four of the twelve. But the *loser* does not change, because for those same four the index-mate
sits at 0.00, 0.00, 0.01 and 0.00. So the argmax is a poor instrument for saying which Tradition
serves a Step and a good one for saying that it is not the one with the matching number. The
chapter makes that distinction explicitly, because it is the difference between the claim the
chapter makes and one it does not.

**Only one of the seven is close.** Step 1's principal supplier is T3 at 1.22 with its own T1
second at 0.99. The other six lose by ranks of fourth to eleventh. The chapter says it would not
want to rest on Step 1.

Every figure in the chapter is now in the notebook with an assertion, including all twelve rows
of the per-step table and Wilson intervals at n = 2,000 on every Monte Carlo proportion. The
exact matrix products are labelled exact and carry no interval, which is the distinction
CLAUDE.md rule 5 asks for.

### Sobol run, and it half succeeded

1,408 evaluations, N = 128, Saltelli for first order and Jansen for total order, on the eight
factors the Morris screen ranked highest. `model/sobol_indices.py`, cached to
`research/sobol.json`, appendix A5.7, notebook section 12b. This was the last quantitative gap
named in the appendix and in threat 5 of A7.

**What worked.** The total-order indices are stable and they answer the question Morris could
not. a[8]'s high Morris sigma was non-linearity in the factor itself, not interaction: its
S_T - S_1 gap is 0.005. a[4] and omega show interaction, though both sit near the Monte Carlo
noise floor of 0.023. And Spearman's rho between Morris mu\* and Sobol S_T is 0.833, with the
same top two, so the Morris ranking is not an artefact of the elementary-effect estimator.

**What it corrected.** A5.5 read delta0 and het_sd as largely additive, on the strength of
sigma/mu\* below one. Sobol says otherwise: both have first-order intervals covering zero and
total-order indices far from it, so on membership they act largely through interaction. That is
a correction to the screen, not a confirmation of it, and threat 5 in A7 has been rewritten
rather than struck out.

**What failed, and it is reported as a failure rather than smoothed.** The first-order indices
are not estimable at N = 128. Three diagnostics, all in the notebook rather than asserted in
prose: S_1 exceeds S_T for one factor on membership and five on practice, which is impossible
for a true decomposition; the practice first-order indices sum to 1.263, which is also
impossible; and splitting the sample in half moves the first-order indices by 0.092 on average
against 0.042 for total order, with p_gate's S_1 moving from 0.338 to 0.633 between halves.
Scaling from the interval widths, resolving p_gate's S_1 to a half-width of 0.10 needs N of
about 1,379, roughly 13,800 evaluations and ten times what was run. Not run. No S_1 value is
quoted anywhere in the appendix.

The honest summary is that the first-order decomposition of a stochastic model of this size is
out of reach at the sample sizes this project uses, and the total-order decomposition is not.
Nothing in the book depends on either.

**Bookkeeping.** Notebook now stores 358 assertions across 49 cells, 0 failures. 17 chapter
files, 62,904 words. `check_chapter.py` all clear, `check_book.py` 0 failures and 15 warnings.


### Part Four completed: Chapters 18 and 17 drafted, and two assertions caught two errors

Written in the plan's order, 18 before 17, and the order paid. Writing 18 second produced an
instrument that repaired a claim in 16.

**The threshold test, and it is the most useful new thing in this part.** Every perturbation
design in Part Four multiplies matrix entries, so a zero row stays a zero row. That made the
two-tier split untestable and made five of Chapter 16's twelve counts untestable with it. The
replacement inverts the question: what uniform strength would a Tradition need across its own
Step's consumed resources before index-pairing held there? One division per Step, exact, and
able in principle to make any index-mate the principal supplier including the five with empty
rows.

Every one of the twelve thresholds exceeds both the mean live entry of the governance matrix,
0.374, and the median, 0.300. At the mean live strength no index-mate wins, with losing margins
from 0.02 at Step 7 to 0.44 at Step 5. The five protective Steps average 0.501 against 0.531 for
the seven enabling ones. **This is the only design in Part Four that could have overturned the
five protective counts, and it does not.** Appendix A5.4b, notebook 11c. Chapter 16 now carries a
paragraph saying its deflation stands as a statement about its own designs and is repaired as a
statement about the claim.

**An assertion failed and corrected Chapter 18 before it was saved.** The main text said the
five protective thresholds sit inside the enabling range. They do not: the protective range
extends below the enabling range at both ends, and the protective mean is 0.501 against 0.531,
so the protective Steps are marginally *closer* to index-pairing holding. That is the direction
an objector would predict. The chapter says so and the correction is in the main text, not the
notes.

**Chapter 18's other new material is historical and it came from Grosh.** Of the five protective
Traditions the Washingtonians had four in written form by 1842. Of the seven enabling ones they
had none, and three are explicitly contradicted by their own manual. A movement that wrote down
the guards and not the thing guarded. Two cautions travel with it in the chapter: one movement is
one case, and Wilson was reading Washingtonian history while drafting the Traditions, so the two
documents are not independent.

**The textual check on the two-tier split half works, and the chapter says which half.** The
obvious criterion, that the five protective Traditions are the ones phrased as prohibitions,
fails: only three carry an explicit "ought never" or "has no opinion", and one of the enabling
seven is phrased as flatly. A second criterion does better: four of the five mention no
individual person at all, the fifth only if a clause about boards being responsible to those they
serve is read as referring to groups, and every one of the enabling seven mentions a person. Four
clean, one strained, no false positives. Reported as such rather than as a finding.

**Chapter 17 answers Kurtz's conflation objection with a test rather than a reading.** Kurtz's
note 16 records that later AA literature substituted *unity* for *single-purposed*. If the
governance matrix absorbed that, Chapter 17's finding is an artefact. The test transfers unity's
governance of one resource to singleness of purpose, wholesale, one resource at a time. Six of
eight transfers leave unity leading by margins of 1.44 to 2.54. Two flip it: continuity and
pressure. So the finding is conditional on two assignments and nothing else in the matrix, and
the chapter defends those two from the published short text of the two Traditions. What it cannot
do is read *AA Comes of Age* pp. 97-98, which Kurtz names as decisive and which this project does
not acquire. Appendix A5.4c, notebook 11d.

**A second assertion failed and corrected Chapter 17.** The text said that stripped of continuity
and pressure, unity falls below the open door. It falls to 2.77 against the open door's 2.69, so
third rather than fourth. Corrected in the main text.

**A finding worth keeping in view.** Unity is the only Tradition governing all eight resources
and sits in the top two for ten of the twelve Steps, but it is **not** the most diffuse by
concentration index: singleness of purpose scores 0.197 against unity's 0.204. The chapter claims
breadth of coverage, not minimum concentration, and says so.

**Repetition.** The first drafts of 17 and 18 shared eighteen seven-word phrases with Chapters 1,
13 and 16. Nine of them were one sentence in Chapter 18 duplicating a sentence in Chapter 13
about how much weight a case carries. Fixed in the prose, not the checker. Back to fifteen
warnings, which is the standing count.

**Bookkeeping.** 19 chapter files, 70,041 words. Notebook 53 cells, 476 assertions, 0 failures.
`check_chapter.py` all clear, `check_book.py` 0 failures. Parts One to Four are drafted.
Propagated to README, BOOK-PLAN, PART-4-PLAN, PARAMETERS.md and appendix A5.4, A5.4b, A5.4c.


### Part Five drafted: four chapters, 4,800 new runs, and a third assertion catch

`model/part5_runs.py` produced everything Part Five needed in one resumable job: a Tradition 3
sweep at five levels, thirty-year trajectories for four conditions with membership and practice
sampled yearly, and a composition experiment. 400 seeds per condition, 4,800 runs, cached in
`research/part5.json`, verified in notebook section 14. **`plans/PART-5-PLAN.md` was written
after the runs**, which makes it the only part plan written with its numbers already in hand, and
it is correspondingly more specific than the others.

**The finding that organises the part: the most dangerous failure has no symptoms.** A group with
no exogenous referral channel looks healthy at every horizon. At year five, 99.5 per cent survive
and the survivors are at 33.5 members and quality 0.353 against a healthy group's 0.341. At year
ten, 90.7 per cent survive, survivors at 29.4 and 0.348 against 0.338. At year twenty, 60.3 per
cent, survivors at 25.8 and 0.346 against 0.324. At year thirty, 36.0 per cent, survivors at 26.6
and 0.335 against 0.320. **The survivors are better than a healthy group on the only measure a
member could perceive, at every horizon, while two thirds of such groups die.**

The unconditional membership series falls 72 per cent over thirty years. The series conditioned on
survival falls 26 per cent. One process, two correctly computed numbers, and only the second is
visible from inside a group.

**This is a selection effect promoted to a finding, and the book has warned against exactly this
reasoning twice.** Chapter 20 and Chapter 21 both say so in the main text. The defence is
procedural: every conditional figure is labelled conditional and the surviving fraction is printed
in the same row, and Chapter 21 states that no version of its argument survives dropping that
column. Appendix A3.4 is the standing threat.

**Chapter 19's counterintuitive result.** Closing the door entirely costs 14.2 members and 5.5
points of survival, **raises** measured quality by 0.046, and **raises** the newcomer share from
0.122 to 0.201. A closed group is smaller, its members look better, and more of it is new at any
moment, because newcomers churn through faster and must be replaced. Both of the two things a
group can measure about itself without any apparatus move the wrong way. The chapter also records
that survival at T3 = 0.75 and T3 = 1.00 is not distinguishable and must not be read as a peak.

**Chapter 22 is deliberately short and provisional, and the plan required that.** The composition
experiment returns a null: spread of 1.8 members across three founding distributions against a
95 per cent half-width of 1.6. But the model computes resources from group aggregates, so
composition can act only through the capacity gate's non-linearity and through heterogeneity, and
a null from a design that could barely produce anything else is weak evidence. The plan specified
that the chapter should not be written at full length without Carrell, Sacerdote and West, and
that it should be rescoped to about 800 words if that could not be obtained. It has not been
obtained. The chapter is 762 words and says so in its first paragraph. **This is the only
outstanding acquisition in Part Five.**

**A third assertion failed and corrected a chapter.** Chapter 22 printed the split condition's
low tier as 0.2769. It is (13.75 - 12 x 0.9) / 13 = 0.2269. Caught before the chapter was saved.
That is three assertion catches in this session, after two in Part Four, and in every case the
error was a transcription or a claimed relation rather than a modelling fault.

**A checker exemption, narrowed after a first attempt was too broad.** The `history` check fired
on `PART-5-PLAN.md` for saying a starved group looks healthy for years, which is a statement about
the runs and not about the project's own history. The first exemption keyed on words like "group"
and "member" and would have silenced the check across most of the plans. It was narrowed to
markers that only appear when a sentence is about the runs, regression-tested by reinserting a
genuine project-history duration claim, which it still catches, and the comment in the file says
not to widen it. The plan sentence was also reworded so its provenance is explicit, which was the
better fix.

**Repetition.** Four shared phrases between Chapters 2 and 19 are both chapters quoting the text
of Tradition 3, which is a quotation and went on the allow-list. Two others were my own phrasing
repeated between Chapters 19, 20 and 21 and were fixed in the prose. Back to fifteen warnings.

**Bookkeeping.** 23 chapter files, 78,914 words. Notebook 55 cells, 630 assertions, 0 failures.
`check_chapter.py` all clear, `check_book.py` 0 failures. **Parts One to Five are drafted.** What
remains is Part Six, three chapters, and the introduction.


### The five proposed steps, executed, and two of them went against the book

**Step 2, Part Two's sensitivity analysis, was the largest gap and it produced a correction.**
Part Two contains the book's central claim and had no sensitivity analysis of any kind: its four
chapters carried no robustness language and the appendix did not mention the mapping.
`model/part2_influence.py`, appendix A8, notebook section 15. All deterministic linear algebra
except one random control.

Three results. **The dose-response Chapter 8 never gave**: it illustrated concentration with two
matrices, flat and one member at 0.35, and the full sweep shows a member holding 0.05 of every
row flooring the consensus error at 0.0465 against a flat 0.0252 at a thousand members, a factor
of 1.84 that grows without bound in N.

**A correction to Chapter 8's mapping.** At fixed magnitude, two of Golub and Jackson's three
obstructions do not obstruct. A clique of three giving a tenth of its attention outward holds
0.029 of the influence at N = 1000 and falling; a member receiving twenty times what he gives
holds 0.020 and falling. Both vanish, so both satisfy the condition. Let the same practices scale
with the group and both become obstructions, flat in N. **So the three obstructions are three
descriptions of sequences in which somebody's share fails to vanish, and whether a practice
obstructs depends on how it scales rather than on its level.** That is Chapter 10's rotation
finding generalised to the whole of Part Two, and both chapters now say so.

**The closed form Chapter 11 said it lacked.** That chapter argued the Washingtonians'
touring-speaker structure concentrated influence and stated plainly it had not simulated it. It
has now been, and the speakers' total influence is exactly `out / (out + back)`, verified to
1.1e-12, **independent of the size of the movement and of the number of speakers**. The first
version of the construction gave the speakers everything at every parameter setting, because with
no attention flowing back they are a closed communicating class and the theorem does not apply.
That case is reported as vacuous rather than as a finding, which is the third time this project
has caught itself about to quote a design that could not have produced any other answer.

**Step 3, structural sensitivity, split the book's strongest simulation claim.**
`model/structural_variants.py`, appendix A9, notebook section 16. Four changes to the model's
architecture rather than its numbers, 10,000 runs. A5.6 had said structural choices were never
perturbed; three of the four it names are now perturbed.

"Losing referrals is worse than losing attraction" is called the most robust thing the simulation
says, in the preface, Chapters 1 and 4, README, CLAUDE.md and PARAMETERS.md. **Nowhere was
"worse" defined.** On survival the ordering holds in five variants of five, by margins from 0.335
to 0.638. On mean membership it reverses in three of the four non-degenerate variants: with a
flat capacity gate the referral-starved group ends at 15.6 members against the attraction-starved
group's 8.4. The core-size ordering reverses in the same three. **Every statement of the claim
has been rewritten to say survival**, and PARAMETERS.md now carries the two readings as separate
rows. The Tradition 3 variant is degenerate and is reported as such: reading the open door as
governing arrival makes zero adherence a group that admits nobody, dead in 400 runs of 400, which
supports Chapter 19's retention reading rather than testing it.

**Step 1, the second governance matrix, is a form rather than a result.** I cannot recruit
readers. `research/GOVERNANCE-MATRIX-ELICITATION.md` is a blank 12-by-8 grid with the eight
resource definitions, the twelve Traditions in short form, instructions to mark only which cells
are non-zero, three follow-up questions, and a note on what will be done with the answers and
what a disagreement would mean. It also specifies the comparison script that does not yet exist.
**This remains the largest unresolved item in the book.**

**Step 4, out-of-sample contact, got as far as naming the instrument.** AA's service material
SMF-132, *Estimated Worldwide A.A. Individual and Group Membership*, is the groups-and-members
series by year. Located, not acquired: it is AAWS material under a content-use policy permitting
a single printed copy, and this project does not acquire AAWS publications. Chapter 21 now names
it and records two limitations that would remain with it in hand: it is worldwide rather than
regional, and a count of groups nets births against deaths.

**Step 5, acquisitions: one of three.**

*Carrell, Sacerdote and West (2013), obtained and read in full* from the lead author's university
copy. Their own model predicted a gain of 0.053 grade points for the lowest-ability cadets they
set out to help; the measured treatment effect was **minus 0.061** at p = 0.055, and the
mechanism was homophily, the students re-sorting inside the squadrons that had been built for
them. **Chapter 22 went from 762 provisional words to 1,297 finished ones** and now leads with
the experiment, using the model's null as the minor corroboration it is. Part Five has no
outstanding acquisitions.

*Pagano et al. (2004)*: not obtained. The 40 and 22 per cent figures were confirmed as belonging
to the study rather than to a garbled secondary account, which is a small improvement. The paper
is behind a challenge page at PubMed Central and paywalled at the journal. **Chapter 15's
sourcing is unchanged and is still the weakest in the book.**

*Alexander (1988)*: not attempted this session.

### Part Six drafted; all twenty-five chapters now exist

**Chapter 23, The Wrong Turns**, lists twenty-five errors sorted by the instrument that caught
them: nine model errors found by simulation, twelve research errors found by reading primary
sources at length, one institutional error found by a reader with experience of the fellowship,
and three caught by notebook assertions. It makes one observation I had not seen before: seven of
the nine model errors were errors in which the model was **too well behaved**, and a model that
behaves smoothly is finished while one that misbehaves gets debugged. It declines to say how long
any error stood, because the progress log is undated.

**Chapter 24, What Would Settle It**, is six measurements in order of how much they would settle,
each with the result that would falsify the book. Item one is the elicitation and is the only one
doable this month. The chapter's closing observation is that four of the six need data about
*groups* and almost all research on AA is about *members*.

**Chapter 25, What a Model Cannot Tell You**, is the ethical close. It states what the three
reported quantities are not, that the book cannot assess anyone's recovery or any meeting, that a
group failing the formal condition is not thereby failing its members, and that the fellowship
has been written about entirely from outside with one exception.

**Two checker exemptions, both regression-tested.** The `sources` check fired on Chapter 23's
table row recording the Crothers misattribution, and the `intervals` check on its row recording
the ten-seed error. Both are chapters confessing to a fault rather than committing one. The
exemptions were narrowed to markers that only appear in retrospective constructions and each was
regression-tested by reinserting a genuine violation, which both still catch.

**Bookkeeping.** 26 chapter files, 87,516 words. Notebook 59 cells, 711 assertions, 0 failures.
`check_chapter.py` all clear, `check_book.py` 0 failures and 16 warnings. **Every chapter of the
book is drafted.** What remains is the introduction, which the plan says is written last, and the
elicitation, which needs three people.


### Full audit pass: the notebook had never been run, and running it broke three things

The request was to work through the whole book to a dissertation standard. The single most
useful thing in the pass was mechanical: **execute the notebook end to end**, which had never
been done. It had been maintained cell by cell.

**Cell 4 had been raising on every run and no check saw it.** It referenced `SEEDS`, defined
nowhere, raised NameError, stored an empty string, and passed `check_book.py` because the status
check looks for stored assertion FAILURES and an empty output is not one. That cell was the one
verifying the model's calibration target.

**So the calibration target was unchecked, and it was wrong.** `model/core_thresholds.py`, 400
seeds: a fully adherent group holds 41.7 members with an experienced core of **7.7 plus or minus
0.5**. Appendix A6, Chapter 4 and Chapter 12 all said "an established core near nine". Nine is
outside the interval. Corrected in all three plus `PARAMETERS.md`.

**And the word "core" meant two different things.** `act_thr` = 0.1 is an ESTABLISHED member,
which is what `simulate()` returns as `n_est` and what the Part Five tables print as "core", at
37.2 of 41.7. `exp_thr` = 0.5 is an EXPERIENCED member, which is the calibration target, at 7.7.
A factor of nearly five, one word. Now named separately everywhere.

**The twelve-Tradition comparison was running at 30 replications and reversed at 400.** This was
the last violation of the 400-seed rule in the project, defended on the ground that common random
numbers make a paired design efficient. Efficiency is not exemption. `model/tradition_paired.py`,
400 paired replications, 5,200 runs. The old table said two of twelve comparisons cleared
significance and both were PROTECTIVE Traditions. The new one says eight of twelve clear, the top
four are all ENABLING, attraction leads at 7.90 members with t = 12.9, and autonomy and
self-support rank fifth and sixth at 2.82.

Chapter 5's table was rewritten. **Chapter 6 was worse and I nearly missed it**: it drew a
methodological moral from the old result, that a simulation with no measurement error still
cannot rank these mechanisms, and therefore comparative history certainly cannot. The moral was
sound and the premise was a small sample. At 400 replications the instrument ranks eight of
twelve. Chapter 6 now says the instrument was not blunt, I was reading it at thirty replications,
and the part of the argument that survives is that comparative history has one observation of
each movement and no replications at all.

**Four equation defects, found by checking every printed equation against the code.**

- Chapter 12's growth equation wrote `C(i)` for a term the code computes as
  `1 - w(i)*(1 - C)`, and omitted the heterogeneity multiplier entirely. A reader could not
  have reconstructed it. Now written in full with `w(i)` and `h(m)` defined.
- Chapter 14 described the per-step phase-in in prose. Now an equation, and stated in both
  chapters so each Machinery is readable alone.
- Chapter 8's central derivation had three text corruptions in one paragraph: a doubled "the
  the", a missing space in "s-transposethe errors", and a stray brace in the displayed formula.
  Rewritten with the belief model, the consensus and the error each given as their own display.
- Chapter 13 presented a CES stage technology under the heading "The stage technology is",
  which reads as though it were the simulation's update rule. It is not; the simulation is
  multiplicative. The chapter now says so, says why the CES form is used instead, and says the
  two agree at the limit that matters.

All equations were then verified numerically against the code: effective adherence, the per-step
weights, beta, the row and column normalisations, the full-adherence cancellation, and the
closed-form error all agree to machine precision.

**An AA-review catch, anticipated rather than received.** Chapter 19 used "closed group"
throughout for a group with an unwelcoming culture. In the fellowship's usage a **closed
meeting** is one restricted to people with a desire to stop drinking, as against an open meeting
anyone may attend, and holding closed meetings is entirely ordinary. The chapter's claim survives
but only when stated about **membership** rather than attendance: a closed meeting may exclude
the curious, the professional and the family member, and cannot exclude an alcoholic who wants
what the room has. The chapter now makes that distinction in its third paragraph and says
"unwelcoming" thereafter. The title is kept and the reason is given.

**Seven chapters had no statement of what was not read**, which CLAUDE.md requires: 7, 8, 9, 10,
11, 13 and 14. All seven now have one, and each is specific rather than formulaic. Chapter 8's
is the one that matters most: the theorem was read at source, and what has not been read is any
work testing whether real deliberating groups behave like DeGroot updaters, which is the step
between the theorem and the fellowship and is untested anywhere in the book.

**Two stale claims removed.** Chapter 11 still said the Rockefeller material was "provisional
pending Kurtz"; Kurtz has been read and Chapter 4 rebuilt on it. Chapter 6's 30-replication
figures, above.

**Three checker changes, each regression-tested by reintroducing the fault.**

1. Status now fails on a code cell whose output text is blank, and on a cell that calls
   `check()` and stored no result line.
2. `tools/run_notebook.py` added: runs the whole notebook in one process, writes real outputs
   back, exits non-zero on exception, failed assertion or blank cell. About twenty seconds.
3. The history pattern was widened after I wrote "for two months of work" into CLAUDE.md while
   documenting the rule against exactly that. It now catches numbered durations.

**Bookkeeping.** 26 chapter files, 89,625 words. Notebook 36 code cells, **779 assertions, 0
failures, runs clean in 18.8 seconds**. `check_chapter.py` all clear. `check_book.py` 0 failures,
16 warnings. Appendix gains A10 on execution integrity.


### Reference sections normalised, and the sensitivity suite cleared against the new ranking

**The reference sections had grown twenty-seven distinct heading variants across twenty-five
chapters.** "Cited at a remove", "Cited at one remove", "Cited at one or more removes", "Cited
by Maxwell, not read directly", "Consulted, not read at source", "Background, not consulted for
this chapter" and "On the 1944 capture episode, cited at one or more removes" were all the same
category wearing different clothes, and the effect was that no reader could see at a glance what
a chapter had actually read.

Normalised to five headings in fixed order: **Read in full**, **Cited at a remove**,
**Referenced but not reproduced**, **Internal, and reproducible from this repository**, **What
was not read**. The third is for AA-copyright text the book paraphrases and does not reproduce,
which is a real category and was previously hiding under "Referenced". The first, second and
fifth are compulsory; a chapter with nothing at a remove says "Nothing." rather than omitting
the heading.

**Sixteen chapters had their not-read statement buried inside another section**, as an inline
bold lead rather than a heading, which is why an earlier audit counted eighteen chapters with a
statement while only seven had a section. All promoted. Chapters 1 and 2 had none at all and now
do; Chapter 1's names White, Alexander and Blumberg and Pittman, and records that the *Pocket
Companion* was on that list until it was obtained.

**A contradiction found in the process.** Chapter 1 listed Grosh under both "Read in full" and
"Cited at a remove", the second a stale stub from before the manual was obtained. Removed. Five
other apparent duplicates were checked and are legitimate: a work read in full alongside a
different work by the same author, or a paper cited from its abstract and listed as unread in
full.

**Entry-level format fixes.** Eight malformed entries: three with a stray ".," left by an older
template, two with a comma where a full stop belongs after the author, one journal article with
no article title, one book with no year or place of publication, and two using "et al." where the
house style is a full author list or an explicit statement that the co-authors were not traced.
En-dashes in page and year ranges normalised to hyphens.

**A new FAIL-level rule in `check_chapter.py`.** Non-canonical headings, headings out of order,
duplicate headings, a missing compulsory heading, and a canonical heading used inline rather than
on its own line are now failures rather than warnings. Regression-tested by introducing each
fault. The inline test initially had a bug, matching across a blank line because `\s` includes
newlines; narrowed to `[ \t]` and retested. The format itself is written into `CLAUDE.md`.

**The sensitivity suite was cleared against the corrected paired result.** Every table in
appendix A4 and A5 and in `PARAMETERS.md` was checked for dependence on the old 30-replication
ranking. None depends on it: those designs perturb parameters and report survival and membership,
not this ranking. Only Chapters 5 and 6 quoted it and both were rewritten. The ranking is now
recorded in its own right as **appendix A5.4d**, with the note that no simulation result in the
book now supports the protective tier being more consequential than the enabling one.

**Bookkeeping.** `check_chapter.py` all clear on 26 files, `check_book.py` 0 failures and 16
warnings, notebook 779 assertions and 0 failures, runs clean in 18.5 seconds.


### Four items off the standing list, and one of them produced a new sensitivity design

**Item 8, the fourth structural choice, is done.** A5.6 had named four structural choices never
perturbed; A9 did three and left the resource list on the ground that changing the number of
resources changes both matrices' column count and is a different model. That is true of the
simulation and false of the coupling, which is exact algebra on two matrices whose columns are
resources. `model/resource_list_test.py`, appendix A9.5, notebook 17. 64 variants: 8 single
deletions, 28 pairwise merges, 28 double deletions.

**Unity's primacy survives 63 of 64.** The one failure drops continuity and pressure together,
which is exactly the pair A5.4c had already identified as the only two able to move it. Two
independent designs agreeing on which two resources carry a result is worth more than either
alone.

**Index-pairing is more sensitive and the sensitivity is in one Step.** Across all 64 variants
only two Steps ever regain their index-mate: Step 1 in fifteen and Step 2 in one. Five of the
seven non-trivial counts never break. Every one of the fifteen Step 1 failures involves deleting
or merging the admission resource, which is what gives Tradition 3 its lead there. **Chapter 16
already called Step 1 the near miss and the only one and said it would not want to rest on it.
This is that caveat measured rather than asserted**, and the chapter now carries the measurement.

The two-tier split is unchanged in all 64 and that is **vacuous** for the same reason the
multiplicative designs cannot reach it. Reported as vacuous. And the design cannot split a
resource or invent a ninth, so the list can be shown to be no *finer* than it needs to be and
cannot be shown to be fine *enough*. Half of A5.6's fourth question remains open and says so.

**Item 2's script half is done, and writing it produced something I did not expect.**
`model/elicitation_compare.py` analyses completed elicitation forms: which rows come out empty,
cell agreement out of 96 with Cohen's kappa alongside the raw rate because chance agreement is
about 55 per cent on a matrix this sparse, and Chapters 16 and 17 recomputed on the respondent's
matrix. **Written before any form came back, so the analysis is fixed in advance and cannot be
chosen after seeing the answers.** A `--self-test` mode runs three synthetic respondents with
known answers, including one who fills Tradition 7 and must be reported as contradicting Chapter
18. It passes.

**The self-test surfaced a real gap.** Its middle respondent, with six cells flipped and the
protective rows untouched, already moved unity out of first place. Every perturbation design in
A5.4 varies the magnitudes and holds the sparsity pattern fixed; a second reader disagrees about
the pattern, and nothing in the project priced that. So: **appendix A5.4e, a sparsity
perturbation.** Flipping k cells confined to the seven enabling rows, 2,000 draws per level:

| Cells flipped | Index-pairing fails on all twelve | T1 largest load |
|---|---|---|
| 1 | 96.3% | 100.0% |
| 4 | 86.2% | 96.5% |
| 8 | 75.0% | 83.7% |
| 16 | 53.0% | 50.8% |

**Part Four tolerates a reader differing on about four of fifty-six enabling cells and does not
tolerate one differing on sixteen.** It is a bound and not a measurement, and the appendix says
why at length: a random flip is not a plausible reader, being harsher in respecting no reason and
gentler in not concentrating on the cells that matter. Only completed forms answer which cells a
reader picks.

**Item 1, the introduction, is written.** `manuscript/ch00b-introduction.md`, front matter
alongside the preface, so no Machinery: every figure it quotes is asserted in the chapter it
belongs to, and `check_book.py`'s figures check confirms it. `check_chapter.py`'s FRONT_MATTER
tuple was extended and the reason recorded in the file.

It leads with the theorem, states in bold that the mapping onto the three Traditions is a reading
of three sentences that no computation touches, and gives the index-pairing result as the weakest
of the three claims. It also carries the Grosh correction as a headline rather than a footnote:
the Washingtonians are usually described as dying of having no rules, that is false, and what they
lacked was the enabling half of a code whose protective half they had written down.

**Repetition.** The first draft shared 54 phrases with other chapters, most with Chapter 25,
because the introduction's warnings section paraphrased the ethical close too closely and the
final line copied it. An introduction restating the book will echo it, but the project's own log
records preface-to-chapter duplication as a real catch, so the prose was fixed rather than the
checker. Eleven passages rewritten; down to one overlap and seventeen warnings against a standing
sixteen.

**Bookkeeping.** 27 chapter files, 92,230 words. Notebook 38 code cells, **809 assertions, 0
failures, runs clean in 19.2 seconds**. `check_chapter.py` all clear, `check_book.py` 0 failures.
**Every chapter of the book now exists.**


### Final audit: code, equations, interpretations

**Code.** Every script compiles and runs. A dead-name scan found five assigned-but-unused
variables, all cosmetic (`unity` returned by `resources()` and discarded by callers that do not
need it, an unused `n` in the kappa helper). The four structural variants were verified to
actually differ from base at a common test point rather than being silently identical, which is
the failure mode a monkey-patching design invites: `gate_flat` and `no_saturation` change growth,
`capacity_all` changes the resource vector, and `t3_admission` correctly leaves both untouched
because it acts only on the dropout and inflow terms.

**One variant was misnamed and the appendix said something false about it.** `no_saturation`
replaces `c/(c+k)` with `min(c/2k, 1)`. That is clipped, so it still saturates; it reaches the
ceiling abruptly at c = 2k instead of approaching it. Above c = 2k it is the *more* saturating of
the two, since the hyperbolic form is only 0.667 there. A9 described it as "linear rather than
saturating", which is wrong read literally. Corrected in the appendix and in the script, with the
verification that the two forms do agree at c = k where both are 0.5, so the change really is of
shape and not of level.

**Equations, re-verified numerically and independently of the code that generates the book's
figures.** The threshold formula c\* = b/w reproduces the beaten value for all twelve Steps
exactly. The touring-speaker closed form out/(out+back) holds to 1.05e-12 across twenty-seven
configurations including non-round group sizes. The Golub-Jackson error identity was checked by
Monte Carlo against a Dirichlet influence vector and agrees with ||s||·sqrt(2/pi) to two parts in
a thousand. The protective rows are exactly zero, 61 zeros of 96 cells, so the 35 non-zero
entries the book quotes is right.

**An inconsistency introduced by my own correction, and not propagated.** Chapter 19 was rewritten
to say the Third Tradition governs membership rather than attendance, because a closed meeting is
an ordinary thing. Four other places still carried the pre-correction phrasing: Chapter 22 said
Chapter 19 "establishes that a group has no such power" over admission, Chapter 2 and appendix A2
said a group "cannot refuse admission", and the introduction said the group "has no procedure for
refusing" without the qualification. All four aligned. Chapter 23's entry on the institutional
error was also extended to record that the same reader would have caught the terminology as well.

**The preface had drifted furthest and its last section was wrong.** It ended by saying the model
rests not on the magnitudes in the two matrices but on their structure, and that the structure is
the part of the apparatus I would defend hardest. `CLAUDE.md` has said since the structural test
was run that this is true of the survival claims and false of the coupling claims, and the preface
had never been updated. It now separates them: survival rests on structure and holds in every
structurally randomised draw; Part Four's central coupling claim holds in 40.6 per cent, which is
less often than it fails. The preface also now carries the warning that the mapping from three
Traditions onto the theorem's condition is unverified, which belongs in the section that sorts
claims by strength and was only in the introduction and the appendix.

**A7's numbering was being read as a ranking.** The preface's new warning said the appendix lists
the mapping first among the threats. It does not; it is threat 7, and renumbering would break
references made from Chapter 21. A7 now opens by saying the order is historical rather than a
ranking and naming threat 7 as the largest and threat 2 as second. The preface was reworded to
match.

**One genuine strengthening.** Chapter 17's reassignment test finds that only continuity and
pressure can move unity out of first place. The resource-list test built for a different purpose
finds that of sixty-four alternative resource lists the only one that dethrones unity is the one
removing continuity and pressure together. Two instruments converging on the same two columns is
worth more than either alone, and Chapter 17 now says so.

**Cross-file numeric consistency** was checked for thirteen headline figures across every chapter,
the appendix, PARAMETERS and README. No figure is stated two ways anywhere.

**Bookkeeping.** 27 chapter files, 92,741 words. Notebook 38 code cells, 809 assertions, 0
failures, clean in 19.1 seconds. `check_chapter.py` all clear. `check_book.py` 0 failures, 18
warnings, 55 citation-subject pairs verified against 13 saved sources.

---

## The paper rebuilt in LaTeX and brought up to the book

The working paper in `paper/` predated all of the verification work and had never been
reconciled with it. It is now a single LaTeX source, `anonymity-as-an-aggregation-condition.tex`,
compiled to a 32-page PDF. **The `.docx` was deleted at the author's instruction**; the `.tex` is
the paper's source of truth as the markdown is the book's. The old `.ipynb` was left in place and
is now superseded by `model/book-calculations.ipynb`; it should probably go, and has not been
touched without asking.

**Nine substantive defects in the old draft were repaired.** Two were found this session and the
rest were corrections the book had already made and the paper had not. They were first written up
as a section of the paper and that section was then removed at the author's instruction, since a
journal article should stand on its own rather than narrate its own revision history. Where a
correction carried a lesson worth a reader's time, the lesson is now stated impersonally in the
place it applies: the decline table's caption says what ten seeds returns, the Tradition table
says what 30 paired replications returns and why variance reduction does not substitute for
replications, and the Tradition 3 discussion states the membership-versus-attendance distinction
as a thing that is easy to get wrong rather than as a thing we got wrong. The record of what
changed lives here, which is where it belongs.

- **Table 1 was mislabelled.** It was captioned "Maximum influence weight" and its four columns
  were consensus *error* values, taken from the flat, rotating, dominant and caucus regimes.
  Verified by recomputation: the old Table 1's rows reproduce this project's error figures to
  three decimals and bear no relation to its influence figures, which are 0.100 and 0.350 at
  N = 10 where the caption printed 0.252 and 0.328. The paper now prints the two quantities as
  separate tables with the constructions stated.
- **Table 3 was the ten-seed decline table**, captioned as such, with referral survival at 0.20
  and full adherence at 45.0 members. Replaced at 400 seeds with intervals throughout.
- The 30-replication Tradition ranking, the calibration target, the two senses of "core", the
  five structurally-forced index-pairing counts, the structural-randomisation result, the
  membership-versus-attendance conflation in the Tradition 3 discussion, and the reading of the
  CES form as the simulation's update rule.

**One error found in this session's own drafting and corrected before compiling.** The paper said
first-order Sobol indices "were not computed". They were computed and are not usable, which is a
different and more informative statement, and appendix A5.7 demonstrates it three ways. The
paper now gives all three diagnostics.

**Everything quantitative in the paper was recomputed rather than transcribed.**

- All 360 decimals in the `.tex` were matched against the manuscript, the appendix, the model
  source and the cached JSON results. None untraceable.
- The paper's stated growth equation, transcribed back out of the LaTeX into an independent
  implementation, reproduces `step_growth` to 2.8e-17 over random states. This is the check that
  the four equation defects found earlier have not reappeared in a new document.
- The coupling table, the load-per-Tradition figures, the threshold table and every summary
  statistic of the governance matrix were recomputed from `S` and `GOV` and match to the printed
  digits. So did the influence and error tables, the pool sweep, the fixed-pool divergence and
  the structural-variant table.
- `out/(out+back)` was re-verified across 81 combinations of movement size, speaker count,
  outward and returned attention: exact to 1e-9 in every one.

**Two gaps in the paper's own apparatus were closed.** The maintenance-capacity gate was
described rather than defined, so the paper stated a growth equation depending on a quantity it
never gave; equation (12) now gives the Hill gate and the group-support floor with their
parameters. And the reassignment and sparsity-perturbation designs were referred to the book's
appendix instead of being reported, which fails the self-containment standard; both now carry
their results, including the finding that Part Four tolerates a reader differing on about four of
fifty-six enabling cells and not on sixteen.

**Two references were listed but never cited** (Galanter 1981, Harrison 1860) and are now used
where they do work. Every remaining reference is cited, and every author-year in the body resolves
to an entry.

**What the paper now says that the old one did not.** A section 7 on the comparative case, built
on Grosh rather than on the received account. The obstruction-scaling corollary. The
touring-speaker closed form. The survival-versus-size split. A limitations section that opens by
naming the mapping as the largest unverified step rather than listing it eighth. Two new
falsifiable predictions, both about elicitation. And a reproducibility appendix stating the
estimand, the design, the seed counts and the named threats.

**Bookkeeping.** Paper 18,820 words rendered, 32 pages, 8 tables, 4 propositions and corollaries,
44 references. Compiles clean under pdflatex with no warnings and no overfull boxes. The book
itself was not modified this session: `check_book.py` 0 failures and 18 warnings, unchanged.

---

## Manuscript audit against the model source, and the first full-book PDF

The paper's verification raised a question the book had not been asked: whether the *manuscript's*
printed numbers can be re-derived from the model source, independently of the notebook that
asserts them. An assertion detects drift between the chapter and the notebook. It cannot detect a
number that is correctly copied from a cell that computed the wrong thing, nor one attached to the
wrong row label. So every deterministic table was recomputed from `aa_group_model.py` and
`part2_influence.py` by a script that never reads `book-calculations.ipynb` or the cached JSON, and
every stochastic table was re-aggregated from the raw per-run records rather than from the stored
summaries.

**157 independent deterministic recomputations. One real error, in Chapter 8.**

The chapter's main text read: "A clique of three that gives a tenth of its attention outward holds
0.375 of the influence in a group of ten, 0.107 in a group of fifty, and 0.029 in a group of a
thousand." Appendix A8.3's table gives that row as 0.7500, 0.3750, 0.1071, 0.0291 at N of 10, 50,
250 and 1000. **The prose had shifted the labels by one column**, so two of the three figures were
attached to the wrong group size, and the first column was dropped entirely. Recomputation from
the model puts the aggregate clique influence at 0.750, 0.375, 0.107 and 0.029 for those four
sizes, which confirms the appendix and convicts the chapter. Corrected, and the sentence split in
two so it clears the length check.

**Why no existing check caught it, which is the more useful finding.** `check_book.py`'s figures
rule verifies that every decimal in a chapter is reachable from the notebook. 0.375 and 0.107 are
both reachable: they are that same row's values at N = 50 and N = 250. The rule can confirm a
number exists in the computation and cannot confirm it is attached to the right thing. That is a
structural limit of the check rather than a bug in it, and the only instrument that closes it is
recomputation from the model with the labels reconstructed independently, which is what was done
here. **Nothing else in the book failed it.**

**A second, smaller thing, recorded because A7's threat 6 is exactly this shape.** The calibration
sentence gives 41.7 members, an established core of 37.2 and an experienced core of 7.7. The first
is over all 400 runs and the other two are over the 398 survivors, and nothing said so.
Unconditionally the cores are 37.0 and 7.7 and membership conditioned on survival is 41.9, so at
99.5 per cent survival the choice moves nothing by more than 0.2 members and changes no claim.
A6 now states the conditioning rather than leaving a sentence that gives one unconditional number
and two conditional ones side by side.

**What re-aggregation from raw runs confirmed.** 60 Part Five statistics, rebuilt from the
per-run yearly series with deaths padded to zero: survival, membership conditional and
unconditional, quality, and every half-width, in all four decline conditions at years 1 through
30. All match to the printed digits. 15 composition statistics likewise. All 12 rows of the
Tradition degradation table, rebuilt from the 5,200 paired runs, match on cost, half-width and
t to the printed digits, including the reference group's mean of 23.44 and cross-seed SD of 11.93
and the count of eight comparisons resolving. The Part Four coupling table, the load per
Tradition, the threshold table, the governance matrix's summary statistics and the identity of
the five zero rows were all rebuilt from S and GOV and match exactly.

**And the paper's equations were checked back against the model rather than against the book.**
The growth equation as printed in the paper, transcribed out of the LaTeX into a fresh
implementation, reproduces `step_growth` to 2.8e-17 over random states. The touring-speaker
closed form was verified across 81 combinations of size, speaker count and attention split, exact
to 1e-9 in every one.

**The book now renders.** `build/nobody-in-charge.md` assembles the preface, the introduction,
all twenty-five chapters with part title pages, and the technical appendix into one document,
which pandoc and xelatex turn into a 227-page PDF. The assembler is a script, not a hand-edited
file, so it can be rerun. Two notes on it: four Unicode subscripts are mapped to plain digits in
the build copy only, because the body font lacks the glyphs and the book's own convention already
writes T11 and delta0 that way; and the source files are untouched by the build.

**Bookkeeping.** 27 chapter files, 92,782 words, plus an 11,470-word appendix; 104,383 words assembled.
Notebook 809 assertions, 0 failures, clean. `check_chapter.py` all clear. `check_book.py` 0
failures, 18 warnings. Paper 31 pages, 18,448 words rendered, compiling clean with no warnings
and no overfull boxes.

---

## The primer, and the assembler that was never a file

Two things were added to the book: a per-Step and per-Tradition primer, and the working paper,
both as appendices. Finding the second one somewhere to live turned up a problem with the
first attempt at building the book at all.

**The assembler did not exist.** `README.md` said to rebuild the book "with the assembler in
the progress log's last entry". The entry describes an assembler and does not contain one. So
the book could not be rebuilt from this repository by anybody who had not watched it being
built the first time, which is the same defect as a figure with no provenance and it was in
the instructions rather than in a chapter. It is `tools/build_book.py` now. The
reconstruction was checked rather than assumed: the previous `build/nobody-in-charge.md` was
kept, the script was run, and the two were diffed. Three hunks, all of them intended. The date
line, the part title page before the appendices, and the appendices themselves. Everything
else is line for line identical, which is the evidence that the script is the assembler and
not a plausible substitute for it.

**The primer.** `reference/PRIMER-steps-and-traditions.md`, one finding for each of the
twelve Steps and each of the twelve Traditions. It exists because the per-item findings are
spread across eleven chapters, and a reader wanting to know what the model says about
Tradition 9 currently has to read most of Part Two to find out. Every entry is in two layers:
a technical statement with its provenance, and a plain-English reading labelled *In plain
terms*.

**It asserts nothing, and that is the thing to remember about it.** Every figure in it is
copied from a chapter Machinery, from the notebook, or from a cached JSON. It is the first
document in the project that carries figures and is reached by no instrument:
`check_book.py`'s figures rule reads chapters, and the notebook asserts chapter values.

**So it was audited the way the manuscript was audited, against the model source rather than
against the chapters it was copied from.** Every deterministic figure was recomputed from
`aa_group_model.py` by a script that does not read the notebook: the twelve
group-dependence coefficients, the row sums, the coupling matrix and every principal
supplier, runner-up, index-mate and rank in it, all twelve top-two margins, the loads and
their concentration, the resource shares, the thresholds and their protective and enabling
ranges, and the governance matrix's summary statistics. Every stochastic figure was
re-aggregated from raw per-run records: the twelve degradation rows and the reference mean
and cross-seed standard deviation from `tradition_paired.json`, all four Part Five conditions
at year thirty and all five levels of the Tradition 3 sweep from `part5.json`, the three
service configurations from `ch15_service.json`, and the calibration figures from
`core_thresholds.json`.

**One real error, and it is a citation rather than a number.** The primer gave Maxwell 1950
as *Quarterly Journal of Studies on Alcohol* 11(3): 410-451. Every other file in the project
gives 11: 410-452, and so does the running header of the saved transcription. An issue number
that is not in any other copy and an end page one short. Corrected.

**Two smaller things.** The provenance list named five notebook sections and needed ten: the
service results come from section 13 and the deliberation tables from section 2, neither of
which was cited. And the Tradition 3 entry put a paired degradation figure and a five-level
sweep in consecutive sentences without saying they come from different designs, which invites
a reader to add them. Both fixed.

**Four places where the plain layer carried further than the technical layer under it.** They
are recorded here rather than tidied away, because they are the failure mode this document
has and the chapters do not. Step Nine's plain note says the propagation result is what
people mean by keeping it by giving it away; the model produces the propagation and not the
saying. Step Twelve's reads a supply constraint as a statement about what a group needs
newcomers for, which is a motive and not a mechanism. Tradition 3's says an unwelcoming group
cannot be told from a healthy one by looking, which is stronger than the sweep supports since
the two differ in survival as well as in appearance. And Tradition 1's tips into advice about
what a group should check, which nothing in the model licenses.

**What no instrument covers, stated so the next session does not have to rediscover it.** The
plain layer is an interpretation of the technical layer directly above it. Nothing checks
that the two still agree. A figure can be corrected in the technical half of an entry and the
paragraph beneath it will keep the old reading and pass every check in the project.
`CLAUDE.md` now says to read the plain paragraph whenever the number above it changes, and
that instruction is the only thing standing between the primer and silent drift.

**The book.** Three appendices now, in order: the technical appendix unchanged, the primer,
and the paper converted from its LaTeX at build time with its headings shifted one level so
its sections do not become chapters of the book. The paper's own PDF is still its
authoritative rendering and the `.tex` is still its source of truth. The part title page that
read "Technical Appendix" now reads "Appendices". All three appear in the contents page,
which is at depth one and so lists them as three entries.

**Bookkeeping.** Primer 7,606 words, 14 pages standalone. Book 275 pages, up from 227;
128,015 words assembled, up from 104,383. Build takes about twelve seconds.

**One more thing the checkers found, and it is the exemption that found it.** Running
`check_chapter.py` over the primer produced four FAILs, all of them the checker insisting a
non-chapter be a chapter: no Machinery section, no `# Chapter <Word>` heading, no `## <Title>`
under it, and Machinery parts wrong. The house rule is to fix the check rather than the
prose, so the checker gained a `BACK_MATTER` exemption alongside the `FRONT_MATTER` one that
already covers the preface and the introduction. It is structural only: the primer is still
held to every notation, punctuation and sentence-length rule.

**And the exemption immediately cost something, which is worth recording because it is the
argument against adding exemptions casually.** Skipping the structural block also skips the
reference-heading rules. The primer's reference section had *Internal, and reproducible from
this repository* before *Read in full*, which is not the canonical order, and it omitted
*Cited at a remove* rather than putting "Nothing." under it. Both are FAIL-level defects in a
chapter. Nothing reported them, because the exemption had just been written. Fixed by hand,
and the comment in `check_chapter.py` now states what the exemption does not cover so the
next person adding to the primer knows the headings are on their honour.

**Standing warning, not fixed.** The primer carries ten sentences over forty-five words
against two in a typical chapter. That is a warning rather than a FAIL and it is left as one,
but the plain-English layer is where it concentrates and a plain-English layer with
forty-five-word sentences is not doing its job. Worth a pass.

**Completeness sweep at the end of the session.** Four things the first pass had missed, all
of them the same kind of omission: a document that restates figures without saying so.

*PART-2, PART-3 and PART-5 plans.* Only the Part Four plan had been told the primer exists.
The primer restates Part Two's influence tables, Part Three's per-Step coefficients and Part
Five's decline conditions as well, so all three now carry the same instruction. Each note
names the risk specific to its part rather than repeating a generic warning: for Part Two the
primer is a lookup table and not another telling of the influence result, so it does not add
to that plan's standing repetition risk; for Part Five the danger is the plain layer dropping
the mortality-not-size qualification from the book's strongest simulation claim; for Part
Three it is that a per-Step list in plain English is the format in this project that most
invites being read as advice about how to work the Steps, which is the thing Part Three's
plan and Chapter 25 both forbid.

*The primer is rendered twice and only one of them regenerates.* The book's appendix is built
from the markdown every time `build_book.py` runs. The standalone
`reference/PRIMER-steps-and-traditions.pdf` does not regenerate itself, so it goes stale on
the first edit and looks current while it is. This is the same defect as a stale built book,
in a file nothing points at. `CLAUDE.md` and README now carry the re-render command.

*README said "Two built artefacts" and listed three.* There are three: the book, the paper,
and the standalone primer.

---

## Staged research corpus organized

The research acquisition package created 4 August 2026 is now located directly at
`research/staged/`, without a `corpus_build_2` wrapper. The package contains 40 files:
source documents and OCR, per-item citations and metadata, pending-source records, the
acquisition ledger, the acquisition report, and future incorporation instructions. Its
internal relative paths were preserved.

This is a location and status change only. No staged item was incorporated into the
manuscript, added to the book's cited-source register, or used to alter a claim. The staged
README and `research/SOURCES.md` state the boundary explicitly so that acquisition status
cannot be mistaken for manuscript use. The repository copy was verified against the prior
deliverable by SHA-256. On 6 August 2026, after that verification, the user asked for the
redundant local delivery folder to be deleted and confirmed that another copy exists elsewhere.

---

## Independent verification brief installed

`AGENT_VERIFY.md` now records the complete cross-layer audit for an independent AI verifier.
Its eighteen release gates cover the executable model, algebra, estimands, intervention
designs, endpoint semantics, sensitivity and uncertainty, notebook/cache provenance,
manuscript, technical appendix, paper, primer, source ledger and rebuilt artifacts. The brief
distinguishes factual checks from editorial and model-design decisions; it does not treat
agreement among prose, cached output and generated PDFs as independent confirmation.

The brief also points to `research/staged/` as the canonical deferred corpus and records the
former delivery location for provenance. The redundant local delivery was subsequently deleted
at the user's request; the user retains a separate copy. Corpus presence is explicitly not
incorporation. No model equation, parameter, result, manuscript claim, paper claim, primer
entry, cache or generated artifact was changed in this installation pass. Release remains open
pending independent verdicts and the user's decisions on the identified design choices.

---

## Maxwell and Golub-Jackson moved from staged to incorporated

At the user's direction on 6 August 2026, `research/incorporated/` was created for the two
already-used sources that overlapped the staged acquisition package. The project's original
Maxwell PDF and text moved into `research/incorporated/Maxwell_1950/`. The later staged Maxwell
PDF had the same SHA-256 as the original; its package and its different OCR were removed rather
than merged. The complete six-file Golub-Jackson package moved intact from staged to
`research/incorporated/Golub_Jackson_2010/`.

The source ledger, manuscript source notes, primer, verification brief, project instructions,
staged metadata and acquisition report were updated to the new paths and statuses. The source
checker now searches the active research root and `research/incorporated/` recursively while
continuing to exclude `research/staged/`, so a merely staged text cannot satisfy a manuscript
citation check. Twenty-eight files remain staged; no other established source was moved.

The final check reported zero failures and the same eighteen repetition warnings; all 55
citation-subject pairs still resolve against thirteen active saved sources. The 274-page book
and 14-page standalone primer were rebuilt and the title, changed-reference and final pages
were rendered to images for visual inspection. The longer incorporated path initially clipped
in two chapter reference lists; those notes now name the incorporated directory while
`research/SOURCES.md` retains the exact filename. The same inspection exposed and corrected an
older clipped Hawkins filename on that page.

This machine had neither Pandoc nor XeLaTeX at the start of the rebuild. Pandoc, Tectonic and
the project's TeX Gyre Pagella fonts were installed. `tools/build_book.py` now prefers XeLaTeX
when available and falls back to Tectonic; the standalone-primer command in README and
CLAUDE.md names Tectonic, matching the verified build environment.

---

## The three remaining screens finished, and the Sobol factor set was wrong

The release round had been paused with the multi-level one-at-a-time sweep 8 parameter jobs into
118. Resuming it completed the remaining 110 and closed the last three quantitative gaps: 944 OAT
perturbation points, a twenty-trajectory Morris screen over all 118 factors at 2,380 points, and a
1,024-row Sobol design at 11,264 evaluations. All three caches match the frozen model hash and
their own script hashes, and `tools/summarize_robustness.py` now generates
`research/ROBUSTNESS-RESULTS.md` from them.

**The OAT screen resolved more cleanly than the global designs.** Across 944 points the
pure-attraction-loss minus referral-loss ordering is strict in 931, tied in 2 and reversed in 11 on
final membership, and 934/10/0 and 933/11/0 on endpoint viability and existence. The eleven
membership reversals are not scattered noise: nine of them are large downward moves of `p_gate`,
`delta0` and `churn`, and the other two are the `S:11,5` and `S:11,6` cells. That is a more
informative failure than a bare percentage, and it is why the counts are reported by parameter
rather than compressed.

Two older claims did not survive the recount. Chapter One said more than half the model's
parameters could move the referral-starved survival probability on their own; the correct figure is
26 of 118. Chapter One and Chapter Six both said the ordering held in all 236 one-at-a-time cases,
which was the retired design and the retired model.

**All 35 governance cells return exactly zero, and that is not a finding.** Maximum absolute
deviation across every outcome and scenario is 5.6e-17. The OAT sweep runs at full adherence, where
column-normalised governance quality is identically 1 whatever the underlying magnitudes are. This
is the vacuous-robustness trap the project has already fallen into twice, so it is now stated as a
property of the reference point in the appendix, the parameter ledger and Chapter Twelve's
Machinery, alongside the reason the Morris and Sobol designs sit at 0.85 instead.

**Three of the eight Sobol factors were wrong.** `model/sobol_indices.py` had carried a `FACTORS`
list from the retired ten-trajectory screen. Against twenty trajectories, `a:8` falls to rank 15,
`a:4` to 27 and `omega` to 37, and `lam_exog`, `a:5` and `a:11` take their places. The membership
cut is untied, 15.87 against 14.34 at the ninth factor. The list was corrected before the Sobol run
rather than after it, and the evaluator was extended at the same time: it had handled scalars and
step speeds only, and would have silently done nothing if a matrix cell had ranked in the top eight,
because writing an `S` or `GOV` id into the parameter dictionary is a no-op. It now mutates the
matrix and rebuilds every derived quantity, matching the OAT and Morris evaluators, and raises on an
unrecognised id. No matrix cell ranked that high this time; the highest is `S:8,6` at 17.

**The bigger base sample half-repaired the first-order column.** At N = 128 the first-order indices
failed three diagnostics and were withheld entirely. At N = 1,024 the membership column is
admissible: no factor has `S1` above its `ST`, and the sum is 0.693 rather than an impossible
number. `p_gate` resolves at 0.404 [0.288, 0.525] and `delta0` at 0.238 [0.156, 0.327]; the other
six cover zero and are unresolved rather than zero. The practice column is still not usable, and it
fails for a smaller reason than before: `delta0` returns `S1 = 0.421` against `ST = 0.417`, and the
practice first-order sum is 1.074 against the old 1.263. So the paper now reports a membership
first-order decomposition it previously refused to report, and continues to withhold the practice
one. Total-order sums of 1.456 and 1.464 still say interaction is present and not dominant, and
`a:5` and `a:11` sit at or below the 0.0429 membership noise floor and are not separated from Monte
Carlo error at all.

**A counting error in the primer surfaced on the way past.** It said three of the four unresolved
Tradition rows were protective Traditions. Seven of twelve contrasts resolve and five do not, so
there are five unresolved rows, of which three are protective. The number three was right and the
number four was wrong.

**On generating platform.** These screens ran on Linux x86-64 under NumPy 2.2.6, while the earlier
caches were generated on macOS. Re-executing a macOS-generated OAT job on Linux reproduced every
discrete outcome exactly and differed on continuous outcomes only in the last representable digit,
around 1e-16. That is far below reported precision and changed no classification, but the caches are
hash-linked to the model and script rather than to a platform, so the provenance is now recorded in
the parameter ledger and the verification brief. An independent verifier should expect agreement to
reported precision, not bit-identical reproduction.

---

## The figure checker was failing, and it had caught a real error

`tools/check_book.py` requires every decimal printed in a chapter to be reachable from the
notebook, the model source, or a cache. It was reporting 102 failures. Fifty-five of those predate
this round; the rest appeared when the notebooks were regenerated, because the compact cache-identity
notebook prints far fewer figures than the 38-cell notebook it replaced.

Restoring the old notebook was not an option. Run against the current caches it reports
`Morris trajectories: got 20.0000, book says 10.0`, has three cells that produce no output, never
contained the sentinel the verification brief requires, and finishes `NOT CLEAN`. It was written
for the pre-correction model and still checks against 41.7 baseline members.

So `tools/regenerate_notebooks.py` now emits a published-figures cell that derives the quoted
values rather than restating them: the part5 trajectories and sweeps, the Chapter 14 decay sweep
and its environment-matched test, service, proxy averaging with Wilson intervals, the OAT influence
ranges, the release gate with Wilson intervals and paired contrasts, the Chapter 7 DeGroot example,
the Chapter 13 cross-partials, the Part Four overlap algebra with its seeded jitter and structural
tests, the Chapter 17 reassignment test, and the Chapter 22 founder constants. That took the count
from 100 untraceable decimals to zero.

Three obstacles were worth recording. The prose rounds half away from zero and Python rounds half
to even, so a cached 57.705 prints 57.70 from `round()` and 57.71 in the book; the cell prints both.
Chapters quote stored proportions as percentages, so both are printed. And the Chapter 14
maintenance figures are stored as `3.03e-08`, which no decimal search can match, so they are also
printed in plain decimal.

**The checker was right about one number.** Chapter 20 and the paper printed the invisible
condition's year-ten membership as 12.99. Every other cell in that row reproduces exactly, and the
correct derivation is 12.9849, so both now read 12.98. That is the whole value of the check: it
does not care that the number looks reasonable.

The two remaining failures were real house-style violations. Chapter 13's Machinery presented
400-replication output with no interval; it now labels the substitution table and cross-partials as
exact algebra and gives Wilson intervals for the proxy-averaging proportions. Chapter 14's decay
sweep now carries 95 per cent half-widths beside its membership series.

## The last clipped table, and why --columns made it worse

Table 41, the paper's mapping table as reproduced inside the book, was cut off on the right. The
cause was not width in the ordinary sense: pandoc emitted it as a **simple** table, one line per
row, which cannot wrap, so it converted to a 211-character table whose relative column widths were
then computed against the default 72-column reference. That put it about three line widths wide.

Setting `--columns` looked like the fix and was not. On the conversion pass it does not change a
simple table's width at all. On the PDF pass it rescales every table in the book, and it took the
count of overflowing pages from two to nine. The actual fix is `-t markdown-simple_tables` on the
conversion, which emits a wrapping grid table. Book margin overflow is now zero pages across 259.

Earlier in the same pass: typewriter filenames were being cut mid-word, the 64-character model hash
overflowed the appendix's first page, Table 48 had lost its final two columns, the book printed
dead `[eq:err]` and `[prop:one]` cross-references where the paper prints numbers, and the mapping
table had lost the `1.` from its Common welfare row because pandoc's LaTeX reader reads a leading
`1.` as an ordered-list marker and drops it.

---

## The staged corpus, worked through

The deferred corpus turned out to be six items, not the twenty-eight the file count suggested:
three American Temperance Union documents, the 2024 AA pamphlet P-17, and two journal articles
that were never actually downloaded. Four are now incorporated and two are not.

**A licensing problem had to be settled first.** This repository is public, and it was carrying
the complete 4.8 MB PDF of P-17 plus a full OCR transcript. The corpus's own metadata calls it
"copyrighted AA literature distributed as an official free PDF" and says to preserve the copyright
notice and not redistribute beyond the authorized source context; the staged README said the
pamphlet was "subject to the project's source-policy and licensing review," and no such review had
happened. It had been public since the initial import. At the user's direction the PDF and OCR
were deleted and replaced by a record holding the citation, the official aa.org URL, the SHA-256
of the July 2024 file, and the passages the project relies on. Citing the pamphlet was never the
problem; mirroring it was.

**P-17 turned out to matter more than expected.** It reproduces Bill W.'s original 1946 "Twelve
Points to Assure Our Future" beside the modern short forms, and states that in all but the Second
Tradition the original language has been modified or shortened. The 1946 Tradition 9 reads "Each
A.A. group needs the least possible organization. Rotating leadership is the best," and goes on to
"the large group its rotating committee." The modern short form on the same page says only that
A.A. ought never be organized but may create service boards or committees. The primer asserts, in
as many words, that the Traditions say to rotate but do not say how many people. Checked against
the short form alone the first half of that sentence is unsupported, because the short form never
mentions rotation. The 1946 long form supplies it outright, and supplies "they do not govern" as
well, which the project had been attributing to Tradition 2 alone. The second half is confirmed:
neither wording gives a number, a fraction, or any scaling rule, which is the gap the deliberation
model fills. Both passages were verified against rendered page images before the file was deleted.

**The 1841 ATU annual report is the earliest contemporary witness the project now holds.**
Chapter 1's founding narrative rested on Harrison (1860), Maxwell (1950) and, through Krout, the
Maryland state report of 1842, all of them later and two of them in disagreement. The ATU appendix
at printed page 39, verified against the page image, describes the Baltimore society within a year
of its founding: six men, a public tavern, a simple total-abstinence pledge, the name, the 5 April
1840 date, and more than a thousand members inside the year. It also records two mechanisms this
project models, in 1841 language: "at their successive meetings, each man to bring a man," which
is inflow through existing members, and "a public relation by each individual of his own
experience and history," which is the supply of identification and of visible proof that recovery
happens. That corroborates Krout's bring-a-friend agreement a year earlier and from a different
organisation. It is a description of a practice, not evidence that the practice caused the growth,
and it bears on nothing in Part Two.

That find forced a status correction in the same chapter. The ATU annual reports were listed under
"Cited at a remove," known only through Maxwell. Three volumes are now held, so the entry says so
and the remove is narrowed to the years still unheld.

**Two articles stay unread, and are labelled unread.** Greenfield and Tonigan (2013) and Pagano et
al. (2004) are `verified_online` with stable PMC locations, and retrieval returned a reCAPTCHA
challenge. The project does not work around access controls, so both remain unusable as claim
support and their recorded summaries are expectations rather than findings. Pagano is the
consequential one: it bears on Chapter 15 and on the recipient resource, whose contrast is
already unresolved, and a reader who wants that argument strengthened will have to fetch it by
hand.

The 1840 report and the 1849 almanac are obtained and consulted but support no claim. They are
recorded as looked at and set aside, which is a different thing from overlooked.

---

## The corpus, normalized, and the documents taken out of the repository

The research folder had grown by accretion: twelve source documents loose at the top level beside
the caches and ledgers, four source directories under `incorporated/` with four different naming
styles, and a verification index for Kurtz sitting on its own. Everything is now one shape.

Each source is a directory, `research/incorporated/<ShortAuthor>_<Year>/`, holding the document,
`citation.md`, `metadata.json`, `source_summary.md` and a verification index. `tools/build_corpus.py`
does the normalization and is idempotent; `--check` reports drift without touching anything.
Citations were lifted out of `research/SOURCES.md` rather than retyped, so there is still one place
for a citation to be wrong.

**No source document is committed any more.** This is the part worth recording carefully, because
the reasoning had been wrong in the ledger for some time. The Maxwell entry justified storing a
1950 journal article by saying "this folder is private." The repository is public and always has
been. The argument was sound and the premise was false, which is worse than a bad argument, and it
had propagated: the same assumption sat behind mirroring the AA pamphlet.

So `.gitignore` now excludes every `.pdf`, `.txt`, `.djvu` and `.epub` under `research/incorporated/`
and `research/staged/`, and the tracked record for each source is its citation, its rights position,
its provenance URL, the SHA-256 of each file, a summary, and an index. The documents remain as local
working files. A checksum and a URL are a better provenance record than a copy anyway, because they
can be checked against the original instead of trusted. The repository stops carrying 53 MB of
scans, of which one file was a 22 MB Grosh PDF.

**The hard part was not losing the citation check.** `tools/check_book.py` confirms that a chapter
citing a source for a subject is citing a work that actually contains that subject, and it did that
by searching the full text. Kurtz already had the answer: it is in copyright, was never stored, and
had a vocabulary-only index instead. Generalizing that pattern exposed one real gap. A vocabulary
set has no word order, so "sheer survival value", "pocket companion" and "timeline followback" all
failed the moment the texts went away. Each index therefore also records which registered subjects
its document contains, decided against the real text at build time and stamped with that file's
SHA-256, and the subject list is read out of the checker rather than duplicated so the two cannot
drift.

That was tested rather than assumed. With every document moved out of the tree, the checker still
verified all 55 citation-subject pairs across 15 sources. Two limitations are declared in
`SOURCES.md` rather than buried: the matcher is deliberately OCR-tolerant, so short subjects can
match spuriously, exactly as they could against full text; and an index shows that a word occurs
somewhere in a work, which is weaker than a page reference, so quotations are still checked against
page images.

Two small things fell out of it. Parsing the checker's subject list needed comments stripped first,
because a comment contained the word "book's" and the apostrophe unbalanced the quote pairing,
which silently produced separator fragments as subjects. And the paper stopped compiling: the new
directory names contain underscores, and an underscore in LaTeX outside math mode is a subscript,
so every corpus path inside a `\texttt` span had to be escaped.

---

## Publication review of the whole repository

A sweep for stale instructions, dead content and contradictions, now that the gate is closed and
the corpus is normalized. Nothing was found in the model or its analysis scripts: every script is
referenced by a cache or a tool, every tracked Python file compiles, and the only apparent TODO
markers are a loop variable named `todo` in the resumable runners. The one retired design named in
code, the 236-point OAT star, is named as history in a sentence that says it is history.

What was stale was the paperwork around the work, which is the usual pattern.

`README.md` still opened by saying the project was *in* a release-gate correction round that had
in fact closed. Its reproduction sequence also omitted two generators whose outputs the release
check requires: `inventory_model_choices.py`, which writes the inventory `check_release.py` reads
for the registered-value counts, and `summarize_release_gate.py`. A reader following the documented
sequence on a fresh clone could not have regenerated everything the gate demands. Both are now in
the sequence, along with `build_corpus.py`, and the paragraph beneath explains what each one is
for. Running them changed nothing but a timestamp, which is the answer one wants: the committed
artifacts already matched their generators.

`BOOK-PLAN.md` still said Part Six and the introduction remained to be written and that Chapter 22
was 762 provisional words waiting on Carrell, Sacerdote and West. All three chapters of Part Six
exist, the introduction exists, and Chapter 22 is about 2,300 words and cites Carrell three times.
The old paragraph is kept as a dated record rather than deleted, because the plan is also a
history. Its Gough path pointed at a `.gz` file that no longer exists under that name.

`plans/PART-3-PLAN.md` still instructed that every cache depending on capability heterogeneity be
treated as invalid until regenerated. They were all regenerated weeks ago and are hash-linked to
the frozen model.

The paper's source-boundary paragraph still described the staged corpus as reserved for the next
iteration. `HANDOFF.md` still described the old boundary in its section 2, still said the round was
unpushed, and still gave the book as 259 pages. `AGENTS.md` pointed a new agent at a checkpoint
that no longer exists.

One rule was wrong rather than stale. `CLAUDE.md` required five reference-status headings at the
end of every chapter. The book uses the applicable subset, in the fixed order, omitting a heading
rather than filling it with a placeholder, and has done so in every chapter since Part One. Twenty
of twenty-one chapters carry four of the five. The rule now describes the practice instead of
contradicting it, which is the right direction to resolve that kind of disagreement: the
manuscript was not wrong.

Two findings were deliberately left alone. The 39 repetition warnings are overlapping n-grams of
one phrase, the registered-set decomposition, restated in the preface and in Chapter 12 because
both need it; that is intentional. And the two em dashes in Chapter 1 sit inside block quotations,
where house style preserves the source's punctuation.

The empty directories left behind when the staged corpus was emptied are gone. Git would not have
carried them anyway, but they were misleading on disk.

---

## The paper notebook stops being a copy of the book's

The release plan asked, in section 3.4, that the stale paper notebook be replaced or explicitly
retired. What happened instead was that both notebooks came to be generated from one cell set and
differed only in their title. That satisfied the release gate, which asks that both execute clean
with stored output, while verifying nothing whatever about the paper. It was recorded as an open
editorial item rather than a defect, which was too generous: the chapters have had a figure
checker since August, and the paper had no counterpart at all.

It has one now. The paper notebook keeps everything the book notebook does and adds two cells.

The first re-derives the paper's headline tables from the caches: all eight release-gate
conditions against their published means, the paired Tradition 3 and Tradition 11 contrasts with
the requirement that their intervals exclude zero, the recipient contrast with the requirement
that its interval crosses zero, the Sobol split where the membership first-order column is
admissible and the practice column is not, and the structural ordering in all five architectures.

The second is the one that was missing. Every decimal the paper prints must be reachable from the
model source, a hash-linked cache, or a derivation shown in the notebook. After excluding DOIs and
the five figures quoted from cited literature, that is 420 numbers, and the check fails closed
naming any that cannot be reached.

Getting to zero needed the derivation extended in four places the chapters never exercised:
structural variant means at two decimals, the horizon series from `mc_error`, the Sobol
first-order and total-order sums, and Wilson intervals on the decline table's viable fractions,
which the chapters print as bare fractions and the paper prints with bounds. It also needed the
governance sparsity pricing recomputed, the seeded test that flips k cells confined to the
enabling rows and asks how often each Part Four claim survives. That table has no cache; it is
recomputed from `model/elicitation_compare.py` at its published seed.

One incidental fix. `tools/check_portability.py` flags Windows absolute paths by looking for a
single letter followed by a colon and a slash. In a JSON notebook every source line carries an
escaped newline, so a Python line ending in a one-letter variable and a colon is stored as that
letter, a colon and a backslash, which matches the pattern exactly. Two variables were renamed so
no line ends that way. The checker is right to be blunt here; the answer is not to weaken it.

The book notebook now runs 8 cells and 71 assertions, the paper notebook 10 and 95, and they are
no longer the same file. `AGENT_VERIFY.md` records that if a verifier finds them identical again,
that is a regression rather than a simplification.

---

## The elicitation kit was leaking its own answer

Checked before sending anything out, on the principle that an instrument should be tested on the
bench rather than on the first respondent. The kit is otherwise in good order: the blank grid's
eight columns are in exactly the model's resource order, so a completed form parses correctly; the
script's self-test passes and, importantly, its second case is a respondent who differs by one row,
which the script correctly reports as contradicting Chapter 18 rather than smoothing over.

Two defects, both in the form.

**It told the respondent how many rows should come out empty.** The section headed "What will be
done with your answers" said the book's chapters rest on the claim that *five* Traditions govern
nothing any Step consumes. A respondent reads that before filling the grid. It does not say which
five, but a count is most of the way there when there are only twelve rows, and the form's whole
premise is that the answers are independent. The same form is scrupulous elsewhere: it declines to
name the two decisive cells, saying in as many words that they are not named so as not to lead the
reader. The count is now withheld on the same grounds and for the same stated reason. The
collator's section still names it, and now says at the top that it is not to be handed to a
respondent.

**It said the comparison script did not exist.** It does, it is what the preregistration consists
of, and the form now says so and gives the two commands to run, including the self-test to run
before any form goes out. The paragraph also records the substitution the script makes for a
bare-marks respondent, since that determines what such a respondent is actually testing.

Neither defect would have been visible from the analysis side. Both would have quietly weakened
the one instrument in the project that can test Part Four from outside.

---

## Two copyrighted works removed from published history, and Pagano finally read

**The history rewrite.** Untracking the Maxwell article and the AA pamphlet stopped them being
distributed going forward, but a public repository still served them at older commits, which is
most of the problem the untracking was meant to solve. Four blobs were purged from every commit:
the Maxwell PDF and text, and the P-17 PDF and OCR. Every citation, metadata file, summary and
verification index survived, the commit count is unchanged, and a fresh clone from the remote
confirms none of the four is reachable.

Two things are worth recording for the next person who does this. A checkpoint reference under
`refs/codex/`, a bare tree rather than a commit, kept the old blobs alive after the rewrite; and
`git log --name-only` does not traverse a tree reference, so the first verification reported
success while a 4.8 MB pamphlet was still sitting in the object database. The check that actually
works is `git rev-list --objects --all`. Also worth stating honestly: GitHub retains unreachable
objects for a while after a force-push, so this makes the files unreachable rather than instantly
unrecoverable.

The remaining bulk of the pack is public-domain scans, which have no copyright problem, so they
were left alone. A full backup bundle sits in the project folder, git-ignored, as the rollback
path.

**Pagano (2004), read at last.** The article was behind a challenge page that blocks automated
retrieval but not a person with a browser, so it was downloaded by hand and added to the corpus.
Chapter 15 had been unusually honest about its own weakness here: it recorded that the forty and
twenty-two per cent figures came from a 2011 university news release rather than the paper, that
the paper's tables had not been seen, and that the full text should be obtained before the chapter
was final. `SOURCES.md` called the chapter's sourcing the weakest in the book.

Reading it settles that. Both figures appear in the paper's own results section, so the press
release had reported them correctly, and the independence from meeting attendance is established
there by proportional-hazards regression controlling for meetings attended. The chapter's existing
caution about the finding being observational was already the paper's own position.

Reading it also added something the press release did not carry, and the chapter now says it: the
authors' first stated limitation is that only 8 per cent of the sample were coded as helping, on a
measure they describe as crude. That makes the selection worry harder to dismiss rather than
easier, which is the honest direction for a new fact to push a chapter that leans on this study.
The copy held is the NIH author manuscript, so its pagination is not the journal's and no
page-specific citation may be taken from it.

One item is left staged: Greenfield and Tonigan (2013), behind the same kind of challenge page.

---

## Greenfield and Tonigan read, and the staged corpus closes

The last staged article was behind the same challenge page as Pagano, so it arrived the same way,
by hand. With it the staged corpus is fully incorporated: six sources acquired on 4 August, all
six now read or consulted and entered in the ledger. What is left under `research/staged/` is the
acquisition report and metadata, which are provenance rather than evidence and stay for that
reason.

**The staged record had the citation slightly wrong.** It gave *Psychology of Addictive Behaviors*
27(2): 553-560; the article's own front matter reads 27(3): 553-561. Both the issue number and the
end page. That is a small thing and it is exactly the class of error that survives indefinitely
when a citation is recorded from a search result rather than from the document.

**The finding is an objection to the model, not support for it, and that is the more useful
outcome.** The study is a measurement paper: 130 new AA affiliates at intake and at three, six and
nine months, comparing a face-valid step-work instrument against an indirect one. Two things in it
matter here.

First, the two instruments disagreed about whether step-work had happened for nine of the twelve
steps. That is direct external support for a caveat the book had been making on its own authority,
that the practice scale is cardinal only inside the model and corresponds to no validated
instrument.

Second, and less comfortably, their factor analysis found step-work is not one thing. It separates
into behavioural and spiritual components with different predictors, different time paths and
different relationships to outcome: behavioural step-work held steady and was predicted by having
a sponsor, spiritual step-work declined over time, and only the spiritual component predicted
percent days abstinent. Behavioural step-work predicted nothing.

This model gives each step a single level. It cannot represent the member their data describes,
whose behavioural practice holds while the spiritual part falls away, and it averages into one
number the only component that predicted an outcome. Chapter 12 now says so, in the chapter that
introduces the dials rather than buried in a limitations list.

Worth being precise about what kind of problem this is. It is not a calibration error and no
sensitivity design in this project can reach it. Every screen here varies the values of the
dials; none varies the decision to have one dial per step. Testing that would take a second model,
not another sweep. The study is also small, nine months long and observational, so it is an
objection to the shape of the apparatus rather than a refutation of it, and the chapter says that
too.

---

## Coherence audit after the two articles were read

Reading a source changes more than its own entry, and this pass was about finding what else had
gone stale. Three documents were still describing Greenfield and Tonigan as unread, in the exact
places a careful reader would check.

Chapter 13 carried a note saying the empirical literature was read at one remove, listing the four
claims it took from the abstract, and instructing that the full paper be read before the chapter
was final. Chapter 24 said two claims rested on material not read, and that the paper was on the
outstanding acquisition list. The paper's bibliography said "abstract and secondary summary only".
Pagano's paper entry still said "cited at a remove; the full text could not be obtained".

All four are now corrected, and the correction is a confirmation rather than a retraction, which
is worth recording because it could easily have gone the other way. Every specific claim those
chapters took from the abstract survives contact with the full text: the two-factor structure, the
differing predictors and time trends, only spiritual step-work predicting percent days abstinent,
and the instrument disagreement on nine of twelve steps. What full reading added was scale and
design, 130 affiliates over nine months, observational, which now sits beside the findings in
Chapter 13 rather than being left to the reader to discover.

Chapter 24's entry improved in a different way. It had said the abstract was enough to establish
that the instrument exists and not enough to say what could be added to it. Having read the paper,
the chapter can now say what the additional analysis would be, because the two-factor structure
gives it an obvious form: score step-work per step rather than summing it.

`SOURCES.md` needed three separate repairs, which is a fair measure of how many places a read
status lives: the staged-corpus section, the limited-status section, which still listed Greenfield
under abstract-only, and a missing full entry beside Pagano's. The limited-status section keeps a
pointer rather than losing the name entirely, so a reader tracing an old citation lands on the
current status instead of a gap.

`AGENTS.md` was rewritten. It had been ten lines pointing at other files, which is thin for a cold
start by an agent that does not read `CLAUDE.md`. It now states what the project is, the six things
not to do, the authority order, where each kind of question is answered, the synchronisation rule,
and the house style, and it says plainly that the release gate is closed and the current state
should be treated as correct until a checker says otherwise.

---

## Corpus audit, and a remove that had been shortened without anyone noticing

A file-level pass over the whole corpus. The structure is uniform: nineteen source directories
under `research/incorporated/`, each with a citation, metadata, a summary and a verification
index, and the documents git-ignored beside them. Nothing loose, nothing duplicated, no downloads
left in place. Two macOS `.DS_Store` files were removed. Every corpus entry is cited somewhere in
the manuscript or paper, and every one appears in the ledger, so there are no orphans in either
direction.

The useful finding was not a stray file. It was that incorporating the AA pamphlet in a previous
session had quietly improved Chapter 5 and nobody had gone back to say so.

Chapter 5 is the chapter about the Twelve Points. Its Machinery said the 1946 and 1949 *Grapevine*
texts remained at one or more removes, being AA copyright and unread, and its reference block
listed Bill W.'s 1946 "Twelve Points to Assure Our Future" as quoted from Kurtz and not read. But
P-17 reproduces those Twelve Points in Bill W.'s foreword, and that text was read directly and
checked against the page images when the pamphlet was catalogued. The chapter was describing its
own sourcing as weaker than it had become.

The correction is careful about what changed. A 2024 AAWS pamphlet is a reproduction, not the
April 1946 *Grapevine*, so it shortens that remove without closing it, and it says nothing about
which of Kurtz's two conflicting issue numbers is the slip, which the chapter still records as
unresolved. What it settles is the wording, which is what the chapter's argument rests on.

It also supplied a fact the chapter had needed and lacked. The pamphlet states that in all but the
Second Tradition the original language has been modified or shortened. Chapter 5 already described
the text being cut after 1946 to sit closer to the length of the Steps; AA's own account turns
that into something sharper, that the familiar short forms are revisions rather than compressions,
with a single exception. Tradition 2, which carries the group conscience and the line about
leaders who do not govern, is the only one a reader meets today in the words Wilson first
published. For a book whose central argument runs through Traditions 2, 9 and 12, that is worth
having in the chapter rather than in a source record.

The general lesson is the same one the Greenfield audit produced: acquiring a source changes
chapters that do not cite it yet. The corpus is where a document lands, and the chapters are
where its consequences have to be chased down by hand.

---

## Three sources arrive, and one of them settles a question Chapter 5 had given up on

Five files supplied by the author: the April 1946 *A.A. Grapevine* article, DeGroot (1974), a Big
Book reprint, and two updated acquisition-status files. None had been in the corpus. Three
observations came before any of it was catalogued.

**The author's own rights review forbade archiving two of them.** The 7 August status file opens
with an instruction not to add a full-text PDF to the corpus unless a listed authorization route is
met, and lists DeGroot and the 1946 Grapevine article as restricted pending permission, the latter
with the direction to cite and quote within applicable limits rather than archive the scan. The
scan does carry an A.A. Grapevine copyright line and a silkworth.net watermark, so it is a
third-party reproduction. Both are therefore held the way P-17 is held: a citation, a rights
position, the hash of the scan consulted, the passages verified from it, and no archived document.
That is not a workaround of the review; it is the route the review names.

**The Big Book file is not what its filename says.** "Big Book 1st edition.pdf" is a 1999 BBSG
publication whose own title page reads "The 4th Edition of Alcoholics Anonymous", where the fourth
edition is that reprint's numbering rather than AAWS's. It states that it reprints the 1939 first
edition and asserts no copyright. The content matches the label; the artifact does not, and
cataloguing it as the 1939 printing would have misdescribed provenance. It is recorded as the 1999
reprint of the 1939 text, with the note that the 1939 public-domain claim is widely asserted and
has been contested rather than settled.

**The DeGroot scan has no text layer at all.** No verification index can be built from it and no
quotation from it can be machine-checked. The paper has been read at source for years and Part Two
restates its updating rule in the project's own notation rather than quoting it, so nothing depends
on the scan; the corpus record simply says so.

**What the Grapevine article settled.** Chapter 5 recorded a citation problem it could not resolve:
Kurtz cites the April 1946 publication twice, once as "Alcoholics Anonymous Tradition: Twelve Points
to Assure Our Future" at 2:10, and once as the long form at 2:11. The article explains the titles.
Its Grapevine headline is "Twelve Suggested Points for A. A. Tradition, By Bill", and inside the
body Bill introduces the list under his own heading, "An Alcoholics Anonymous Tradition of
Relations, Twelve Points to Assure Our Future". Kurtz is citing the internal heading, AAWS's
pamphlet uses the same phrase, and the chapter takes its title from it. Two names, one article,
neither citation wrong about the title. The issue numbers are still unadjudicated, because the scan
carries no issue or page markers, and the chapter still says so.

The three sentences Chapter 5 quotes as its thesis are now read from the article rather than from a
historian's account of it, and they are exact.

**A naming collision the checker caught.** The new directories were first called `AA_Grapevine_1946`
and `AA_BigBook_1939`. `check_book.py` identifies a source in prose by the leading token of its
directory name, so both became "AA", which appears on nearly every page of a book about Alcoholics
Anonymous and manufactured thousands of spurious citation-subject pairs. They are now
`Grapevine_1946` and `BigBook_1939`, and the checker refuses any source token shorter than three
characters rather than trusting it silently. Three is the floor because "ATU" is distinctive and
"AA" is not.

---

## 10 August 2026, later: three copyrighted works read, and a rule corrected

Three works were read in full and catalogued as record only, bringing the corpus to 26 sources and
the record-only category to seven: AAWS *Twelve Steps and Twelve Traditions* (1953), Rohr's
*Breathing Under Water* (2011), and an undated Ernest Kurtz talk placed at about 1984 by internal
evidence. No document is held for any of them.

**The rule that changed.** Several chapters said, in various wordings, that this project does not
acquire AA copyright material, and treated that as a reason not to read it. That conflated two
different things. A rule against **holding** a copyrighted work is a copyright rule and the project
keeps it strictly. A rule against **reading** one was never a copyright rule at all. The old
wording has been removed from Chapters 2, 10, 16, 17, 18 and 25, from the primer, from
`research/SOURCES.md`, from the paper in three places, and from `CLAUDE.md`.

**What the error had cost.** The 1953 commentary contained four things the book had recorded as
unavailable:

1. The book's own thesis in Wilson's words. The chapter on Tradition 2 concludes that the group
   conscience, well advised by its elders, will in the long run be wiser than any single leader,
   and illustrates it with the group overruling Wilson's plan to become a paid lay therapist.
2. **The strongest objection to that thesis, from AA itself.** Two pages earlier the same chapter
   describes elder statesmen as the real and permanent leadership of AA, the voice of the group
   conscience, to whom a perplexed group inevitably turns. They hold no office and so rotate out of
   nothing. That is a persistent influence concentration, endorsed rather than warned against, and
   it is what the Golub and Jackson condition forbids. The same chapter calls the committee that
   does rotate sharply limited, unable in any sense to govern or direct, which means the fellowship
   rotates the positions its own commentary says carry no weight.
3. The disproof of the index-pairing conjecture. Across the twelve Tradition chapters, none cites
   the Step of its own number; across the twelve Step chapters, the word Tradition does not occur.
   The only indexed cross-reference in the book is Tradition 8 citing the Twelfth Step. Chapter 16
   had recorded that it could not say how strongly AA literature gestures at the pairing; it does
   not gesture at all, and that paragraph is withdrawn rather than edited.
4. Corroboration for Chapter 17. The chapters on Traditions 1 and 5 keep unity and singleness of
   purpose distinct, which is the assignment Kurtz's conflation charge threatened. This is not the
   passage Kurtz named, in *Comes of Age*, which is still unread.

**What was added to the model.** `model/part2_influence.py` gained an `elders` family, sections 5b
and 5c, with a cache rebuild. The frozen model was not touched and the room capacity, seed counts
and release designs are unchanged. Three elders holding a tenth of every row between them floor
maximum influence at alpha over e, computed 0.0342 at N = 1000 against a predicted 0.0333 and a
flat benchmark of 0.0010; the error ratio against flat runs 1.012, 1.075, 1.350, 2.079 at
N = 10, 50, 250, 1000. Setting the rotation pool to Chapter 10's recommended twenty-six per cent
does not rescue it: maximum influence runs 2.5, 9.2, 34.2 times flat at N = 50, 250, 1000 with
three elders at a tenth, against 2.0 flat-relative at every size for rotation alone.

The error ratio is stored in the cache rather than left to be divided out of two other numbers,
because `check_book.py` flagged 2.08 as untraceable, which it was.

**A subject that had to be withdrawn the same day.** Seven verification subjects were registered
with these sources. `rotating leadership` was one of them and lasted one run: it is the book's own
vocabulary as well as the Twelve and Twelve's, so it appears in chapters not citing that source,
and it paired with Gough in Chapter 2. That is precisely the manufactured pair the SUBJECTS comment
warns against, so the subject was dropped rather than the checker loosened. The remaining six are
each literally present in exactly one of the three new sources and absent from the other two.

**The Rohr provenance problem, recorded rather than smoothed.** The copy consulted carried an
OceanofPDF.com imprint, which is an unauthorized distribution site, and the work is a current
in-print commercial title, so the posting was plainly not authorized. This is a stronger objection
than the unverified-authorization cases of DeGroot and the 1946 *Grapevine*. The file was not
retained; the bibliographic record was confirmed against publisher and library listings
independently of it, giving Franciscan Media 2011, ISBN 9781616361570, with the copy consulted the
SPCK 2016 UK edition; and both claims the manuscript draws from Rohr are absence claims, checkable
by anyone holding a lawful copy. Any Rohr citation should be confirmed against a lawful edition
before release.

**A reading copy, held outside the repository.** AAWS publishes the Twelve and Twelve free as
twenty-nine per-chapter PDFs. They were assembled locally into one 187-page document in printed
order and left in the user's own folder, not in the repository. The assembly's SHA-256 is recorded
in `research/incorporated/TwelveAndTwelve_1953/metadata.json`.

---

## 10 August 2026, later still: the elicitation packet typeset, and the handoff rewritten

**The elicitation packet is now a set of typeset documents rather than five markdown files.**
Source in `research/elicitation/`: a shared style file matching the book's typeface, five LaTeX
documents, and `build.sh`. The PDFs were also copied to a folder outside the repository, on the
user's own machine, for sending out.

Two things changed in the move and both came from looking at the rendered pages rather than the
source. The grid had no vertical rules between its eight columns, which is fine on screen and
unusable on paper: a respondent filling it in by hand cannot tell which column a mark belongs to.
Columns are now ruled and widened to 12mm. And the collator's warning, previously a line of text,
is now a red-bordered box at the head of the document, because that document names the answer and
the instruction not to send it must not be skimmable.

The disclosure discipline was verified mechanically after building, not assumed: no
respondent-facing PDF contains the row count, the row names, or the filled-cell count, and the
collator notes do. That check is worth repeating if the packet is ever regenerated.

`model/elicitation_compare.py --self-test` passed again before the packet was copied out. It
still correctly reports a one-row-different respondent as contradicting Chapter 18 rather than
smoothing it.

**Corpus consistency.** The record-only category was previously legible only in prose. All seven
record-only sources now carry `"record_only": true` and a reason in their metadata, and the three
that have no verification index, `AAWS_2024_P17`, `DeGroot_1974` and `Grapevine_1946`, now say why
in the record: no text was retained to build one from. A verifier should not report either as
drift.

**Two live uses of the retired rule were found and fixed.** Chapter 21 and the SMF-132 entry in
`research/SOURCES.md` still gave "this project does not acquire AAWS publications" as the reason
SMF-132 is unread. That is no longer the rule, and SMF-132's own content-use policy permits a
single printed copy, so reading it is allowed. Both now say it is simply not yet obtained, which
makes it a task rather than a policy question. The remaining occurrences of the old phrase in the
repository are all descriptions of the retired rule, which is correct, plus one historical
progress-log entry, which stays as written.

**`HANDOFF.md` was rewritten as a cold-start document.** It previously assumed a reader who had
been in the room. It now opens with what the project is and what it argues, states the authority
order and the frozen-model rule before anything else, carries the full reproduction sequence, the
synchronisation rule, the corpus rules including the record-only category, what changed on
10 August and what it cost, the elicitation round with its warning, the house style, the list of
claims that must not be made, and what to do if you change anything. It is written to be usable by
Claude, ChatGPT, Cursor or a person with no prior context.

`AGENTS.md` gained two ground rules to match: do not edit the preregistered
`model/elicitation_compare.py`, and do not restore the retired copyright wording.

---

## 16 August 2026: project authorship and rights notice added

The anonymous bylines in the book builder, working paper and reference primer were replaced with
the repository's designated credit: Primary Author **theonlymuffinbot**
(`theonlymuffinbot@outlook.com`) and Co-Author **Christopher Melhauser**
(`christopher.melhauser@gmail.com`). The manuscript preface, technical appendix, README, handoff,
agent instructions and master book plan now carry the same attribution.

`ATTRIBUTION.md`, `LICENSE` and `CITATION.cff` now state the copyright and citation metadata.
The rights notice applies to original project material only and expressly leaves third-party AA
material and research sources under their own rights and provenance records. The book, paper and
primer PDFs were rebuilt and their title pages inspected after the change.

Later that day, the legal attribution was clarified: Christopher Melhauser is the sole copyright
holder and legal rights contact. theonlymuffinbot is acknowledged as an AI Writing Collaborator,
not as an author or rights holder. The title pages retain both credits and omit both email
addresses; the contact addresses remain in the repository metadata and notices.

Later still, all original project material was dedicated to the public domain under The Unlicense.
The manuscript, paper, code, documentation, research records, and generated project outputs are
covered by that dedication. `LICENSE` requests non-binding courtesy credit for Christopher
Melhauser and theonlymuffinbot while preserving the exclusion for third-party sources.

---

## 16 August 2026: Recovery Dharma catalogued, and appendix A12

A user question asked whether the model shows the Twelve Steps simplified into the Dharma. The
Recovery Dharma second edition (2023) was read in part to answer it, catalogued as
`research/incorporated/RecoveryDharma_2023/`, and the answer written as appendix section A12. The
work is appendix-only by request: no chapter, no notebook, no cache, and no stochastic claim.

**The answer is no, on three grounds that precede any evidence.** The Eightfold Path predates the
Twelve Steps by roughly two and a half thousand years, so a derivation claim in the direction asked
is ruled out by dates. The model has no parameterisation for the fellowship, and authoring two more
unelicited matrices would compound the weakness A11 item 2 already records. And the model has no
object corresponding to a comparison of fellowships.

**The count test kills the word simplification.** Recovery Dharma distributes thirty-five
enumerated items across seven lists: three jewels, four Noble Truths, eight path factors, five
precepts, four heart practices, four foundations of mindfulness, seven commitments in The Practice.
AA as the model codes it is twenty-four items in two. The eight-against-twelve comparison that makes
simplification look true sets one list against one list. There is a real simplification in the
source and it is of grouping, not count: the eight factors sit under three headings and are not
worked in sequence.

**The carrier census is the part with model content.** Deterministic quantities from the canonical
`S`: Steps 1 and 12 both carry maximal group dependence at 1.000; Step 12 is the sole carrier of
recipient opportunity, which holds the largest governance mass in `GOV` at 2.40; Step 1 holds 0.800
of admission and 0.588 of identification; Step 5 holds 0.667 of confidentiality. Read against the
source, the eight resources scatter across four Recovery Dharma documents, and three of them,
confidentiality, recipient opportunity and gentle pressure, are absent from the Eightfold Path
entirely. The counterpart of the Steps is not the Path but the union of the Path, The Practice, the
Sangha chapter and the meeting script.

**The governance asymmetry is the finding worth keeping.** The fellowship has no
Traditions-equivalent charter; the functions live as procedure inside a meeting script whose own
header invites meetings to edit it. A2.4's effective-adherence construction presumes a fixed
constitution whose adherence can vary while the constitution stands still, and an editable script
offers no such stable row. So the model can state exactly what it would need to say anything here,
and the source shows the required object does not exist. That is a result about the model's scope,
not about which fellowship is better governed, and it was added to A11 as threat item 9.
**Superseded later the same day:** item 9 was removed from A11 and folded into A12.7 when the
section was made self-contained. A11 carries eight items. See the entry below.

**Provenance took two steps, and both are recorded.** The PDF first read was an ephemeral session
attachment, removed from disk before it could be copied into the corpus. The source was catalogued
as record only, with no SHA-256 and no verification index, and the gap was written into the handoff
and verifier instructions rather than papered over. A filesystem search then located the user's own
copy, which was confirmed to be the same document by page count (172), byte size (871,059) and
verbatim spot-checks against passages read from the attachment. That copy is now hashed, extracted
to 57,419 words of text, and indexed, so the source sits on the ordinary footing and the
record-only language was withdrawn everywhere it had been written.

What survives from the first pass is worth keeping: this is the one source in the corpus whose
licence, CC BY-NC-SA 4.0, would permit committing the document outright. It is git-ignored anyway,
because the rule is uniform. `tools/build_corpus.py` gained a `RIGHTS` entry so the default
pre-1929 public-domain assertion is not applied to a 2023 book. The remaining open item is that the
bibliographic record came from the file's own title and copyright pages rather than an independent
catalogue entry.

Corpus counts moved from 26 to 27 sources; record-only stays at seven.
`research/incorporated/RecoveryDharma_2023/` holds the document, text, citation, metadata, summary
and index. The index's `subjects_present` reports three short tokens that are matcher artifacts and
are inert, since no chapter cites this source.

**A12.6 was added the same day, answering a second question: boil the model down to its core
inferences and ask which relate to Recovery Dharma.** Six inferences, stated without AA vocabulary:
the one-way causal chain from member states to group resources; multiplicative gating, where the
capacity weight rises from 0.05 at the first practice to 1 at the last; retention loading on early
practice and reproduction on late practice; dispersion as a multiplier on three of the eight
resources through the `unity` term; openness compounding super-additively across its two channels;
and referral loss being slow and disguised.

**The most useful result is a negative one.** Inferences 2 and 3 both descend from the order gate,
and the Eightfold Path is explicitly not worked in sequence, so neither travels. Remove the sequence
and there is no structural reason for the reproduction-driving practice to be the costliest one.
That is a larger difference between the two programs than any count, and the model can name it only
because the order gate is an explicit term.

Two further notes were registered. Affinity meetings read, in the model's vocabulary, as deliberate
management of within-room dispersion, raising `unity` while shrinking the room; the model names the
trade in both directions and cannot score it, having one room of capacity 60. And the uncertified
mentor role enlarges the recipient denominator, which sounds like a finding and is not: the clean
recipient ablation is 1.028 [-0.259, 2.314] and unresolved, so the paragraph ends by telling a
reader to stop at the ablation.

`tools/check_book.py` caught one real defect during the write-up: the referral sentence claimed a
duration without a marker tying it to the runs. The prose was fixed rather than the exemption
widened, which the checker's own comment forbids.

---

## 16 August 2026: defect sweep, A12 restructured to house format, primer follow-up

**The duration-claim defect was swept repository-wide and is isolated.** `tools/check_book.py`
scans only CLAUDE.md, README.md, the appendix, PARAMETERS.md and the plans, so the same class of
error could have been sitting unchecked in the manuscript, the paper, the primer or the tools. The
checker's own regex and exemptions were re-run by hand over all of them. Fifteen candidates
surfaced and every one is legitimate: sourced history about Gough, Dr Bob, Hawkins and the
Washingtonians; model output about accuracy at ten members; the progress log itself, which is the
dated record the rule appeals to; the regex in the checker; and Chapter 23's record of the two
project-history claims already removed for this exact reason. The single real instance was the one
introduced and fixed earlier the same day.

**The gap that sweep exposed was closed rather than noted.** `check_history` now also scans
`HANDOFF.md`, `AGENTS.md`, `AGENT_VERIFY.md` and `BOOK-PLAN.md`. Those four narrate or instruct
about the project's own course, which is exactly where an unverifiable duration claim would live,
and they were not being checked. All four were clean when added, so this closes a hole rather than
papering over a finding. Chapters stay out deliberately: their durations are sourced history or
model output, and the progress log is not the authority for either.

**A12 was restructured to the book's chapter format and made self-contained.** It now ends with
`A12.7 The Machinery`, carrying the four-part block the chapters use: what the comparison says, the
technical version, notes on sources, and references under the canonical status headings. Read in
full, Referenced but not reproduced, Internal, and What was not read all carry content; Cited at a
remove is omitted rather than filled, per the convention.

Two bleeds were removed so the section stands alone. The paragraph about `RecoveryDharma_2023` in
A9 is gone, and threat item 9 was removed from A11 and folded into A12.7 part 1, where it is
labelled as a threat visible only from that section. Within the book, A12 is now referenced from
nowhere but itself. The corpus bookkeeping stays in `research/SOURCES.md`, `README.md`,
`HANDOFF.md`, `AGENT_VERIFY.md` and `CLAUDE.md`, which are repository documentation rather than
book text. **The consequence to be aware of:** the architecture threat is no longer in the
appendix's global threats list, so a reader working through A11 alone will not meet it.

**The primer gained a follow-up section**, "asking the same questions about a different
fellowship", placed before its reference block and written in the primer's plain register. It
carries the chronology point, the count, the absent charter, and the sequence argument, and it says
plainly that none of it changes a figure in the primer and that the model's reach is narrower than
"recovery groups": it is about groups with a numbered sequence and a fixed charter. Recovery Dharma
was added to the primer's Read in full block and its unread parts to What was not read, along with
the unsearched literature on Buddhist and mindfulness-based recovery programs.

**On CI: there is none.** No `.github/workflows`, and no Travis, CircleCI, GitLab, Jenkins,
Makefile or pre-commit configuration anywhere in the repository. The release gate is local and
manual, which is what `AGENT_VERIFY.md` already describes. This is recorded so that a later reader
does not assume a green build exists somewhere.

**Staleness check.** `model/aa_group_model.py` hashes to the canonical
`c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952`. No retired room size, no
1,000-seed rule, and no retuned 45/9 calibration target appears anywhere; the three surviving
occurrences of the retired copyright wording are all descriptions of the retired rule, which is
correct. The primer PDF was rebuilt and produces the same eight TeX warnings as the pre-edit
version, four of them overfull boxes, so the new section introduced none. Book and primer PDFs
rebuilt and the new pages inspected. `check_book.py` 0 failures, `check_chapter.py` on the primer
clear, `check_portability.py` clear, `build_corpus.py --check` 0 problems, `check_release.py`
136 passed and 0 failed.

---

## 16 August 2026: the deep read, a corrected finding, and the schism

**The user asked whether the sangha is the group conscience. It is, and A12 had said otherwise.**
That was the error of the day and it is worth recording plainly. The first pass read Section I and
the meeting format, skipped the fourteen personal stories, and concluded the fellowship had no
Traditions-equivalent object. It was wrong twice over. The meeting script already had every member
affirm trust in the wisdom of the Sangha, which is a group-conscience analogue sitting in a document
that had been read. And the stories, which had not been read, contain the fellowship's founding
history. A12.4 is rewritten and now says the sangha **is** the analogue; what is actually absent is a
written decision procedure, established by mechanical search of the full text rather than by reading
alone, with zero hits for "group conscience", "consensus", "business meeting", "trusted servant",
"quorum", "rotation", "bylaw" and "governance".

**Reading Section II produced the strongest finding this source has, and it went into the book.**
Recovery Dharma is a 2019 schism from Refuge Recovery, an organization built around a single named
founding teacher. The stories are written by people who held office in the predecessor: its
executive director, and a member who ran its retreats and conferences for five years. Her account is
that the community was heavily influenced by inequities among its leaders, and that people were
harmed and a sangha was fractured. The successor's first commitment, recited at every meeting, is
that it is peer-led and follows no one leader or teacher, and the executive director's account of
the founding says the framework was chosen deliberately. That is Traditions 2 and 9 arrived at
independently, eighty-four years after AA, by people with no knowledge of this argument. One story
also records that all the meetings in a region **voted** to switch, which is a group-conscience act
in a fellowship whose literature never describes one.

**Four paragraphs went into Chapter 24 at the user's direction**, after a recommendation and an
explicit decision. Chapter 24 is the chapter that lists what would settle the book's claims and
admits that item five, the measurement bearing most directly on the central claim, has no ethical
method. A case that occurred on its own belongs there. It is framed as corroboration and not
confirmation: one case, testimony rather than measurement, written by participants in their own
founding literature, silent on whether dominance *scales*, which is item five's actual question.
**The individual at the centre of the predecessor's collapse is named in the source and is named
nowhere in this project.** The structural claim does not need it and nothing here can adjudicate an
allegation about a living person. The restriction is recorded in the chapter, the appendix, the
primer and the source metadata.

**A12 gained a stories section and grew to eight subsections.** A12.5 reports what the fourteen
accounts show: arrival is almost entirely exogenous, through a noticeboard flier, the Buddhist
Recovery Network website, a free online book, internet searches, online meetings, a therapist and a
prison chaplain, which inverts the model's endogenous arrival term and is why core inference 6 does
not carry over. Membership overlaps rather than substitutes, which the one-room model cannot
express. Two contributors left Twelve Step fellowships over singleness of purpose and outside
issues, which is the cost side of Traditions 5 and 10 reported by people who paid it. One member
describes the Eightfold Path as kaleidoscopic rather than consecutive, which is the order-gate
argument in a member's own words. One states the affinity-meeting trade the model cannot score. And
a founder describes going from five people doing everything to not knowing half the board, which is
Part Two's scaling problem from the inside.

**All three PDFs were fixed for margins and overflow.** The primer had no geometry at all and was
rendering at LaTeX defaults; it now sets a4paper with 1 inch margins and takes the book's
typography, so the two documents match. Overfull boxes went from twelve to zero in the book, four to
zero in the primer, and one to zero in the paper. The fixes were `tolerance` and `hbadness` at 1500
with `emergencystretch` at 4em, which prefers a slightly loose line to one in the margin;
`tabcolsep` at 4pt; explicit relative column widths on three wide result tables in Chapters 15 and
20, whose long row labels were the cause; and `scriptsize` on the paper's decline table. The
primer's duplicate title, which repeated its YAML title as an H1, was removed, and
`tools/build_book.py` now inserts the appendix heading rather than substituting for that H1.

**One thing could not be done.** The user uploaded the 4th edition of *Alcoholics Anonymous* for the
corpus. As with the Recovery Dharma attachment earlier in the session, the file was not on disk by
the time it was wanted, and a search of the user's home directory found only the 1939 first edition
already in `research/incorporated/BigBook_1939/`. Nothing was catalogued and no claim was drawn from
it. It remains an open request.

**A stale reproduction command was caught by the margin work.** Appendix A10 still told a reader to
build the primer with a hand-typed pandoc line. That line no longer reflects how the primer is
built, and its `text` block was also the one place in the whole book where content sat outside the
type block without TeX reporting an overfull box, because verbatim does not wrap. Both are fixed:
A10 now calls `tools/build_primer.py`, its file table is re-laid to fit, and it states the
zero-overfull requirement. Every page of the book now measures the same 73.4pt right margin.

---

## 17 August 2026: the "4th edition" is the 1939 first edition, and A13

**The file supplied as AA's fourth edition is not it.** Its title page reads "The 4th Edition of
Alcoholics Anonymous" and, directly beneath, "This book contains a complete reprint of the 1st
edition 1939", published by the Alcoholics Anonymous Big Book Study Group and marked "No Copyright
1999". The fourth edition is the reprinter's own printing number. The contents are the 1939 stories,
"The Doctor's Nightmare" through "Ace Full Seven-Eleven", not the 2001 selection. AA's actual fourth
edition has a different set of stories and roughly four hundred more pages and the project still does
not hold it.

**It was also already in the corpus.** The stored `BigBook_1939.pdf` carries the same "The 4th
Edition" title, the same 193 pages, and 99.91 per cent identical extracted text; the two files differ
by a few bytes. So the upload was a second copy of source five, whose row had read "acquired; not yet
used as claim support" since it was catalogued. The naming trap is now recorded in that source's
summary so it does not catch anyone again.

**The request behind it was still answerable, and produced the strongest evidence in the project for
a modelling choice.** The twenty-nine personal stories were read and coded against one thing: the
arrival term of A2.7, which gives member-carried arrival the dominant role over the exogenous
constant. That weighting is one of the 118 registered values and had never been checked against
anything.

The stories support it. Twenty of twenty-seven automatically segmented stories carry explicit
personal-contact language, and that figure is recorded as a lower bound because the phrase matcher
misses accounts phrased differently; its clearest miss is Dr Bob's own arrival, which is described
without any matched phrase. The recurring shape is a visit by a recovered drinker, often several: one
writer records that about twenty men called on him in hospital, another that a doctor sent two of the
members, a third that men came to him one by one.

**The exception is the best evidence of all, because it runs against its authors' interest.** "Lone
Endeavor" is a man reached only by letter and a pre-publication copy of the book. The fellowship
frames it as "our initial effort to help others through the book alone", "the first time we have had
an opportunity of trying to help an alcoholic at long distance", and records that during the silence
that followed it "began to think this book was inadequate without personal contact". A fellowship
publishing a book had every reason to claim the book sufficed. Its own literature says it doubted so.

**Read beside A12.5, the pair bounds the parameter rather than confirming it.** Recovery Dharma's
fourteen accounts arrive through a flier, a website, a free book, internet searches, online meetings,
a therapist and a chaplain, with almost no member-carried arrival. Two fellowships eighty-four years
apart sit at opposite ends of the same term. The arrival weighting is therefore a claim about an
organization and a period, not about mutual-aid groups, and A13.5 says so.

**Written as appendix A13 with the house Machinery block**, and deliberately not put in a chapter:
this is corroboration of a modelling choice, which is appendix work, whereas the Recovery Dharma
schism in A12.4 was evidence bearing on the book's thesis and went into Chapter 24. The primer's
follow-up section gained a plain-language paragraph. `research/SOURCES.md` and the source summary
now record `BigBook_1939` as used rather than merely acquired, which retires the last "not yet used"
line in the corpus.

**The governing limitation is stated in A13.5 and is severe.** The twenty-nine accounts are of people
who recovered, selected for a book meant to persuade. They are the least representative sample
imaginable of everyone the fellowship met, they cannot set a rate, and they say nothing about
retention, dropout or group survival.

**Audit pass, same day.** Two defects in the new material were found by checking it against the
sources rather than against itself.

The census denominator in A13 was wrong. Automatic segmentation recovered twenty-seven segments, but
one of them, "A Vision For You", is Chapter 11 of the basic text and not a story. The correct figure
is twenty of **twenty-six** story segments, not twenty of twenty-seven, and it is corrected in A13.3,
in the Machinery summary and in the technical version. The section now also names all six segments
the matcher failed to match, and identifies two of them as certain false negatives with the reason,
so a reader can judge the size and direction of the error instead of taking a lower bound on trust.

`RecoveryDharma_2023`'s `absence_claim_scope` was stale on two counts: it still asserted the
fellowship had no Traditions-equivalent object, which was the corrected error, and it still described
the personal stories as unread, which they no longer are. It now states the surviving narrow claim,
records that it was tested by mechanical search of the full text rather than by reading alone, and
notes the tension that one story reports meetings voting while the literature describes no decision
procedure anywhere.

Corpus counts were verified against disk rather than against the prose that asserts them: twenty-seven
source directories, seven carrying `"record_only": true`, three without a verification index, matching
the figures in `README.md`, `AGENTS.md`, `AGENT_VERIFY.md`, `HANDOFF.md` and `CLAUDE.md`. Every phrase
quoted in A13 and in the primer's follow-up was re-checked for literal presence in the extracted text.

---

## 17 August 2026: test suite, coverage gate, and continuous integration

The repository had no tests and no CI. It now has both.

**`tests/test_model.py`, 65 tests over the canonical model.** They assert semantics rather than
exercising lines: that `Snorm` rows sum to one, that `beta` is maximal and equal at Steps 1 and 12,
that Step 12 is the sole carrier of recipient opportunity, that the five protective Traditions have
zero governance rows, that the column-normalised `GOVW` makes governance quality exactly one at full
adherence, that `het_sd` moves dispersion and not the mean, that the order gate shuts later Steps
when earlier ones are zero, that zero membership is absorbing under any referral rate, and that
existence, viability and closure are three different estimands. Writing them found two bugs, both in
the tests rather than the model: the external-modifier test asserted that entries which are
themselves zero would be scaled to 0.7, and the crossing-and-recovery test used a configuration that
never crossed. Both are fixed and the second now documents why its configuration was chosen.

**`tests/test_release_invariants.py` pins what CLAUDE.md calls non-negotiable**: the canonical
SHA-256, that CLAUDE.md and the appendix still quote it, room capacity 60, viability threshold 5,
and the 22 + 12 + 49 + 35 = 118 decomposition. A change to any of these now fails the build instead
of being caught by a reader comparing prose against a cache.

**Coverage is 100 per cent of `model/aa_group_model.py`, enforced with `fail_under = 100`.** The
scope is deliberate and is argued in `.coveragerc`: that file is the thing everything rests on, it
is hash-frozen, and it is pure computation. The scripts under `tools/` and the analysis scripts
under `model/` are batch jobs that write hash-linked caches and render PDFs; unit-testing them to
100 per cent would mean running the release designs on every commit or mocking until the tests meant
nothing. They are covered instead by `tests/test_tools_integration.py`, which runs each checker for
real, compiles every script, and asserts that no source document has been committed.

Two lines could not be covered by a test and are handled honestly rather than ignored. The
`__main__` block is exercised through `runpy`. The defensive closure re-check after the arrival draw
is provably unreachable, because the loop breaks on an empty room before arrivals are drawn; since
the model cannot carry a `# pragma: no cover` without changing its digest, the line is excluded by
pattern in `.coveragerc` with the reasoning written out.

**`.github/workflows/ci.yml` defines two jobs.** `checks` runs on every push and pull request across
Python 3.11, 3.12 and 3.13: the suite with its coverage gate, the model-hash assertion, the corpus
drift check, portability, and `check_book`. `release-gate` runs on `main`, installs pandoc and
tectonic, rebuilds the primer and the book, fails if either produces an overfull box, and runs the
fail-closed gate with the slow integration tests enabled.

One design point is worth recording because it would otherwise look like an oversight. The release
gate is behind `NIC_SLOW_TESTS=1` rather than in the fast job, because part of what it checks is
that each PDF is at least as new as its sources. A fresh clone gives every file the same checkout
timestamp and checkout order can leave a source microseconds ahead of its artifact, so the gate has
to run against artifacts that were actually built. The CI job rebuilds them first.

`requirements-dev.txt` records the four dependencies as floors rather than pins: results here are
pinned by the model hash and the caches, not by the toolchain.

### 17 August 2026, later: the first CI run failed, and it failed for a real reason

The workflow added earlier the same day went red on its first execution. The three `checks` jobs
passed on Python 3.11, 3.12 and 3.13. `release-gate` failed at the build step, six seconds in.

The cause was a genuine missing dependency rather than a flaky runner. Both PDF builds ask
fontspec for `TeX Gyre Pagella` by name, which is a fontconfig lookup. On this machine that font
sits in the author's personal per-user font directory, so every local build was quietly satisfied
by a file that is not part of the repository and could not be part of it. A fresh Ubuntu runner
has no such font, and XeTeX stops with an unrecoverable error before it typesets a single line.
The failure was reproduced locally by asking tectonic for a font name that does not exist, which
produces the same abort.

Three things were changed. `release-gate` now installs `fonts-texgyre` and then asserts that
fontconfig can see the family, so the failure mode is one sentence rather than forty lines of
XeTeX transcript. `build_book.py` and `build_primer.py` now print the last forty lines of the
pandoc log on failure instead of only naming the log file: in CI that file is discarded with the
runner, so a bare path left a red build that could not be diagnosed from the run page at all.
And the prerequisite is now written down in `README.md` and `CLAUDE.md`.

The same pass found a stale command. `README.md`'s reproduction block still rebuilt the primer
with a hand-typed `pandoc` call, which is exactly what `tools/build_primer.py` was written on 16
August to replace. That call renders at LaTeX's default article margins and without the
line-breaking settings, so following the README literally would have produced a primer that fails
the one inch margin requirement and pushes long file paths outside the type block. The block now
calls the script, and says why a bare pandoc call is not the release artifact.

The lesson is the one the clean-clone rehearsal was supposed to teach and half taught. That
rehearsal ran the fast checks and caught a home-relative path, but it did not rebuild the PDFs,
so a host-local font dependency survived it.

### 17 August 2026, later still: the overfull box, and what it was

The second CI run got further. The font fix worked, both PDFs built, and the gate then failed
on a single overfull box in the book, 8.2pt too wide, which is about three millimetres of text
sitting outside the type block. The primer was clean.

Finding it took a diagnostic that did not exist. TeX reports the line number of the LaTeX it was
handed, pandoc discards that file after the run, and Ubuntu ships an older pandoc whose template
shifts every line number, so the warning pointed into a file nobody could open and the local line
numbers did not match. The gate now regenerates the intermediate LaTeX with the same pandoc and
quotes the offending line, which identified it immediately: the seven-column scenario table
converted from the paper's LaTeX, first data row.

The cause is worth recording because it is not obvious. Pandoc sizes each `p` column as a
fraction of `linewidth - 2*ncols*tabcolsep`, so column padding is subtracted from the text width
before the columns are measured. A wide table pays that padding seven times over, and the cells
in this one are set maths, which cannot be broken or hyphenated: a cell that does not fit runs
into the margin rather than wrapping. At `tabcolsep` 4pt the row had less than 8pt of slack, and
the Debian packaging of TeX Gyre Pagella is enough wider than the OTFs used here to consume it.

The headroom was measured rather than guessed, by rebuilding with the table width artificially
reduced until a row overflowed: 4pt survives a 7pt reduction, 3pt survives between 14 and 20pt,
2pt survives more than 30pt. The setting is now 3pt, roughly twice what the platform difference
costs, which keeps the tables looking like a book. The measurement is written into the header
comment in `tools/build_book.py` so the next person does not have to redo it.

Note what this says about the earlier `-1pt` shave, which was added for pandoc's column-width
rounding. It was correct and it was not sufficient, because it addressed a rounding error of a
tenth of a point while the binding constraint was two orders of magnitude larger.

### 17 August 2026: the primer entries now state their own assumptions

Every entry in the primer was carrying a result and hiding its inputs. The arithmetic in Part
Four is exact and its inputs are one person's reading, and a reader who saw only the technical
line could easily mistake the precision of the calculation for the precision of the matrices.

Each of the twenty-four entries now carries a third part, **What was assumed**, between the
technical statement and the plain reading. It quotes the actual authored cells for that row, the
step speed and gate exposure where they apply, and says in plain language what would follow if
the choice were wrong. The values were read out of `model/aa_group_model.py` rather than
transcribed, so they are the model's and not a paraphrase.

A fifth standing caution was added because the three kinds of assumption are not equally well
guarded. The magnitudes are tested by jitter and by wholesale replacement. The resource list is
tested by the 64 leave-one-out, merge and drop-two variants. Nothing tests whether a resource
should have been split or a ninth one added, because that needs judgement from outside the
tables, and no computation inside them can supply it.

Several entries got sharper in the writing. Step Four's index-mate zero is a restatement of an
input rather than a finding. Step Ten's widest-margin result comes from the same judgement
appearing in both tables, so it is not independent corroboration. Tradition 4 and 7, and
Tradition 6 and 10, are guaranteed identical figures before any simulation runs. Tradition 8's
unresolved result cannot distinguish a Tradition that does little from one coded as doing
little. Each of those was already implied somewhere in the project and none was stated where a
reader of the primer would meet it.

### 17 August 2026: the overfull box was unbreakable maths, not a tight margin

The `tabcolsep` change reduced the overflow from 8.21pt to 6.82pt and did not remove it, which
was the useful failure. Reducing column padding widens each column by the padding saved times
that column's fraction, and the binding column here is an eighth of the table, so 1pt of padding
bought about a seventh of a point. The lesson is that global width settings barely reach a narrow
column, and chasing this by shrinking every table in the book until the worst row happened to fit
would have been buying margin against a defect rather than removing it.

The defect: pandoc sizes each longtable column as a fraction fixed in the markdown intermediate,
not by what the cells render to, and the paper's seven-column scenario table gives
`$N$ if viable, y10` about an eighth of the width. Set as maths, `$29.40 \pm 1.16$` is one
unbreakable box very near that width. Maths cannot be hyphenated or broken, so a cell that does
not fit runs into the margin instead of wrapping, and whether it fits depends on the font build.

`tools/build_book.py` now writes those cells as text when converting the paper, so the value
keeps its meaning, matches how the book's own chapters already print the same quantities, and
gains ordinary breakpoints around the sign. A tight cell now wraps. `tabcolsep` stays at 3pt,
which is worth having on its own.

Two things were tried and rejected, both recorded because they looked reasonable. Widening the
paper conversion from 90 to 140 columns changes the fractions to match content and made things
worse, three overfull boxes rather than one, because it reallocates width away from other tables.
Shrinking longtables to `\scriptsize` was measured rather than assumed and was not enough: the
binding cell needed about 17 per cent and `\scriptsize` gives 11.

A note on method, since this cost two red builds. The first attempt calibrated headroom by
rebuilding with the table width artificially reduced, and concluded 3pt had 14 to 20pt of slack.
That proxy was wrong, because reducing the whole table's width moves a one-eighth column by an
eighth of that amount. The proxy has to act on the same quantity as the real difference, and here
the real difference was the rendered width of one cell.

### 17 August 2026: continuous integration is green, and what it took

The workflow added earlier in the day passed for the first time. Eleven runs separate the first
red build from the first green one, and the failures were five distinct faults rather than one
fault resisting five attempts. Recording them because the sequence is the useful artefact.

**The font.** Both PDF builds ask fontconfig for TeX Gyre Pagella by name. On this machine it
sits in a per-user font directory, so every local build had been satisfied by a file that is not
in the repository and cannot be. A fresh runner has none, and XeTeX stops before typesetting a
line. The gate now installs `fonts-texgyre` and checks that fontconfig can see the family, so the
failure is one sentence rather than a transcript.

**The overfull box.** One row of the paper's seven-column scenario table sat 6.82pt outside the
type block. It took four wrong diagnoses. Content was ruled out correctly, by three rewrites of
the row that left the deficit identical to five decimal places. Then the deficit was read as twice
the column padding, which fitted two data points and was wrong. Then as an unbreakable 41pt cell,
which fitted two more and was also wrong. The experiment that settled it was one that made things
worse: shaving the table by 14pt moved the overflow by 1.6156pt, which is 0.1154 of 14pt to four
decimals, and 0.1154 is the first column's fraction in the spec the runner's pandoc writes. The
column was named by a failed fix.

The cause is that pandoc's column fractions are not stable across versions. The same table gives
its first column 0.2577 here and 0.1154 there, and "unwelcoming" is wider than the second.
Hyphenation should have absorbed it and could not be relied on: pandoc sets columns
`\raggedright`, which suppresses hyphenation, and TeX will not hyphenate the first word of a
paragraph, which is what a table cell is. The fix writes a soft hyphen into over-long words in
table rows, which pandoc turns into an explicit `\-` that TeX honours regardless of alignment,
patterns or position. It applies only to words of eleven letters or more and only splits a known
suffix with four letters left before it. `ed` was in that list until it produced "hypothesiz-ed".

**The reports.** The gate requires each derived report to be at least as new as every cache it
summarises, and a fresh clone gives every file one timestamp. The job now regenerates them, which
also makes it the documented reproduction sequence rather than a subset of it.

**The paper.** Same rule, same cause: the job rebuilt the book and the primer and not the paper,
so the paper failed the freshness check every time. Tectonic builds it.

**The mirror.** The install step twice hung on the runner's Azure apt mirror, once for ten minutes
before it was killed by hand. The first attempt at robustness made it worse by retrying a slow
operation three times instead of failing fast. Rewriting the sources to the mirror that answers,
with bounded Acquire timeouts and no retry on update, brought the whole job to 1m46s.

The diagnostic work was worth more than any single fix. Printing the deficit in points, then the
resolved source line, then the column spec and the sum of its fractions, is what turned a
typography puzzle into arithmetic. Those diagnostics stay in the workflow. The lesson to carry:
change one thing and read whether the number responds. A constant under a change means the cause
is elsewhere; a constant under the control you are adjusting means the control is not connected.
Both were on display here, and only the first was recognised at the time.

The deprecated Node 20 actions were updated in the same pass.

### 17 August 2026: pandoc is pinned, and that is the durable part

The green build came from removing apt rather than fixing it. The runner's Azure mirror went
unreachable three times, the sources rewrite did not take, and retrying only repeated a slow
failure. Pandoc now comes from its GitHub release as a `.deb` and the TeX Gyre fonts from CTAN.
Neither can be broken by a mirror, and the whole job dropped to about a minute.

The pin matters more than the speed. Pandoc computes the column widths of every table in the book,
and it does not compute them the same way across versions. That single fact produced the overfull
box, four wrong diagnoses, and most of a day: the unpinned runner gave the paper's scenario table
a first column of 0.1154 where 3.10.2 gives 0.2577. CI now installs 3.10.2, which is the version
the book is written against, so the artifacts it renders are the ones an author sees locally.

This is the same discipline the project already applies to results and had not applied to
rendering. The model is hash-frozen and the caches record the hashes they were made with, but the
PDFs were built by whatever pandoc happened to be installed. Raising the pin is now a deliberate
act, and the PDFs should be re-read when it happens.

The soft hyphens stay. They are no longer load-bearing, because CI and local now agree on the
column widths, but they cost nothing and they are what makes a narrow column safe on a machine
whose pandoc is not the pinned one.

Final state: four jobs green, the release gate in about a minute, 136 release checks passing, 100
tests passing on Python 3.11, 3.12 and 3.13, and zero overfull boxes in both rendered documents.

### 17 August 2026: a production-readiness audit, and the five things it found

A full pass over the repository looking for staleness rather than for a failing check. Every
checker was already passing, so this was about claims nothing verifies.

**The primer was dated 6 August and had been rewritten on the 17th.** A date in a source file is
exactly the kind of fact nothing checks and nobody reads. Fixed at the cause rather than the
symptom: the date is removed from the Markdown and `tools/build_primer.py` now stamps it at build
time, as `tools/build_book.py` already did, so the printed date is when the artifact was made.

**`CLAUDE.md` ran the release gate before the three builds.** The gate requires every rendered
artifact to be at least as new as its sources, so the documented order fails on the artifacts it
is about to be given. `README.md` and the CI job both had it right. Corrected, with a sentence
saying why the order is not a matter of taste.

**Two counts in `AGENTS.md` were wrong.** Nineteen analysis scripts, not twenty, and five
checkers rather than seven; the checkers are now named rather than counted. The eighteen caches
were right, and the count is the gate's own required list. Numbers that cannot be checked should
be either checkable or absent.

**Two broken relative links**, in the AAWS P-17 README and the staged-corpus agent note, both
pointing at the wrong directory depth. A sweep of every backtick-quoted file path in every
Markdown file now resolves cleanly, treating a path as valid if it resolves either from the
referring file or from the repository root, and excepting the git-ignored corpus documents, whose
absence is the design.

**The pandoc pin was undocumented outside the workflow.** It governs table geometry, so a builder
using a different pandoc gets different column widths. Now stated in `README.md` and `CLAUDE.md`
where someone reproducing the build will meet it.

One thing deliberately left alone. The progress log refers to `kurtz-1991-verification-index.json`
under its pre-normalisation name. That entry is a dated record of what was true when it was
written, and correcting it would be rewriting a history rather than fixing a fact.

**The PDFs were measured rather than eyeballed.** All three are A4. Ink extents were computed for
every page of all three documents: no content reaches the paper edge, the closest approach is
68pt, and the only breaches of the nominal type block are sub-3pt and are all words ending in a
period, which is `microtype` protruding terminal punctuation on purpose. A line-collision pass
flagged candidates that turned out to be inline mathematics and horizontal rules, confirmed by
rendering the flagged pages. Zero overfull boxes in the book and the primer remains the
authoritative statement, since it is TeX's own.

### 17 August 2026: the appendix named the person the project undertook not to name

Looking for open items found a rule violation instead, and it is the most serious thing this
session turned up.

`appendix/APPENDIX.md` named the founder of the organization Recovery Dharma split from in 2019,
in a paragraph that goes on to quote a contributor describing a community "heavily influenced by
unhealthy masculinity" where "people were harmed". The rule against it is stated twice, in
`CLAUDE.md` and in that source's own `metadata.json`, and the reason is not squeamishness: the
structural claim does not need the name, and this project cannot adjudicate an allegation about a
living person. It had shipped in a rendered PDF.

The sentence now describes him by role. The argument is unchanged, because the argument was never
about who he was: a teacher-centred predecessor fractured, and the successor's constitution
abolishes the office. The point survives the name's removal intact, which is the evidence that it
was never doing any work.

**The rule is now enforced rather than merely written down.** `tools/check_book.py` grew a
`check_withheld_names` pass over the manuscript, appendix, primer, plans, front-matter documents
and the paper. It cannot contain the name, because a checker that stores the string it forbids
publishes it; it stores SHA-256 digests of the lowercased full name and surname and hashes every
word and adjacent word pair it finds. It was regression-tested by reinserting the name across a
line break, which it caught, and it reports clean now.

Removing the name exposed a second thing worth recording. Reflowing the paragraph moved "for five
years" onto a line without a quotation mark, and the duration checker caught it, having previously
skipped that line as a quoted example. The tenure was dropped rather than the checker widened: the
claim being made is that the contributors were officers of the predecessor, and how long one of
them held a post is not part of it. The checker's own comment says do not widen the exemption, and
it was right.

### 17 August 2026: the open-items list was three different lists, none complete

`HANDOFF.md` section 10 listed six items, `AGENTS.md` announced "the one thing still outstanding",
and a summary written in this session named three, two of which were recorded nowhere. Four
accounts of what remains, no two alike.

Section 10 is now the single list, and it says so. It has eight items in two groups, because the
grouping carries the information: one item could change a conclusion, and seven qualify one. Every
item in the second group is blocked on a document the project does not hold, which is stated
plainly so that nobody tries to close one by inference. The two that were missing are AA's actual
fourth edition of 2001, without which Appendix A13's census is a reading of 1939 and not of the
fellowship as it is now, and an independent account of the 2019 schism, everything about which
currently comes from the successor's own literature.

`AGENTS.md` no longer claims one outstanding item and points at section 10 instead, with a line
telling a reader not to trust any shorter list, including its own paragraph.

Nothing was closed by editing. Five of these need a book bought and read.

### 17 August 2026: three items closed by checking whether the publisher gives them away

Five items on the remaining-work list had been described, by me, as needing a copyrighted book
bought and read, and therefore as impossible from here. That was true of two of them. It was never
checked for the other three, and all three are published free and officially.

**SMF-132**, the worldwide group-and-member series, is a free PDF on aa.org. It had sat on the
list since 2 August, first behind a policy that was retired on 10 August and then behind nothing
at all. Read at source on 17 August. It closes the out-of-sample comparison Chapter 21 proposed:
reported members divided by reported groups gives 18.4 per group on average across 2001 to 2020,
falling from 22.1 to 16.5 over that period, against a modelled endpoint membership at full
adherence of 17.80 [16.92, 18.68]. The model was not fitted to it. Room capacity, arrival and
dropout were set long before the table was read.

**That is recorded as a consistency check and not a validation, and the source is the reason.**
AA keeps no membership lists; these are reports from groups registered with general service
offices. A ratio of two estimated aggregates is not a sample of group sizes, carries no interval,
and describes no distribution, which is certainly skewed. The model produces a distribution and
the table produces a point. They agree at the point. The chapter now says so in a sentence and
keeps its two older limitations, that the series is worldwide rather than regional and that a
count of groups is not a count of group deaths.

**The Twelve Concepts for World Service** are also free on aa.org, in short form. They had been
listed as unread and as the place where the fellowship's own thinking about rotation is set out at
greatest length, with a note that the last AA text left unread on copyright grounds turned out to
contain the strongest objection to this book's argument. Read on 17 August. The finding is a
narrowing rather than a reversal, and it is more interesting than the claim it replaces.

Concept 4, the Right of Participation, asks for voting representation in reasonable proportion to
the responsibility each element of the structure discharges. So AA does hold a proportionality
principle about service, explicitly, and Chapter 10 had assumed it held none. But it proportions a
different pair: voting weight to responsibility, where the model's result concerns the size of the
rotating pool relative to the size of the group. A structure could satisfy Concept 4 exactly and
still rotate twelve people through a fellowship of eight hundred, which is the configuration
Chapter 10 shows to be a permanent oligarchy. The claim is now that AA has the instinct for
proportion and applies it to representation rather than to the pool.

**An independent account of the 2019 Recovery Dharma schism** exists, in *Tricycle*, 13 July 2019.
Appendix A12.4 had rested entirely on the successor fellowship's own literature, written by people
who left, which is the weakest evidential position available for a claim about why a schism
happened. The independent account confirms the structure from outside and corrects the contrast.
Both organizations describe their meetings as peer-led and democratically run, and the
predecessor's own book did so before the split, so the difference was never that one had peer-led
meetings. What separates them is the layer above the meeting: teacher-led retreats and a
professional treatment option on one side, nothing above the sangha on the other.

That correction improves the fit rather than damaging it. The model has no representation of a
meeting's internal democracy, which both fellowships share. It has a governance layer that can be
concentrated or diffuse, and the split is precisely about whether such a layer exists at all.

All three are held as **record only**, which brings the corpus to 30 sources, ten of them record
only and six of those without a verification index. Nothing was downloaded into the repository.
The rule stands: read what is lawfully readable, hold nothing, record the provenance.

The general lesson is not about AA literature. Three items sat on a list as impossible because
nobody asked whether the publisher gives them away, and the cost of asking was one search each.

### 17 August 2026: the Rohr objection is closed, and it never needed a purchase

I listed this as needing a copyrighted book bought or borrowed. That was wrong twice over, and the
Human Author said so: he owns the book.

The objection was never about acquisition. `Rohr_2011` was catalogued on 10 August with the
strongest provenance problem in the corpus, that the copy read bore an OceanofPDF.com imprint and
was therefore an unauthorized posting of a current in-print title. What that puts in doubt is the
project's *access*, not the accuracy of the reading, and a lawfully obtained copy on the author's
shelf settles it. The record now says so, in `CLAUDE.md`, `research/SOURCES.md`, the source's own
`metadata.json` and `HANDOFF.md` section 10.

Two things are worth stating precisely rather than waving through.

What changed is that the work is lawfully to hand and re-checkable at will. Nobody has re-read it
against the owned copy, and the two claims stand as they were read on 10 August. That is the
ordinary footing of every other source here and is not a weakness peculiar to this one.

The edition difference is immaterial, and it is worth recording why rather than asserting it. The
citation prints the 2011 Franciscan Media first edition; the copy consulted was the 2016 SPCK
printing. A grep for page citations to Rohr across the manuscript, the appendix and the paper
returns none: every use is a year cite attached to an unquantified statement about how the book
reads its subject, which is the weakest use the four-layer rule allows. Pagination therefore
reaches nothing the book says.

The pattern from earlier in the day repeated. Three items sat on the remaining-work list as
impossible because nobody checked whether the publisher gives them away. This one sat there
because nobody asked the author whether he owned the book.

### 17 August 2026: the fourth edition arrives, and the arrival census is repeated

The Human Author owns several copies of the 2001 fourth edition and supplied the text; AAWS also
posts the book in per-section PDFs. That closes the last of the acquisition items, and it closes it
the same way the previous four closed, which is to say that the obstacle was never checked.

Appendix A13 previously read the twenty-six story segments of the 1939 first edition and found
explicit personal-contact language in twenty of them. A13.7 now repeats that on all forty-two
stories of the fourth edition.

**The coding rule had to be extended, and the extension is the finding.** A13.2 asks whether a
recovered alcoholic made contact before the subject stopped drinking. In 1939 that has two answers,
because someone who wanted to find the fellowship had almost no way to: it was small, unadvertised
and in no directory. By 2001 there are three, and the middle one is new. Thirteen stories describe
a member seeking the subject out, six a subject going looking and finding the fellowship, eleven a
professional or an institution referring. Twelve do not state the channel plainly and are reported
as unresolved rather than assigned, on the principle the release gate applies to an interval
crossing zero.

Member-initiated arrival is 43 per cent of the thirty classifiable stories, against 77 per cent in
1939.

**What it supports.** The model's arrival term has an exogenous part and a member-carried part, and
the code comment on `lam_exog` names courts, treatment and desperation. In 1939 that term had
almost nothing to point at. The fourth edition supplies a judge sending a man to A.A. for a month,
a college making attendance a condition of readmission, counsellors producing meeting lists, and
repeated arrival through treatment centres.

**What it bounds, and this is the more useful half.** `lam_exog` is fixed at 0.12 per week in every
run. The two censuses together say that a fellowship's exogenous arrival rate grows with its own
institutional presence, which the model cannot represent at all. That is now stated in the appendix
as a limitation rather than left as a detail.

**What neither census is.** A sample. The stories are selected by the fellowship for publication
and selection on outcome is total: every subject recovered. The comparison is between two edited
collections sixty-two years apart, not a time series, and estimates nothing about any population.

The corpus is 31 sources, eleven record only, seven without a verification index. Nothing was
copied into the repository.

### 18 August 2026: continuous integration split by what a network can break

Eleven of the last twenty runs failed and every failure was in one job. The fast job has never
failed for an environmental reason; the release-gate job failed on a hung apt mirror, a CTAN
mirror timing out, a certificate that would not verify, and four separate cold-cache fetches
inside tectonic.

The diagnosis was in the numbers rather than the logs. Of the 136 release-gate checks, **seven**
concern rendered artifacts. The other 129 are cache existence and completeness, model and script
hash currency, the registered design counts, and the model invariants, and not one of them needs a
TeX toolchain. They were sitting behind pandoc, tectonic and a font download, so a CTAN timeout
meant the checks that actually catch a stale cache did not run at all. That is backwards, and it
was the real defect rather than any individual flake.

`check_release.py` now takes `--skip-artifacts`, which omits those seven and nothing else. The
fast job runs the remaining 131 on every push and pull request across three Python versions, with
no network beyond pip. The renamed `documents` job builds the three PDFs, asserts zero overfull
boxes and runs the full gate, on `main` and on demand.

Calling that a weakened checker would be the wrong reading, and the flag's comment argues the
case. In a fresh clone every file carries one checkout timestamp, so "artifact newer than its
source" can only be satisfied by building the artifact and then asserting the thing just built is
newer than its input. That is circular and says nothing about the PDFs committed. A release still
runs the full gate with the artifacts built, which is where those seven mean something.

Three stability changes came with it. The tectonic bundle and the font directory are now cached
between runs, which removes the cold-fetch failure mode rather than retrying through it. Both
caches live inside the workspace rather than under the runner's home directory, because
`check_portability.py` flags a home-relative path in any tracked file and does not exempt CI; it
caught the first attempt immediately. And the diagnostic scaffolding built while chasing the
overfull box, the resolved-source-line dump and the column-spec probe, is gone: pandoc is pinned
now, so the geometry that produced it cannot drift.

The file went from 280 lines to 219, and the useful checks went from running sometimes to running
on every push.

### 18 August 2026: continuous integration is runnable here

Both jobs were verified step by step on this machine, and the verification is now a script,
`tools/run_ci_locally.sh`, because doing it by hand took a dozen commands and nobody repeats
that. It mirrors the workflow's two jobs in order, takes an optional `checks` or `documents`
argument, and reports a pass and fail count. Twelve steps, none failing.

Two things about it are worth stating rather than assuming.

It is a convenience and not an authority. The workflow file is the authority, nothing enforces
that the two agree, and they will drift unless changed together. The script says so at the top.

And it cannot check the thing that has actually broken this repository's CI. Every environmental
failure came from obtaining pandoc, tectonic or the font on a fresh runner, and the script
deliberately uses the toolchain already installed here, because reinstalling it would be slower
and less faithful to what the author builds with. A green local run is evidence about the
repository, not about the runner.

One incidental finding. Re-running the builds produces three modified PDFs and a modified
`model-choice-inventory.json` every time, and all four are timestamp churn: the extracted text of
all three PDFs is byte-identical to the committed versions, and the JSON differs only in
`created_utc`. Those were reverted rather than committed. Worth knowing before someone reads a
four-file diff as a content change.

### 18 August 2026: a staleness pass after the CI rewrite, and the two things it found

A sweep for claims that had stopped being true, rather than for a failing check. Everything was
already green, which is the condition under which this kind of drift survives.

**A job name I changed myself.** The CI rewrite renamed `release-gate` to `documents`, and
`CLAUDE.md` still said `release-gate` checks for the font. One line, and exactly the sort of
reference that is wrong for months because nothing reads it. The same line has been widened to
say where CI actually gets the font, from CTAN mirrors with a cache, since `fonts-texgyre` is
the Debian route and not what the workflow does.

**A propagation gap in the verification document.** `tools/run_ci_locally.sh` was documented in
`README.md`, `CLAUDE.md` and `AGENTS.md` and not in `AGENT_VERIFY.md`, which the synchronisation
rule lists as a layer of its own. It is there now, together with the point a verifier most needs:
that verifying a release means running `check_release.py` with the artifacts built, never with
`--skip-artifacts`, because that flag omits precisely the seven checks a release cares about.

Everything else checked out against the tree rather than against itself. 31 corpus sources, 11 of
them record only and 7 of those without a verification index; 18 required caches, taken from the
gate's own list; 19 analysis scripts; 25 numbered chapters; 131 and 136 checks in the two modes.
No retired phrase survives outside the rules that forbid it, the withheld name appears nowhere,
and every backtick-quoted file path in every Markdown file resolves.

### 18 August 2026: branch flow, lint, and checks on what the PDFs actually are

Three changes, and the lint one had a trap in it worth recording.

**Branch and pull request flow.** Work now happens on a branch and merges through a pull
request; `main` takes no direct commits. `lint` and `checks` run on pull requests and
`documents` does not, because it renders PDFs and needs a network, so a green pull request is
not a green release. `tools/run_ci_locally.sh` runs all three and is what closes that gap.

**Lint, and the file it must not touch.** `ruff` with a deliberately narrow ruleset: syntax
errors, pyflakes, bugbear. The wider style rules were measured before being rejected rather
than rejected on taste. Clearing them would mean reformatting 373 long lines and 19 import
blocks, much of it in files whose bytes are load-bearing.

That is the trap. Nineteen analysis scripts under `model/` record their SHA-256 in the caches
they produced, and `check_release.py` fails if a script hash stops matching its cache.
Removing an unused import from one of them would invalidate a cache that took hours to
compute, to silence a warning about a line that does nothing. **A linter pointed at a
hash-pinned file is a hazard rather than a safety net.** They carry waivers by rule, not
wholesale, so a genuine defect in them still fails.

`model/aa_group_model.py` was the interesting case: it passes the full ruleset clean, with no
waiver needed. CI now asserts that with `--isolated`, which ignores `ruff.toml` entirely, so
the waivers written for its neighbours cannot reach the one file that is the release identity.

Four real defects were fixed in code that is free to change. Three `zip()` calls without an
explicit `strict=`, which is silent truncation waiting to happen in a checker: two compare a
slice against a term of the same length and are now `strict=True`, which turns a slicing
mistake into an exception; the third is the bigram idiom in `check_withheld_names`, where the
iterables are deliberately ragged and `strict=False` says so. And one exception raised inside
an `except` without chaining.

**A checker for what the PDFs are, not what the log said.** `tools/check_pdfs.py`: each
document parses, has a plausible page count, is A4, embeds every font, yields extractable
text, and keeps its ink clear of the paper edge. The overfull gate reads what TeX chose to
warn about; this reads the rendered result. It was negative-tested rather than trusted, by
truncating a PDF and by substituting a valid one-page document, and it caught both.

One deliberate choice in it. The ink bound is the paper edge, not the type block, because
microtype sets terminal punctuation a point or two into the margin on purpose and a
type-block bound would fail on correct typesetting. Measured, the closest any ink comes to
the paper edge across all three documents is 68pt.

The workflow is linted too, by actionlint, which also runs shellcheck over every `run:` block.

**The first pull request caught something on the first run.** shellcheck flagged
`cd "$(dirname "$0")/.."` in the local runner with no failure branch. If that `cd` ever
failed, the script would run every check against whatever directory it happened to be in and
report the result as this repository's. That is a worse outcome than not running at all, and
it was in the script whose entire purpose is to tell you whether a push will go red.

It also exposed a gap in the runner itself: it looked for `shellcheck` only on `PATH`, so it
skipped the check locally while CI ran it. `shellcheck-py` is now a dev dependency, which
bundles the binary, and the runner looks in `.venv/bin` first, as it already did for ruff.
Local and CI now run the same three linters.

Note which job caught it. `documents` was correctly skipped on the pull request, so the
design worked as intended on its first outing: the fast jobs gate the branch, and the
rendering job waits for `main`.

### 18 August 2026: the PDF checker had an undeclared system dependency

The pull request merged green and `main` went red on the next run, which is the gap the
branch flow documents: `documents` does not run on pull requests, so a green pull request is
not a green release. It failed on the checker added in that very pull request.

`tools/check_pdfs.py` shelled out to poppler for `pdfinfo`, `pdffonts` and `pdftotext`. Those
are on this machine and not on the runner, so it passed here and failed there with
`pdfinfo not found`. **A checker with an undeclared system dependency is a checker that does
not run**, and I had shipped one while writing about how the local runner cannot check
whether a fresh runner can obtain its toolchain.

It is rewritten on pypdf, a pip dependency needing nothing from the system: parse, page
count, page size, font embedding and text extraction all work without a binary. Reinstalling
apt for one package was the alternative and was rejected; apt is what hung three times, and
removing it is most of why the job is stable now.

One check could not follow. The ink measurement needs poppler's `pdftotext -bbox`, because
pypdf's text transformation matrices are not accurate enough for it: on a correct page they
report a left edge at -0.3pt, which would fail a bound the typesetting has not breached. It
now runs where poppler exists and reports itself skipped where it does not. That is the
weakest of the six, since the overfull gate already catches text leaving the type block from
TeX's side.

**And the skip is counted separately from the passes.** The first version appended the skip
line to the notes list, so three checks that had not run were reported as three that had
passed. A check that did not run is not a check that succeeded, and counting it as one is how
a checker comes to mean nothing.

The negative tests were re-run against the rewrite rather than assumed to still hold: a
truncated file, and a valid one-page document substituted for the primer. Both are caught.

### 18 August 2026: a branch, tag and release structure, built around the model hash

The repository had no tags, no releases and no changelog. What it did have was an identity
already: the SHA-256 of `model/aa_group_model.py`, which every cache records and the gate
checks. The scheme is built on that rather than imported from a library project, because
nobody depends on an API here and what a version has to describe is the state of an argument.

**`RELEASING.md`** is the authority. Branch prefixes, `model/` being the serious one because
it changes the release identity and invalidates every cache keyed to it. Semantic versioning
mapped to what can actually change: MAJOR is a changed model hash or a reversed conclusion,
MINOR is new evidence or analysis, PATCH is corrections and tooling.

**It stays below 1.0 while the elicitation round is open**, and the reason is stated rather
than implied: Part Four rests on a matrix one person wrote down, no computation can test its
pattern of empty cells because every check holds that pattern fixed, and until a second reader
marks those cells the central claim has not been checked by anyone but its author. 1.0 means
that item is closed, not that the prose is finished.

**A tag has to be earned**, and the six conditions are listed. The one worth repeating is that
a release runs `check_release.py` with no `--skip-artifacts`: those seven artifact checks are
the entire point of a release, and the flag exists for a fresh clone.

**`.github/workflows/release.yml`** runs on a version tag and re-runs the full gate against the
tagged tree. It cannot make a bad tag good and does not pretend to; what it does is record
publicly whether the claim held. It also rejects a lightweight tag, and rejects an annotated
one whose message does not contain the model SHA-256 in the tree. A tag that does not say
which model produced it is close to useless here, since every number downstream is keyed to
that hash.

**`CHANGELOG.md`** records what changed between tags with the model hash for each, so that
somebody who wants the difference between two versions does not have to read a progress log
that is now several thousand lines.

A GitHub Release is treated as a publication rather than a mark in the history, and the rule
written down for agents is not to publish one unless asked. The repository is public.

`tools/check_book.py` now scans `CHANGELOG.md` and `RELEASING.md` for unsupportable duration
claims about the project. A changelog is the most likely place for the next one to appear.
Both were clean when added.

### 18 August 2026: the release workflow failed on the first tag, and the tag was fine

`v0.9.0` was pushed after verifying all six conditions in `RELEASING.md`, and the release
workflow rejected it: the tag message did not contain the model SHA-256. The message does
contain it. The check was broken, not the tag.

`actions/checkout` does a shallow fetch by default. That gives the commit and a ref, but not
the annotated tag object, so `git for-each-ref --format='%(contents)'` returns nothing useful
and a correct tag fails. The fix is `fetch-depth: 0` with `fetch-tags: true`, and the logic was
reproduced locally against the real tag before pushing rather than guessed at again.

Two things were wrong beyond the fetch depth, and both mattered more than the depth did.

The lightweight-tag branch could not fire. It tested for an empty message, but an unfetched
annotated tag also yields an empty message, so a genuine lightweight tag and a fetch problem
produced the same error. It now asks `git cat-file -t` what the object actually is, which
distinguishes them.

And the failure said only that the message did not contain the hash, without showing the
message. A check that reports a mismatch should show what it compared; this one sent me to
read a tag I had written twenty minutes earlier. It now prints the message.

The tag itself is being deleted and re-applied rather than left in place with a red
verification against it. Nothing depends on it, it is minutes old, and a tag whose recorded
verification failed is worse than no tag: `RELEASING.md` says a tag is a claim, and a claim
with a failed check attached invites exactly the wrong inference, that the tree was bad.

### 18 August 2026: the tag check, second attempt, and why the first fix was not enough

`fetch-depth: 0` with `fetch-tags: true` did not put the annotated tag object on the runner.
The improved diagnostic is what showed it: the second run reported `v0.9.0 is a lightweight
tag`, which is false locally and was the useful sentence, because the first version would have
reported the same unhelpful mismatch twice.

The step now fetches the tag by ref itself, `refs/tags/NAME:refs/tags/NAME`, so the annotated
object is present whatever the checkout action did or did not do. Depending on a third party's
default for something a check is built on was the mistake, and it took two runs to see it.

It also stops using `git rev-parse` to identify the object. `rev-parse` peels an annotated tag
to the commit it points at, so `cat-file -t` on its output answers a different question from
the one being asked. `for-each-ref --format='%(objecttype)'` reports what the ref points at
without peeling, which is the distinction the check exists to make.

Tested both ways locally against a deliberately constructed lightweight tag, rather than
assumed. That test also showed why the original empty-message branch could never have worked:
`%(contents)` on a lightweight tag returns the commit message, not an empty string, so a
lightweight tag would have sailed past a check looking for emptiness and failed later with the
wrong reason.

### 23 August 2026: the release itself, published and verified

`v0.9.0` was published as a GitHub Release, marked pre-release because the repository stays
below 1.0 while the elicitation round is open. The three rendered PDFs were attached, then
downloaded back and hashed against the files at the tagged commit: all three matched, so what a
reader gets from the release page is provably what the tag verified, not a second copy that
only looked right at upload time.

`gh release list` was checked empty before publishing, closing the one open question left from
the tag work: whether an earlier attempt had left a partial release behind. It had not.

### 24 August 2026: a staleness pass and the release recorded in prose, not just in git

Nothing here was stale. Reran the full check surface: `pytest`, `check_release.py
--skip-artifacts` (131/131; the seven artifact checks only run against a tagged tree, and
passed there at tag time), `check_book.py`, `check_chapter.py` on the primer,
`check_portability.py`, `build_corpus.py --check`, and `elicitation_compare.py --self-test`.
All clear. `git fetch --prune`, `gh pr list`, and `gh release list` confirmed no stray branches,
every pull request merged, and exactly one release matching the one tag.

What was missing was not code but record: `README.md`, `RELEASING.md`, `CHANGELOG.md`,
`AGENTS.md`, and `AGENT_VERIFY.md` all described the release *process* without saying a release
had actually happened. Each now states that `v0.9.0` is tagged and published, with the date and
a link, without loosening the standing rule that the next one still needs the Human Author to
ask for it. `HANDOFF.md`'s header date and verification table were refreshed to today rather
than left reading 16 and 10 August.


### 24 August 2026: a sweep of all 121 tracked Markdown files, and what a release left behind

Read every tracked `.md` file outside `build/` against the tree rather than against itself.
Mechanical checks first: every 64-hex string against the canonical hash, every relative
Markdown link resolved from its own directory (121 files, zero broken), every backticked path
resolved, and every stated count re-derived from the repository.

Nothing scientific was stale. What was stale was the record of the three changes made between
18 and 23 August, none of which had been propagated the way the synchronisation rule requires.

**The `lint` job.** Added 18 August, and six sentences still said continuous integration had two
jobs: `README.md`, `CLAUDE.md`, `AGENTS.md` twice, `AGENT_VERIFY.md`, and the header comment of
`tools/run_ci_locally.sh`, which documented a `checks` or `documents` argument while the script
had supported `lint` since the day it was written. `RELEASING.md` and `CHANGELOG.md` had it
right, which is how the contradiction was visible at all.

**`check_pdfs.py`.** Added 18 August and named in `RELEASING.md`'s release conditions, but absent
from the reproduction sequences in `README.md`, `CLAUDE.md` and `HANDOFF.md`, and absent from
`AGENTS.md`'s inventory, which said five checkers and listed five while the tree held six. That
inventory claims to be countable from the tree, so it was wrong on its own terms.

**`BigBook_2001`.** Read 17 August, record-only, and the thirty-first source. `CLAUDE.md`'s
corpus narrative stopped at thirty and never named it; `README.md`'s record-only paragraph said
eleven and enumerated seven; `AGENT_VERIFY.md` enumerated the corpus twice and omitted all four
of the 17 August additions from both lists. The totals were right everywhere and the
enumerations were short, which is the failure mode that reads as correct.

Three more, found by re-deriving rather than by reading. `HANDOFF.md` gave the built PDFs as 270,
34 and 18 pages against an actual 296, 34 and 23, and credited `model/` with 20 analysis scripts
when it holds the frozen model plus 19. `BOOK-PLAN.md` still called the book a 260-page PDF.

`HANDOFF.md`'s reproduction block told the reader to build the primer with a bare `pandoc`
command, which `README.md` explicitly says is not the release artifact, because it renders at
LaTeX's default article margins instead of the one inch `build_primer.py` holds. The two files
had disagreed since `build_primer.py` was introduced. `HANDOFF.md` now calls the script.

Two items were not stale so much as unverifiable. `research/SOURCES.md` asserted thirteen active
text files, a count of git-ignored local working files that no fresh clone can check and that had
grown to twenty. It now derives from the corpus instead: the twenty sources holding a document
carry one text file each, the eleven record-only entries carry none, and a clone with none of
them is not drift. And `research/GOVERNANCE-MATRIX-ELICITATION.md`, the working source for the
elicitation form, carries the collator's section inline, so sending that file would spoil the
round exactly as sending `4-collator-notes.pdf` would. It now says so in a banner at the top and
points at `1-respondent-form.pdf`.

`research/staged/agent/SOURCE_INCORPORATION_AGENT.md` still gave a by-hand recipe for adding a
source, which the current rule forbids; it now points at `tools/build_corpus.py`. `CITATION.cff`
had no `version` and a `date-released` of 16 August, predating the tag, so anyone citing the
published release would have cited it as undated and unversioned. It now carries 0.9.0,
23 August, and the repository URL.

The pattern worth keeping: every one of these was a *count or an enumeration* that a tool could
have re-derived, sitting in prose no checker reads. The checkers verify numbers that come from
caches. Nothing verifies a sentence that says how many jobs CI has.

### 24 August 2026: a checker for the sentences, because nothing was reading them

The sweep earlier today found eleven stale claims and every one was a count. Not a number from
a cache, which the gate already guards, but a sentence saying how many jobs continuous
integration has, how many checkers the tree holds, how many sources the corpus contains. The
gate never looked at any of them, so they drifted for five days without anything noticing.

`tools/check_docs.py` closes that. It derives each value from the tree and then scans tracked
Markdown for claims that contradict it: CI job names and count from the workflow, checkers from
`tools/check_*.py`, corpus size and record-only status from the `metadata.json` files, analysis
scripts from `model/`, chapters from `manuscript/`, every relative link, every digest labelled
as the model hash, and the three rendered page counts.

Three design decisions worth keeping.

**It refuses to flag history.** `research/progress-log.md` is excluded outright and blockquoted
lines are skipped everywhere else, because a retired claim kept in a blockquote is how this
project records what it used to believe. `CLAUDE.md` narrates the corpus growing through 26 and
27 on its way to 31, and all three numbers are correct; only present-tense phrasing is checked.
A checker that fails on a correct historical statement teaches people to ignore it.

**The label decides, not the neighbourhood.** The first version flagged two digests as wrong
model hashes. Both were correct: one an analysis-script hash in a generated report, one the
SHA-256 of the P-17 PDF. The repository is full of legitimate non-canonical digests, so the test
is now what the digest's own label calls it, read from the text before it on its line or from
the nearest preceding line when it stands alone.

**Page counts skip rather than pass when the PDFs are absent.** That is what lets the same file
run in the network-free job and in `documents`, and it follows `check_pdfs.py`, which already
counts a skip apart from a pass on the principle that a check which did not run is not a check
that succeeded.

Tested by breaking things rather than by trusting green output: the job count regressed to two,
the corpus to 30, a page count to 270, a link pointed at nothing, a job was renamed in the
workflow while prose still named it, and the book PDF was moved aside. Six deliberate defects,
six catches with file and line, and the skip path confirmed.

It caught itself immediately. Adding it made the checker count seven while `AGENTS.md` said six,
under a sentence promising the count was countable from the tree. That is the entire point, and
it is now the seventh condition in `RELEASING.md`, wired into both CI jobs, the local runner, and
`tests/test_tools_integration.py`.

What it does not do is judge prose. It checks arithmetic about the repository, which is the part
a machine can own. Whether a paragraph still means what it says is still a reading job.

### 30 August 2026: split unit-tests from checkers in continuous integration

The `checks` job ran pytest and every version-independent checker three times, once per Python
version, which tripled the runner minutes without adding coverage. The workflow now has four jobs:
`lint`, `unit-tests`, `checkers`, and `documents`. `unit-tests` keeps the matrix; pull requests
use 3.12 only and `main` still runs 3.11, 3.12 and 3.13. `checkers` runs once on 3.12. The lint
job uses `shellcheck-py` from pip instead of an apt package. `tools/run_ci_locally.sh` gained
`unit-tests` and `checkers` arguments; `checks` remains an alias for both.

### 12 September 2026: the 1939 working manuscript, read on every page

The Human Author supplied 241 photographs of Hazelden's *The Book That Started It All* (2010), the
colour facsimile of the multilith copy onto which the comments on the February 1939 draft of the
Big Book were collated, and asked for a cleaned PDF, a reading, a corpus entry, and a summary with
suggested uses for the manuscript.

**Processing.** The frames came in four orientations, with shadow fall-off and some faint
impressions. Each was straightened by running a fast OCR pass at every rotation and keeping the one
that returned the most common English words; a plain letter count had picked upside-down pages.
Each was flattened by dividing it by a text-free estimate of its own illumination, given a black
point where the print was faint, and OCRed with Apple's Vision framework. Three frames needed their
orientation forced by hand. The reading copy keeps colour on the 168 facsimile pages, because the
annotations are told apart by pencil colour, and drops it on the typeset ones; an invisible text
layer makes it searchable. Book pages 22 and 23 were not photographed.

**Holding.** It is in copyright and in print, which in this corpus has so far meant record only.
The Human Author asked for the PDF in the corpus as well as in their Downloads folder, so it is held
on the ordinary footing, git-ignored with a hash and an index. The departure is written into its
`metadata.json`, into a named rights entry in `tools/build_corpus.py`, and into `CLAUDE.md`, so that
it reads as a decision and not as drift.

**Method.** Every facsimile page was read as an image rather than from the OCR, and every change
that mattered was checked against `BigBook_1939`. Two limits of that baseline surfaced: it carries
one bracketed editorial note quoting the multilith, and it omits the 1939 appendix on the Alcoholic
Foundation, so the manuscript's Foundation page cannot be compared with print from the corpus.

**What it found**, set out with page references in `edits_and_suggested_uses.md`:

- Step 3's "as we understood Him" is typed in the circulated draft; Step 11's is written in by hand
  over a struck "a Power above us"; and the "choose your own conception of God" episode in Bill's
  Story is a handwritten insert on two loose leaves that the draft did not contain.
- Instruction to "you" becomes a report of what "we" did on nearly every programme page, and
  selling, kneeling and the throw-the-book-away ultimatum go with it. The readers' own word for what
  they objected to was moulds, borrowed from a story typed in the same draft.
- "Group" comes out wherever the text speaks as a body, partly to shed the Oxford Group, and at the
  galleys a "rule" became a "principle"; "the Fellowship" became "Fellowships" in each city and hamlet.
- The Foreword already held public anonymity, no organization, no fees and a single requirement,
  beside a proposed trust with a permanent outside majority whose approval every business engagement
  needed.
- Ten of the thirty printed stories were added after the draft circulated; the one story struck with
  a withdrawal note was printed anyway, at the very end.
- Members' own meeting sizes for early 1939 run from thirty to eighty: a consistency check on the
  model's room of sixty, not a validation.

**What it corrects.** Chapter 4 says the comment round softened "you must" to "we ought". The pages
show the person changing, not the modal: "You must take the lead" became "we found we had to" in
pencil and "We must take the lead" in print, and no "you must" becomes "we ought" anywhere. The
chapter is not changed here, because it is the author's text; the correction is item 5 in
`HANDOFF.md` section 10. Item 6 is Appendix A13's count of twenty-nine 1939 stories, where the
contents page of `BigBook_1939` lists thirty titles.

**A stale sentence found on the way.** `AGENTS.md` still said five items qualified a conclusion,
three of them needing a copyrighted book, when section 10 had listed one book and two loose ends
since 17 August. `check_docs.py` could not catch it, because the number describes another file's
list. The sentence now points at the list instead of restating its size.

**Ownership.** The Human Author confirmed the same day that the copy photographed is their own, and
the rights note says so, as `BigBook_2001`'s does. Book pages 22 and 23 are to follow.

**What did not change.** No model value, cache, notebook, rendered PDF or release check.

### 13 September 2026: the working-manuscript note, typeset and committed

The Human Author asked for a formatted PDF of `edits_and_suggested_uses.md`, and for the note,
that PDF and the reading copy to be saved in the repository with the reading copy git-ignored.

**The reading copy** needed nothing. The copy in the Downloads folder is byte-identical to
`WorkingManuscript_1939.pdf`, whose SHA-256 matches `metadata.json`, and the corpus rule in
`.gitignore` already ignores it.

**The note.** The Downloads copy had been edited that morning and differed from the committed
one in a single clause: the opening paragraph no longer says who photographed the book or on
which days. The committed copy now matches it. The provenance is unchanged in `metadata.json`.

**The PDF** cannot sit beside the note. Every PDF under `research/incorporated/` is a source
document by rule, `test_no_source_document_is_tracked_by_git` fails if one is tracked, and
`build_corpus.py` would take a second PDF in that directory for the source. It is committed as
`build/WorkingManuscript_1939-edits-and-suggested-uses.pdf` and built by a new
`tools/build_note.py`, with the primer's typography, so that it is not the product of a pandoc
command that lives nowhere. It is a reading copy and not a release artifact; the release gate
does not check it.

**What did not change.** No model value, cache, notebook, release artifact or release check.

### 13 September 2026: a lawful copy of every source the corpus can hold

The Human Author asked for the full corpus: copies of every source, including the eleven held as
record only, and a search for everything still missing. Record only had been a deliberate choice,
a stronger condition than git-ignored, and the change is theirs. What it does not change is the
rule that matters for a public repository: no document is committed.

**What was already on disk.** A search of the Human Author's machine by recorded SHA-256 and by
Spotlight found two of the August copies. The official P-17 PDF sat, byte-identical, in two older
non-Git copies of the project, left from the August corpus build. The Kurtz talk transcript read in
August is the Human Author's own transcription of the audiobook and sat in their documents. The
Rohr PDF read in August was also there; it is the unauthorized posting the record already flags,
and it was not copied in. Nothing else was found.

**What was fetched, with approval, and verified.** Sixty-four files from aa.org and AAWS's own file
host. P-17, SMF-132 and the short-form Concepts match, byte for byte, the digests recorded in
August. The *Twelve Steps and Twelve Traditions* was reassembled from aa.org's twenty-nine chapter
PDFs, which the old metadata miscounted as thirty; it comes to 187 pages, as before, and its
vocabulary overlaps the August index at 0.82, the gap being the different text extractor. The
2001 Big Book was assembled from thirty-one section PDFs. The chapter PDFs are AES-protected, so
they were merged with the macOS PDF framework rather than a new Python dependency.

**Six sources left record only**: P-17, the 12&12, the Kurtz talk, SMF-132, the short-form
Concepts and the 2001 Big Book. Each `metadata.json` keeps its old reason under
`formerly_record_only`. **Five remain**: Kurtz (1991), DeGroot (1974), the April 1946 *Grapevine*,
Rohr (2011) and *Tricycle* (2019), each needing a copy only the Human Author can obtain.

**A fourth "unobtainable" item was free.** The Concept 4 essay, carried in `HANDOFF.md` section 10
as needing a purchase, is in the 2024-26 *A.A. Service Manual*, which AAWS posts whole on its own
file host. It is now `ServiceManual_2024`, the corpus's thirty-third source. The Concept IV essay is
about voting participation in proportion to responsibility and holds no rule on the size of a
rotating pool, which confirms Chapter 10's narrower reading. Rotation doctrine is in Concept XI: it
was adopted for the staff after one dominant worker, who had hired people who would not compete
with her, collapsed; it ties term length to responsibility; and it warns against attempting more
rotation than that. Concept V calls the well-heard minority the chief protection against a hasty
majority. None of that is yet in the manuscript.

**Checked and not changed.** `check_book.py` names a source by the text before the underscore in
its directory name. `BigBook_1939` and `BigBook_2001` share "BigBook", which would matter once the
2001 text exists, but no chapter uses the token, so the collision checks nothing. P-17's "AAWS"
appears twelve times in the chapters; with its text present every citation-subject pair still
verifies.

**Still to come.** The partly-read sources on disk, and a second list of free open-access papers
found in the search, which needs approval before anything is downloaded.

### 13 September 2026: the partly read sources, read to the end

The third part of the approved plan was to finish reading what the corpus already held. Five sources
had been read only in part: the three American Temperance Union documents, Gough's 1869
autobiography, and the practice pages of *Recovery Dharma*. All five are now read in full, and
`research/SOURCES.md` records what each added. Nothing in the manuscript changes; every finding is
candidate material.

**Recovery Dharma.** The selected meditations and inquiry questions, the only pages left, are
practice material with no governance text, so appendix A12's absence claim now holds over the whole
book. The appendix and primer still state the narrower scope, which remains true.

**The ATU volumes.** Three things deserve a chapter's attention. The Sons of Temperance's own
statistics for 1848, in the 1849 almanac, count 8,001 members who broke the pledge in the year among
149,372, beside 8,043 expulsions. They were checked against the page image. So was the almanac's
founding date of 1841, which conflicts with the 1842 call Chapter 2 takes from Eddy and should not
be adopted. The 1840 report describes temperance beneficial societies in Philadelphia from 1836 with
the Sons' own rationale, six years before the Sons. And the treasurer's accounts, both checked
against page images, show one donor, E. C. Delavan, giving 37 per cent of the Union's receipts in
1839 and 47 per cent in 1840. The 1841 report also carries John Hawkins's account of the Baltimore
meeting rules, "no sectarianism, no politics or arguments", and an 1833 clause making each
temperance society independent of every other.

**Gough.** The unread chapters change nothing in Chapter 3. They add Gough's own statement that he
did not agree with the Washingtonians, his receipts per lecture, the movement's habit of counting
signatures rather than members kept, and the 1857 to 1860 schism between the moral-suasion League and
the prohibitionist Alliance that ended in *Gough v. Lees*.

**Not changed, and why.** Appendix A12, the primer, Chapter 1's note that the 1840 report and 1849
almanac were "obtained but consulted only", and Chapter 2's list of unread Sons material now
understate the reading. None is false. Correcting them changes the sources of the book and primer,
so it waits for the next rebuild, and the rebuild waits until `tools/build_book.py` no longer writes
the author block back into artifacts that `main` carries anonymized. `HANDOFF.md` section 10
carries it as item 7.

### 13 September 2026: the book rebuilt anonymously, read scope synced, seven papers held

Three things the Human Author asked for in one message.

**The author block.** PR #10 anonymized the committed book by editing its rendered files, and the
primer at source, but three sources still named the Human Author: the YAML header in
`tools/build_book.py`, the preface's opening paragraph and the appendix's attribution line. Every
rebuild therefore put the name back, which is why the read-scope corrections below had been
waiting. All three now say the book is by an anonymous author, in PR #10's wording, and neither
rebuilt artifact carries a name. The paper's title block still names the Human Author; PR #10 left
the paper alone and so does this.

**Read scope.** Appendix A12, the primer's Recovery Dharma entry and Chapters 1 and 2 now say what
`research/SOURCES.md` says. Correcting them turned up more staleness than `HANDOFF.md` item 7 had
recorded. A12's introduction still said the fourteen stories were unread, false since 16 August; its
carrier table marked them "not read"; and its list of what was not read said nothing independent
about the 2019 schism had been consulted, though A12.4 has used *Tricycle* since 17 August and its
references never listed it. Chapter 2's list of unread sources named Krout, Harrison, Marsh and
Eddy, all read at source long before. The inquiry questions add one carrier to A12.3's counsel
column: they suggest working through them with a mentor, wise friend or group, and ask whether the
reader has one to turn to (136, 139, 143), checked against the page images.

**Seven papers.** With the Human Author's approval, seven free copies were downloaded from NBER, the
first author's university site and ASREC, and filed as `Angrist_2014`, `CunhaHeckman_2007`,
`CunhaHeckmanSchennach_2010`, `HuSchennach_2008`, `Lembke_nd`, `Dinerstein_2022` and
`CohenJohnstonLindner_2023`, bringing the corpus to 40. None has been read. Where a plain surname
occurs in chapter prose the directory token is compound, so no token pairs a citation. The Hu and
Schennach copy is a JSTOR download that the first author posts, cover page included.

The book and primer were rebuilt, and the full release gate passes, 136 of 136.

### 13 September 2026: the seven new papers, read

The papers downloaded that morning were read the same day: Cunha and Heckman (2007), Cunha, Heckman
and Schennach (2010), Angrist and Lembke in full; Hu and Schennach, and the two skill-depreciation
papers, in part. The quotations recorded were checked against page images. Nothing in the
manuscript or the paper changes, and `research/SOURCES.md` has the detail.

**What holds.** Every attribution Chapters 12 and 13 and the paper make to these works is
supported, and the paper's claim that Cunha, Heckman and Schennach was read at source is now
documented page by page. Three precision points came out of it: the book's ρ is their φ, and they
use ρ for something else; Chapter 12's "multiplicative production of a stage" is a CES in the
sources; and Chapter 13's "and solve it" says more than they claim for endogenous investment. One
candidate addition came out too: the sign of their estimated substitution parameter for cognitive
skill changes between early and late childhood, which is the empirical shape of Chapter 13's
chain-or-menu question.

**The finding that matters most.** The model's decay rate. Six per cent a week is a half-life of
about eleven and a half weeks. Dinerstein and colleagues estimate teaching-skill depreciation at 4.3
and 17.2 per cent a year, half-lives of about sixteen and about four years, and Cohen and colleagues
find no measurable decline in general skills over up to three years of unemployment. Both measure
skill, and the model's dial is practice, which may lapse faster, so this does not calibrate the rate.
It does make Chapter 12's statement that the literature was never consulted untrue, and it points
the search at habit and relapse rather than labour economics.

**Why nothing was changed.** Each finding changes the author's text. `HANDOFF.md` section 10 carries
them as item 7 for the Human Author to decide.

### 13 September 2026: what the seven papers bear on, applied

At the Human Author's direction everything `HANDOFF.md` item 7 had carried for decision was
applied, and the reading was cross-checked against every place in the book it could reach.

**Chapter 12.** The decay rate of six per cent a week is now set, in the narrative and in the
notes, against the two skill-depreciation papers, whose main texts were read in full for the
purpose: about four per cent a year for early-career teachers' skill, and no measurable decline in
workers' cognitive skills over up to three years of unemployment. Reading them in full added two
caveats, Dinerstein and colleagues' weak district-level first stage and Cohen and colleagues'
finding that several self-assessed traits, conscientiousness among them, did fall. The chapter now
says the rate rests entirely on the difference between a practice and a skill, and states how much
rides on it.

**The cross-check that mattered.** The existing one-at-a-time screen already showed that large
downward moves of the decay rate are among the few that reverse the ordering of referral loss
against pure attraction loss on final membership, and at a quarter below the default the
referral-starved group is viable in all three seeds. Chapter 1 recorded the reversals; it now says
why they are the ones to watch. Chapter 24, which names that ordering as the strongest candidate
for an empirical test, now says the decay rate is the assumption to measure alongside it. Appendix
A11, `research/PARAMETERS.md` and the paper's limitations carry the same point.

**Corrections to attributions.** Chapter 12 no longer credits Cunha and Heckman with
multiplicative stage production; Chapter 13 says Cunha, Heckman and Schennach address endogenous
investment rather than solve it, and explains the rho and phi notation; and Chapter 14 no longer
credits them with a depreciation structure, which their technology does not have. The last was not
on item 7's list and was found by checking every citation of those papers.

**Additions.** Chapter 13 and the paper add Cunha, Heckman and Schennach's estimate that the
substitution parameter changes sign between early and late childhood, as an analogy for the design
of a study. Chapters 2 and 15 use Lembke. The paper's bibliography marks the papers read.

**The model is unchanged.** The two depreciation papers measure skill, and the model's dial is
practice; neither gives a value for how fast a practice lapses, and replacing one authored number
with another chosen after reading them would not be an improvement. A 400-seed run of the
attraction-versus-referral ordering at slower decay is carried as `HANDOFF.md` item 7 instead.

### 13 September 2026: Chapter 4's "you must" to "we ought", corrected

**The claim.** Chapter 4 said the 1939 comment round softened "you must" to "we ought" in various
places. That came from secondary accounts, and the working manuscript, held since 12 September,
shows no such edit.

**What the chapter now says.** The paragraph on the comment round is first-hand for the manuscript
layer: comments collected on one surviving copy, Dr. Howard named in the margins, the kneeling
instruction and the ultimatum struck, and a change of speaker from "you" to "we" that mostly keeps
the modal, with "You must take the lead" printed as "We must take the lead" after the pencil had
softened it, and "You must find Him now!" the one clear softening. The "four hundred copies" is now
the editors' "as many as four hundred", and the effect on who can walk into a room and stay is marked
as the author's reading rather than something the pages show.

**How it was checked.** Every quotation against the facsimile's page images, PDF pages 62, 63, 64,
73 and 74 for MS pp. 30, 31, 32, 41 and 42, and the printed wording against the 1939 reprint at
printed pages 71 and 95. Dr. Howard's name was confirmed on seven of the eight pages the note lists;
the eighth, MS p. 56, is not legible enough at the resolution checked, so the chapter names seven.

**Propagated to** the chapter's notes and references, where the 1939 first edition moves from unread
to held, the claim register (the row is now P, with five new rows), `research/SOURCES.md`, the
working-manuscript note and its PDF, `HANDOFF.md` section 10 (item 4 closed and the rest
renumbered) and the changelog.

**What did not change.** No model value, cache or notebook. The paper, the appendix and the primer
never carried the claim.

### 13 September 2026: Appendix A13's count of the 1939 stories

**The error.** A13 said the 1939 edition has twenty-nine personal stories. Its contents page lists
thirty, from "The Doctor's Nightmare" to "Ace Full Seven-Eleven", and the working manuscript
accounts for every one: nineteen in the circulated draft, a twentieth struck through there and
printed anyway, and ten added after the draft went out.

**What changed.** A13 now says thirty wherever it counted the stories, and states that the census
covers the twenty-six story segments the automatic split recovered; the split did not separate the
other four and was not retained, so which four is not recorded. The primer, `research/SOURCES.md`
and the `BigBook_1939` summary say thirty, and the working-manuscript note records the recount as
made. `HANDOFF.md` section 10 item 4 is closed and the rest renumbered.

**What did not change.** Every census figure, including twenty of twenty-six and its comparison
with the 2001 edition, was computed over the recovered segments and stands. No model value, cache
or notebook.

### 13 September 2026: the referral-versus-attraction ordering at slower decay, at 400 seeds

**Why it was run.** The one-at-a-time screen reverses the pure-attraction-loss minus referral-loss
ordering on final membership when `delta0` is 25, 50 or 75 per cent lower, on three seeds per
endpoint. The skill-depreciation reading earlier the same day made a slower lapse plausible, so the
screen's three `delta0` points were re-run as a confirmatory design.

**The design.** `model/decay_ordering.py`: both channels, pure attraction loss (the T11 attraction
path removed, governance held at one) and referral loss (`lam_exog = 0`), at `delta0` unchanged and
25, 50 and 75 per cent lower, full adherence otherwise, 1,560 weeks at dt 0.5, seeds 0 to 399
shared by all twelve cells. 4,800 runs, cached hash-linked in `research/decay_ordering.json`.

**What it found.** At the default rate the cells reproduce the released values and the ordering
holds on every outcome. At 25 per cent lower it reverses on final membership, -14.97 [-17.21,
-12.73], and holds on endpoint viability, 0.2450 [0.2028, 0.2872], and existence, 0.1600 [0.1240,
0.1960], all paired intervals: the referral-starved group ends larger but is viable in 75.50 per
cent of runs [71.06, 79.46] and closes in 64 of 400. At 50 and 75 per cent lower every
referral-loss run is viable and ends near capacity. The screen was right about direction, and the
reversal is confined to final membership.

**Where it went.** Chapter 12's notes, with the full design and intervals; a sentence each in
Chapters 1 and 24 and a paragraph in Chapter 4's notes; appendix A7.1, A7.5 and A11; the paper's
decay limitation; the primer; `research/PARAMETERS.md` sections 2, 3 and 8.1; `research/SOURCES.md`;
`research/ROBUSTNESS-RESULTS.md`. The cache is registered in `tools/check_release.py`, now 142
checks, 136 of them run under `--skip-artifacts`, and in both notebooks, which assert that the default-rate
cells reproduce the released figures. `HANDOFF.md` section 10 item 5 is closed.

**What did not change.** The canonical model and every released number. The run checks a
sensitivity rather than recalibrating anything: `delta0` stays at 0.06 until something measures how
fast a practice lapses.

### 13 September 2026: a review pass over the three stacked pull requests

**What it found.** `tools/check_release.py --skip-artifacts` counted its own skip notice as a passed
check, so "137 checks passed" meant 136 had run, and the gate's comment, `CLAUDE.md`,
`AGENT_VERIFY.md` and both workflows said the flag omits seven checks where it omits six. Appendix
A7.5 and `research/PARAMETERS.md` section 8 still said "all three caches" after the decay-ordering
cache joined them. `HANDOFF.md` section 10 lacked four open items recorded elsewhere: the
facsimile's unphotographed pages 22 and 23, fourteen background citations with no documented read
status, the point at which the decay ordering first reverses, and the working manuscript's seven
other suggested uses. Chapter 12 says Ben-Porath (1967) was read at source while
`research/SOURCES.md` records no read status for it; item 6 flags that for the Human Author rather
than guessing which is right.

**What changed.** The gate reports the six as skipped, and the five documents say six. The two
intros count the fourth cache, and the robustness report says its decay section is confirmatory
rather than a screen. `HANDOFF.md` section 10 gains items 5 to 8 and a closed entry, and the Part 5
plan names the decay run as the case for naming an outcome. `tools/summarize_robustness.py` and
`tools/regenerate_notebooks.py` expose what they generate, and seven new tests execute both
notebooks, compare the notebooks and the robustness report with their generators, check the gate's
skip count, recompute three cached decay-ordering cells from the script, and exercise the two
generators' entry points.

**What did not change.** No model value, cache, notebook or released number.

### 14 September 2026: Ben-Porath (1967) read at source

**The discrepancy.** The review pass of 13 September found that Chapter 12 says Ben-Porath (1967)
was read at source and lists it as read in full, while `research/SOURCES.md` recorded "read status
not documented" and Chapter 14 listed it as cited at a remove.

**The resolution.** The Human Author confirmed that it was read at source. `research/SOURCES.md`
now says so, with the date of the confirmation; Chapter 14 moves it to read in full; the paper's
bibliography marks it read at source; and `HANDOFF.md` item 6 drops it from the undocumented list,
which is now thirteen.

**What did not change.** No claim, number, model value or cache. The corpus holds no copy of the
paper, so it stays among the works to obtain.

### 14 September 2026: a withheld name found in two verification indexes

**How it was found.** A pass looked for personal information in everything the public repository
publishes: the current tree, its history, the rendered PDFs and the release assets. It found the
surname of the founder this project never names in the committed vocabularies of
`RecoveryDharma_2023` and `Rohr_2011`. `check_book.py` had enforced the rule since 17 August 2026,
but only over a fixed list of prose files. No verification index was on that list, and an index's
vocabulary publishes every word it holds.

**What changed.**
- The digests moved to `tools/withheld.py`. Its test also catches the name inside a possessive or
  a hyphenated compound, which the old test missed.
- `build_corpus.py` leaves a withheld word out of every vocabulary it builds. It strips one from
  any existing index, including the record-only ones, and `--check` reports an index that holds
  one.
- `check_book.py` now scans every tracked text file, and `check_pdfs.py` scans the text of each
  rendered PDF.
- The two indexes each lost that one word and nothing else. No subject, citation or claim depended
  on it.
- Six new tests cover the change, using an invented name.

**What else the pass found.**
- **The current tree:** nothing else. It has no host paths, no personal disclosure and no machine
  metadata, and neither do the caches, notebooks or PDFs.
- **Author attribution:** the attribution to the Human Author in `README.md`, `ATTRIBUTION.md`,
  `CITATION.cff`, `LICENSE` and the paper is deliberate.
- **The published history:** it still holds four things:
  - the name, in the states of 16 and 17 August 2026 and in the two indexes;
  - host paths and four source documents from the initial import;
  - a second personal email address in commit metadata.

  Removing them means rewriting published history. That decision is recorded as `HANDOFF.md`
  item 9, for the Human Author.

### 14 September 2026: six background papers, read at PubMed Central

**What arrived.** The Human Author supplied a zip described as the full extracted text of six papers
the paper cites, with an updated list of sources to obtain. The six files were summaries of three
to four kilobytes written by another tool. They had bullet-point findings and notes guessing at what
this book says, and two were marked as truncated. A summary is not the source, and an index built
from one would certify subjects against the wrong text, so none was filed.

**What was done instead.** Every scripted route to the articles refused. PMC's PDF links return a
bot check, Europe PMC holds no full text for them, and AMS returns 403 for Banks et al. (2014). At
the Human Author's direction, the five PMC articles were read in the in-app browser. No copy is
held; a PDF saved from each article page would give the corpus one.
- **Gorman et al. (2006), read in full.** Social contagion among agents on a one-dimensional lattice.
  Susceptibles always convert. The drinker and former-drinker shares settle at a level set by the
  stop and resume biases. Conversion is fastest at an intermediate mixing speed, and a single bar
  clusters drinkers, which buffers susceptibles while concentrating drinking. Outlet density is left
  for future work.
- **Rynes and Tonigan (2012), read in full.** 115 new AA affiliates were followed at 3, 6 and 9
  months. A sponsor at 3 months predicts more abstinent days at 9 months. The abstinent share of the
  social network stays near half throughout and does not mediate the effect. The authors attribute
  the earlier positive mediation findings to cross-sectional or partly lagged designs.
- **Banks et al. (2017), read in full.** An individual-level dynamical model fitted to one patient's
  daily data on drinks, norm violation, confidence and commitment by iterative weighted least
  squares. The preliminary model fails, and a revision driven by rates of change fits. The equations
  did not render in the page text and were read through the authors' term-by-term description.
- **Witkiewitz and Marlatt (2007), read in full.** The case for relapse as a discontinuous process,
  a qualitative review of Gilmore's catastrophe flags, and a refit of Hufford's cusp on Project
  MATCH. Among those still drinking at twelve months, the cusp models beat linear and logistic ones
  on AIC, BIC and pseudo-R-squared. Abstainers are excluded, and the program offers no significance
  test. The passage Chapter 14 holds at two removes through Hunter-Reel and colleagues is not in this
  paper.
- **Kelly, Humphreys and Ferri (2020), read in full apart from the per-study tables, forest plots,
  search strategies and references.** 27 studies and 10,565 participants. Manualized AA/TSF raises
  continuous abstinence at 12 months over other established treatments (risk ratio 1.21, 95% CI 1.03
  to 1.42; 2 trials; high certainty). It does about as well on intensity, consequences and severity,
  and it probably offsets healthcare costs.
- **Banks et al. (2014), not read.** It is cited at a remove through the 2017 paper, which describes
  its top-down method.

**What was recorded.**
- `research/SOURCES.md`'s paper-only table, Chapter 14's references and the paper's bibliography now
  record these statuses.
- Four citations gained a subtitle or an issue number, checked against Crossref.

**What it bears on.** Four statements in the paper and Chapter 14 say more or less than their sources
do:
- the paper's summary of the Cochrane review;
- its claim that the mechanism literature converges on network change;
- its description of Gorman et al.;
- Chapter 14's sizing of the older strand's warrant.

They are proposed to the Human Author as `HANDOFF.md` item 10 and not yet made. No number the book
computes changes.

### 14 September 2026: the four corrections made

The Human Author approved the four corrections proposed above.
- **The Cochrane review.** The paper's literature review now says that the review finds, with high
  certainty, that manualized interventions raise continuous abstinence at twelve months over
  established alternatives such as cognitive behavioral therapy, from two trials with 1,936
  participants, and that they do about as well on most other drinking outcomes.
- **The mechanism literature.** The review says most of that literature credits network change,
  keeps Kaskutas, Bond and Humphreys (2002) as the example, and names Rynes and Tonigan (2012) as the
  clearest dissent.
- **Gorman et al. (2006).** It is described as the contagion model it is, with a single bar that
  concentrates drinkers.
- **Chapter 14.** The chapter keeps Hufford's two preliminary samples as Hufford's warrant. It adds
  that Witkiewitz and Marlatt refitted the same specification to Project MATCH, and gives the
  refit's limits: drinkers only, and fit indices without a significance test.

No number the book computes changes. The paper prints no new decimal, so its traceability cell is
unaffected. `HANDOFF.md` item 10 is closed.

### 14 September 2026: the published history rewritten

**Decision.** The Human Author approved rewriting the published history (`HANDOFF.md` item 9). They
chose three things:
- map the second address, which appears nowhere in the tree, to the GitHub no-reply address;
- leave the address the attribution files publish on purpose;
- set this repository's commit email to the no-reply address so new commits do not bring the old
  one back.

**Method.** `git filter-branch`, because `git-filter-repo` was not installed and installing it would
have meant a download. The one thing `git-filter-repo` does that `git filter-branch` does not is
rewrite commit hashes quoted in commit messages, and no commit message here quotes another commit's
hash. The run had four parts:
- **An index filter.** It dropped every source document under `research/incorporated/` and
  `research/staged/`, and the ten versions of the book PDF whose text printed the withheld name. It
  rewrote the text blobs that held the name or a home-directory path. The appendix passage took the
  wording of the 17 August fix, and the two indexes lost the one token.
- **An environment filter.** It mapped the second address to the no-reply address.
- **The tag.** `v0.9.0` was recreated with the no-reply tagger and its original date and message.
- **Where it ran.** First as a trial on a scratch copy, then for real on a fresh copy of GitHub's
  `main` after #22 merged. The helper script held the name as a search pattern, so it stayed outside
  the repository.

**Verification before the push.**
- The rewritten `main` has the same tree as the published one, byte for byte.
- It keeps all 107 commits with identical messages.
- The tag's tree differs from the old tag's only by the one token in two indexes.
- A scan of all 1,475 paths reachable from `main` and the tag found no source document, no
  occurrence of the name in any text or PDF text, no home-directory path, and no trace of the old
  address in commit or tag metadata.

**The push.**
- `main` and the tag were force-pushed with leases, so the push would have failed had either moved.
- The four merged branches were deleted on GitHub.
- The local clone was reset to the new `main` and its stale branches removed.
- The release still hangs off the tag with its three assets.

**What remains.** GitHub still serves old commits by hash, which was checked after the push, and
through the pull-request references. A request to GitHub Support was drafted to purge them, but on
15 September 2026 the Human Author decided to leave things as they are. The old commits therefore
stay reachable in those two ways, and `HANDOFF.md` no longer carries the item. New commits use the
no-reply address.

**A slip on the way.** PR #20 was merged before GitHub's CI had run on it. Retargeting a pull
request's base does not trigger this repository's pull-request workflow, and the merge guard read
"no checks reported" as passing. The full local CI had passed on that exact branch, and the push
run on `main` for the merge passed. #21 then had its CI dispatched by hand and passed before it was
merged, and #22 targeted `main` from the start.

### 15 September 2026: the working manuscript's seven suggested uses

**What was asked.** The Human Author asked for the seven remaining suggested uses in
`edits_and_suggested_uses.md` to be drafted, so that each can be kept or dropped on its own. They
went in as seven commits, one per addition, followed by one commit for the shared records.

**How each was checked.**
- Every quotation and page reference was found through the OCR text and then checked on the
  facsimile's page image.
- Printed wordings were checked against `BigBook_1939`.
- Quotation from the facsimile was kept to a few words, and only where the wording is the evidence.
- Hazelden's essays are cited at a remove wherever they are used: for the date and circulation of
  the draft, for Wilson's description of himself as umpire in a talk they reproduce, and for
  Silkworth's July 1939 remark.

**What went where.**
- **Chapter 5.** The typed Foreword already asks for anonymity before the press, disclaims
  organisation in the conventional sense, takes no fees or dues, and sets one requirement. The
  chapter names the corresponding Traditions without deriving them from the Foreword, and sets
  beside it the Foundation page's permanent outside majority. Six claim-register rows were added.
- **Chapters 9 and 7.** The founding text was settled by a collator and an umpire, an outside
  psychiatrist is named on seven pages, and Akron's group was centred on its doctor. This is an
  analogy to prominent agents, and the chapter says plainly that it is not a test.
- **Chapter 18.** The removal of claims doctors and clergy would contest, the struck paragraph on
  institutions, and "rule" printed as "principle", set against the Foundation page.
- **Chapter 15.** The necessity of helping was defended in editing, and its cost was stated down.
- **Chapter 19.** The one requirement, the handwritten Step Eleven qualifier, and members taken
  back. This illustrates the membership rule, not either of the model's paths.
- **Chapter 22.** The founders' plan to grow from a nucleus, and Silkworth's remark, recorded as a
  belief. It neither agrees nor disagrees with the unresolved composition contrasts.
- **Chapters 24 and 21.**
  - Chapter 24 gets one large room centred on one person, which says nothing about scaling.
  - Chapter 21 gets the meeting sizes as a check on the room capacity of sixty, not on the 17.80
    endpoint.

**What was left out.**
- The title vote and the four people at the galleys.
- Household autonomy on serving liquor.
- The Bill's Story insert.

**What was corrected.**
- Dr. Howard is named legibly on seven pages, not eight, as Chapter 4 already said. MS p. 56 is too
  faint to count.
- Chapters 21 and 24 carried stale SMF-132 status and now record it as read and held.
- The Part One register no longer says the project acquires none of AA's copyrighted texts.

**What did not change.** No model value, cache, notebook or registered number. The room capacity
stays at sixty. No other public document states the SMF-132 comparison, so none needed the 1939
figures beside it.

### 21 September 2026: where the decay rate turns the ordering

**What was asked.** The optional item 7 in the handoff: a 400-seed paired run at 10, 15 and 20 per
cent lower decay, to locate the rate at which the referral-versus-attraction membership ordering
first reverses. `research/decay_ordering.json` had it holding at the model's rate and reversed at
25 per cent lower, and the one-at-a-time screen, on three seeds, still found it strict at 10 per
cent lower, so the turn was known only to lie in a gap fifteen points wide.

**The design.** `model/decay_reversal.py` is `model/decay_ordering.py` with a different level list
and a different docstring, and nothing else: same three conditions, same interventions, same
outcome definitions, same 1,560-week horizon at dt 0.5, same seeds 0 to 399. That is what lets the
two caches be read as one seven-level series, and a test now asserts it by parsing both scripts,
dropping the docstring, substituting the names and the level list, and comparing what is left.
3,600 runs took five minutes and thirty-seven seconds on eight workers.

**What it found.** Attraction loss minus referral loss on final membership is 10.92 members
[10.18, 11.66] at 10 per cent lower and 6.35 [5.03, 7.68] at 15 per cent lower, so the published
ordering holds at both. At 20 per cent lower it is -2.79 [-4.77, -0.81], with the attraction-loss
group smaller in 157 paired runs, tied in 10 and larger in 233. The turn is therefore between 15
and 20 per cent, a half-life between 13.6 and 14.4 weeks against the model's 11.6. The strict
counts fall monotonically across the whole series, 394, 373, 317, 233, 143, 0, 0. Endpoint
viability and existence are reversed in no paired run at any of the three new rates, so the
reversal stays confined to final membership, which is what the earlier run concluded at its own
distances.

**Where it went.** Chapter 12 carries the three new levels in full and now says a fifth rather than
a quarter where it states the condition on the book's comparisons; Chapters 1, 4 and 24, the primer
and the paper carry the located threshold; appendix A7.5 interleaves the levels into both tables
and adds a locating paragraph, and A11 item 9 and `research/PARAMETERS.md` replace "at 25 per cent
lower" with the interval. The gate registers the cache and runs 148 checks, 142 under
`--skip-artifacts`. `research/ROBUSTNESS-RESULTS.md` and both notebooks read the merged series.

**What did not change.** No model value and no released number. The decay rate stays at six per
cent a week, because nothing measured how fast a practice lapses; what changed is how precisely the
book can say what rests on it.

**One stale count corrected in passing.** The handoff's verification table said the notebooks run
78 and 102 assertions. They ran 81 and 105 before this session and 84 and 108 after it.

### 21 September 2026, later: the lapse literature searched

**What was asked.** Whether anything measures how fast a practice lapses, which `HANDOFF.md` item 3
had carried as unsearched and which is the evidence the decay rate would need.

**What was found.** Three literatures, none of them measuring that quantity, recorded with their
numbers in `research/DECAY-RATE-LITERATURE-SCAN.md`. Deliberate habit degradation is measured daily
and well: Edgren, Baretta and Inauen (2025) fit person-specific curves to 11,805 daily automaticity
ratings from 194 people and find decay stabilising in a median of 9 to 10 days, range 1 to 65. That
is an actively removed unwanted habit, which is the opposite case from a wanted practice fading for
want of renewal, and it is an order of magnitude faster than six per cent a week. A computational
habit model carries a decay parameter of the same family at 0.15 to 0.2, but per behavioural
opportunity rather than per week. The nearest thing in substance is participation falling away:
Kaskutas, Bond and Avalos (2009) find a descending AA-attendance class going from about 150
meetings in year one to about six by year five, mindfulness home practice running at about 40 per
cent of what is recommended, and a mobile exercise cohort with a median dropout time of 14 weeks.

**What it changes.** The model is unchanged and no number moved. What changed is the shape of the
ignorance: Chapter 12 currently sets the rate against skill depreciation alone, which is one to two
orders of magnitude slower, and the scan shows the rate sits between two measured literatures rather
than outside one. Saying so in the book requires holding and reading the two open-access papers
first, which is the Human Author's decision, so nothing was written into a chapter and no source was
catalogued. The *Psychology & Health* companion paper sits behind a publisher bot check, which this
agent does not attempt.

### 22 September 2026: the two papers that bracket the decay rate

**What was asked.** The Human Author directed that the two papers the 21 September scan turned up
be held and read, so that Chapter 12 can say the decay rate is bracketed rather than merely
untested.

**How they were obtained.** Neither as a PDF. Wiley's own PDF, the Europe PMC render and the PMC
download route all refuse a scripted request, the last with a proof-of-work interstitial, which is
a bot check and not something this project attempts. What both publishers do serve is the deposited
full text: Edgren from the Europe PMC REST service, and the Kaskutas author manuscript from NCBI
E-utilities. Each was rendered to plain text with headings, paragraphs and tables preserved, and
held git-ignored with a SHA-256 and a verification index like every other source. The figures are
images and are in neither deposit, so no figure is quoted from either paper anywhere in the book.

**What the reading found.** Edgren, Baretta and Inauen followed 194 people for 91 days, one
self-selected habit each, 11,805 daily automaticity ratings, six curves fitted per person. Decay
settled at 95 per cent of the lower asymptote in a median of 9 to 10 days, range 1 to 65, in the 42
people whose fits were valid and whose trajectory crossed the scale midpoint, with 76 per cent of
variance between persons. That is an order of magnitude faster than six per cent a week, and it is
the opposite case: an unwanted habit actively removed with an implementation intention, not a
wanted practice left unrenewed. The authors' own cautions are recorded with it. Kaskutas, Bond and
Avalos followed 586 alcohol-dependent people for seven years and found four attendance classes,
63, 16, 11 and 10 per cent of the sample, with participation falling away over years in all but the
medium class. Their emphasis is that the falls in attendance were not matched by falls in
abstinence, which is a caution against reading the model's practice variable as a meeting count.

**One correction.** The scan record had the descending class falling to about six meetings by year
five. That number came from a search summary, and the paper's text does not say it; the per-year
counts are in a figure the author manuscript does not carry. The scan file now says so.

**One naming decision.** The directory is `KaskutasBondAvalos_2009`, not `Kaskutas_2009`, for the
reason the Cohen directory already records: the paper's bibliography cites Kaskutas, Bond and
Humphreys (2002) as well, and a bare surname token would let `check_book.py` check a citation of
one against the text of the other.

**Where it went.** Chapter 12 gains a paragraph and two references, the paper's limitation item and
bibliography, appendix A11 item 9, the primer's "what was not read" entry,
`research/PARAMETERS.md`, `research/SOURCES.md` and the scan file. The corpus is 42 sources.

**What did not change.** No model value, cache, notebook or released number. The decay rate stays
at six per cent a week. What the book can now say is that the value sits between two measured
literatures rather than outside one, which is plausibility and not evidence.

### 22 September 2026, later: a review pass over the two merges

**What was checked.** Everything the decay-reversal run and the two new sources touched, read
rather than grepped, for statements that were true when written and are not now.

**Three were.**
- `research/DECAY-RATE-LITERATURE-SCAN.md` still said Chapter 12 "currently" sets the rate against
  one literature only. That was true for about a day. It now says what changed and when.
- `research/SOURCES.md` listed Kaskutas, Bond and Humphreys (2002) with no note that a different
  Kaskutas paper is now held, which is the confusion the directory token was chosen to avoid. The
  row says so.
- Chapter 24 asked for a study that records how fast practice lapses without saying what would
  not do. The new source answers that: attendance fell away after year one in three of the four
  trajectories while abstinence did not follow it down in the two that had attended most, so a
  study must record practice rather than attendance. The chapter says it and carries the reference.

**What did not change.** No model value, cache, notebook or released number, and no count.

### 24 September 2026: two copies that were said to be unobtainable

**What prompted it.** Holding Edgren and Kaskutas on 22 September used a route the project had not
tried: the deposited full text, served by the Europe PMC REST service and by NCBI E-utilities. The
handoff had five papers recorded as read at PubMed Central and impossible to hold, on the ground
that "every scripted route refuses". That claim was worth retesting against the route that had just
worked.

**What came back.** Two of the five. Banks et al. (2017), PMC5551482, and Rynes and Tonigan (2012),
PMC3248627, are NIH author manuscripts whose full text the E-utilities API serves in JATS. Both are
now held git-ignored with a SHA-256 and a verification index, on the standing direction of 13
September that the corpus hold a lawful copy of every source it can. The other three, Gorman et al.
(2006), Kelly, Humphreys and Ferri (2020) and Witkiewitz and Marlatt (2007), return metadata only
from both services and still need a copy saved by hand.

**What was not done.** No bot check was bypassed. The PDF routes still refuse, and PMC's serves a
proof-of-work interstitial, which is a bot check and is left alone. The distinction is the point:
an API that serves a deposit to anyone who asks is not a door that was locked.

**Read statuses are unchanged.** Both papers were read in full on 14 September 2026 and what the
reading found is already in `research/SOURCES.md`. What changed is provenance: the claims they
support can now be checked against a held copy and a vocabulary index rather than against a memory
of a web page. The Banks deposit carries its display equations as MathML, which does not survive
rendering to text, and that is recorded in its metadata and summary, because it is how the paper
was read in the first place.

**One naming decision.** `BanksBekeleMaxwell_2017` rather than `Banks_2017`, since the paper also
cites Banks et al. (2014) at a remove and a bare surname token would let `check_book.py` check a
citation of one against the text of the other. `Rynes_2012` keeps the bare surname, which is
unambiguous and therefore gets real citation checking.

**What did not change.** No model value, cache, notebook or released number, and nothing in the
book.
