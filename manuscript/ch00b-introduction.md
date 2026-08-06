# Introduction
## Nobody in Charge

In 1840, six drunks in a Baltimore tavern founded a society to keep each other sober. Within four years there were societies like it across the United States and the movement claimed to have reached hundreds of thousands of people. Within ten years it was gone, so completely that a century later almost nobody had heard of it.

In 1935, in Akron, two more drunks founded another one. It is still here, a worldwide fellowship of autonomous groups, and its constitution has stood essentially unchanged since 1950. I do not give a current membership or group count because the AA service document that would support one has been located but not read.

The obvious question is what the second one had that the first one did not, and the obvious answer is a set of twelve rules that the second one wrote down in 1946. This book is about whether that answer is right, and it arrives at a smaller version of it than I set out to prove.

---

The rules are the Twelve Traditions, and their most striking feature is how little they resemble a constitution.

They forbid the group having a leader who leads. They forbid taking money from outside. They forbid organising into a hierarchy. They forbid holding an opinion on anything that is not the group's single purpose. They forbid using a member's name in public. Whoever wants to be a member is one, and the group has no procedure for refusing, though it may restrict who attends a particular meeting.

Written down like that they read as humility, or as the sort of thing an organisation says about itself in a brochure. They are also, on their face, a catalogue of ways to be worse at things. An organisation that cannot direct its members, cannot accumulate capital, cannot build a hierarchy, cannot take a position and cannot screen for commitment is an organisation that has given away every ordinary instrument of effectiveness.

This book is an argument that at least three of those renunciations are not renunciations at all. They are what has to be true before a room that decides by discussion can be trusted with the decision, and there is a theorem that says so.

---

The theorem is not mine. Benjamin Golub and Matthew Jackson published it in 2010, and it concerns what happens when people update their beliefs by listening to each other.

Imagine a room where everyone begins with a rough opinion, each of them wrong in some random direction, and everyone revises toward the average of the people they attend to. The question is whether the room converges on the truth as it gets larger. More people means more information, so it ought to.

Golub and Jackson prove that it does if and only if one condition holds: the largest share of attention held by any single person must shrink toward nothing as the group grows. Not merely be small. Shrink, without limit, as the group expands. If one member, or one clique, or one office holds a fixed fraction of the room's attention however large the room gets, then the room does not converge on the truth. It converges on that person's error, and it does so with increasing confidence.

That is the condition. Three of the Twelve Traditions look very much like the conditions for satisfying it: the one that says leaders do not govern, the one that forbids hierarchy, and the one that keeps names out of the room. A fellowship of alcoholics with no theoretical apparatus at all appears to have arrived, in 1946, at the requirements of a result published in 2010.

That is the book's central claim and I want to be exact about its status before anything else. **The theorem is proved and I have read it. The mapping from those three Traditions onto its condition is a reading of three sentences, it is mine, and nothing computational in this book touches it.** It is the largest unverified step here, and Chapter Twenty-Four says what would settle it.

---

Two other things follow, and both came out differently from how I expected.

The first is about rotation. AA rotates its service positions, and the usual explanation is that this prevents anyone becoming important. The theorem says something sharper: the condition requires the largest share of attention to *shrink as the group grows*, and rotating through a fixed pool of twelve people does not shrink. It flattens out, so a room of eight hundred rotating a dozen people is further from the requirement than a room of fifty doing exactly the same thing. Rotation has to be proportional, and the figure is about a quarter of the membership at every size the model was run at.

The second is about the relationship between the Steps and the Traditions. There are twelve of each, published side by side for more than seventy years, and the natural guess is that they pair off by number. They do not pair off. Not one Step is chiefly served by the Tradition sharing its number, and the two correspondences anyone would guess are reversed: Step Five, telling another human being, is served principally by Tradition Twelve, anonymity; Step Twelve, carrying the message, by Tradition Five, singleness of purpose.

That third result is the weakest of the three and Part Four spends most of its length saying why. Five of the twelve counts follow from a prior fact rather than standing alone. The whole thing rests on the magnitudes in two matrices I built, and it does not survive replacing those magnitudes with random numbers. A reader who thinks the matrices are arbitrary should not be persuaded, and the chapters say so rather than borrowing a robustness argument that was established for something else.

---

There is a simulation running underneath most of this, and it is worth being plain about what it is for.

It represents a fellowship group as twelve perishable capabilities per member, eight things the room produces, twelve adherence dials, and a population that turns over. It has a hundred and eighteen registered sensitivity values, plus fixed constants, structural zeros and design choices, and nothing to fit them to because the longitudinal data such a model would need has never been collected.

A model like that cannot show that anything is true. It can show that a set of ideas is consistent, that a mechanism is available, and that certain things follow from certain assumptions and certain other things cannot. That is worth having and it is not evidence about the world.

What it turned out to be best at was destroying my own claims. The model found that a single-equilibrium version made group collapse mathematically impossible, which meant the first version could not represent the thing the book is about. It found that a decline table I had published was computed from ten random seeds and was wrong by a factor of two when recomputed from four hundred. It found that the most robust thing the simulation says holds on one measure and reverses on another, and that I had never said which measure I meant.

Chapter Twenty-Three is a list of twenty-five such errors, sorted by which instrument caught each one. It is the most useful chapter in the book for anybody doing work of this kind, and it exists because the corrections were more informative than the results.

---

A note on the first fellowship, because it is not only a control case.

The Washingtonians are usually described, in the literature that descends from AA, as a movement that died of having no rules. That description turns out to be false, and I only discovered it late, when the movement's own manual finally came into my hands. They had rules. They wrote them down within two years of founding, printed them in a pocket edition, and circulated a model constitution through a convention and a newspaper.

What they had, in writing, were analogues of four of the Traditions this book calls protective: each society independent and subordinate to none, its funds controlled by its own members, nothing political or sectarian admitted to its meetings. What they did not have was any of the seven this book calls enabling, and on anonymity they took the opposite position deliberately and with an argument, preferring publicity to what their manual calls whisperings and secrecy.

They committed the protective half of the code to paper and none of the rest, and they were finished inside ten years.

That is the comparison this book actually makes, and it is a better one than the version I started with, because it is not rules against no rules. It is one written code against another, and the ones missing from the first are the ones the theorem points at.

---

Three warnings about how to read what follows.

**Every chapter ends with a section called The Machinery**, in four parts: what the model says, the technical version, notes on how far the sources can be trusted, and the references. You can skip the second part of every one of them without losing the argument. The Machinery exists so that a reader who wants to check a number can find it, and so that a reader who wants to know how much a claim is worth can find that too. Where a claim is weak, the Machinery says so, usually at more length than the claim itself.

**No sentence here bears on how any individual is doing.** What the model calls practice is a coordinate on a scale I made up, and it diagnoses nobody. The book cannot grade a meeting either, and it offers no advice to anyone. Chapter Twenty-Five is entirely about that limit, which is why it comes last.

**And the fellowship in question would rather nobody spoke on its behalf.** This account stands wholly outside it, drawing on the published short text of the Traditions and on historians with no stake in the outcome, since AA's own writing is under copyright and the project leaves it alone. On the single occasion somebody who knows the rooms read a draft, they identified a case I had constructed that the Third Tradition rules out, and no other intervention in the project changed as much for as few words. The implication for the parts nobody has checked is uncomfortable.

---

The shape of the book is straightforward.

Part One is the history: the Washingtonians, their fade, the man whose relapse cost them their credibility, and the founding of the second fellowship. Part Two is the theorem and the argument that three Traditions implement it. Part Three is the individual: what a member is, in the model, and what the group supplies them. Part Four is where the two halves meet, and where the book is most speculative. Part Five is how groups die, and contains the one result I did not expect and cannot get out of my head: that the most dangerous failure has no symptoms at all, because a group starved of newcomers from outside looks entirely healthy right up until it is gone.

Part Six is what I do not know, which is a good deal.

A sociologist named Milton Maxwell compared these two fellowships in 1950 and concluded that AA would outlast the Washingtonians on account of its Traditions, singling out anonymity as the one with, in his words, sheer survival value. He was right. He had no way to demonstrate it and no theorem to reach for.

What this book adds is the theorem. Whether the theorem is what Maxwell was actually pointing at is a separate question, and the last chapter returns to it without settling it.
