# Chapter Ten
## Rotation Has to Be Wide

The Traditions say that service positions rotate. They do not say how many people should be in the rotation, and it turns out that this is the number that matters.

The instruction itself is clear enough and is followed almost everywhere. Terms are typically one or two years. The secretary hands over to somebody else, the treasurer hands over, the group service representative hands over, and the fellowship is unusually firm about it: rotating out of a job you are good at is treated as part of the discipline rather than a waste of talent. Chapter Eight explained why. Rotation stops influence accumulating in anybody, which is one of the three ways AA prevents any single member from holding a fixed share of the group's judgment.

But there is a hole in that argument, and it opens as a group grows.

---

Picture a meeting of four hundred people. Large, but not extraordinary; plenty of city groups run at that size.

It rotates conscientiously. Every position turns over on schedule and nobody serves two consecutive terms in the same job. And, as tends to happen in a large group, the same dozen or so people cycle through those positions between them. They are the ones who volunteer. They are reliable, they know how the group works, and when a position comes open somebody suggests one of them, because who else would you suggest.

Nothing here is a violation. Everyone would describe this group as rotating properly, and by the letter of the thing it is.

Now do the arithmetic. In a group of four hundred where influence is spread evenly, the largest share anybody holds is one four-hundredth, which is 0.0025. In this group, rotating twelve people, the largest share works out at 0.031.

That is twelve times the flat benchmark. The group's error is about 0.089 against 0.040 for an evenly weighted room of the same size, so it is roughly twice as inaccurate as it could be, permanently.

I want to be careful not to oversell this. It is not the disaster that a dominant old-timer is, and it is nowhere near the closed core from the last chapter. A group like this is functioning. It is simply carrying a cost that nobody has any reason to notice, and the cost does not go away.

---

The worse part is what happens as the group keeps growing.

Take that same group with its same dozen volunteers, and let it reach eight hundred members. The flat benchmark halves, as it should: one eight-hundredth, 0.0013. The rotating group's largest share moves from 0.031 to 0.030.

It does not improve. It cannot, because the number of people among whom influence is being shared did not change when the group doubled. Twelve is twelve at any size.

So the gap widens. At fifty members a rotating pool of twelve is twice the flat benchmark. At two hundred it is six times. At four hundred, twelve times. At eight hundred, twenty-three times. The group is getting bigger and the benefit of being bigger is being thrown away, one term at a time, by a practice everybody agrees is correct.

This is the condition from Chapter Eight failing in slow motion. It requires the largest share to *shrink toward nothing as the group grows*. A fixed rotation pool does not shrink. It converges to a floor at roughly the officeholder's share divided by the size of the pool, and sits there.

Rotation, by itself, is not the answer. Rotation is the answer when the number of people rotating grows with the group.

---

So how wide is wide enough?

I ran this for groups of fifty, a hundred, two hundred, four hundred and eight hundred, asking in each case how large the pool has to be before the largest share comes within a factor of two of an evenly weighted room.

The answer is the same every time, and I did not expect it to be.

**About twenty-six per cent of the group.**

Fifty members needs thirteen people in the rotation. A hundred needs twenty-six. Two hundred needs fifty-two, four hundred needs a hundred and four, eight hundred needs two hundred and eight. The proportion does not move.

That is a usable number, and it is the most directly checkable thing in this book. It says: **look at how many different people have held any service position in your group over the last few years, and compare it with how many people are in the group.** If the answer is a quarter or more, the rotation is doing what the Tradition intends. If it is a dozen names in a group of four hundred, it is not, however faithfully the terms are being observed.

Nobody needs a mathematician for this. It needs a service roster and some arithmetic, and both already exist.

---

There is a reason this hole exists in the Traditions, and I think it is worth naming rather than treating as an oversight.

As Chapter Five argued, the Traditions are a record of failures rather than a derivation from principles: what got written down in 1946 was whatever had already gone wrong often enough to generate mail. And in 1946 there were not many groups of four hundred. The failure this chapter describes is one that only appears at a scale AA had barely reached when the rules were written, and it appears gradually, and it never produces an incident anybody would write a letter about.

A group with a narrow rotation does not blow up. Nobody resigns in protest. There is no scandal and no schism. The meeting simply makes slightly worse decisions than it could, forever, and grows without getting better at deciding, and no one inside has any way of perceiving it.

Which is exactly the shape of every failure in this part of the book. The visible signs of a healthy group are all present. What is missing is invisible from any chair in the room.

---

## The Machinery

### 1. What the model says

Rotation is modelled by averaging the trust matrix over a rotation cycle. During each term, one member holds an officeholder's share of the group's attention; over a cycle of R terms, R different members each hold it for one term. Time-averaged influence is therefore roughly the officeholder's share divided by R, plus the flat weight everybody carries anyway.

That produces the central result: a fixed pool gives a **floor** rather than a decline. Maximum influence converges to approximately alpha over R and stays there regardless of group size, while the flat benchmark keeps falling as one over N. The gap between them grows without limit.

The twenty-six per cent figure is the pool size at which maximum influence comes within a factor of two of the flat benchmark, and it holds at every group size tested from fifty to eight hundred. It is a proportion rather than a headcount, which is the practically useful form: the question is not whether a group rotates twelve people but whether it rotates a quarter of itself.

A caveat on interpretation. This is a statement about influence over a rotation cycle, not about any individual meeting. Within a single term the current officeholder does hold a larger share; the model asks what the group's decision-making looks like averaged over years, which is the horizon on which a group's accumulated decisions actually matter.

### 2. The technical version

The rotation matrix is constructed by averaging over a cycle: for each of R terms, a matrix in which one member receives share alpha of every row with the remainder split evenly, then averaged across terms. Influence is the normalised left dominant eigenvector; error is the closed form from Chapter Eight, the length of the influence vector times the square root of two over pi, with sigma set to one.

**Pool sweep at N = 400, alpha = 0.35:**

| Pool R | max influence | error | alpha/R |
|---|---|---|---|
| 3 | 0.118 | 0.165 | 0.117 |
| 6 | 0.060 | 0.119 | 0.058 |
| 12 | 0.031 | 0.089 | 0.029 |
| 25 | 0.016 | 0.067 | 0.014 |
| 50 | 0.009 | 0.054 | 0.007 |
| 100 | 0.005 | 0.047 | 0.004 |
| 400 | 0.003 | 0.040 | 0.001 |

Flat benchmark at N = 400: max influence 0.0025, error 0.040. The alpha over R approximation tracks the computed value closely, which is the check that the mechanism is what the text says it is.

**Fixed pool of twelve, as the group grows:**

| N | max influence, pool 12 | flat benchmark | ratio |
|---|---|---|---|
| 50 | 0.041 | 0.020 | 2.1 |
| 100 | 0.035 | 0.010 | 3.5 |
| 200 | 0.032 | 0.005 | 6.4 |
| 400 | 0.031 | 0.0025 | 12.3 |
| 800 | 0.030 | 0.0013 | 23.9 |

The first column converges; the second does not. That divergence is the whole chapter.

**Pool required to come within a factor of two of flat:** 13 at N = 50, 26 at 100, 52 at 200, 104 at 400, 208 at 800. Twenty-six per cent throughout.

For comparison, at N = 400 a caucus of three holding half the influence between them gives maximum influence 0.167 and error 0.231. A rotating pool of twelve, at 0.031 and 0.089, is well short of that. It sits between the flat case and the concentrated one, closer to flat on both measures, and the honest description is a real but moderate permanent cost rather than a failure of the same kind.

### 3. Notes on sources

**Nothing in this chapter is reported at a remove.** The construction is mine, the theorem is Golub and Jackson read at source, and every figure is computed rather than cited.

**The rotation construction is a simplification and the shape of the result depends on it.** I model an officeholder as attracting a fixed share of attention during their term, and I average over a cycle. Real service positions differ enormously in how much attention they attract: a group service representative is not a coffee maker. A more careful model would give each position its own share and would probably show that what matters is the pool for the few positions that carry weight, not the pool across all positions. That refinement would sharpen the practical advice and I have not done it.

**The twenty-six per cent is a property of my parameter choices**, specifically alpha = 0.35 and the within-a-factor-of-two criterion. Both are judgement calls. What does not depend on them is the qualitative result, that a fixed pool floors while the benchmark falls, and that the required pool scales with the group rather than being a fixed headcount. Treat the proportion as an order of magnitude, not a threshold.

**On the historical claim.** The suggestion that this failure mode is absent from the Traditions because AA had few very large groups in 1946 is my inference, not something I have found stated anywhere. It is consistent with the account in Chapter Five of how the Traditions were compiled, but I have not verified it against the record of what groups actually wrote to New York about.

### 4. References

**Read in full:**

Golub, B. and M. O. Jackson (2010). "Naive Learning in Social Networks and the Wisdom of Crowds." *American Economic Journal: Microeconomics* 2(1): 112-149. The vanishing-influence criterion, and the requirement that maximum influence go to zero as the society grows, which is what a fixed rotation pool fails.

**Cited at a remove:**

Nothing.

**Referenced but not reproduced:**

The Twelve Traditions of Alcoholics Anonymous, paraphrased. The text is copyright Alcoholics Anonymous World Services, Inc. and is not reproduced here.

**Internal, and reproducible from this repository:**

The pool sweep at N = 400; the fixed-pool scaling series from N = 50 to 800; the required-pool calculation at each size. Code and assertions in `model/book-calculations.ipynb`, section 2.

**What was not read:**

Anything about how AA groups in fact rotate service. The claim that rotation must scale with the group is derived from the theorem and from a constructed matrix; whether real groups rotate a fixed dozen or a fixed proportion is an empirical question I have not investigated and that Chapter Twenty-Four proposes as a survey. The Twelve Concepts of World Service, which is where the fellowship's own thinking about rotation is set out at length, are AA copyright and have not been read.
