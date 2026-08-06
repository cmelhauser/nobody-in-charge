# Part Three: The Individual

Chapters 12 to 15, roughly 14,000 words.

Master plan: `../BOOK-PLAN.md`. Companions: `PART-1-PLAN.md`, `PART-2-PLAN.md`.

---

## 1. What changes in Part Three

Parts One and Two are about groups. Part Three turns to the person, and three things
about the material change with it.

**The claims get weaker and must be labelled as weaker.** Part Two rests on a published
theorem. Part Three rests on a simulation whose parameters I chose. Nothing here has been
fitted to data, and the chapters have to carry that without either apologising in every
paragraph or quietly forgetting it.

**The strongest result is somebody else's.** The helper-therapy finding, that people who
help other alcoholics are roughly twice as likely to be sober a year later, is real
empirical work by Pagano and colleagues on Project MATCH data. It is the best-evidenced
thing in the entire book and it belongs to Chapter 15.

**One chapter is a question rather than an answer.** Chapter 13 argues that whether the
Steps can be skipped is measurable and unmeasured. That is its whole content, and it
should not pretend otherwise.

---

## 2. Chapter plan

### Chapter 12. Twelve Dials
*Target 3,000 words. **Next to draft.** Not started; it is third in the sequence by design,
not overdue.*

**What two drafted chapters have already promised Chapter 12 must deliver.** Both are
forward pointers that currently do not resolve, and they are the only two in the book.

1. The preface, paragraph on the model, says the model "is described properly in Chapter
   Twelve". So this chapter owns the full description of the apparatus: twelve dials, the
   eight group resources, the governance matrix, and the thirty-year membership flow. No
   other chapter does this, and Parts Four and Five will assume it has been done.
2. Chapter 14's references say Ben-Porath (1967) is "the ancestry of the depreciation
   structure, described in Chapter Twelve rather than here". So the depreciation structure
   and its human-capital ancestry belong here, not in a Machinery note.

**What Chapters 13 and 14 have already spent, and must not be re-derived.** Chapter 13 owns
the CES stage technology, the rho parameter and the substitutability question. Chapter 14
owns maintenance capacity, the Hill gate, and the audit of whether the released model
actually produces multiple attractors. Chapter 12 introduces the pieces; it does not argue
from them. In particular **Chapter 12 must not restate the threshold**, and if it mentions
gating at all it should flag that Chapter 13 turns the gate exponent into a testable
parameter and leave it there.

**Numbers available and already asserted in the notebook:** the derived group-dependence
coefficients, running 1.00 at Steps 1 and 12 down to 0.17 at Step 7, mean 0.53; the
upward-to-downward transmission ratio, 1 to 6.0 and averaging 1.9. These are section 5 of
the notebook and need no new computation.

**The parameter honesty line for this chapter:** 118 numbers chosen by hand out of 226
cells, none fitted. See `../research/PARAMETERS.md`, which was corrected on 2 August 2026
and whose breakdown had been wrong in four of six rows.

The person as a state vector, in plain language. Twelve dials, each from zero to one,
each reading how much of that step is currently live practice rather than something done
once in 1994.

Three properties do the work, and the chapter should establish them concretely before
any of them is used:

- **Everything leaks.** Left alone, every dial falls. This is not a moral claim; it is
  the standard structure of any human-capital model with depreciation, and it is why
  "I did that step" is a different statement from "that step is at 0.8".
- **Steps are gated.** A dial cannot rise much while the one before it sits near zero.
  Chapter 13 turns this into a testable parameter, so Chapter 12 should state it as an
  assumption and flag that it is about to be interrogated.
- **The group enters unevenly.** Some steps are almost entirely social and some are
  almost entirely solitary, and the difference is large: the derived coefficients run
  from 0.17 for Step 7 to 1.00 for Steps 1 and 12.

**The Machinery.** The growth equation term by term; the derived group-dependence
coefficients; the depreciation structure and its Ben-Porath ancestry.

**Risk:** this is the chapter most likely to read as a model being described rather than
an argument being made. It needs a human spine. The candidate is a single member's first
year, used to make each property concrete as it arrives.

---

### Chapter 13. Can You Skip a Step?
*Target 3,500 words. The most interesting chapter in Part Three.*

Everyone in AA says you cannot skip a step. As far as I can establish, nobody has ever
checked, and the claim has never been stated in a form that could be checked.

The chapter's argument:

1. State the folk claim fairly and take it seriously, because it is probably right.
2. Show that the informal rule is the extreme corner of a family of possibilities: the
   steps could be a strict chain, or a partial chain, or a menu in which a strong group
   carries someone past a step they never did.
3. Show how a CES substitution parameter makes one version of the ordering question
   explicit. Negative values imply stronger complementarity; positive values imply more
   substitution within that constructed technology.
4. Use the simulation only as a modest proxy-averaging demonstration under oracle-known
   regressors. It does not recover a nonlinear latent-state estimator or establish a
   three-measures-per-latent design rule.
5. State the obstacle honestly: group input is endogenous to member state, groups attend
   to people who are struggling, and until that is handled the parameter cannot be
   estimated cleanly.

**The Machinery.** The CES formulation from Cunha, Heckman and Schennach; the Leontief
corner; the measurement system and anchoring; and a 400-replication, oracle-known
proxy-averaging demonstration. The exercise measures attenuation under one versus three
noisy output proxies. It is not a nonlinear latent-state estimator and supplies no general
rule for how many measurements an empirical study would need.

**The literature search is done, and it changes the chapter.** See the findings below.
The core claim survives: step ordering as such has not been tested. But there is a finding
that bears directly on the answer and must be confronted rather than ignored.

**What the search found.**

Greenfield and Tonigan (2013) state the gap almost in the terms this chapter needs:
working the steps is widely prescribed, the relative merits of different ways of measuring
step work have received minimal attention, and even less is known about how step work
predicts later substance use. They followed 130 new AA affiliates at intake, three, six
and nine months.

Three things from that study matter here.

**One: the field measures steps as a count, not a sequence.** The standard construct,
following Cloud and colleagues, is the *sum of steps completed*, alongside attendance and
self-identification. A sum discards order entirely. So the ordering question has not been
tested because the instruments in use cannot express it, which is a stronger and more
interesting version of the claim than "nobody got round to it".

**Two, and this is the complication: the steps do not factor as one thing.** Exploratory
factor analysis of the General AA Tools of Recovery scale found a **two-factor structure**,
which Greenfield and Tonigan label behavioural step work and spiritual step work. The two
have different predictors and different effects: behavioural step work was stable over
time and predicted by having a sponsor, while spiritual step work declined over time and
rose with meeting or treatment attendance. Only spiritual step work prospectively
predicted percent days abstinent. Behavioural step work did not predict substance use at
all.

That is evidence against the simplest version of the chain hypothesis. A strict
twelve-link chain would not obviously produce two separable factors with opposite time
trends and different outcome relationships.

**Three: measurement choice changes the answer.** Significantly more participants endorsed
step work on the indirect measure than on the direct one for nine of the twelve steps.
Which instrument you use determines what you conclude, which is exactly the
measurement-error problem the chapter's identification strategy is built to handle.

**What this does to Chapter 13.** The chapter gets better and its claim gets narrower. It
can no longer say the question is untouched. It should say: the ordering question has
never been asked, because the standard instruments record a count; and the one study that
looked closely at the structure of step work found two dimensions rather than one chain,
which is a reason to doubt the strict version before any modelling begins. The chapter's
contribution then becomes making the ordering question *askable* and stating what data
would settle it, which is a more defensible position than claiming virgin territory.

**Still to check before drafting:** Carroll (1993) on adherence to the steps, and whether
any treatment-manual literature has tested sequence effects experimentally.

---

### Chapter 14. The Leaky Bucket
*Target 3,500 words.*

Steps 10, 11 and 12 are the daily ones, and in the model they are not three steps among
twelve. They are the thing that holds the other nine up.

- Maintenance capacity as the average of those three.
- The gate: a structural mechanism capable of nonlinear response, whose claimed
  two-attractor baseline must be tested in the model's actual resource environment.
- The empirical warrant, which is real: Hufford and colleagues found a cusp catastrophe
  model outperformed linear and logistic specifications on relapse data, and
  Witkiewitz and Marlatt argued the same case more broadly.
- Hysteresis as an externally motivated possibility, not a result established by the
  corrected released simulation.

**The honest part, which must not be buried, is now a failed model result.** The original
high state, separatrix and hysteresis calculation froze an environment produced by the
retired uncentred-capability model. Re-estimation from 400 corrected endpoints finds
high/low-start separation above 0.05 in only 7 environments, or 1.75 per cent, and one
near-zero state in the mean environment. Those earlier constants may remain only as an
obsolete-environment diagnostic. The chapter may claim that the architecture can generate
nonlinearity and that outside data motivate testing it. It may not claim that the released
baseline establishes typical-member bistability, a separatrix, or hysteresis.

**The Machinery.** The Hill gate; the corrected 400-environment high/low-start test; the
group decay-rate sweep; and the labeled retired diagnostic.

---

### Chapter 15. Helping Is Not the Reward
*Target 3,000 words.*

Step 12 is usually read as what you do once you are well. In the model, removing it lowers
membership by 5.325 members and maintenance capacity by 0.0135 in 400 paired runs. The
estimated Step 9 decrease is 0.0055 with a 95 per cent interval crossing zero, so the
earlier broad spillover claim is withdrawn.

This is the chapter where the book's best outside evidence lives. Pagano and colleagues,
using Project MATCH data, found forty per cent of those who helped other alcoholics were
abstinent at twelve months against twenty-two per cent of those who did not. Riessman
had named the helper-therapy principle in 1965. The model did not discover this and
should not claim to; what it adds is a structural account of why it would be true.

The chapter also carries the recipient problem, which connects forward to Part Five: the
work requires somebody to do it for, and a group that runs short of newcomers runs short
of the raw material its established members need.

**The Machinery.** Recipient opportunity per high-practice potential helper, the clean
resource override whose membership contrast is unresolved, the paired Step 12 ablation,
the Pagano result and its limits as observational data, and the connection to the inflow
channels from Chapters One and Four.

---

## 3. Definition of done, per chapter

Unchanged from Part Two, and the second item is the one that bites:

1. Drafted with the four-part Machinery.
2. **Every number added to `../model/book-calculations.ipynb` with an assertion**, in a
   section for that chapter, and the notebook re-run clean.
3. `python3 ../tools/check_chapter.py <file>` returns no FAIL.
4. Warnings cleared or consciously accepted.
5. Cross-checked for repetition against neighbouring chapters. Part Two needed three
   fixes at this stage, including twenty-one shared phrases between Chapters 9 and 11.

---

## 4. Sequence

~~1. The step-ordering literature search.~~ **Done.** Findings in section 2 under
Chapter 13, which was rewritten around them.

~~2. Chapter 13.~~ **Drafted.** Passes the checker; figures asserted in the notebook.

~~3. Chapter 14.~~ **Drafted, then materially corrected 6 August.** The first draft
   claimed a typical-member two-attractor shape while refusing its location. The release
   audit found that result depended on a frozen environment from the retired uncentred
   heterogeneity model. The current verdict and replacement design are recorded in section
   6 below; the earlier separatrix, fragility and staggered-cliff interpretation are no
   longer baseline claims.

~~4. Chapter 12.~~ **Drafted.** 2,012 words, FK 7.7, passes the checker, zero shared
   seven-word phrases with any other chapter. Both forward pointers discharged: it now owns
   the full description of the apparatus and the Ben-Porath ancestry of the depreciation
   structure. It does not restate the threshold and defers the CES substitution question to
   Chapter 13.

   Its spine turned out to be the distinction between "I did Step Four" and "Step Four is at
   0.8", from which the three properties follow. Two things it carries that were not in this
   plan. First, the derived group-dependence coefficients support a claim worth having in
   its own right: the group is most necessary at the two ends and least necessary in the
   middle, since Steps 1 and 12 sit at the maximum and Step 7 at a sixth of it. Second, the
   full sweep found the step-ordering exponent to be the single strongest influence on
   outcomes anywhere in the model, which is a better argument for Chapter 13's research
   programme than Chapter 13 makes for itself.
5. **Chapter 15 next and last in Part Three**, since it points forward into Part Five and
   benefits from knowing what Part Five will need. Note what the other three have already
   spent: Chapter 12 owns the apparatus and the group-dependence coefficients, Chapter 13
   the substitution parameter, Chapter 14 maintenance and the threshold. Chapter 15's own
   material is the recipient resource and its saturation in newcomers per available helper,
   the Pagano result, and the connection back to the inflow channels of Chapters 1 and 4.
   The recipient resource is the one group resource no drafted chapter has yet used.

---

## 5. Risks

**The honesty problem is sharper here than anywhere else in the book.** Part Three's
results come from a simulation with 118 hand-chosen parameters, none fitted. (This line
said "roughly twenty-eight" until the parameter audit; see `../research/PARAMETERS.md`.)
The chapters have to be readable and confident enough to be worth reading, while never
letting a reader come away thinking any of it has been measured. The mechanism is the
same one used elsewhere: the claim goes in the main text, the caveat goes in the main
text beside it, and the full accounting goes in the Machinery.

**The retired threshold result may be quoted as current** if its obsolete environment is
not adjacent to it. The chapter now labels it as a diagnostic rather than a baseline result.

**Chapter 12 risks being a model tour.** See the note above.

**And the standing constraint from Part One applies throughout:** nothing in Part Three
can tell any individual how their recovery is going. The model has never been tested
against a single real person. Chapter 25 says this at length, but Parts Three and Five
are where a reader is most likely to start believing otherwise, and each chapter should
carry a line to that effect rather than deferring it all to the end.

**That constraint is now under more strain, because of a document added 5 August 2026.**
`reference/PRIMER-steps-and-traditions.md` restates this part's per-Step figures, the
group-dependence coefficients, the gate exposures, the service results, once for each of
the twelve Steps, and it restates each of them a second time in plain English. A per-Step
list written in plain language is the format in the whole project that most invites being
read as advice about how to work the Steps. The primer's entries were written against
that risk and two of them still lean toward it, both recorded in the progress log. Any
future edit to those entries should be checked against this section before it is saved.

The mechanical part of the same problem: the primer is derived, it asserts nothing and no
checker reads it, so a corrected figure in Chapters 12 to 15 has to be carried there in
the same session. `CLAUDE.md` has the rule.

---

## 6. Release-gate corrections, opened 6 August 2026

The parameter and measurement layer will be regenerated after the model correction:

- all lognormal capability draws are mean-centred at one;
- the \(\rho\) exercise is described only as a modest proxy-averaging result, not as proof that the latent state is recovered;
- the recipient statistic is labelled opportunity per potential helper for low- and high-practice members, with a clean resource-override ablation that holds \(S\), \(\beta\), and the realized group fixed;
- “118 registered parameter–statistic pairs” replaces any suggestion that 118 independent parameters were tested; and
- exploratory screens are distinguished from confirmatory paired contrasts, with explicit seed, horizon, replication, tie, and conditioning rules.

Every cache depending on capability heterogeneity, resource allocation, or survival must be treated as invalid until regenerated with provenance.

### Chapter Fourteen correction

The pre-release individual-attractor calculation froze a resource vector and group-capacity
constant from the uncentred-heterogeneity model. Re-estimating those state-dependent inputs
from 400 corrected full-adherence endpoints leaves a capability-one high/low-start separation
above 0.05 in only 7 environments (1.75 per cent); the mean environment has one near-zero
maintenance attractor. Retire the typical-member bistability, separatrix and eleven-week
hysteresis values as baseline results. Preserve them only as a labeled obsolete-environment
diagnostic, keep the fitted double-well literature as external motivation, and report the
corrected group decay sweep without claiming it averages individual cliffs.
