# Chapter Nine
## Confident and Wrong

The condition in the last chapter says nobody may keep a fixed share of the answer. This chapter is about the three ways that goes wrong, and about why none of them looks like anything going wrong.

They are not exotic. Each has a face you would recognise from any long-running meeting, and each was named, in the abstract, by the two economists who proved the condition. They called them prominent agents, insufficient dispersion, and imbalance. In a church basement they have other names.

---

The first is the old-timer.

He has twenty-two years. He was there when the meeting started, in a different building, with different people, most of whom are dead or gone. He does not chair anything, does not want to, and would be embarrassed to hear himself described as influential. When a question comes up he usually speaks near the end, briefly, and afterwards the room settles.

Nobody appointed him and nobody could unappoint him. His weight is not a rule; it is a fact about how people in that room actually listen, which is the only kind of weight that matters.

Say his view accounts for thirty-five per cent of where the room lands. What the arithmetic says is this. At ten members, his share is thirty-five per cent. At fifty members it is thirty-five per cent. At two hundred and fifty, and at five hundred, it is thirty-five per cent.

The meeting can grow by a factor of fifty and his share will not move, because his share is not a function of how many people are present. It is a function of how they listen.

And so the group's accuracy stops improving. A room with flat influence gets steadily better at deciding things as it grows: off by 0.25 at ten members, 0.11 at fifty, 0.04 at five hundred. The room with the old-timer starts at 0.33, improves to about 0.28, and stays there forever. By five hundred members the healthy room is roughly eight times the more accurate of the two, and it has been that way for years without anybody noticing, because nothing ever went wrong on any particular evening.

---

The second is the caucus.

Three or four long-timers who have been sober a long time and who talk to each other constantly. They are close friends. They mean well, and they are usually right, which is a large part of the problem. By the time a question reaches the business meeting they have discussed it among themselves, and what happens in the meeting is less a deliberation than a ratification with commentary.

Say the three of them hold half the influence between them. Then no individual holds more than about seventeen per cent, which sounds much healthier than the old-timer's thirty-five. It is not. The group's error settles at 0.23 instead of 0.28, which is an improvement of less than a fifth, and it is just as permanent.

This is the failure mode that hides best, because if you go looking for a dominant individual you will not find one. Everyone will tell you, honestly, that no single person runs the group. That is true and it is beside the point. Influence does not have to be concentrated in a person to be concentrated.

---

The third is the strangest and it took me by surprise when I computed it.

Picture five members who are widely respected. Everybody in the room listens to them. And they, in turn, listen mostly to each other, because they have been sober longest and have the most in common and have long since stopped expecting to learn much from the newer people.

There is nothing malicious in it. It is what happens naturally when a group develops a core.

Attention now flows in one direction. Five people receive a great deal of it and return almost none. And the mathematics of that arrangement is brutal in a way I did not anticipate: in the limit, those five hold **all** of the group's influence. Not most. All. Everyone else holds approximately nothing.

Which means a meeting of two hundred and fifty people, structured this way, decides exactly as well as a meeting of five. Its error is 0.357, which is precisely what you get from averaging five independent views. The other two hundred and forty-five members are, from the point of view of the decision, not in the room.

They are talking. They are being heard, in the ordinary social sense. Their views are simply not entering the answer, because the people whose views do enter the answer are not updating on them.

---

Here is what the three have in common, and it is the thing this chapter exists to say.

**None of them produces an argument.**

The dominated group reaches consensus. The caucus-run group reaches consensus. The group with the closed core reaches consensus, smoothly, probably faster than a healthy group would. There is no deadlock, no faction, no shouting, no split. Everybody gets to speak. People genuinely change their minds during the discussion, which is what makes the influence real rather than nominal.

From a chair in the room, on any given evening, a group that has stopped aggregating information looks exactly like a group that is aggregating it beautifully. The visible features of good deliberation are all present. What is missing is invisible: the thing that was supposed to happen to everybody's errors did not happen to them.

And it gets worse as the group grows, in a specific and cruel way. The healthy group is getting better. The broken group is not. So the gap widens year after year, while the broken group's confidence, if anything, increases, because it is larger than it used to be and larger groups feel more authoritative.

At ten members you cannot tell them apart. By five hundred one is eight times more accurate than the other. Neither has any internal signal telling it which one it is.

---

There is a reason to care about the first of these beyond the abstract, and his name was John Gough.

He relapsed twice, in 1843 and 1845, and the first time nothing happened. Chapter Three set out why: by 1845 a movement had made him load-bearing, and load-bearing men get sick. What that cost, and which of the three failure modes above the Washingtonians actually had, is the subject of Chapter Eleven, once the rest of the machinery is in place.

---

The fellowship's own founding text was not settled by a room either, and it is worth seeing how without pretending the comparison proves anything. The draft of the Big Book went out for comment early in 1939, and the comments came back onto a single copy, which survives in facsimile. An outside psychiatrist, Dr. Howard, is named in its margins on seven pages. One of his changes, "Faith" for "God" in a sentence about working twenty-four hours a day, went into print; another, to the "Heavenly Father" who closes one of the Akron stories, did not. Wilson, in a talk the facsimile's editors reproduce, remembered his own part in the arguments as the umpire's. And two of the typed stories describe the Akron group as gathered round its doctor, one of them calling him its "human center". Those are prominent agents in this chapter's sense, in the fellowship's first months, described by the members without complaint. They are an analogy and not a test. One pass of editorial collation is not repeated averaging, the theorem is about beliefs rather than texts, and nothing here shows that the founding text was wrong. What the pages show is how the fellowship settled things before it wrote down the rule this book is about.

---

One more thing, and it is the reason the Traditions are addressed to groups rather than to individuals.

In the model underneath this book, group resources are built from member states,
but not with one common linear weight. They use means, threshold counts, sums,
dispersion and saturation. The return path is nonlinear too: resources are
normalized into Step bundles and then pass through beta, sequential gates,
maintenance capacity and remaining headroom. So the earlier shorthand that
damage travels upward at weight one and downward at beta was wrong.

What remains defensible is narrower. The authored consumption matrix gives some
Steps a larger resource-supported share of growth than others. That is a
within-model dependence index. It is not a reciprocal transmission ratio and it
does not say that a single member's collapse reaches the group without discount.

Which is why the Traditions are addressed to groups. An individual's recovery is his own; the Steps are for that. What the Traditions protect is the thing that no individual can repair on his own, and that everyone's recovery draws on.

---

## The Machinery

### 1. What the model says

Three failure modes, three arrangements of the trust matrix.

The **dominant member** is Golub and Jackson's prominent agent: one member receives a fixed share of everyone's attention. The **caucus** is their insufficient dispersion: a small subgroup receives a fixed share collectively while no individual is dominant. The **closed core** is their imbalance: a subgroup receives far more attention than it gives.

Imbalance is qualitatively worse than the other two and I did not expect that before computing it. The first two put a floor under the group's error. The third effectively deletes the rest of the group from the calculation: in the limit, all influence accrues to the closed subgroup, and the group's accuracy is exactly that of the subgroup alone, regardless of how many other people are present.

The practical reading is that the dangerous question about a group's core is not whether it is respected. It is whether it listens.

On direction: no state-free transmission ratio is implemented. A local effect
would need a specified state, perturbation and derivative; a long-run effect would
need a paired trajectory contrast.

### 2. The technical version

Influence vectors are the normalised left dominant eigenvectors of row-stochastic trust matrices. Consensus error is computed in closed form as the length of the influence vector times the square root of two over pi, as derived in Chapter Eight. All figures use sigma = 1, against a single-person baseline of 0.798.

**Maximum influence weight:**

| N | flat | dominant | caucus of 3 | closed core of 5 |
|---|---|---|---|---|
| 10 | 0.100 | 0.350 | 0.167 | 0.200 |
| 50 | 0.020 | 0.350 | 0.167 | 0.200 |
| 250 | 0.004 | 0.350 | 0.167 | 0.200 |
| 500 | 0.002 | 0.350 | 0.167 | 0.200 |

**Consensus error:**

| N | flat | dominant | caucus of 3 | closed core of 5 |
|---|---|---|---|---|
| 10 | 0.252 | 0.328 | 0.275 | 0.357 |
| 50 | 0.113 | 0.289 | 0.238 | 0.357 |
| 250 | 0.050 | 0.281 | 0.232 | 0.357 |
| 500 | 0.036 | 0.280 | 0.231 | 0.357 |

Constructions: dominant, one member receives 0.35 of every row, remainder split evenly. Caucus, three members receive 0.50 between them. Closed core, five members receive 0.45 of every row and distribute their own attention only among themselves.

The analytic limits confirm the tables. Dominant tends to 0.35 times the square root of two over pi, which is 0.279. The caucus tends to 0.230. The closed core sits at exactly the square root of two over pi divided by the square root of five, which is 0.357, the error of a five-member group: the influence of the outside members is identically zero at every N, which is why that column does not vary.

**Dependence index.** Normalized row sums of the authored consumption matrix run
from 0.17 for Step 7 to 1.00 for Steps 1 and 12, with a mean of 0.53. They blend
autonomous and resource-supported peer growth inside the Step equation. Their
reciprocals are not implemented member-to-group weights.

### 3. Notes on sources

**Almost nothing in this chapter is reported at a remove.** The theorem is Golub and Jackson, read at source. The trust matrices are constructed and the figures computed rather than cited. The Gough material is from his own 1869 autobiography, read at source, and is treated at length in Chapter Three.

**The 1939 passage rests on the working manuscript**, read on every page on 12 September 2026, and each point in it was checked against the facsimile's page images. Dr. Howard is named on MS pp. 10, 11, 18, 19, 23, 46 and 86; a possible eighth mention, on MS p. 56, is too faint at the resolution checked to count. The "Faith" change is on MS p. 11 and the "Heavenly Father" request on MS p. 86, and the printed wording of both was checked against the 1939 text. The Akron descriptions are on MS pp. 128 and 132. Two things are at a remove: the draft's date and circulation, which are the facsimile editors' account, and Wilson's description of himself as umpire, from a 1954 talk they reproduce. The comparison with prominent agents is an analogy, for the reasons the text gives.

**The closed-core result is new to this project** in the sense that I had not computed it before writing this chapter. It is not new to the literature: it is a direct consequence of Golub and Jackson's imbalance condition, and the fact that a closed subgroup captures all influence in the limit is standard for absorbing states in Markov chains. What is worth reporting is the magnitude, which is much starker than the other two failure modes and which I would not have guessed.

**The extension from group deliberation to public reputation, in the Gough passage, is an analogy and not an application.** The theorem concerns members averaging beliefs about a shared question. What the outside world believed about the Washingtonians was not formed that way. I have flagged this in the text rather than relying on the reader to notice.

**The dependence index rests on a hand-written matrix.** It is a normalized
summary of the author's resource assignments and inherits their uncertainty.

### 4. References

**Read in full:**

Golub, B. and M. O. Jackson (2010). "Naive Learning in Social Networks and the Wisdom of Crowds." *American Economic Journal: Microeconomics* 2(1): 112-149. The three obstructions to the wisdom condition: prominent agents, insufficient dispersion, and imbalance.

Gough, J. B. (1869). *Autobiography and Personal Recollections of John B. Gough.* Springfield, Mass.: Bill, Nichols & Co. The September 1845 episode; treated in Chapter Three.

*The Book That Started It All: The Original Working Manuscript of Alcoholics Anonymous.* Center City, Minn.: Hazelden, 2010. A colour facsimile of the multilith copy onto which the comments on the 1939 draft were collated. **Read in full on 12 September 2026**, every facsimile page, from photographs the Human Author took of their own copy; held as a git-ignored reading copy in `research/incorporated/WorkingManuscript_1939/` and never committed. Used here for the single collated copy, Dr. Howard's marginal notes, and the two Akron stories that describe the group as centred on its doctor.

*Alcoholics Anonymous*, 1st ed. (1939). New York: Works Publishing. Held as the 1999 Alcoholics Anonymous Big Book Study Group reprint in `research/incorporated/BigBook_1939/`. For this chapter, the printed wording of the two passages Dr. Howard marked.

**Cited at a remove:**

The facsimile editors' essays in *The Book That Started It All* (2010), for the date and circulation of the 1939 draft, and Wilson's 1954 talk as they reproduce it, for his description of himself as the umpire.

**Referenced but not reproduced:**

The Twelve Traditions of Alcoholics Anonymous, paraphrased. The text is copyright Alcoholics Anonymous World Services, Inc. and is not reproduced here.

**Internal, and reproducible from this repository:**

Influence weights and consensus errors for four governance regimes at N = 10, 50, 250 and 500, with the analytic limits. Per-step group-dependence coefficients from the model module. Code in the companion notebook.

**What was not read:**

Any measurement of attention or influence inside a real mutual-aid group. The three regimes in this chapter are constructed matrices, not observed ones, and appendix A8 sets out what would have to be measured to know whether any of them resembles a meeting. Chapter Twenty-Four lists that measurement and admits it may not be obtainable ethically in an anonymous fellowship.
