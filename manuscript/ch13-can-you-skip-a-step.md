# Chapter Thirteen
## Can You Skip a Step?

Ask anyone in AA whether you can skip a step and the answer comes back fast. You cannot make honest amends for harm you never wrote down. You cannot hand your inventory to another person if you never took one. The steps are a sequence, they are in that order for a reason, and people who try to jump to the end are the people you see again in six months.

I think that is probably right. I also think it has never been tested, and this chapter is about why that is stranger than it sounds, and what it would take to settle it.

---

Start with what is actually known, because the honest answer is less than you would expect from a programme that has been running ninety years and studied for sixty of them.

Researchers have measured step work many times. The standard way of doing it, following work by Cloud and colleagues, treats twelve-step affiliation as a combination of meeting attendance, whether a person identifies as a member, and **the sum of steps completed**.

Read that last phrase again, because everything in this chapter follows from it. A sum. Not a sequence. Someone who has done Steps One, Two and Three scores three. Someone who has done Steps One, Nine and Eleven also scores three. The instrument cannot tell them apart.

So the reason nobody has tested whether order matters is not that researchers looked at the question and found it uninteresting. It is that the standard measurement discards the information required to ask it. The question has not been declined. It has been made invisible.

---

There is one study that got closer than any other, and it complicates the folk claim rather than confirming it.

Greenfield and Tonigan followed a hundred and thirty new AA affiliates for nine months, measuring step work at intake and at three, six and nine months, on two different instruments. They open by stating the gap almost exactly as I have: working the steps is widely prescribed, the relative merits of different ways of measuring it have had minimal attention, and even less is known about how step work predicts later drinking.

Then they did a factor analysis, and found that step work does not behave as one thing. It came apart into two components, which they call behavioural and spiritual. The two have different predictors: behavioural step work was stable over time and was predicted by having a sponsor, while spiritual step work actually declined over time and rose with meeting attendance. And they have different consequences. Spiritual step work predicted percentage of days abstinent. Behavioural step work did not predict drinking at all.

That is not what a strict chain looks like.

If the twelve steps were a single sequence in which each link enables the next, you would expect them to move together and to have a common relationship with outcomes. Two separable factors, pulling in opposite directions over time, with only one of them predicting whether people drink, is evidence for something more like two intertwined processes than one ladder.

I want to be careful about how much weight that carries. It is one study, of a hundred and thirty people, using an exploratory method on self-reported data. It does not show that the steps can be done in any order. But it is the closest thing we have to evidence on the question, it arrived before I built anything, and it points away from the simplest version of what everyone says.

---

Here is the move that makes the question answerable.

Instead of asking whether the steps are a chain, ask **how much a person's work on one step can be substituted for by everything else available to them**: their own accumulated practice, what the group supplies, the daily maintenance they are doing. That is a quantity, not a doctrine, and economists have a standard way of writing it down. Cunha, Heckman and Schennach used exactly this apparatus to study how children's capabilities accumulate, where the same question arises in the same form: does early investment have to come first, or can later investment make up for its absence?

Their formulation has a single parameter governing substitutability. Set it very negative and the inputs are strict complements: the whole thing runs at the speed of whatever is missing, and a missing input stops everything. Set it positive and the inputs substitute: plenty of one thing compensates for absence of another.

Now apply that to a step whose predecessor has not been done at all, and watch what happens as the parameter moves.

At the extreme negative end, output is zero. There is no partial credit. That is exactly the folk claim, stated formally: you cannot make amends you have no inventory for, and no amount of meetings or sponsorship or willingness compensates. Bring the parameter up to minus four and it is still zero. Minus one, still zero. Even at exactly zero, the boundary case, it is still zero.

Push it just above zero and the picture changes completely. At 0.3, a person with no prior step at all is running at about 22 per cent of what they would otherwise manage. At 0.6, about 39 per cent. At 0.9, about 48 per cent. The group is carrying them past the gap.

**So the entire question reduces to the sign of one number.** Negative or zero, and the steps are a chain, and everyone in the rooms has been right for ninety years. Positive, and they are more like a menu with a strong recommended order, and a well-supported person can get most of the way without a step they never did.

That is a question with an answer. Nobody has to argue about it.

---

There is a second thing the same apparatus tells you, and it is worth having because it survives whichever way the first question goes.

Ask whether help from the group is worth more to somebody who has done the preceding work than to somebody who has not. In the formulation, that is a cross-partial derivative, and it comes out positive across the entire range: strongly positive when the steps are complements, weakly positive when they substitute, but never negative.

That is dynamic complementarity, and it is the same property Cunha and Heckman found in children's skill formation, where the slogan is that skill begets skill. Here it means something specific and useful. Sponsorship, meetings, the attention of a group: all of it lands harder on someone who has already done some work. Not because they deserve it more, but because there is more for it to attach to.

Which is a reason to be careful with the most natural objection to this chapter. Somebody will say the whole question is idle, because in practice people do the steps roughly in order anyway. Perhaps. But if the chain is real, then a person stalled at Step Four is not merely behind schedule; everything the group offers them is worth less until they move, and that is worth knowing.

---

The last piece is a design requirement, and it is the practical contribution.

Latent practice, how much of a step somebody is actually living, is not observable. What is observable is a questionnaire answer, which is a noisy proxy. AA research already has several: an involvement scale, an affiliation scale, a practices scale, direct step counts.

I ran a deliberately modest proxy-averaging exercise. The simulation supplies the true
inputs and the proxy loadings, adds noise only to output proxies, and repeats each cell
400 times. That is not the empirical problem, where the inputs are latent and group help
is endogenous to member state. It asks only how averaging three noisy outputs changes
the behaviour of this oracle estimator.

The answer is precision, roughly by a factor of two. Near the boundary, estimates have a
standard deviation of 0.07 with three proxies and 0.15 with one. At a true value of minus
four, the figures are 0.31 and 0.65. At a true value of plus 0.5, 399 of 400 one-proxy
runs and all 400 three-proxy runs return a positive estimate. At exactly zero, the sign
splits near half in both designs, as it should.

That result does not establish that three measures are sufficient, necessary, or even
identifying in real data. It shows that averaging several noisy readings can improve
precision when the difficult parts of the measurement problem have already been solved
by assumption. A real study would need a prespecified precision target, a model of error
in the inputs, justified loadings, an anchored latent scale, and a strategy for endogenous
group attention. The practical contribution of this chapter is the estimand and the list
of obstacles, not a three-measure rule.

An earlier draft drew a design rule from one simulated dataset, and the first correction
enlarged that to twenty-five replications without fixing the mismatch between the exercise
and the claim. Four hundred replications now describe this estimator more precisely. They
cannot turn an oracle proxy exercise into validation of a latent-variable design.

Greenfield and Tonigan's result quietly makes the same point from the other direction. They used two instruments on the same people and got materially different answers, with significantly more participants endorsing step work on the indirect measure than the direct one for nine of the twelve steps. Which questionnaire you hand out changes what you conclude. That is not a nuisance to be averaged away. It is the reason the design has to be built around it.

---

I should be plain about what this chapter has and has not done.

It has not shown that the steps are a chain, and it has not shown that they are not. What it has done is take a claim that everyone in AA makes, that has never been tested, and that the standard instruments cannot even express, and turn it into a parameter with a sign, an estimator, and a data requirement.

Whether anybody goes and measures it is not up to me. But it is now the kind of question that could be settled by a study rather than by argument, and it could be settled with instruments the field already has, on populations the field already follows, in about a year.

That is a smaller claim than the one I set out to make. It is also the one the evidence supports.

---

## The Machinery

### 1. What the model says

Each step is written as a production stage combining four inputs: the person's own accumulated practice of that step, their practice of the preceding step, what the group supplies for that step, and their maintenance capacity. The functional form is the constant-elasticity-of-substitution aggregator used by Cunha, Heckman and Schennach for skill formation, with a single parameter rho governing how substitutable the inputs are.

The main result is a reduction rather than a discovery. The informal rule that a step cannot be skipped is the limiting case of this family as rho goes to minus infinity, where the aggregator becomes the minimum of its arguments. That means the folk claim is not a separate hypothesis requiring its own apparatus; it is one point on a continuum, and the continuum is indexed by a number that can be estimated.

The threshold is at zero rather than at minus infinity, which is worth stating because it widens the chain hypothesis considerably. Strict ordering holds for every rho less than or equal to zero, not merely at the extreme. The chain does not require perfect complementarity; it requires only the absence of substitutability.

### 2. The technical version

**This section analyses a formalism that the simulation does not use, and the distinction matters.** The simulation's update rule is the multiplicative one in Chapter Twelve, in which the preceding step enters as a gate raised to an exponent. The constant-elasticity-of-substitution aggregator below is a *reformulation* chosen because it has a parameter that indexes substitutability directly, which the multiplicative form does not. The two agree at the limit that matters: as rho goes to minus infinity the aggregator becomes the minimum of its arguments, and a step with a prior step at zero cannot grow, which is exactly what the simulation's gate does when x(i-1) is zero. Nothing in this chapter's conclusion depends on the simulation being CES, and no figure in the rest of the book is computed from it.

The stage technology, in that reformulation, is

> x(i, t+1) = A(i) * [ g1 * x(i,t)^rho + g2 * x(i-1,t)^rho + g3 * G(i,t)^rho + g4 * M(t)^rho ]^(1/rho)

with weights summing to one and elasticity of substitution 1/(1 - rho). Weights used throughout: 0.30 own stock, 0.30 prior step, 0.25 group input, 0.15 maintenance.

**Output with the prior step at zero**, other inputs at 0.7, 0.8 and 0.6:

| rho | elasticity | output |
|---|---|---|
| -100 | 0.00 | 0.0000 |
| -4 | 0.20 | 0.0000 |
| -1 | 0.50 | 0.0000 |
| 0 | 1.00 | 0.0000 |
| +0.3 | 1.43 | 0.2167 |
| +0.6 | 2.50 | 0.3933 |
| +0.9 | 10.00 | 0.4803 |

**Cross-partial in prior-step stock and group input**, evaluated at (0.7, 0.4, 0.5, 0.6): +1.729 at rho = -4, +0.523 at -1, +0.199 at 0, +0.084 at +0.5. Positive throughout, larger the more complementary the technology.

**Measurement.** A future empirical version would observe latent practice through proxies Z(j) = mu(j) + lambda(j) * ln x + error. The nonlinear factor-model results of Schennach and of Hu and Schennach, as applied by Cunha, Heckman and Schennach, explain what a real identification design would have to solve. The exercise below does not implement that design: it supplies the four regressors and the proxy loadings without error and adds noise only to the output proxies. It is therefore a resolution check under oracle information, not validation of a latent-variable estimator. Any real latent scale would also have to be anchored in an interpretable outcome.

**Proxy-averaging exercise.** Estimand: the substitution parameter rho within the simulated oracle design. Estimator: grid search over 300 points on [-8, 0.95], fitting the rescaled mean of the output proxies against predicted log output with an affine transformation absorbing scale and location. Design: n = 1200 per replication, proxy loadings evenly spaced on [0.8, 1.2], measurement noise standard deviation 0.35, and **400 independent replications per cell**, each with its own seed. Mean and standard deviation across replications:

| true rho | one proxy | sd | three proxies | sd |
|---|---|---|---|---|
| -4.0 | -4.09 | 0.65 | -4.02 | 0.31 |
| -1.0 | -1.02 | 0.16 | -1.00 | 0.08 |
| 0.0 | -0.00 | 0.15 | +0.00 | 0.07 |
| +0.5 | +0.49 | 0.17 | +0.50 | 0.08 |

Bias never exceeds 0.09 in any cell. The modest result is about proxy averaging: with oracle-known inputs and loadings, three output proxies roughly halve the standard deviation. It does not follow that three proxies are sufficient, necessary, or identifying in real data.

**Sign recovery.** At a true rho of +0.5, 399 of 400 one-proxy replications and all 400 three-proxy replications returned a positive sign. At a true rho of exactly zero, the estimate was non-positive in 53.5 per cent of one-proxy replications and 55.5 per cent of three-proxy replications. That near-half split is what an approximately centred estimator at zero should produce; it is not evidence that the empirical sign has been identified.

**The resulting design lesson**, stated narrowly: averaging three output proxies improved precision in this oracle exercise. A real study would have to pre-specify its desired resolution, model measurement error in the inputs, justify the loadings, and solve endogeneity. This calculation supplies none of those things.

**A correction, recorded rather than tidied away.** This table first reported one draw per cell and was then enlarged to twenty-five replications. The release gate found that even the larger version was being described as validation of a latent-variable estimator it did not implement. The current 400-replication version narrows the Monte Carlo error and the prose narrows the claim. Replication can describe the behaviour of this estimator under its assumptions; it cannot repair a mismatch between the exercise and the empirical identification problem.

**The unsolved obstacle.** Group input is endogenous to member state. Groups direct attention toward members who are struggling, and members who are doing well attract sponsees. Estimating this technology without handling that will attribute to the technology what is really selection. Cunha, Heckman and Schennach face the identical problem with parental investment and solve it; adapting their approach is necessary before any of this touches real data, and I have not done it.

### 3. Notes on sources

**The empirical literature is read at one remove.** Greenfield and Tonigan's study reaches me through its published abstract and through summaries of its findings, not through the full paper. The specific claims used here are the two-factor structure, the differing predictors and time trends of the two factors, the finding that only spiritual step work predicted percent days abstinent, and the discrepancy between instruments on nine of twelve steps. All are stated in the abstract. **The full paper should be read before this chapter is final**, and it may well qualify things the abstract states baldly.

**Cloud and colleagues' definition of twelve-step affiliation** as attendance plus self-identification plus sum of steps completed reaches me through a later methodological paper citing it, not from the original.

**Carroll (1993) on adherence to the steps has not been consulted**, and it is the most likely place for a prior treatment of sequencing. It should be checked before this chapter is final.

**I have not established that no experimental test of sequencing exists**, only that none appeared in a reasonable search and that the standard measurement instrument could not support one. Those are different claims and the chapter states the weaker one.

**The formal apparatus is read at source.** Cunha and Heckman (2007) and Cunha, Heckman and Schennach (2010) for the technology and the identification strategy.

**The numbers are computed, not cited**, and are asserted against these printed values in the companion notebook.

### 4. References

**Read in full:**

Cunha, F. and J. J. Heckman (2007). "The Technology of Skill Formation." *American Economic Review* 97(2): 31-47. Self-productivity and dynamic complementarity.

Cunha, F. J. J. Heckman, and S. M. Schennach (2010). "Estimating the Technology of Cognitive and Noncognitive Skill Formation." *Econometrica* 78(3): 883-931. The CES stage technology, the measurement system, anchoring, and the treatment of endogenous investment.

**Cited at a remove:**

Greenfield, B. L. and J. S. Tonigan (2013). "The General Alcoholics Anonymous Tools of Recovery: The Adoption of 12-Step Practices and Beliefs." *Psychology of Addictive Behaviors* 27(3): 553-561. Read via abstract and secondary summary; full text not obtained.

Cloud, R. N. and colleagues (2004). The definition of twelve-step affiliation as attendance, self-identification and sum of steps completed. Reached through a later methodological review; the original has not been located and the co-authors are therefore not named here, which is a defect in this entry rather than a house style.

Schennach, S. M. (2004). "Estimation of Nonlinear Models with Measurement Error." *Econometrica* 72(1): 33-75; and Hu, Y. and S. M. Schennach (2008). *Econometrica* 76(1): 195-216. The identification results underlying the measurement strategy, known through their application in Cunha, Heckman and Schennach.

**Internal, and reproducible from this repository:**

The substitution table and cross-partial series are checked in `model/book-calculations.ipynb`. The 3,200 proxy-averaging jobs, 400 replications for each of four true values and two proxy counts, are in `research/ch13_reps.json`, generated by `model/ch13_reps.py`.

**What was not read:**

Greenfield and Tonigan in full, which is the one study that bears directly on this chapter's question and which is described here from an abstract. Also unread: any work estimating a substitution parameter for a sequential practice of this kind in any domain. The chapter's central move is to say that the folk rule is the limiting case of a family indexed by rho, and that rho is estimable in principle; nobody has estimated it, here or elsewhere, and the chapter should not be read as implying that anybody has.

Carroll, S. (1993). On adherence to the twelve steps.
