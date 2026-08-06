# Chapter Twenty-Two
## What You Cannot Engineer

Suppose you could choose who was in the room.

Not who becomes a member, since Chapter Nineteen sets out why the Third Tradition removes that decision from the group, but who founds a new meeting. A district starting a group in a new town has to send somebody, and it is a natural thought that the sending should be designed. Send five very experienced members and let them anchor it. Or spread the experience thin across many, so that nobody dominates. Or split the difference and send a solid dozen.

The question has an obvious appeal, because it is the one lever in this whole book that an organisation could actually pull without changing anything about itself.

There is a very good study of what happens when somebody pulls it, and it is worth the whole chapter.

---

In 2013 Scott Carrell, Bruce Sacerdote and James West published the result of an experiment they had run on entering freshmen at the United States Air Force Academy. The Academy assigns cadets to squadrons, squadrons are where the studying and the living happen, and for years the assignment had been random. Random assignment is a gift to a researcher, because it gives clean estimates of how much your peers affect your grades, free of the usual problem that people choose their friends.

The three of them had those estimates. They were good estimates, from real data, on the actual population, with the actual outcome measure. And the estimates were non-linear in an interesting way: they suggested that a low-ability cadet did better when surrounded by high-ability ones, and that high-ability cadets were not much harmed by the company.

So they did the thing the estimates invite. They wrote an assignment algorithm to maximise the performance of the weakest students, took half the incoming cohorts, and built squadrons designed to help: roughly fifteen of the lowest-ability students placed with roughly fifteen of the highest, and the middle left out of those squadrons entirely. The other half of the cohort was assigned as before.

Their own model predicted that the bottom third of the academic distribution would gain, on average, 0.053 grade points, and that the strong students would be unaffected. That is a modest, sensible, well-founded prediction.

What they measured was a treatment effect of **minus 0.061 grade points** on exactly the students they had set out to help, statistically significant at conventional levels.

Not zero. Negative, and of the same size as the intended gain, in the opposite direction.

---

The reason is the part that matters here.

The engineered squadrons did not behave like the observed ones. Given a room containing fifteen strong students and fifteen weak ones and nobody in between, the weak students did not spread themselves among the strong. They found each other. The paper measures this directly, as homophily in peer choice, and finds that low-predicted-grade students in the treatment squadrons actively sought out other low-predicted-grade students at rates the control squadrons never showed.

The peer effect the researchers had measured was real. It was a fact about squadrons where the ability distribution was continuous and people mixed. The moment the distribution was made bimodal by design, the mixing stopped, and the estimated effect described a world that no longer existed.

The authors' first title for the working paper says it better than any summary: *Beware of Economists Bearing Reduced Forms? An Experiment in How Not To Improve Student Outcomes.*

---

This is not a story about peer effects being fake. It is a story about a specific failure mode of good evidence, and the failure mode has a name in economics: the intervention changed the thing being intervened on.

That has a direct bearing on this book, and I want to state it against my own work rather than somebody else's.

Everything in Parts Three, Four and Five is a set of estimated relationships in a model whose members do not choose each other. They contribute to group aggregates and consume from them. Nobody in this simulation avoids anybody. If you engineered a group in the way the Air Force Academy engineered a squadron, this model would have no way of telling you what went wrong, because the mechanism that made it go wrong is not in it.

So when the model is asked whether founding composition matters, its answer should be discounted heavily before it is even read.

---

Here is the answer anyway, because it is worth knowing what the model does say.

Take twenty-five founding members with a fixed total amount of practice between them, and distribute it three ways. Even: everybody at the same middling level. Concentrated: five members near the ceiling and twenty well below. Split: twelve strong and thirteen weak, which is the Air Force Academy's design in miniature.

Run each four hundred times for thirty years.

Even ends at 17.80 members. Concentrated ends at 18.09. Split ends at 17.45. Their ninety-five per cent half-widths are 0.88, 0.99 and 0.93. Endpoint viability is 98.5, 98.75 and 98.5 per cent. Established-member practice is 0.2645, 0.2628 and 0.2660.

Unresolved. Relative to even founders, the paired membership difference is 0.29 [-0.90, 1.48] for concentrated and -0.35 [-1.47, 0.78] for split. Neither interval excludes zero, and no equivalence margin was specified in advance, so the experiment establishes neither a difference nor practical equality.

The old draft said the split condition was lowest on all three measures. It is now lowest on membership but highest on established practice, another reason not to narrate an ordering the paired contrasts do not resolve.

---

What should be concluded from a null result produced by a model that could barely have produced anything else?

Very little on its own, and something in combination.

On its own, the experiment says only that these 400 paired runs do not resolve the contrasts. Founding practice changes the ordering gates, resource capacities, dropout, attraction and maintenance immediately, so it is not a one-channel test. Without a prespecified equivalence margin, failure to reject a difference is not evidence that composition has no meaningful effect.

The Air Force Academy result still says that engineering composition from measured peer effects can backfire because people re-sort. The simulation adds no directional evidence about the upside or downside of arranging a founding group. Its value is diagnostic: it shows how little this aggregate model can identify about a relational intervention.

---

There is a version of this that a fellowship might actually face, and it is worth separating from the version I have modelled.

Nothing in AA assigns anybody to anything. There is no algorithm, no district officer with a spreadsheet, and no mechanism by which a person could be placed in a meeting against their inclination. People go to the meeting near their house, or the one at the right time, or the one where they know somebody. If the Air Force Academy's cadets could re-sort inside a squadron, an alcoholic can simply go somewhere else on Thursday.

So the fellowship is already living in the world the experiment describes, permanently and by construction, and the practical question is not whether to engineer composition but whether the absence of any means of engineering it is a cost or a protection.

This model cannot answer that. What Part Five's other chapters suggest is that the variables which actually move the outcome by ten or fifteen members are not about who is in the room at all. Whether people are carrying the message. Whether anything outside sends people in. Whether the room keeps the ones who come. Those are large effects, they are about what the room does rather than who is in it, and none of them requires anybody to be assigned anywhere.

---

## The Machinery

### 1. What the model says

Founding composition enters every state-dependent channel at once. Each founder receives the same initial value on all twelve Steps, so changing the distribution changes step-order gates, maintenance, resource capacities, dropout risk and attraction at the start of the run. The three conditions use the same random streams, including the same slot-specific mean-one heterogeneity draws, which makes the contrasts paired but does not isolate a single mechanism.

Resources are still computed from aggregates; no member's state appears in another member's growth equation except through those aggregates. The model therefore has no representation of mentoring, pairing, cliques or sponsorship. **It also has no representation of the mechanism that produced the Air Force Academy result**, which is people choosing whom to associate with after composition was arranged. An unresolved result should be read against that absence.

### 2. The technical version

Three founding conditions, twenty-five founders each, identical total initial practice of 13.75 across the group, 400 seeds per condition, thirty-year horizon.

- **even**: all twenty-five at 0.55.
- **concentrated**: five at 1.00 and twenty at 0.4375.
- **split**: twelve at 0.90 and thirteen at 0.2269.

Viability carries a 95 per cent Wilson interval; continuous means carry a 95 per cent half-width. Conditions share seeds and random streams, so comparisons use paired differences.

| Condition | Endpoint viable | 95% interval | Mean N | ± | Established practice | Established count |
|---|---|---|---|---|---|---|
| even | 0.985 | 0.968 to 0.993 | 17.80 | 0.88 | 0.2645 | 13.97 |
| concentrated | 0.9875 | 0.971 to 0.995 | 18.09 | 0.99 | 0.2628 | 14.16 |
| split | 0.985 | 0.968 to 0.993 | 17.45 | 0.93 | 0.2660 | 13.89 |

Paired membership differences relative to even are concentrated 0.29 [-0.90, 1.48] and split -0.35 [-1.47, 0.78]. No equivalence margin was prespecified. The correct verdict is unresolved, not equal and not null.

**The design cannot separate dispersion from threshold composition.** All twenty-five founders exceed the 0.1 established threshold in all three conditions. The counts exceeding the stricter 0.5 experienced threshold are 25, 5 and 12. A difference, had one resolved, could not have been attributed to variance rather than to this threshold composition or to any other state-dependent channel changed jointly.

**What would make this a real test.** A version of the model in which a member's growth depends on the states of particular other members rather than on aggregates, and in which members can choose which other members to attend to. That second half is what the Air Force Academy experiment turns on and it is the harder of the two to build. Together they are a different model, not a different run, and it is the largest single piece of work outstanding on the technical side of this book.

### 3. Notes on sources

**Carrell, Sacerdote and West is now read at source and it carries this chapter.** The earlier version of this chapter was 762 words, marked provisional, and said it should not be written at full length until the paper was in hand, per `plans/PART-5-PLAN.md`. The paper was obtained on 2 August 2026 from the lead author's university page. Figures used here, all from the paper itself: the predicted gain of 0.053 grade points for the bottom third of the academic distribution, the observed treatment effect of minus 0.061 on the lowest-ability students, significance at p = 0.055, the design pairing roughly fifteen lowest-ability with roughly fifteen highest-ability cadets, and the homophily finding that low-predicted-grade students in treatment squadrons actively sought out other low-predicted-grade students.

**The working-paper title is quoted because it is the authors' own framing.** The NBER record for working paper 16865 notes that an earlier version circulated as *Beware of Economists Bearing Reduced Forms? An Experiment in How Not To Improve Student Outcomes.*

**Where the analogy is strained, and it is.** Cadets are assigned to squadrons and cannot leave them; AA members assign themselves to meetings and can leave at any time. So the experiment's setting is one where engineering was possible and backfired, and the fellowship's setting is one where engineering is not possible at all. The chapter says this rather than letting the analogy carry more than it can. What transfers is the mechanism, not the situation: a measured relationship between people and their peers stopped holding once the peer groups were built from it.

**The model's null is honestly weak and the chapter leads with that**, because a null from a design that could barely have produced anything else is the sort of result that looks like evidence and is not.

### 4. References

**Read in full:**

Carrell, S. E. B. I. Sacerdote and J. E. West (2013). "From Natural Variation to Optimal Policy? The Importance of Endogenous Peer Group Formation." *Econometrica* 81(3): 855-882. doi:10.3982/ECTA10168. **Read at source** from the author's copy at the University of California, Davis. Earlier circulated as NBER Working Paper 16865, March 2011, under the title *From Natural Variation to Optimal Policy? The Lucas Critique Meets Peer Effects*, and before that as *Beware of Economists Bearing Reduced Forms?*. Used here for the design, the predicted and realised treatment effects, and the homophily mechanism. **In copyright; the full text is not stored in this repository.** See `research/SOURCES.md`.

**Cited at a remove:**

Nothing.

**Internal, and reproducible from this repository:**

`model/part5_runs.py` for the composition experiment and for the three lines it duplicates from `simulate()` in order to seed founders individually. `research/part5.json`, `model/book-calculations.ipynb` section 14.

**What was not read:**

Any literature on peer-group composition in mutual-aid settings specifically. The Air Force Academy is a residential military institution with assigned membership and graded outcomes, and I have found nothing comparable on voluntary fellowships. Whether districts in fact think about composition when starting a meeting is also something I have not investigated; the chapter's opening premise is a natural thought rather than a documented practice.
