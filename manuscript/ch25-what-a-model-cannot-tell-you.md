# Chapter Twenty-Five
## What a Model Cannot Tell You

There is a person in this book who never appears.

Every equation in it has a term for him. He is a row in a matrix, twelve numbers between zero and one, a hazard rate, a contribution to somebody else's resource supply. When the model reports that a group holds forty-two members at thirty years, he is one of the forty-two, or he is one of the ones who is not there any more, and the model does not distinguish those two outcomes in any way that would matter to him.

It is worth setting out precisely what the book has done to him and what it has not, because the temptation at the end of a project like this is to let the apparatus imply more than it holds.

---

Nothing in this book can tell you whether anyone is recovering.

The quantity the model calls practice is not a measure of a person's condition. It is a number that goes up when the group supplies what a step consumes and down when it does not, and its units are arbitrary. When Chapter Twenty says an unreferred group's survivors sit at 0.348 against a healthy group's 0.338, that is a comparison between two simulated populations on a scale I invented. It is not a statement that anybody is doing well.

Nothing here can tell you whether a particular meeting is a good meeting.

The model has four failure modes and a healthy case, and a real room is not in one of those states. It is in some combination of all of them, changing week to week, with a history the model has no representation of and people in it whose reasons for being there the model does not encode. A person who reads Chapter Twenty and starts assessing their home group against the three fingerprints will be doing something the model does not license.

Nothing here can tell anyone what to do.

The strongest practical-sounding claim in the book is that a fellowship cannot see the failure that kills it by looking at the health of its groups, and would have to count groups instead. That is a claim about what a measurement would show. It is not advice, it is not addressed to anybody in particular, and it comes with no estimate of what acting on it would cost.

---

There is a specific way this could go wrong and it is worth naming rather than gesturing at.

The book argues that three Traditions implement a formal condition for reliable group deliberation. Suppose that is right. It does not follow that a group failing the condition is failing its members, and it particularly does not follow that a member of such a group is worse off.

The condition is about whether a group's collective judgement converges on the truth as the group grows. That is one thing a group does. It is not obviously the main thing this kind of group does, and I have not argued that it is. A room might reach unreliable conclusions about every question put to it and still be the place where somebody stopped drinking, and the model has nothing to say about that person, because what happened to him is not in the outcome variable.

I have tried throughout to say "a group's decisions are more reliable" rather than "a group is better". Where I have slipped, the slip is mine and it is the error this chapter is most concerned about.

---

The people in Part One are the other case, and they need a different kind of care.

John Hawkins was a hatter who drank for twenty years, was reclaimed in June 1840, spoke to the Maryland legislature within eight months, and spent the rest of his life at it. John Gough was the most famous reformed drunkard in America and was found, in 1845, in circumstances he described by writing *I have fallen*. William Mitchell was a tailor who proposed a joke and made it into an institution. Six men in a bar in Baltimore.

They are used in this book as evidence. Their movement is a control case: the fellowship that had the same insight and did not last, whose absence of certain rules makes the presence of those rules in AA legible. That is a legitimate use of history and it is what historical evidence is for.

It is also a use that flattens them. Gough's relapse appears in Chapter Three because of what it cost a movement whose credibility sat in named men, and the sentence *I have fallen* is quoted because it is more honest than the account I expected to find. It was also a very bad week in a man's life, and he did not write it to illustrate a point about institutional design.

I do not think there is a way to write this book without doing that. I do think the reader should know it is being done.

---

And there is the fellowship the book is about, which has asked not to be spoken for.

Everything here is written from outside. The Traditions are read as text, the model is built from a reading of that text, and no part of the argument was checked by anybody with standing to check it except in the single instance Chapter Twenty-Three records, where a reader with experience of the fellowship found a scenario I had built that the Third Tradition makes impossible.

That correction is the only place in the book where the institution's own knowledge entered, and it improved the work more per sentence than anything else. What that suggests about the rest of the book is not comfortable.

The fellowship also has a rule about this. Its members do not speak for it, and it does not speak through its members, and a book which claims to have found the mathematics underneath its constitution is doing something the constitution would view with suspicion. Anonymity at the level of press and film is a rule about not lending the name to arguments. This book does not have the name and does not claim endorsement, and that is the most it can honestly say.

---

So what is left.

A set of ideas has been shown to be consistent. A fellowship's rules turn out to have a shape that can be described formally, and the description is not vacuous: it implies things that could have been false and are not, and it implied several things that were false and had to be removed. A movement that lacked those rules died, and the model gives an account of how a movement can die without anybody inside it noticing, which is a candidate explanation for a silence in the historical record and is not more than that.

Against that: a hundred and eighteen chosen numbers, two matrices built by one person, a central mapping that no computation touches, and no contact with any real group at any point.

The right way to hold the two is not to average them. It is to notice that they answer different questions. The book shows that a particular explanation is *available*. Whether it is *true* is a question about the world, and nothing in these pages has been near the world.

---

There is one thing I did not expect and will say plainly.

I started this to find out whether an argument worked. What the work actually did was find twenty-five errors, most of them mine, and each correction made the claim smaller. The decline figures shrank. The twelve counts became seven. The most robust thing the simulation says turned out to hold on one measure and reverse on another. Part Four learned that it rests on judgement and not on structure. The book at the end claims considerably less than the book at the beginning intended to.

That is what it is supposed to feel like, and it took me longer than it should have to recognise it.

The Washingtonians wrote their principles down in 1842, in a pocket manual, with directions for starting a society and a section admitting how much their societies disagreed with each other. They had four of the five rules this book calls protective and none of the seven it calls enabling, and they were gone within a decade. Alcoholics Anonymous wrote twelve points in 1946 which its author insisted were not rules and could never become law, and it is still here.

I have spent a long time on why. I am fairly sure the answer is in this book. I am not sure it is the part I think it is.

---

## The Machinery

### 1. What the model says

Nothing. This is the only chapter in the book without a model result in it, and that is deliberate.

The one methodological point worth recording is about the outcome variable. Every quantitative claim in this book is about membership, group survival, or a scale I have called practice. None is about a person's condition, and the model contains no representation of harm, of suffering, or of anything that happens to somebody who leaves. A member who drops out is a row that stops contributing. The model's silence on what that means is total and is not an oversight; it is the boundary of what an aggregate model can be built to say.

### 2. The technical version

There is none, and the absence is itself the content of the chapter.

For completeness, the three quantities the book reports and what each is not:

**Membership**, the count of living rows at a horizon. Not a count of people helped, since it does not track anyone who left, and Chapter Twenty-One shows that a group can hold its membership while its population turns over completely.

**Survival**, the fraction of runs ending above five members. Not a measure of a fellowship's health, since a fellowship of small stable groups and a fellowship of large fragile ones can score identically.

**Practice**, the mean of twelve numbers between zero and one. Not a clinical measure, not validated against anything, and not comparable between model configurations except in the ordinal sense the sensitivity work supports. Appendix A6 records that it is calibrated to a stylised fact rather than to data.

### 3. Notes on sources

**This chapter makes no factual claims that require sourcing**, with two exceptions.

The biographical details in the fourth section are from Chapters One and Three and carry those chapters' sourcing: Hawkins from his son's 1862 compilation read at source, Gough from his 1869 autobiography read at source, the founding from Harrison 1860 and Marsh 1866 read at source. The phrase *I have fallen* is Gough's own and Chapter Three gives its context.

The characterisation of the Washingtonians' written code in the closing section is from Grosh's *Washingtonian Pocket Companion* of 1842, read at source, and the count of four protective and none of the enabling is Chapter Eighteen's.

**The claim about the institutional correction is at one remove and cannot be otherwise**, as Chapter Twenty-Three also records. It came from a reader, not a document.

**What this chapter cannot source and should not be read as sourcing.** Every statement about what the fellowship would think of this book. I have inferred those from the text of the Traditions and I have no standing to make them.

### 4. References

**Read in full:**

Nothing new to this chapter. All sources named are cited in the chapters the material comes from.

**Cited at a remove:**

Nothing.

**What was not read:**

Anything written by the fellowship about itself for its own members, all of which is in copyright and none of which this project acquires. So the book's account of what AA thinks it is doing comes from an independent historian reading AA's archives, and its account of what AA's rules say comes from the short published text, and at no point does the institution speak here in its own voice.
