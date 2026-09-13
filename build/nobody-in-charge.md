---
title: "Nobody in Charge"
subtitle: "How a Fellowship of Drunks Solved a Problem in Mathematics Without Knowing It"
author:
  - "Anonymous"
date: "Draft of 13 September 2026"
documentclass: report
classoption: [11pt, oneside]
geometry: [a4paper, margin=1.05in]
mainfont: "TeX Gyre Pagella"
linestretch: 1.06
toc: true
toc-depth: 1
numbersections: false
colorlinks: true
linkcolor: black
urlcolor: black
header-includes:
  - \usepackage{microtype}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \setlength{\emergencystretch}{4em}
  # Prefer a slightly loose line over one that runs into the margin. Without these,
  # twelve paragraphs overflowed, the worst by 25pt, which is a third of an inch of
  # text sitting outside the type block. Long unbreakable tokens cause most of them:
  # an email address in the preface, file paths, and identifiers TeX will not hyphenate.
  - \tolerance=1500
  - \hbadness=1500
  - \usepackage[htt]{hyphenat}
  - \usepackage{xurl}
  - \usepackage{etoolbox}
  # Let a long word in a narrow table column break.
  #
  # Two things stop it, and both have to go. Pandoc sets each column \raggedright, and
  # LaTeX's \raggedright gives the line infinite stretch, so no line is ever bad enough
  # for TeX to try hyphenating; ragged2e's \RaggedRight is the same alignment with a
  # finite stretch, which lets hyphenation happen. That alone is not enough, because TeX
  # will not hyphenate the first word of a paragraph, and a table cell's content is the
  # start of one. A zero-width space ahead of it makes the first word an ordinary word.
  #
  # Verified on the failing cell at the width the runner gives it: "unwelcoming, combined
  # T3 loss" in a 47pt column overflows by 9.358pt under plain \raggedright, overflows by
  # exactly the same under \RaggedRight alone, and fits under both together, breaking as
  # "unwel-".
  #
  # This is needed because column fractions are not stable across pandoc versions. The
  # runner gives the paper's scenario table a first column of 0.1154 where the local
  # pandoc gives 0.2577. That was confirmed rather than guessed: shaving the table width
  # by 14pt moved the overflow by 1.6156pt, which is 0.1154 of 14pt to four decimals.
  #
  # The shave stays at 1pt, its original size, for pandoc's four-place rounding; removing
  # it costs twelve overfull boxes. Enlarging it makes this case worse, because a narrower
  # column is the problem here and not the cure.
  # Load the language explicitly so hyphenation patterns are certainly active. Without a
  # language selected, whether TeX hyphenates at all depends on the distribution's
  # defaults, and a build that cannot hyphenate cannot break a long word in a narrow
  # table column however the column is aligned.
  - \usepackage[english]{babel}
  - \usepackage{ragged2e}
  - \newcommand{\nictabragged}{\RaggedRight\hspace{0pt}}
  - \AtBeginEnvironment{longtable}{\footnotesize\let\raggedright\nictabragged\addtolength{\linewidth}{-1pt}}
  # Wide result tables were the last thing sitting outside the type block. Pandoc sizes
  # each p-column as a fraction of (linewidth - 2*ncols*tabcolsep), so column padding is
  # taken out of the text before the columns are measured, and a wide table with
  # unbreakable cells starves first. The seven-column scenario table converted from the
  # paper is the binding case: its cells are set maths, which cannot be broken or
  # hyphenated, so a cell that does not fit runs into the margin instead of wrapping.
  #
  # 4pt was too tight to survive a change of platform. The same source built with the
  # Debian packaging of TeX Gyre Pagella rather than the OTFs used here needs about 8.2pt
  # more room on that row, and CI failed on exactly that box on 17 August 2026. Measured
  # headroom, by rebuilding with the table width artificially reduced until a row
  # overflows: 4pt survives a 7pt reduction, 3pt survives between 14 and 20pt, 2pt
  # survives more than 30pt. 3pt is roughly twice what the platform difference costs and
  # keeps the tables looking like a book rather than a spreadsheet.
  - \setlength{\tabcolsep}{3pt}
  - \usepackage{titlesec}
  - \titleformat{\chapter}[display]{\normalfont\Large\bfseries}{}{0pt}{\Large}
  - \titlespacing*{\chapter}{0pt}{0pt}{28pt}
---

# Preface: What This Book Knows, and How

*Nobody in Charge* is by an anonymous author. Released to the public domain under The Unlicense.
See `LICENSE`.

This book makes claims of three different kinds, and they are not equally good. Since the whole argument turns on that difference, it is worth setting out before anything else.

---

The first kind is a **theorem**. Chapters Seven through Eleven rest on a result published by Benjamin Golub and Matthew Jackson in 2010, about when a group that reaches decisions by discussion can be relied upon to be right. That result is proved. It does not depend on anything I chose, and it would be just as true if I had never written this book.

**One warning belongs here rather than three hundred pages later.** The theorem is proved. That three particular Traditions are the things which satisfy it is an interpretation of their wording, arrived at by me, and untouched by any computation in these pages. That step is the book's central assertion and its least verified, and the appendix names it as the largest of the threats to the whole enterprise. When Part Two computes what happens to a group of five hundred with a dominant member, it is doing arithmetic on a matrix I constructed, not running a simulation with parameters I tuned. Anyone can check it by hand.

The second kind is a **claim about history**. Parts One and Six make assertions about what happened in Baltimore in 1840, in Akron in 1935, and in a courtroom in Westminster in 1858. These are only as good as the sources, and the sources vary enormously. Where I have read a document at first hand I say so. Where I am reporting somebody's report of it, I say that too, and the reference list at the end of each chapter separates the two. Several chapters have already been rewritten because a primary source contradicted what a secondary source claimed, and I have left the corrections visible rather than tidying them away.

The third kind is a **simulation result**, and this is where the caution belongs.

---

Underneath Parts Three, Four and Five sits a computer model of a mutual-aid group: members with twelve dials each, the resources a group produces, the traditions that govern the supply of those resources, and people arriving and leaving over thirty years. It is described properly in Chapter Twelve.

The registered sensitivity set contains **118 numeric values**: twenty-two scalar defaults, twelve step speeds, forty-nine nonzero consumption cells and thirty-five nonzero governance cells. That is not a count of every choice in the model. Fixed coefficients, founder and arrival states, the time step, the horizon, the viability threshold, equations and 108 structural zeros are choices too. The blanks encode the author's claim that a relationship is absent; they are not facts discovered by the model.

Not one of those numbers was fitted to data. There is no dataset of AA members' step practice over time to fit them to. Some are borrowed from literatures where analogous quantities have been estimated, some were set to target a stylized group size, and some are simply my judgement about what seemed reasonable. The target now fails: after correcting member heterogeneity to have mean one, 400 runs average 17.80 members and only 1.25 experienced members above the stated threshold, against targets of 45 and 9. I did not retune after seeing the failure. The two matrices are the most judgemental objects of all, and everything in Part Four inherits from them.

A model like that can show that a set of ideas fits together. It cannot show that the ideas are true, and it certainly cannot be run backwards to tell you anything about an individual person.

---

So I did the obvious thing, which is to perturb everything and see what survives.

Every registered value is now examined in several designs. The global screen uses 1,002 independent perturbation draws, 334 at each of twelve and a half, twenty-five and fifty per cent. The multi-level one-at-a-time screen uses 944 endpoints, moving each registered value in both directions at four distances. A tiered screen and a randomized-matrix screen use 1,000 draws each; Morris uses twenty trajectories; the Sobol base sample is 1,024 rows. Those are screens over stated ranges, not proofs that a claim is structural or universal.

The expanded global screen demonstrates why the results cannot be sorted into one robust and one fragile pile. Each draw compares referral loss with pure attraction loss on three separate outcomes. At 12.5 per cent perturbation, final membership is ordered, tied and reversed in 301, 0 and 33 of 334 draws; endpoint viability in 323, 10 and 1; and existence in 318, 16 and 0. At 25 per cent the corresponding counts are 251/1/82, 269/64/1 and 262/72/0. At 50 per cent they are 213/17/104, 201/117/16 and 215/117/2. A sentence saying only that the ordering "survives" would conceal both the outcome and the failures.

Full adherence has the same qualification. It is endpoint-viable in all three common seeds in 302, 291 and 256 of the 334 draws at the three amplitudes, while existence in all three seeds holds in 334, 325 and 287. Those are screening counts from three seeds per parameter point, not estimates of a population probability.

At the unperturbed point, where the estimate does use 400 seeds, the baseline ends at 17.80 members, exists in every run, is endpoint-viable in 98.5 per cent and closes in none. Referral loss ends at 0.51 members, exists in 10.5 per cent, is viable in 2.75 per cent and closes in 89.5 per cent. Pure attraction loss ends at 12.38 members, exists in every run, is viable in 98.5 per cent and closes in none. These are finite thirty-year model outcomes, not historical rates.

The structural audit then changes four choices one at a time and compares them with the base architecture, 400 paired seeds for every condition. Under the corrected mean-one capability model, referral loss has lower existence, lower endpoint viability and lower mean final membership than pure attraction loss in all five architectures. The old result in which the size ordering reversed under three variants came from the retired capability-inflated model and does not reproduce. Agreement across five architectures is useful evidence inside the model, not a theorem about every architecture somebody might write.

The two matrices remain the most judgemental objects in the model. One exact result is worth separating from every screen: the governance matrix is column-normalised, so at full adherence its thirty-five nonzero cells cancel and governance quality is one for every resource. A perturbation design that moves those cells while scoring only a fully adherent group has not tested their magnitudes at all. At partial adherence they are live, and the matrix and sparsity audits report them separately.

---

Which brings me to the sentence this preface used to end on, and why it is no longer here.

It said that what the model rests on is not the magnitudes in those two matrices but their structure, and that the structure is the part of the apparatus I would defend hardest. That is true of some of the book and false of the rest, and the difference is now the most important thing in this section.

**One endpoint comparison does rest on the matrix sparsity pattern rather than its nonzero magnitudes.** Replace every nonzero entry of both matrices with an independent random value and keep only the empty cells: pure attraction loss still ends larger and more viable than referral loss in all 1,000 draws; existence is strictly higher in 999 and tied in one. That does not make the fully adherent group uniformly robust: it is viable in all three screening seeds in 784 of those 1,000 draws. A comparison and an absolute persistence claim are different results.

**The coupling claims of Part Four do not.** Run the same test on the central one, that the numbering does not indicate which Tradition serves which Step, and it holds in 40.6 per cent of draws. It fails more often than it holds. Part Four rests on the magnitudes, the magnitudes are my judgement, and the chapters there argue for them one at a time instead of borrowing a robustness figure earned somewhere else.

And the structure itself is only so firm. Flipping cells of the governance matrix at random, holding the empty rows fixed, Part Four's claims survive a reader who differs from me on about four cells of fifty-six and not one who differs on sixteen. Whether the empty rows belong where I put them is a question no computation in this book can reach; it needs a second person, the form for it is written, and nobody has filled it in.

That correction is the most useful thing in this preface. It is exactly the error the exercise exists to catch, and nothing short of running it would have caught it.

---

There is one more caution and it is the one that matters most.

**Nothing in this book can tell any individual how their recovery is going.** The model has never been tested against a single real person and was never built to describe one. It describes a fictional group of fictional members, and its purpose is to make certain claims sharp enough that somebody could go and check them against real groups, which nobody yet has.

If you are reading this because of your own recovery or somebody else's, the model is not the tool. A sponsor is. A doctor is. This book is about institutions, and it is written by someone with no standing to tell you anything about yourself.

---

The last thing to say is what would make the book wrong.

If a historian shows the Washingtonian movement declined for reasons other than the ones in Part Two, most of Part One fails. If it turns out that AA members do not in fact work the steps in order, the whole chain structure in Part Three should be discarded rather than patched. And the release audit has already falsified Chapter Fourteen's original typical-member threshold result: its frozen environment came from the retired capability-inflated model. Under 400 corrected endpoint environments, high and low starts separate in only seven. The external case for nonlinear relapse dynamics remains worth testing; this simulation does not establish the claimed typical-member bistability.

I have tried throughout to state what would falsify each claim alongside the claim itself. A book that cannot be wrong about anything is not saying much.

# Introduction: Nobody in Charge

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


\clearpage
\thispagestyle{empty}
\vspace*{0.32\textheight}
\begin{center}
{\Large\bfseries Part One}\\[0.6em]
{\large\itshape The First Fellowship}
\end{center}
\clearpage

# Chapter One: Chase's Tavern

The argument that started it was about hypocrisy, and the six men having it were drunk.

It was the first week of April 1840, in a tavern on Liberty Street in Baltimore run by a man named Chase. Six regulars sat around their usual table. They had been sitting around it for years. Among them were two blacksmiths, a tailor, a carpenter, a coach-maker, and a silversmith, William Mitchell, David Anderson, George Steers, John Hoss, James McCurley, Archibald Campbell. Working men with trades and families and, by every account including their own, a serious problem with drink.

There was a temperance lecture that night, somewhere across town. A clergyman preaching in the city had given public notice that he would speak on the subject. Temperance lectures were not unusual. The country was in the middle of a decades-long moral campaign against alcohol, and a man in an American city in 1840 could hardly cross the street without being handed a pledge card. What was unusual was that the six men at Chase's decided to send a delegation.

They meant it as a joke. That is the part everyone forgets. They were not seekers; they were hecklers. Four of them would go and hear what the man had to say, and come back, and they would all have a laugh about it over another round.

The four went. The four came back. And something in the report did not land the way anyone expected, because one of the six said, more or less seriously, that after all, temperance was a good thing.

Chase, who owned the tavern and sold the liquor, said the temperance people were all a parcel of hypocrites.

McCurley, the coach-maker, turned on him. Of course you'd say that, he said. It's your interest to cry them down.

And then Steers, the blacksmith, said the sentence that started everything:

*I'll tell you what, boys. Let's form a society, and make Bill Mitchell president.*

They laughed. Then they kept talking about it. Then they kept laughing, and the more they laughed and talked it over, the more the idea pleased them.

---

It should have ended there. Ideas hatched at midnight in a bar have a mortality rate close to one. But on Sunday the sixth of them were out walking together, and, in the phrase of the man who first wrote it down, between walking and treating they managed to arrange the matter to their entire satisfaction. Treating means buying rounds. The whole enterprise was conceived in a state of some impairment, and somewhere on that walk the joke turned into a decision: one of them would draw up a pledge, and they would all sign it the next day.

On Monday morning Mitchell, the tailor, wrote it. It ran:

> We, whose names are annexed, desirous of forming a society for our mutual benefit, and to guard against a pernicious practice which is injurious to our health, standing, and families, do pledge ourselves as gentlemen that we will not drink any spirituous or malt liquors, wine, or cider.

Read it twice, because almost everything that matters is already in it. *For mutual benefit*, this is not a society for the improvement of others. *Injurious to our health, standing and families*, not to the nation's morals, not to public order, but to *ours*. *We pledge ourselves as gentlemen*, no clergy, no oath before God, no external authority at all. Six men promising each other, on nothing but their own word, in the first person plural.

Mitchell took the paper around at about nine in the morning. He found Anderson in bed, sick from the effects of Sunday. Anderson got up, dressed, listened to the pledge read aloud, and then walked down to his own shop to fetch pen and ink, a detail I find impossible to read without affection, and became the first man to sign the Washington pledge. He was hungover, and he went and got the pen himself.

Mitchell collected the other four names and added his own last.

They elected officers, because that is what nineteenth-century working men did with any idea that survived a week. Mitchell president, as Steers had proposed in jest. Campbell vice-president. Hoss secretary. McCurley treasurer. Steers and Anderson the standing committee. Membership cost twenty-five cents to join and twelve and a half cents a month thereafter, real money to a carpenter, roughly a few dollars in today's terms, and worth noticing that they charged themselves anything at all.

They named it after George Washington. It was 1840; everything was named after George Washington.

And then, having founded a total abstinence society, they continued to hold its meetings at Chase's Tavern. For weeks. In the bar. At the same table.

They stopped only when Chase's wife objected, not on moral grounds, but because the society was costing the house its best customers.

---

Here is what those six men had built, without any of them intending to build it.

They had a fellowship of people with the problem, for people with the problem, run entirely by people with the problem. No doctors. No clergy. No reformers. The temperance movement of the 1840s was thick with respectable people organising on behalf of the intemperate; the Washingtonians were the intemperate, organising on behalf of themselves.

They had weekly meetings, held at a fixed time and place, whose central activity was members standing up and describing their own drinking, not in the abstract, not as moral instruction, but as narrative. What it had been like. What had happened. What it was like now. The form was so distinctive that contemporaries commented on it: these people did not lecture, they *testified*.

They had a single requirement for membership, and it was a pledge about one's own future conduct rather than any statement of belief.

They had the practice of seeking out other drinkers directly, going to them, in their homes and their taverns, and talking to them. One drunk talking to another. They understood, apparently by instinct, that a man who has been where you are can say things to you that a man who has not cannot.

They had dues paid by the members themselves.

And, this is the detail that stops me every time, until November of 1840, their meetings were closed. Outsiders were not admitted. If you had not had the problem, you could not come in. Historians of American addiction treatment credit these as the first widespread closed meetings of alcoholics gathered for their own mutual support.

Alcoholics Anonymous would be founded in Akron, Ohio, in 1935. Six drunks in a Baltimore bar had assembled a recognisable draft of it ninety-five years early, and they did it as a joke that got out of hand.

---

The growth was not gradual.

Two new members came to the second meeting. By November the society was large enough and confident enough to hold its first public gathering. And once the public meetings started, the thing detonated.

The mechanism was the testimony. American audiences in 1840 had heard a great deal of temperance oratory, polished, moralising, delivered by men in good coats who had never woken up in a doorway. What they had not heard was a hatter from Baltimore standing up and describing, in plain language and without apology, exactly how far down he had gone. It was riveting in a way the respectable version had never been. People came for the spectacle and left having signed a card.

The best of the speakers was a man named John H. W. Hawkins, who signed in the middle of June 1840, ten weeks after the founding, after more than twenty years of heavy drinking. He had been apprenticed to a hatter at fourteen, in a trade where it was then customary to teach the rising generation to drink, and he drank his way out of it; the panic of 1837 finished the job and left him on public relief.

He described his last morning himself, from the platform, and his son printed the speech. It is worth having in his own words rather than mine.

> Never shall I forget the 12th of June last. The first two weeks in June I averaged as much as a quart and a pint a day. That morning I was miserable beyond conception, and was hesitating whether to live or die. My little daughter came to my bed and said, "I hope you won't send me for any whisky to-day." I told her to go out of the room. She went, weeping. I wounded her sorely, though I had made up my mind I would drink no more. I suffered all the horrors of the pit that day. But my wife supported me. She said, "Hold on, hold on." Next day I felt better. Monday I wanted to go down and see my old associates who had joined the Washington Society. I went and signed.

Two things in that are worth not skating past. The first is *I suffered all the horrors of the pit that day*, which is a man describing unmedicated withdrawal in 1840 and having no other vocabulary for it. The second is his wife, saying hold on, hold on. The version of this story that circulates has Hawkins saved by his daughter's reproach. His own telling has the daughter break him and his wife carry him.

He turned out to have an extraordinary gift for the platform, a big man with a carrying voice and a talent for speaking without notes. Within eight months he was addressing the Maryland legislature as a man who twelve months earlier had been, in his own phrase, almost out of the gutter. He eventually made his living at this, taking a paid position as secretary of the Massachusetts Temperance Society in 1841.

Hold that last sentence somewhere. We will come back to it.

Societies formed in city after city, mostly by simple imitation. There was no headquarters worth the name, no charter, no franchise agreement, nobody's permission to ask. Baltimore's own society had about three hundred members by December 1840, of whom, a local observer wrote, upward of two hundred were reformed drunkards, reformed within the previous eight months. On the first anniversary, 5 April 1841, roughly a thousand reformed drunkards and five thousand other members and friends paraded through Baltimore in front of something like forty thousand spectators.

Mitchell had a motto for the weekly meetings, and it is the whole growth mechanism in nine words: *Let every man be present, and every man bring with him a man.*

Teams of speakers went out on tour. Two Baltimore men, Pollard and Wright, worked central and western New York, then New Jersey and Pennsylvania, and collected 23,340 signatures, of which perhaps a fifth, it was supposed, were common drunkards. Another pair, Vickers and Small, opened Pittsburgh, where in a short time ten thousand signed, then Wheeling, then Cincinnati, which became the movement's western capital. From Cincinnati other teams fanned out: one pair took 6,529 signatures in an eight-week campaign in the surrounding country. A correspondent in Pittsburgh, writing in April 1842, said the work had spread at a rate that defied any accurate registration of its triumphs, eight or ten missionaries in the field continuously since the previous June, leaving no school house, country church, village, crossroads, forge, furnace, factory or mill unvisited.

The movement also spread sideways, into populations the six founders had not imagined. In May 1841 the first Martha Washington Society met in New York, organised for women and children: it gave moral and material support to female inebriates and to the wives and children of male ones, and it was the first temperance organisation in which American women took leadership roles in their own right. Juvenile auxiliaries followed. Freed Black Americans organised separate Washingtonian societies of their own.

That expansion is usually told as evidence of the movement's reach, and it is. It is also, read against what happens in the next chapter, the first visible sign of a boundary problem. A society founded by six alcoholics for six alcoholics had within a year become a structure that non-alcoholic women, children and sympathisers could join and lead.

How many people this actually reached is a question I have to handle carefully, because the honest answer is that nobody knows and the famous numbers do not survive inspection.

The figure usually quoted is six hundred thousand. It traces to the American Temperance Union's 1843 report, which claimed that half a million hard drinkers and a hundred thousand sots had been brought to sign the pledge in two years. A larger claim also circulated: five million pledge signers by 1843, which would be something near a quarter of the entire American population aged fifteen and over. Per-capita consumption of distilled spirits among Americans aged fifteen and over fell by only 14.3 per cent between 1840 and 1850, on Jellinek's estimate, from a base of 4.9 gallons, which is not what a quarter of the adult population going dry looks like. Marsh, who produced the original estimate, quietly revised it down to four million by 1848, and later put the number of drunkards permanently rescued at 150,000, having, five years earlier, described half a million.

The terminology is the deeper problem. The sources distinguish drunkards from common drunkards from confirmed drunkards from inebriates from sots from tipplers from tipplers in a fair way to become sots, and no one defined any of it.

So: a great many people. Tens of thousands of alcoholics, plausibly. Beyond that the record will not bear weight.

Abraham Lincoln, then a thirty-three-year-old state legislator in Illinois, thought the phenomenon important enough to address directly. In February of 1842 he gave a speech to the Washingtonians of Springfield praising exactly the thing that made them different: that the reformation was being carried out by drunkards themselves, and that this was why it was working where the moralisers had failed.

---

By 1848 it was essentially over.

Not disgraced. Not banned. Not broken up by opponents. Simply, gone. The societies thinned and folded. The great processions stopped. The speakers moved on to other platforms and other causes. By the time Bill Wilson and Dr Bob Smith met in Akron in 1935, the Washingtonian movement was so thoroughly extinct that it had to be *rediscovered*, dug out of libraries, as a curiosity: a thing that had once happened, at scale, and left almost nothing behind.

Six hundred thousand people. Eight years. Gone.

That is the fact this book exists to understand, and I want to be careful about it immediately, because the tidy version of the story is very tempting and it is not obviously true.

The tidy version, the one told in a thousand meeting rooms, and I will be examining it closely in the next chapter, is that the Washingtonians destroyed themselves by getting distracted. They took up prohibition. They took up abolition. They took up sectarian religion and party politics and any other cause that came through the door. They quarrelled. They leaned on famous speakers, and when one of the famous speakers was found drunk in 1845 the movement's credibility went down with him. They lost sight of the one thing they had been for.

Every element of that account has some evidence behind it. But the most careful historian of the movement, writing in the *Quarterly Journal of Studies on Alcohol* in 1950, describes something less dramatic and more unsettling. There was no collapse. There was no scandal that finished them. The practices came to seem outmoded, the novelty wore off, the emotional charge faded, and the societies simply stopped being places anyone particularly needed to go. They did not fall. They dissolved.

And there is a set of numbers I am going to leave here without explanation, because they will mean much more later than they can now.

The Washingtonian societies did not restrict membership to alcoholics, and the proportion who were varied enormously. Baltimore, at eight months, claimed two-thirds. Cincinnati at the end of 1841 reported nine hundred reformed drunkards out of eight thousand members, about eleven per cent. A society in Brattleboro, Vermont reported a hundred and fifty members, of whom six or seven were hard cases: four or five per cent.

And in 1844, across eighty-two Vermont towns, out of 42,273 pledged members, the number of reformed drunkards was 518.

That is one and two-tenths per cent.

---

Two years after Chase's Tavern, the movement wrote its rules down.

An earlier draft of this chapter listed the *Washingtonian Pocket Companion* among the things I had not read, and said it was the document that would most sharpen or most damage the argument of this book, because it is the movement's own statement of how a society should be started, organised and run. It is the direct counterpart to AA's Traditions. I have now read it, and both halves of that prediction came true.

Most of it is a hymnal. A. B. Grosh compiled it, B. S. Merrell of Utica published it, and by 1842 it was in a second edition; something over two hundred pages of temperance hymns and songs, arranged by occasion, several of them marked with an asterisk to show that Grosh had greatly altered them. The first fifteen pages are the part that matters. A definition of principles. Directions for commencing, organising and conducting the meetings. Advice to Washingtonians. A section on the differences between societies. And two pledges, the Baltimore one and the Utica one.

The definition of principles has three numbered paragraphs contrasting the new societies with the old. The second is this, transcribed with its own punctuation, including the long dashes that Grosh uses where a modern writer would use commas:

> Other societies, generally, were auxiliary to a County—that to a State—and that to a National Society. Sometimes the employed agents, or other persons of a particular way of thinking, used their influence to oppose the political and religious feelings of other portions of community. In consequence, many have been led to fear danger to political and religious rights, by the interference of such combinations with the laws of the land, and their lectures and publications contrary to the party predilections and religious views of many of the people.
>
> "WASHINGTONIANISM," carefully avoids these difficulties, by making each society independent—its funds, its actions, to be all under the direct control of its members—in fellowship with all whose principles are the same; but subordinate (auxilliary) to none. And it prevents all political and religious strife or jealousy, by providing that nothing shall be introduced into our periodicals, lectures, meetings or proceedings inimical to the feelings of any political party or religious denomination.

Read what is in that paragraph. Each society independent: Tradition 4. Its funds under the direct control of its members: half of Tradition 7. Subordinate to none: the between-society half of Tradition 9. Nothing political or sectarian in the periodicals, lectures, meetings or proceedings: Tradition 10. Four of AA's twelve, in a single paragraph, published a century before AA wrote them, by a movement AA would later be told died for want of exactly these.

And the reasoning is not vague piety about keeping out of politics. It is a diagnosis. The old societies were arranged in a hierarchy, county under state under national, and a hierarchy has employed agents, and employed agents have views, and a member of a local society finds his name attached to positions he did not take. The Washingtonians identified the mechanism and legislated against the mechanism. That is the argument this book makes about Tradition 9, made in 1842 by the people who lost.

The directions carry it into the constitution. A society's second meeting adopts a constitution, and Grosh lists what it should contain. Article 2 declares that love, kindness and moral suasion are the society's only principles and measures. Article 3 forbids "the introduction of sectarian sentiments or party politics into any lectures, speeches, singing, or doings of the society." Article 4 provides for officers, committees and their election. Article 9 provides for labours with those who violate their pledges, and for the withdrawal of members. A footnote records that on 22 February 1842 a Washingtonian mass convention at Utica passed a declaration of principles and a constitution for the adoption of all Washingtonian societies, that it was printed in the *Utica Washingtonian* of 25 February and again in October because of the demand, and that a copy should be procured wherever a society is to be organised.

So the standard picture, in which the Washingtonians were a spontaneous movement with no written code and AA is the one that wrote things down, is simply false. They had a code, it was in print within two years, it was sold in a pocket edition, and a convention had adopted a model constitution and told societies where to buy it.

It also disposes of an explanation I had reached for before reading it, which was that what the Washingtonians lacked was any means of transmitting a rule *as* a rule, so that their good practices spread by imitation and lapsed the same way. The means existed. A manual in its second edition, a convention, a newspaper, and reprints run off to meet demand are a transmission mechanism, and a better one than a fellowship of 1946 had.

What they did not have was three particular rules, and the omissions are not silences.

On anonymity the *Pocket Companion* takes the opposite position, deliberately, with an argument. Grosh's directions for the first meeting say that after the pledge is read, those who wish to join should rise or come forward and call out their names for the secretary to write down, and then, in the same paragraph: "Publicity and freedom are preferable to private solicitations, whisperings, and secresy in giving the names." Once the names are entered, every man rises again and answers to his name as it is called, so that nobody is missed. This is not a movement that failed to think of anonymity. It is a movement that considered the alternative, named it whispering and secrecy, and ruled against it in the manual it sold to anyone starting a society.

On leadership there is no rotation and no doctrine of service. Officers and committees are elected, always preferring reformed inebriates as far as possible and consistent, which is the one gesture in the direction of AA's second Tradition. But the president is an office with powers: if a member transgresses the principles of the society, "the President must call him to order, and he should sit down, unless permitted to proceed on promise to observe the right spirit." That is a chairman who can end a discussion. Nothing in the manual limits how long he holds the chair.

And on singleness of purpose the manual is not silent but expansive: its opening definition claims the whole of society for the movement's efforts and puts curing intemperance alongside preventing it, a passage Chapter Two quotes in full because that is where it does its damage. The section on differences between societies records that some admitted only those who had made, sold or used liquor within the past year, others everyone but young children, others children too with a parent's consent. The porous boundary that Chapter Two will identify as the thing that killed the movement was not drift. It was written into the definition of principles as a virtue, and the variation between societies was recorded without embarrassment, because nothing bound them to agree.

I want to be careful about what I have just done, because it has the shape of a fit. This book will argue in Part Two that three Traditions, the second, the ninth and the twelfth, do the load-bearing work, and I have just reported that the Washingtonians had four others and lacked exactly those three. The selection of those three does not come from this history. It comes from a theorem, and Part Two derives it without reference to 1842. But a reader is entitled to suspicion, so the fair test is what the *Pocket Companion* could have contained and does not. Had it prescribed rotation of the chair, or advised societies against giving members' names to newspapers, the argument of this book would be in serious trouble, and I would have had to say so here. It prescribes the reverse of the second and says nothing about the first.

The limits are worth stating too. This is one compiler's manual, in one edition, from Utica rather than Baltimore, and it is prescriptive: it says what a society ought to do, not what any society did. Its own section on differences is the evidence that societies varied. But that cuts the way the argument goes rather than against it. A movement whose manual has to include a chapter on how much its societies disagree is a movement whose rules had no purchase, and the *Pocket Companion* tells you which rules those were.

---

Ninety-five years after Chase's Tavern, in a house in Akron, a failed stockbroker and a proctologist who could not stop drinking founded a fellowship on almost exactly the same insight: that one alcoholic talking to another does something no outsider can do.

The Washingtonians had that insight first, executed it beautifully, and reached six hundred thousand people with it.

Alcoholics Anonymous has been running for more than ninety years. This project has not read
the current service document needed to support a present membership count, so it does not
state one.

The difference between those two outcomes is not the insight, because the insight was the same. It is not the founders' talent; Mitchell and Hawkins were formidable and Bill Wilson said so. It is not the era, or the medicine, or the money.

The difference is a set of rules that the second fellowship wrote down in 1946, after eleven years of watching its own groups tear themselves apart in exactly the ways the first fellowship had, rules that look, on the page, like nothing more than good manners. Do not endorse things. Do not take outside money. Do not have leaders who lead. Do not use your last name in public. Keep to one purpose.

They read like humility.

This book is an argument that they are engineering, that at least three of them turn out to be the precise conditions under which a group of people talking until they agree can be trusted to be right, and that a fellowship of drunks arrived at those conditions in 1946, six decades before anyone proved them.

But first we have to be honest about how the Washingtonians actually died, because the story AA tells about them is a story with a moral, and stories with morals are exactly the ones you should check.

---

## The Machinery

*Every chapter ends here, with the workings shown. Four parts: what the model behind this book says about the chapter, the technical version of that, notes on how far the sources can be trusted, and the references. You can skip part 2 without losing the thread.*

### 1. What the model says

Running underneath this book is a simulation of a mutual-aid group, members, the things a group produces that members need, and the flow of people in and out. I built it before I knew any of this history, and its parts are described properly in Part Three. Here is the one thing it has to say about a founding.

The model has two separate ways a new person can arrive. **Attraction**: existing members are out doing the work, someone notices, they come. **Referral**: somebody arrives from outside the group's own efforts entirely, sent by a court, a hospital, a treatment programme, a doctor, a worried family.

Modern AA runs on both. In 1840 the second channel did not exist. There were no treatment programmes to be referred from, no courts assigning attendance, no medical consensus that this was a condition anyone treated. Every single Washingtonian arrived because another Washingtonian went and got him.

That is a group operating on one engine. And a one-engine group has a property the model makes very stark: its growth is proportional to how much its members are *currently* out carrying the message, so it can grow explosively, which the Washingtonians did, faster than almost any voluntary organisation in American history, and it has no floor underneath it. Nothing arrives on its own. If the carrying slows for any reason at all, inflow does not slow proportionately. It stops.

I did not go looking for this. It fell out of noticing what the model needed and what 1840 could supply, and it reframes the growth in this chapter: the six hundred thousand is not only evidence of how well the thing worked. It is evidence of how completely everything depended on one mechanism.

The other model connection here is the Worcester number, and I will only gesture at it. In the model, one of the resources a group produces is an *opportunity to help*. Its proxy is the number of low-practice members per high-practice potential helper. That is not a count of newcomers: the model contains no tenure or sponsorship state and cannot know who arrived when. A society of five hundred containing fifty alcoholics can therefore illustrate the intuition, but the historical example is not something the simulation measures.

### 2. The technical version

Inflow in the model is

> λ = λ_exog + λ0 · (Σ x12) · T11

where λ_exog is the referral floor, Σx12 is total twelfth-step practice summed across members, and T11 is adherence to the attraction principle. Setting λ_exog = 0, the 1840 condition, makes inflow strictly proportional to current member activity, with no additive term.

The consequence appears in the model's decline runs, over a thirty-year horizon with four hundred paired random seeds. Endpoint viability means more than five members; existence means at least one; closure is permanent once membership reaches zero. Mean size counts a closed group as zero.

| Configuration | Endpoint viable | Exists | Closed | Mean size ± 95% half-width |
|---|---:|---:|---:|---:|
| Both channels intact | 0.985 | 1.000 | 0.000 | 17.80 ± 0.88 |
| Attraction lost, referrals intact | 0.985 | 1.000 | 0.000 | 12.38 ± 0.34 |
| Referrals lost, attraction intact | 0.0275 | 0.105 | 0.895 | 0.51 ± 0.23 |
| Both lost | 0.000 | 0.0025 | 0.9975 | 0.0025 ± 0.0049 |

A one-engine group is therefore not merely smaller. It sits on the fragile branch: no floor, and extinction when the engine falters.

**How far to trust these numbers.** They are Monte Carlo estimates inside a constructed model, not historical rates. The 95 per cent Wilson interval for endpoint viability is 0.968 to 0.993 in the baseline and 0.015 to 0.049 without referrals. The latter condition closes in 358 of 400 runs. These corrected results are much more severe than the earlier cache because the individual heterogeneity draw is now mean-centred; the old lognormal implementation silently raised average capability above one and cannot be compared to this release.

The second is what survives that. Under a global perturbation of every model parameter by up to twelve and a half per cent, the ordering in this table holds on endpoint viability in 323 of 334 draws, ties in ten and reverses in one. At twenty-five per cent it holds in 269, ties in 64 and reverses in one. At fifty per cent it holds in 201, ties in 117 and reverses in sixteen. That is the viability column and it is the column the claim is about; the mean-size column is weaker at every amplitude and behaves differently under changes to the model's architecture, and appendix A9 sets out how. The ordering also survives a harder test, in which each of the model's hundred and eighteen numbers is moved alone by ten, twenty-five, fifty and seventy-five per cent in each direction. Across those 944 points the final-membership ordering holds in 931, ties in two and reverses in eleven, and the reversals are concentrated in large downward moves of the ordering exponent, the decay rate and churn. Chapter Twelve gives reason to think the decay rate may be well below what the model assumes, which makes those reversals the ones to watch. The endpoint viability of the referral-starved case is robust to nothing at all, and twenty-six of the hundred and eighteen parameters can move it on their own. Read the ranking, not the figures.

The recipient resource is defined as low-practice members *per high-practice potential helper*, saturating in that ratio rather than in raw membership. Worcester in June 1841 motivates the idea of a crowded room with few relevant recipients; it does not validate the proxy.

**Caveat, stated plainly:** the model has no term for a competing organisation. That absence matters enormously in the next chapter, and I flag it here so it does not arrive as a surprise.

### 3. Notes on sources

**This chapter has been rewritten against the primary scholarship.** An earlier draft relied on Maxwell's 1950 study as quoted inside AA-affiliated websites. I have since read the paper in full, and several things in that draft were wrong. Hawkins did not lose two wives, that detail came from a secondary source and Maxwell's account has his wife supporting him through withdrawal. The Baltimore procession figures I had were from a popular 1948 retrospective; Maxwell's are better. And the striking Worcester statistic I originally used is not in Maxwell at all; he has better-documented equivalents from Cincinnati, Brattleboro and Vermont, and the Vermont figure is more dramatic than the one I had.

**The famous numbers do not survive contact with the source.** Maxwell devotes a section to demolishing them, and the demolition is more interesting than the numbers. His conclusion is that the statistics are varied, contradictory and unreliable, that they conflate pledge-signers with reclaimed drunkards, and that the vocabulary of the period distinguished grade after grade of drinker without defining any of them. He lists the terms he found in use, and there are ten: hard drinkers often drunken, confirmed drinkers, drunkard, common drunkard, confirmed drunkard, inebriate, sot, tippler, common tippler, and tipplers in a fair way to become sots. An earlier version of this note said eight, which was a floor rather than a count.

**The dates, and a small overstatement corrected.** Maxwell gives Thursday 2 April 1840 for the tavern conversation and Sunday 5 April for the decision on the walk. For the signing he writes only that the president was to compose the pledge "which they would all sign the next day", which makes it Monday 6 April by arithmetic rather than by his say-so. An earlier version of this note said Maxwell was precise about all three dates. He is precise about two. Harrison independently puts the pledge on the Monday morning. Sources that give a single founding date are compressing this.

**The dialogue is reconstructed, and I have now read the reconstruction at source.** Harrison's *A Voice from the Washingtonian Home* of 1860 is where the tavern exchange comes from, and Maxwell takes it from there. It was written twenty years after the event by people invested in the founding being charming, and it should be read that way. But reading it directly rather than through Maxwell changed three things in this chapter, and the third is the one that matters.

**The preacher is not named.** Harrison, the earliest of the three accounts, says only that a clergyman preaching in the city had given public notice he would deliver a discourse on temperance. No name. Maxwell supplies Matthew Hale Smith; Marsh, from the Maryland State Temperance Society's report, supplies Elder Knapp. Both are later, both are confident, and they disagree. The earliest source is silent, which is usually what a silence means: the six men did not record who it was, and two later traditions filled the gap differently. This chapter now leaves him unnamed.

**Four went, not one.** Harrison has it that four of the six were sent to hear the sermon. Marsh's source says four. Only Maxwell has a single delegate. Two independent accounts against one settles it as well as it is going to be settled, and the chapter follows the two.

**And Harrison dates it to a Friday.** He writes "Friday evening, the second of April, 1840." The second of April 1840 was a Thursday. Maxwell has Thursday and is right on the arithmetic. This is a small thing, but it is a useful calibration of Harrison: he is the origin of the scene and he is loose about detail, which is a reason to keep the dialogue as reported speech rather than promoting it to fact.

One correction to the chapter's own sequence. Harrison has the pledge written on the Monday morning, not on the Sunday walk: what happened on the walk was the agreement that somebody would draw one up and that they would all sign it the next day. Corrected above.

**Hawkins is now quoted from his son's compilation rather than through Maxwell**, and the edition matters. The book I have read is the 1862 Boston printing by Briggs and Richards, described on its title page as the sixth thousand; the edition usually cited, and the one Maxwell used, is the Jewett printing of a few years earlier. I have not compared them, so I cite what I read and say which it is. Anyone checking a page reference against the Jewett edition should expect it to be wrong.

**And Hawkins's own account puts his signing a day later than Maxwell does.** Maxwell has 14 June 1840. Hawkins says the crisis was the 12th, that the next day he felt better, and that he signed on the Monday. The 12th of June 1840 was a Friday, which makes his Monday the 15th; the 14th was a Sunday. Either Maxwell is a day out, or Hawkins was loose about the weekday twenty years on, and I cannot tell which. The chapter now says the middle of June and does not pick. It changes nothing about the argument, and pretending to a precision two sources do not jointly support would be the error this book keeps finding in itself.

**Krout corroborates the founding independently, and adds a rule I had missed.** John Krout's 1925 *Origins of Prohibition*, which I have now read at source rather than through Maxwell, takes the scene from the Maryland State Temperance Society's annual report of 1842. The officers, the twenty-five cent fee and the twelve-and-a-half cent dues are all there as this chapter has them, which is worth knowing because it means those details rest on two independent readings of a contemporary report rather than on one historian's summary. Krout adds two small things: the six agreed that each would bring a friend to the first regular meeting, and a proposal to name the society after Jefferson was rejected before they settled on Washington.

The thing I had missed is a rule, and it is not the same as the closed meetings described above. Closed meetings governed who could come in, and they ended in November 1840. This governed who could speak, and it did not. As the Baltimore society grew and the problem of keeping meetings interesting arose, Mitchell proposed that the programme be limited to members narrating their own experience, and the society **admitted no outside speakers unless they came to relate their experience as reformed men**.

That is a deliberate restriction on who may address the room, and it is functionally a Tradition. It is close kin to AA's singleness of purpose, and the Washingtonians had it in their first year.

So the honest statement of this book's comparison is not that the Washingtonians had no rules and AA had twelve. They had at least one good one, early, and it worked. Krout's next sentence is that the standard for other Washingtonian societies was thereby set, and his mechanism is imitation: the practice spread because people copied a meeting that was visibly working. **An earlier version of this note went on to say that imitation was all they had, and that no means existed of transmitting a practice as a rule. The *Pocket Companion* shows that to be wrong**, and the main text now carries the correction. Mitchell's speaking rule is not in Grosh's directions, which is a different and smaller point: a mechanism existed and this particular rule did not travel through it. Chapter Two is about what happened then.

**A second version of the founding, and a conflict on one detail.** John Marsh, Corresponding Secretary of the American Temperance Union, prints the same scene in his 1866 memoir, taken from the eleventh annual report of the Maryland State Temperance Society, and I have now read it at source. The wording is close enough to be the same tradition: after all temperance is a good thing; a parcel of hypocrites; it is for your interest to cry them down; let's form a Temperance Society, and make Mitchell president. Two things differ. Marsh's source says **four** of the six went to the sermon, not one delegate. And it names the preacher not as Matthew Hale Smith but as **Elder Knapp**, presumably the revivalist Jacob Knapp. I cannot resolve which is right from anything I have; the two accounts descend from different Baltimore informants and both are retrospective. The chapter follows Maxwell on the preacher's name and I record the disagreement rather than choosing silently.

**And the sermon itself was disputed at the time.** Marsh adds a sentence that is worth more than the detail it corrects: *This statement was afterward denied by some who preferred that the movement should be considered an immediate impulse from Heaven, without any human instrumentality.* So within twenty-five years there were already two constituencies, one holding that six men were moved by a preacher and one holding that they were moved by God directly. That is a founding myth under construction, visible in the act, and it is a reason to hold every detail of this scene loosely. What is not in dispute is the outcome: they organised, and they signed.

**A significant omission, flagged rather than fixed.** This chapter tells the Washingtonian story as six working men and their imitators, which is broadly how Maxwell tells it and entirely how the AA-derived literature tells it. It is incomplete. The movement spawned the Martha Washington Societies from May 1841, in which women took leadership roles for the first time in American temperance, giving moral and material support to female inebriates and to the wives and children of male ones. It spawned juvenile auxiliaries. And freed Black Americans organised separate Washingtonian societies. Ruth M. Alexander's 1988 article in the *Journal of American History* treats the class and domestic dimensions directly and I have not read it. A historian would notice the absence immediately, and it bears on the argument as well as the coverage: a movement that generated auxiliaries for non-alcoholic women and children is a movement whose boundary was porous by design, which is the absorption thesis of Chapter Two appearing earlier than I have placed it.

**The pledge is independently corroborated, and the corroboration is two years old rather than a hundred and ten.** This chapter takes the pledge text from Maxwell, who took it from the Baltimore records. Grosh prints it in 1842 as "the original or Baltimore Pledge", set beside the Utica pledge that some societies preferred, and the two texts agree word for word apart from punctuation: Grosh uses long dashes where this chapter has commas, writes "Society" with a capital, and drops the comma before "or cider". Nothing in the wording differs. The claim moves from scholarly to primary, and the fact that a Utica compiler in 1842 could print the Baltimore wording as the original is itself evidence that the text travelled intact.

**The *Pocket Companion* has been found and read, and it was the acquisition this chapter most needed.** Grosh, A. B., comp. (1842), *Washingtonian Pocket Companion*, second edition, Utica: B. S. Merrell; read from the Harvard copy digitised by Google and held by HathiTrust, saved as `research/incorporated/Grosh_1842/` with the page images as `.pdf`. It supplies, first-hand and uncontaminated by any later use of Washingtonian history, four things this chapter previously took at a remove or did not have at all: the definition of principles with its independence and anti-hierarchy clause, the model constitution's articles, the explicit preference for publicity over secrecy in taking names, and the movement's own statement that it embraces all classes, sexes, ages and conditions. It also falsified a sentence of this chapter's, recorded above. Two cautions travel with it. It is prescriptive rather than descriptive, and its own section on differences between societies is the evidence that practice varied. And it is a Utica imprint by a compiler who was not one of the six; it is the movement's manual, not Baltimore's minute book.

**What I have still not read.** White's *Slaying the Dragon*; Alexander (1988); Blumberg and Pittman (1991). Where this chapter depends on them it depends on them through Maxwell, and that is one remove I have not closed. Alexander is the gap that matters most now: Grosh confirms first-hand that women organised, sometimes as a benevolent society within a Washingtonian society and sometimes as separate societies with numerous names, and that the movement urged it, but the class and domestic argument is Alexander's and I have not read her.

### 4. References

**Read in full:**

Maxwell, M. A. (1950). "The Washingtonian Movement." *Quarterly Journal of Studies on Alcohol* 11: 410-452. **Read in full**; the original project PDF and text are stored in the Maxwell subdirectory of `research/incorporated/`. **Note the copy.** What is saved is a retyped reproduction circulated on the web, not a scan of the journal, and it carries transcription errors: the movement's rise is dated to "the early 1940's", "confirmed" is repeatedly set as "conformed", "from" appears as "form", and Brattleboro is spelled Battleboro. Every Maxwell citation in this book has now been checked against it, which is a check against a transcription rather than against the journal. Source for the founding sequence, the pledge text, Mitchell's motto, Zug's December 1840 letter, Hawkins's biography and his own account of 12 June 1840, the anniversary parade figures, the touring teams and their signature counts, the Pittsburgh correspondent, and the entire critique of the membership statistics including the Vermont figure of 518 in 42,273.

Harrison, D. Jr. (1860). *A Voice from the Washingtonian Home: Being a History of the Foundation, Rise, and Progress of the Washingtonian Home... Together with a Sketch of the Temperance Reform in America.* Boston: Redding & Co. **Read at source**; saved as `research/incorporated/Harrison_1860/`. The earliest of the three founding accounts and the origin of the tavern dialogue. Used for the scene, the six men and their trades, the unnamed clergyman, the four delegates, the walking and treating, the Monday morning pledge and the Anderson signing. Its Friday dating is wrong and that is recorded above.

Hawkins, W. G. (1862). *Life of John H. W. Hawkins.* Compiled by his son. Boston: Briggs and Richards, sixth thousand. **Read at source**; saved as text in `research/`. Hawkins's account of 12 June 1840 in his own words, including the quart and a pint, the daughter, the horrors of the pit, and his wife's *hold on, hold on*. **Note the edition**: this is not the Jewett printing usually cited and the two have not been collated.

Krout, J. A. (1925). *The Origins of Prohibition.* New York: Alfred A. Knopf, chapter IX. **Read at source**; saved as `research/incorporated/Krout_1925/`. Used here for the officers, the independent corroboration of the officers, fee and dues, the bring-a-friend agreement, the rejected Jefferson proposal, and Mitchell's rule admitting no outside speakers except reformed men relating their experience. Krout takes these from the Maryland State Temperance Society's annual report of 1842.

American Temperance Union (1841). *Annual Report of the American Temperance Union.* Appendix, page 39. **Read at source**; public-domain Internet Archive scan `annualreportamer00amer_5`, stored with its citation and metadata in `research/incorporated/ATU_1841/`. The quotation below was verified against the page image rather than the OCR. This is the earliest source in this chapter and the only contemporary institutional one: a national body describing the Baltimore society within a year of its founding, and independent of Harrison, of Maxwell, and of the Maryland state report Krout used. It gives the founding date as 5 April 1840, confirms the six men, the public tavern, the simple total-abstinence pledge and the name, and reports that the society passed a thousand members inside a year, most of them formerly "grossly intemperate." Its account of how the room worked is the reason it is quoted rather than merely cited:

> They also resolved to form a society to be called the Washington Temperance Society, and at their successive meetings, each man to bring a man. These meetings soon attracted attention, through a public relation by each individual of his own experience and history.

Both halves of that sentence are mechanisms this book later models. *Each man to bring a man* is inflow through existing members, which is the attraction path; *a public relation by each individual of his own experience and history* is the supply of identification and of visible proof that recovery happens, which are two of the eight group resources in Part Four. It is worth being clear about what this does and does not license. It is a contemporary description of a practice, not evidence that the practice is what made the movement grow, and certainly not evidence for anything in Part Two. It corroborates Krout's bring-a-friend agreement from a year earlier and from a different organisation, which is all a second witness can do.

Grosh, A. B. comp. (1842). *Washingtonian Pocket Companion: containing a choice collection of temperance hymns, songs, &c. With brief directions for commencing, organizing, and conducting the meetings of Washingtonian Temperance Societies; and for the private action of Washingtonians.* Second edition. Utica, N.Y.: B. S. Merrell. **Read at source**; saved as `research/incorporated/Grosh_1842/` and `.pdf`. Harvard copy, digitised by Google, from HathiTrust, https://hdl.handle.net/2027/hvd.32044004487591. Public domain. Used here for the definition of principles and its three numbered contrasts with the older societies, the independence and non-subordination clause, the clause on nothing political or sectarian in periodicals, lectures, meetings or proceedings, the contents of the model constitution including Articles 2, 3, 4 and 9, the footnote recording the Utica mass convention of 22 February 1842 and its publication, the directions for taking names publicly, the president's power to call a member to order, the preference for reformed inebriates as officers, and the section on differences between societies.

Marsh, J. (1866). *Temperance Recollections.* New York: Charles Scribner & Co. **Read at source**; saved as `research/incorporated/Marsh_1866/`. Used here for the second version of the founding scene, taken by Marsh from the eleventh annual report of the Maryland State Temperance Society, and for the contemporary dispute over whether a sermon triggered it at all.

Lincoln, A. (1842). Address before the Springfield Washington Temperance Society, 22 February. Confirmed independently; Maxwell notes the occasion.

The pledge text dates from 1840 and is in the public domain.

**Cited at a remove:**

American Temperance Union (1840-1849). *Annual Reports of the Executive Committee.* New York: American Temperance Union. The membership and pledge claims; also, through their year-by-year language, Maxwell's index of declining interest. **Status partly upgraded.** Three of these volumes are now held at source and have been read in full: the 1841 annual report, listed above for its Washingtonian passages, and the 1840 report and the 1849 almanac, read on 13 September 2026, neither of which changes anything in this chapter; what they add is recorded in `research/SOURCES.md`. The series is still cited at a remove for every other year, and Maxwell's index of declining interest still rests on his reading of the run as a whole rather than on mine.



Jellinek, E. M. (n.d.). Per-capita consumption estimates for 1840-1850. Quoted by Maxwell (1950); the original is not identified there and has not been traced.

**What was not read:**

White, W. L. *Slaying the Dragon: The History of Addiction Treatment and Recovery in America.* 2nd ed. Bloomington, Ill.: Chestnut Health Systems. The closed-meeting claim rests on it at one remove and it has not been obtained.

Alexander, R. M. (1988). "'We Are Engaged as a Band of Sisters': Class and Domesticity in the Washingtonian Temperance Movement, 1840-1850." *Journal of American History* 75(3): 763-785. The women's dimension. Grosh 1842 now supplies the organisational fact first-hand; Alexander's class and domestic argument is what this chapter still cannot make.

Blumberg, L. U. with W. L. Pittman (1991). *Beware the First Drink! The Washingtonian Temperance Movement and Alcoholics Anonymous.* Seattle: Glenn Abbey Books. The only book-length modern treatment of this comparison. Not obtained.

The *Washingtonian Pocket Companion* was on this list until 2 August 2026 and is now read at source, which is why the chapter's account of the movement's own rules changed.

# Chapter Two: The Fade

There is a story about how the Washingtonians died, and you will hear it in AA meeting rooms on any night of the week. It goes like this.

They forgot what they were for. Having reformed themselves, they got ambitious, and started taking positions on things. They came out for prohibition. They came out against slavery. They tangled with the churches. They quarrelled about religion and politics until the quarrelling was all that was left. They built themselves around celebrity orators, and when the most celebrated of them was caught drunk in 1845 the whole edifice lost its credibility. They took outside money and outside causes and outside attention, and it killed them.

And therefore, the story concludes, we do not endorse things, we do not take outside money, we have no opinions on outside issues, we keep to one purpose, and nobody's name goes on anything.

It is a good story. It has a clean moral, it flatters the listener's institution, and it is repeated so consistently that it has acquired the texture of established fact.

I have spent enough time with the sources now to think it is, at best, half true, and that the true half is not the half people usually mean. What actually happened to the Washingtonians is stranger, quieter, and considerably more useful, because the thing that finished them was not a scandal. It was a better offer.

The story also has an author, a date, and a motive, and I did not know that when I drafted this chapter.

Ernest Kurtz, whose 1979 history of AA is the standard scholarly treatment, tracks the story to its source. In the August 1945 *Grapevine*, under the title "Modesty One Plank for Good Public Relations", Bill Wilson published his reading of Washingtonian history. He had been prompted by a member's article the month before. He praised the movement for having motivated, as he put it, about a hundred thousand alcoholics who were helping each other stay sober, and lamented that its influence had so completely disappeared that few of us had ever heard of it. Then he listed four flaws that had killed it: overdone self-advertising exhibitionism; an inability to learn from others, becoming competitive rather than cooperative; the original strong and simple group purpose dissipated in fruitless controversy and divergent aims; and a refusal to stick to that purpose and so refrain from fighting anybody.

Read the four again. They are Traditions Eleven, Ten, Five and Ten. That is not a coincidence, and Kurtz does not treat it as one: Wilson was, in Kurtz's words, explicitly conscious of seeking support for the Traditions he was formulating. The article ran **eight months before the Twelve Traditions were published**.

So the story told in meeting rooms is not folk memory that happened to align with the Traditions. It is a case made for the Traditions by the man drafting them, in the fellowship's own magazine, while he was drafting them. Between 1945 and 1976 the *Grapevine* carried twelve separate articles on the Washingtonians.

I want to be careful about what that does and does not show. It does not show Wilson was wrong. Two of his four flaws are recognisable in the record and this chapter defends versions of them. What it shows is that the story's *shape* was determined by what it was needed for. A man assembling twelve rules will find, in a century-old movement he has just been told about, precisely the number of failures his rules prevent. That is the strongest possible statement of the problem this chapter opened with, and it comes from AA's own historian.

---

Start with what the tidy story gets wrong.

**There was no collapse.** This is the first and largest problem. The narrative wants a fall, a moment, a crisis, a body. There isn't one. Milton Maxwell, whose 1950 study in the *Quarterly Journal of Studies on Alcohol* remains the most careful scholarly treatment, describes something much less satisfying to tell. Different regions faded on different timetables; the first signs perhaps in 1843, in most places not until 1844 or later, and in some of the territory Hawkins covered the movement was still at full tide in 1846.

Maxwell's best evidence is beautifully mundane. He reads the annual reports of the American Temperance Union year by year and watches the language cool. The 1842 report details the spread enthusiastically. 1843 is still enthusiastic. By 1844 the movement "has continued through its fourth year with as much interest as could be expected." By 1845 Marsh thinks it has in considerable measure spent its force. In 1846 it is described in the past tense, as something that once deeply enlisted the sympathies. The 1847 report admits that reforming drunkards has not this year been a prominent part of the work.

The 1848 report does not mention the Washingtonians at all.

That is what dying looks like in the archive: not a scandal, but an organisation gradually stopping being mentioned by the people who used to be excited about it.

The clearest contemporary statement of it is a private letter, and I have now read it in the volume where Marsh printed it rather than through a summary. Lyman Beecher wrote to him from Cincinnati on 21 January 1845, urging him to come west and bring Gough:

> The flood of Coffee House opposition has rolled over us, and though the Washingtonians have endured, and worked well, their thunder is worn out. The novelty of the common-place narrative is used up, and we cannot raise an interest which will command the respect and attention of those who have been restrained and half convinced, but have not joined us, or wholly given up their wine, and are now beginning to turn against us by open transgression in high places. We must open a new campaign, and you and Mr. Gough must come.

Read it slowly, because it is doing something more specific than lamenting. Beecher is not saying the Washingtonians failed, and he is not saying they were absorbed. He grants that they endured and worked well. What he says is that the *format* wore out: the novelty of the commonplace narrative is used up. A movement whose method was that ordinary drunkards stand up and tell what happened to them had, after four years, a supply problem that was nothing to do with recruitment. Everybody had heard it.

That is a third mechanism, alongside absorption and political entanglement, and it is the one this chapter had least to say about because it reached me at second hand. It deserves more weight than I had given it, and I take it up again at the end.

**The religion charge is thin.** The claim that the Washingtonians alienated the churches turns out, on inspection, to rest on a small number of real local frictions, generalised outward, plus the opinions of a few extremists taken as representative. Maxwell's judgment is that the accusation is a misinterpretation of scattered difficulties rather than a description of the movement.

And there is a detail here worth pausing on, because it is a lesson about sources that applies to everything in this book. Much of what later historians knew about the Washingtonians came through the publications of the American Temperance Union, edited by a man named John Marsh. Marsh had been the movement's earliest and most enthusiastic promoter. By 1842 he was expressing concern about the Washingtonians: a reluctance to acknowledge dependence on God, a certain casualness about the Sabbath, an unwillingness among some professed Christians to link the temperance cause to religion.

Now, Marsh genuinely cared about reforming drunkards. But his larger commitment was to the temperance *cause*, which is not the same thing. A movement of ex-drunkards who declined to make their sobriety a religious argument was, from where he sat, a wasted asset. The record that reached later historians was curated by someone with a stake in what the Washingtonians should have been.

**Two weaknesses were named at the time, and the first of them is this book's thesis in advance.** John Krout wrote the first scholarly history of American temperance in 1925. He reports that shrewd observers had pointed out two fundamental weaknesses in the movement's early days. I have read his chapter at source rather than through Maxwell, and the first weakness is worth quoting closely.

There was no connection between the various societies. Each group was allowed to follow its own course, because centralised control was considered too great an infringement on the rights of the individual society. Krout's consequence is three clauses long and every clause matters: systematic organisation was impossible, uniformity in methods was never attained, and **chance largely determined the formulation of principles**.

Hold that against AA. Tradition 4 says each group is autonomous. The Washingtonians had that, and held it for the same reason, and the observers of 1842 could already see where it led. Krout is reporting the reason at eighty years' distance. The movement's own manual gives it in the first person in the year the observers were speaking, undertaking that each society shall be independent and subordinate to none, with its funds and its actions controlled by its own members. Chapter One sets the passage out in full. It is not a movement that drifted into having no centre. It chose one and wrote the choice down. What AA has that they did not is the rest of the set: a primary purpose that fixes what a group is for, a common welfare that comes first, and a conscience procedure for deciding. Autonomy alone does not produce a movement whose groups resemble each other. It produces a movement in which chance determines the principles, which is Krout's phrase and not mine.

That is the sharpest formulation of this book's argument I have found anywhere, and it was written in 1925 by a historian with no interest in Alcoholics Anonymous, which did not yet exist.

Krout's second weakness is the membership: reformed inebriates who had signed during a period of emotional exaltation and were liable to a corresponding relapse. Relapses were frequent, and they impaired public confidence. That is Chapter Three's argument arriving from another direction, and it is worth noting that it is a *structural* observation about who the movement recruited rather than a moral one about the men themselves.

**The political-entanglement charge is contested even inside AA's own literature.** *AA Comes of Age* names religion, politics, and abolition as root causes of the decline. But AA-affiliated researchers who have gone back to the primary material have noted, in print, that while individual cases certainly occurred, there is no compelling evidence that these issues were the major cause. The moral was arrived at first and the history assembled afterwards.

**Gough's relapse was 1845.** The movement was already fading. A scandal cannot be the cause of a decline that preceded it. It can accelerate one, and I think it did, and Chapter Three is about precisely what a fellowship risks when its credibility is concentrated in one man's continued sobriety. But it is a chapter about a mechanism, not about a cause of death.

---

So if they weren't killed, what happened?

Two things happened, and Maxwell rates the second as the more important. They were superseded, and then they were absorbed.

The supersession first. The organisation that superseded them was founded by Washingtonians.

In the autumn of 1842, thirty months after Chase's Tavern, with the movement still near its peak, a group of Washingtonians in New York City started something new. Their reasoning was not that the Washingtonian society had gone wrong. It was that it did not go far enough. Men who had been that far under the power of drink, they judged, needed more care and more fraternal support than a society as loose as theirs could provide. They were worried, specifically and concretely, about backsliding.

Richard Eddy, writing in 1887, prints the founding documents, and I have read them at source rather than through a summary. The motive is stated plainly: they wanted a more perfect organisation, one that *should shield the members from temptation, and more effectually elevate and guide them*. About ten men agreed to draft a plan, and a call went out to some forty prominent Washingtonians for a select meeting on Thursday evening, 29 September 1842. Sixteen came.

They called it the Order of the Sons of Temperance, and the call itself says what they were building: a beneficial society based on total abstinence. It gives the terms. Initiation one dollar, dues six and a quarter cents a week, four dollars a week if you fell sick, thirty dollars for your funeral.

Read that last clause again. Thirty dollars for your funeral. These are men who had watched other men die of this, and the first thing they wrote down was what the society would pay when it happened.

Look at what they added.

**Screening.** To join the Sons, you had to be nominated by an existing member. Three other members would then investigate your life and determine whether you were worthy. This is the sharpest possible break from the Washingtonian pledge, which asked nothing of you but your name and your intention.

**A price.** The founding call sets it at one dollar to initiate plus six and a quarter cents a week, and the fee rose afterwards. Set that beside what the Washingtonians charged, which Krout gives from the Maryland report of 1842: twenty-five cents to join and twelve and a half cents a month. The Sons cost four times as much to enter and roughly twice as much to stay. Unlike the Washingtonians, they gave you something measurable back. The Sons made membership expensive on purpose, and they made it worth buying.

**Ritual and hierarchy.** Secret ceremonies, regalia, passwords, degrees of membership, Grand Divisions above local Divisions. Where the Washingtonians had a president because six men in a tavern thought it would be funny, the Sons had an architecture.

**Material benefit.** Four dollars a week if you fell sick. Thirty dollars to your family if you died. The Sons' own statement of purpose put it plainly: to shield members from the evils of intemperance, to give mutual assistance in illness, and to elevate their character as men. You joined and you got something tangible.

**Respectability.** This one matters more than it looks. Many working people had come to teetotalism hoping to improve their standing in the world, and they had begun to want the meetings they attended to *look* like the respectability they were reaching for. The Washingtonian experience meeting, a hatter describing his worst night to a hall full of strangers, followed by teetotal songs, was thrilling, but it was not respectable. The Sons offered less entertainment and more dignity.

And the members moved. Slowly at first, from late 1842, and then decisively. Maxwell's phrase is that the Sons increasingly displaced the *function* of the Washington societies. By 1850 the order had thirty-five Grand Divisions, 5,563 local divisions, and 232,233 members; it eventually went international and peaked around 700,000. Other orders followed and split off, the Temple of Honor in 1845, the Cadets of Temperance for youth, the Bands of Hope for children, and in 1852 the Independent Order of Good Templars, whose first president was a prominent Washingtonian.

A later chronicler of the Sons said the order had been brought into existence to preserve the fruits of the Washingtonian movement. Maxwell's judgment is drier: one of its functional results was the displacement of the societies it was meant to preserve.

So the first answer is that a fellowship was not destroyed by its enemies. Its own most safety-conscious members built a better-organised alternative, and its ordinary members walked across the street to it.

But Maxwell thinks the chief cause lies somewhere else, and he is right, and it is worse.

---

**The movement was absorbed into the cause that had sponsored it, and stopped being itself.**

The Washingtonians never had a clean boundary, and this is the point at which the movement's own manual is most damaging to it. The definition of principles in the *Washingtonian Pocket Companion* does not describe a fellowship of reformed drunkards. It says that Washingtonianism, while it embraces all classes, sexes, ages and conditions of society in its efforts, makes special efforts to snatch the poor inebriate, and aims to cure as well as to prevent intemperance. Special efforts within a general mission. The breadth was the doctrine, printed and sold, and the absorption Maxwell describes is that doctrine working as written. Even the Baltimore society admitted non-alcoholics. Outside Baltimore, the touring missionaries were almost always sponsored by existing temperance organisations, and those organisations had their own reasons for the sponsorship. The temperance movement in 1840 was in trouble: its 1836 turn to total abstinence had cost it members and money, and its leaders were casting about for something to restore momentum. Then a group of reformed drunkards appeared who could fill any hall in America and prove, simply by standing up, that total abstinence could reclaim even the hopeless.

Marsh and the temperance leadership promoted the Washingtonians brilliantly. They also, in Maxwell's reading, understood them as a *method*, a way of sparking the temperance cause, rather than as an end in themselves. And in time the Washingtonian leaders came to see it the same way. Hawkins kept up work with alcoholics for years, but across the last dozen years of his life his interest shifted to the broader cause. Gough made the same shift.

Then the cause moved somewhere the Washingtonians could not follow. Temperance turned toward legal prohibition, and Washingtonianism was built on moral suasion, Mitchell had held that his societies should say nothing against the liquor traffic at all, and would admit sellers as members. When the movement's sponsors wanted legislation, the Washingtonian position was not merely dated; it was an obstacle. A senator looking back in 1888 called that emphasis on moral suasion a trace of maudlin insanity.

What the Washingtonians did was not hold the line. Marsh describes a Connecticut convention at which the delegates marched from the Centre Church to the State House alongside the Hartford Washington Society, and adopted resolutions on the Washingtonian movement and on prohibiting the sale of intoxicating liquors by law. He adds a parenthesis, and it is the most useful five words in this chapter: *for a great change had come over the Washingtonians in this matter*. They did not resist the turn toward legislation. They came round to it.

The senator's line about maudlin insanity is worth having in full, because read whole it is not a stray insult but an indictment, and it shows what the moral-suasion position had come to cost by 1888. Henry Blair, who had spent a career trying to write prohibition into the Constitution, is reckoning up the movement's ledger. He allows that a hundred and fifty thousand reformed men held to their pledges and were saved, and then asks what are one hundred and fifty thousand among so many. Then this:

> And who knows that the demoralization of public sentiment which the Washingtonians created in their opposition to legal restraint was not the principal reason why the cup of temptation and destruction was again put to the lips of the four hundred and fifty thousand who fell and perished in that last state which is worse than the first? ... This feature of the Washingtonian movement must have been a trace of maudlin insanity which pledges could not eradicate.

He is charging them with four hundred and fifty thousand relapses. Not with being ineffective, but with being *responsible*, because by refusing to attack the traffic they left the public unconvinced that the traffic was the enemy.

Two things follow. The first is that this is a hostile witness reciting the six hundred thousand figure Chapter One shows cannot be supported, which is a reminder that a number can outlive its evidence and be picked up by people on both sides of an argument. The second is more useful to this chapter. Being neutral on the traffic was not a quiet eccentricity that went out of fashion. It became, in the eyes of the men who inherited the cause, a moral failure with a body count. That is what happens to a group with no rule about outside issues when the outside issue wins.

That is the political-entanglement charge, and reading it from a participant rather than from a summary changes what it means. Taking a position on prohibition was not a mistake the Washingtonians made. It was the price of remaining in the room where the cause was now being decided.

An earlier draft of this chapter ended that thought by saying that having no rule against it, they had no way to decline, and that AA a century later wrote a rule and could point at it. That is wrong, and correcting it makes the chapter's argument harder and better. They had the rule, in two places, and Chapter One quotes both: a clause in the definition of principles barring anything inimical to any party or denomination from the movement's publications and meetings, and Article 3 of the model constitution circulated after the Utica mass convention of February 1842. It was in print, in a pocket edition, three years before the Connecticut delegates marched to the State House.

So the difference between the two fellowships is not that one wrote a rule about outside issues and the other did not. Both did, within two years of founding in the Washingtonian case and eleven in AA's. The Washingtonian rule failed, and reading it beside the event it failed to prevent shows two reasons, neither of which is a lack of rules.

The first is scope. Article 3 governs what may be introduced into the doings of *a society*. Marsh's Connecticut resolutions were not passed at a society meeting. They were passed at a convention, by delegates, marching from a church to a state house alongside the Hartford Washington Society, which is a venue the article does not reach and which existed precisely because the societies were subordinate to none and therefore had to meet somewhere to act together at all. The independence clause and the anti-politics clause were written in the same paragraph and pulled against each other.

The second is that a rule barring politics from the meeting cannot help a movement whose identity is already a position on the political question. Moral suasion rather than force was not a procedural preference the Washingtonians held quietly; it was the first thing their manual said about them. Grosh's phrasing is about how to treat sellers and drinkers rather than about statute, so it is not itself a position on prohibition, and I will not claim otherwise. But contemporaries read it as one, which is what Blair is doing when he calls it maudlin insanity, and once it was read that way the anti-politics article had nothing left to bite on. A society could keep party politics out of its Tuesday meeting while the movement it belonged to was the losing side of the political question of the decade.

AA's Tradition 10 differs on both counts. It binds the fellowship as well as the group, in terms, and the thing it declines to have an opinion on includes the reform of drinking itself. That is a narrower fellowship and a wider rule, and Chapter Five is about what it cost to arrive at both.

So the experience meeting palled, and moral suasion fell out of favour, and what was left of Washingtonianism as a distinct thing was only the reclaiming of drunkards, which was by then a secondary interest of nearly everyone involved. Maxwell's summary is that the movement turned into something it had not started out to be: a revival phase of the organised temperance movement.

The sharpest line in his paper is not his own. It comes from E. M. Jellinek, in a personal communication, and it is nine words long:

> the Washingtonian movement was not equipped with an ideology distinctive enough to prevent its dissolution.

Not attacked. Not scandalised. Not outcompeted, exactly. *Absorbed*, because it had no clear enough sense of what it was to resist being turned into something else by people who admired it.

---

I want to sit with this, because it is the most important thing in Part One and it is not what I expected to find.

The Sons of Temperance solved a real problem. Backsliding *was* rampant among the Washingtonians, that is why the Sons were founded, by people who had watched it happen. If you are designing a mutual-aid society for alcoholics and your central difficulty is that people take the pledge and then drink again, the fraternal-order solution is obviously reasonable. Make it hard to get in, so that only the committed apply. Charge enough that leaving costs something. Add ritual, so that membership becomes an identity rather than a decision. Add benefits, so that staying pays. Add ranks, so there is somewhere to climb.

This is not a foolish design. It is, in fact, the design that economists studying religious and communal groups would formalise a century and a half later: demanding groups screen out free-riders through costly entry requirements, and the sacrifice that looks irrational from outside is exactly what makes the community strong. On that theory, the Sons of Temperance should have beaten the Washingtonians. And for about a decade, it did.

Now hold that beside what Alcoholics Anonymous did in 1946, when it wrote down its own rules after eleven years of watching its groups fight about money, publicity, and personalities.

AA forbade **screening**: the only requirement for membership is a desire to stop drinking. Nobody investigates you. Nobody votes on whether you are worthy.

AA forbade **a price**: there are no dues or fees; the group supports itself by passing a basket that you are free to ignore.

AA forbade **hierarchy**: no organisation in the ordinary sense, leaders who serve rather than govern, offices that rotate.

AA forbade **material benefit**: the group does exactly one thing, and that thing is not sick pay.

AA forbade **respectability**: anonymity at the level of press and public, principles before personalities, no last names. You cannot climb a status ladder in a room where nobody is allowed to know who you are outside it.

Every single innovation the Sons of Temperance introduced to fix the Washingtonians' retention problem, AA specifically prohibited.

The Sons of Temperance today is a vestige. Alcoholics Anonymous remains a worldwide fellowship of autonomous groups, still operating under Traditions it has not substantially amended since 1950. The current group and membership counts appear in an AA service document that this project has located but not read, so I do not reproduce them.

---

That is the puzzle this book is about, and I can now state it properly.

It is not "why did the Washingtonians fail and AA succeed." That framing invites the tidy moral, and the tidy moral is mostly wrong. The Washingtonians did not fail in any simple sense; they worked, spectacularly, for about six years, and then a better-organised successor absorbed their function and their members.

The real question is this. When AA faced the same problem eighty years later, how do you hold a fellowship of alcoholics together, it had two solutions available. One was the Sons of Temperance solution: screen at the door, charge for entry, build ranks and ritual and benefits, make membership respectable and costly and therefore valuable. That solution had a track record, a plausible theory behind it, and the endorsement of the Washingtonians' own most thoughtful members.

AA rejected all of it, and adopted in every case the *opposite* rule.

And AA is the one still standing.

Either that is an accident of history, and it might be; institutions survive for stupid reasons all the time, or those rules are doing something that is not obvious from reading them. Something that outperforms screening, ritual, hierarchy, and benefits over a long enough horizon, at the cost of performing worse over a short one.

I think it is the second, and I think what those rules are doing can be stated precisely. Three of them turn out to be the exact conditions under which a group of people who decide by talking until they agree can be relied upon to be right. That is a claim with a proof behind it, published in 2010, by two economists who had never heard of any of this.

But we are not there yet. There is one more thing to establish first, and it happened in 1845, to the most famous reformed drunkard in America.

---

## The Machinery

### 1. What the model says

This chapter turns on a distinction that the model makes precisely, and it is worth having in plain form.

**A collapse is a claim about causes. A fade is a claim about rates.** Any group sustained by arrivals declines whenever departures exceed them, and this can happen with nothing visibly going wrong on any particular evening. These are not the same story at different volumes; they are different kinds of explanation, and they call for different evidence.

The model predicts the fade in some detail, and predicts something unpleasant about it: **the group looks fine from inside while it happens.** In every declining scenario I ran, the members still present were practising at full strength right up to the end. Quality per member holds; only the count falls. Nobody in the room experiences a decline, because at any given meeting there is no decline to experience, there are simply fewer people than last year, which is not a thing you notice week to week.

Set that beside Maxwell's account of what actually happened to the Washingtonians. No collapse. No scandal that finished them. Practices that came to seem outmoded; interest that waned; societies that stopped being places anyone needed to go.

That is the model's signature, described by a historian in 1950 who had no model, and described in a private letter in 1845 by a man watching it happen.

There is a second destination, and it is easy to miss because it is not an organisation of the same kind. T. D. Crothers, a physician who ran an inebriate hospital in Hartford and edited the *Journal of Inebriety*, looked back in 1911 and traced a line of descent the temperance historians do not. The lodging houses set up for men who had broken their pledges became, in his account, the beginning of the hospital system of cure; one of them, opened in Boston in 1857, had grown into the Washingtonian Home, by then among the oldest institutions in the world for the physical care of inebriates.

So the movement's residue went two ways. Some of it went into the Sons of Temperance and the other fraternal orders. Some of it went into medicine, and kept the name. Crothers' judgement is that the movement was a clearing house: it broke up old theories and forced the question of what inebriety actually was into public attention, and then the wave went out.

He is also worth having on the numbers, because he is a sympathetic witness who declines to inflate them. He puts five million pledges between 1840 and 1845, and then says, without embarrassment, that of those five million *a certain unknown number* remained abstainers for life. Unknown. A doctor writing seventy years later, with every professional reason to want a figure, says he has not got one. That is the same conclusion Chapter One reaches from Maxwell's demolition of the statistics, arrived at independently and much earlier.

Marsh himself, writing his memoirs in 1866, gives the absorption thesis in a single sentence and gives it as an eyewitness rather than an analyst. The marvellous Washingtonian movement, he says, had indeed finished its course, and its fruits were gathered into new organizations: Rechabites, Samaritans, Temples of Honor, and above all the Order of the Sons of Temperance, which by 1850 had swelled beyond any other single organisation. Fruits gathered in. Not a movement that died, a movement that was harvested.

There is a detail in the same passage that bears on Chapter One's argument about boundaries, and I would have missed it reading Marsh through anybody else. Marsh went to the Sons of Temperance national meeting in Boston in June 1850 but was not a member of the order, and he gives his reason in a parenthesis: not being a reformed man. The Sons, unlike the Washingtonians, had a membership condition he did not meet. He adds that he still preferred open organisations as best fitted to the cause. The secretary of the American Temperance Union thought the closed body was the wrong shape, and the closed body was the one that grew.

**Now the honest part, and it is the more interesting half.** The model cannot explain this chapter's central finding, because the model has no competitor in it. It contains one group. It has no term for another organisation drawing on the same population, and no way to represent a member leaving because somewhere else offered more.

What actually happened after 1842 is a competing-risks problem. Once the Sons of Temperance existed, a man who would have joined a Washingtonian society had somewhere else to go, so Washingtonian decline cannot be read as evidence about Washingtonian quality without accounting for the alternative. "They lost members" and "they got worse" are different claims, and the record supports the first far better than the second.

This is a limitation I would rather state than paper over. The model is a model of an AA-shaped group: open door, no screening, no dues, no hierarchy. The Sons of Temperance were a different institutional species, and the model has no vocabulary for them.

There is a second limitation, and Beecher's letter is what forced me to name it. His diagnosis was that the novelty of the commonplace narrative was used up. That is a claim about a resource depleting through use: the movement's method was the public testimony of ordinary drunkards, and testimony has diminishing returns on the same audience. The model has eight group resources and not one of them behaves that way. Every one of them is produced by members and consumed without exhaustion. Nothing in the apparatus can get *stale*.

I do not think this is fatal to the argument, because AA's meetings have run on the same method for ninety years without exhausting it, which is itself evidence that the effect is weaker than Beecher thought or that something about AA's structure renews it. But I cannot demonstrate that from the model, and a satisfying account of the Washingtonian decline would have to say why the same format wore out in four years there and has not in ninety here. The honest position is that Beecher named a mechanism I have not modelled and cannot currently rule out.

### 2. The technical version

The relevant simulation results use a thirty-year horizon and four hundred paired seeds, with a group at full adherence as the baseline. Practice is the mean level among established members, with closed runs contributing zero to the displayed all-run mean. Endpoint viability means more than five members.

| Scenario | Endpoint viable | Exists | Closed | Mean size | Established practice |
|---|---:|---:|---:|---:|---:|
| Full adherence | 0.985 | 1.000 | 0.000 | 17.80 ± 0.88 | 0.2645 ± 0.0058 |
| Attraction path lost (T11 attraction = 0) | 0.985 | 1.000 | 0.000 | 12.38 ± 0.34 | 0.2580 ± 0.0070 |
| Referrals lost (λ_exog = 0) | 0.0275 | 0.105 | 0.895 | 0.51 ± 0.23 | 0.0292 ± 0.0091 |
| Both lost | 0.000 | 0.0025 | 0.9975 | 0.0025 ± 0.0049 | 0.0013 ± 0.0026 |
| T3 friction and governance lost | 0.5475 | 0.750 | 0.250 | 6.76 ± 0.59 | 0.2246 ± 0.0160 |

The cache uses common random streams across conditions, so effects are estimated with paired contrasts. The corrected, mean-one heterogeneity distribution changes the level of every row materially; values from the earlier non-centred lognormal cache are not release evidence.

The row that matters for this chapter is the third, and specifically its last column. Groups dying of inflow starvation do not show degraded practice on the way down. The prediction is that decline is invisible to its participants, detectable only by counting arrivals and returns, never by asking how the meetings feel.

One caution about that last column is unavoidable. In the referral-starved condition only eleven runs finish viable and forty-two contain any member at all. The all-run practice mean therefore falls almost to zero. Any claim about how the rare surviving room feels must display how heavily it conditions on those selected runs; the correct unconditional result is mass closure, not hidden health.

The gatekeeping row is the model's nearest analogue to what the Sons of Temperance did, and it is a poor one. In the model, exclusionary culture operates on *retention*: an AA group cannot refuse membership to an alcoholic who wants it, whatever it does about attendance at a given meeting, so unwelcoming behaviour raises early dropout rather than blocking entry. Formally, the Tradition 3 term multiplies the early-tenure dropout hazard, weighted by how new a member is, so veterans are insulated from door-culture and arrivals are not. The result is a group about a third smaller that survives comfortably.

The Sons did something the model genuinely cannot represent: they screened *at the door*, before entry, by nomination and investigation. That is Iannaccone's club-good mechanism, costly entry requirements that exclude free-riders and thereby strengthen the community, and it is precisely the mechanism AA forbids in Tradition 3. A model built to describe AA has no way to express it.

**Where this leaves the argument.** The model supports the fade rather than the collapse, and supports the claim that such a fade would have been invisible to the people living through it. It cannot adjudicate the supersession story at all. I have relied on the historical record for that, and the reader should discount accordingly.

### 3. Notes on sources

**A priority problem I have to state plainly.** Having now read Maxwell in full, I find that he made a substantial part of this book's argument in 1950. His final section compares the Washingtonians with AA point by point and concludes that AA's advantages are exclusively alcoholic membership, singleness of purpose, a definite programme of recovery, anonymity, and what he calls hazard-avoiding traditions. On anonymity he is explicit that it has *sheer survival value*, and he reaches that conclusion by exactly the route I intended to take in the next chapter: Gough's relapse, and what it cost a movement whose credibility sat in named men. He also identifies the tradition of keeping authority in principles rather than in offices and personalities, and connects it to rotating leadership.

He did not have the mathematics. The formal claim in Part Two, that three Traditions implement a specific and provable condition for group decision-making, is not in Maxwell, and could not have been in 1950. But "AA's traditions are why it survived where the Washingtonians did not, and anonymity in particular is structural rather than merely modest" is Maxwell's thesis, published more than seventy-five years ago, and this book is in that respect a formalisation rather than a discovery. Saying otherwise would be a straightforward misrepresentation of the record.

**Maxwell is not a neutral party either.** He wrote as a sociologist, but he wrote partly to address a worry then circulating among AA members that their fellowship was destined for the Washingtonians' fate, and his conclusion is reassuring: he sees no inherent reason why AA should not continue indefinitely. His doctoral work was a study of AA. This does not make his historical analysis unreliable, it is careful, and it repeatedly contradicts the movement literature, but a reader should know that the man debunking AA's version of Washingtonian history was himself sympathetic to AA.

**The *Pocket Companion* falsified a sentence of this chapter's, and the correction is in the main text rather than here.** The sentence held that the Washingtonians had no rule against outside issues and so had no way to decline the temperance movement's turn to legislation. They had one, in two places, within two years of founding. I have left the old claim visible beside its replacement because the replacement is the more interesting fact: the failure of the Washingtonian rule was a failure of scope and of standing, not of existence, and a book arguing that written rules are what saved AA has to be able to say why a written rule did not save them. What I have not established, and cannot from Grosh, is how widely the model constitution was actually adopted. The manual urges societies to procure a copy; whether they did is not in it.

**AA's own account is later than Maxwell's and disagrees with it.** *AA Comes of Age* (1957) names religion, politics and abolition as root causes. Maxwell (1950) had already examined and largely rejected the religion charge, attributing it to a few extremists and to the curatorial interests of John Marsh. Where they conflict I follow Maxwell, and note that he was first.

**The Marsh problem, now confirmed at source.** Maxwell states directly that the American Temperance Union's publications, edited by Marsh, were a major source for later historians, that Marsh's overriding interest was the temperance cause rather than the reformation of drunkards specifically, and that later historians overlooked how much of Marsh's criticism addressed minority behaviour. This is not my inference; it is Maxwell's, and I had it second-hand before I had it first-hand.

**A reading of Tradition 3 in Iannaccone's own terms.** Lembke applies Iannaccone to AA directly and puts the difference from the Sons somewhere other than this chapter does. On that reading AA does charge an entry cost, but in stigma rather than sacrifice: it asks for nothing but a desire to stop drinking, which lets in the drinkers least able to pay any other price, and the screening Iannaccone expects is done afterwards, by sponsors holding people already inside to the standard. If that is right, AA does not forbid the club-good mechanism so much as move it past the door, and the model, which has neither stigma nor sponsors, cannot represent either version. The paper is theoretical and illustrated with two clinical cases, so it offers a frame and not evidence.

**Once unread, now read.** Krout (1925), Harrison (1860), Marsh's own *Temperance Recollections* (1866) and Eddy (1887) were listed here as unread, and all four have since been read at source. The Sons of Temperance's own record has been reached once: the American Temperance Union's almanac for 1849 prints the order's figures for 1848, read on 13 September 2026 and recorded in `research/SOURCES.md`. The rest of what the Sons published is still unread. The 1850 membership figures for the Sons come from Maxwell; encyclopaedia sources give slightly different numbers, and I have used his.

### 4. References

**Read in full:**

Grosh, A. B. comp. (1842). *Washingtonian Pocket Companion.* Second edition. Utica, N.Y.: B. S. Merrell. **Read at source**; saved as `research/incorporated/Grosh_1842/` and `.pdf`. Used here for the definition of principles, its independence and non-subordination clause, its clause on nothing political or sectarian in periodicals, lectures, meetings or proceedings, Article 3 of the model constitution, the Utica mass convention of 22 February 1842, and the statement that the movement embraces all classes, sexes, ages and conditions. Full bibliographic detail in Chapter One.

Kurtz, E. (1979, expanded 1991). *Not-God: A History of Alcoholics Anonymous.* Center City, Minn.: Hazelden. **Now read at source.** Chapter Five, pp. 115-117, on AA's use of Washingtonian history. Used here for Wilson's *Grapevine* article of August 1945, its four listed flaws, its hundred-thousand figure, its date eight months before the Traditions were published, and Kurtz's judgement that Wilson was explicitly seeking support for the Traditions he was then formulating. Also for the count of twelve *Grapevine* articles on the Washingtonians between 1945 and 1976. **In copyright; the full text is not stored in this repository.** See `research/SOURCES.md`.

Maxwell, M. A. (1950). "The Washingtonian Movement." *Quarterly Journal of Studies on Alcohol* 11: 410-452. The year-by-year reading of the American Temperance Union reports; the founding of the Sons of Temperance by New York Washingtonians in autumn 1842 and its benefit structure; the 1850 membership figures; the absorption thesis; the moral-suasion split and Mitchell's position on the liquor traffic; the Jellinek communication; and the comparison with AA discussed above. The Beecher letter is no longer taken from Maxwell; see Marsh below.

Eddy, R. (1887). *Alcohol in History: An Account of Intemperance in All Ages, together with a History of the Various Methods Employed for Its Removal.* New York: The National Temperance Society and Publication House. **Now read at source**; saved as `research/incorporated/Eddy_1887/`. Used here for the founding of the Sons of Temperance, including the text of the call of 29 September 1842 and its fee and benefit schedule; for Dr Jewett's first-hand report of Mitchell's position on the liquor traffic; and for Eddy's judgement that Washingtonianism was not an irreligious movement and not a failure.

Crothers, T. D. (1911). *Inebriety: A Clinical Treatise on the Etiology, Symptomology, Neurosis, Psychosis and Treatment.* Cincinnati: Harvey Publishing. **Now read at source**; saved as `research/incorporated/Crothers_1911/`. **A citation was corrected here.** Earlier drafts cited Crothers for the founding rationale of the Sons of Temperance. He does not mention the Sons at all; that material is Eddy's, and the misattribution was caught by a source check written the same day. What Crothers does supply is the five-million pledge figure with the explicit concession that the number who stayed sober is unknown, and the line of descent from the movement to the Washingtonian Homes and thence to inebriate hospitals.

Krout, J. A. (1925). *The Origins of Prohibition.* New York: Alfred A. Knopf. **Now read at source**, chapter IX, "The Washingtonian Revival," pp. 182-222; saved as `research/incorporated/Krout_1925/`. The first scholarly history of the American temperance movement, written twenty-five years before Maxwell and independent of him. Used here for the two fundamental weaknesses contemporaries identified, in particular the absence of any connection between societies and the consequence that chance largely determined the formulation of principles; and for the founding motive of the Sons of Temperance, which Krout gives as the need to devise an organisation that would hold members after the first enthusiasm had spent itself, at Teetotalers' Hall, 71 Division Street, on 29 September 1842.

Marsh, J. (1866). *Temperance Recollections: Labors, Defeats, Triumphs. An Autobiography.* New York: Charles Scribner & Co. **Now read at source**, from the public-domain scan held by the New York Public Library and digitised by the Internet Archive; saved in the repository as `research/incorporated/Marsh_1866/`. Marsh was Corresponding Secretary of the American Temperance Union for thirty years and editor of the reports on which the whole decline chronology rests, so his memoir is a participant document rather than a historian's. Used here for the Beecher letter of 21 January 1845 in full; the statement that the movement finished its course and its fruits were gathered into new organisations; the Connecticut convention and the parenthesis about the change that had come over the Washingtonians on prohibition; and Marsh's own exclusion from the Sons of Temperance for not being a reformed man.

Lembke, A. (n.d.). "Sacrifice, stigma, and free-riding in Alcoholics Anonymous (AA)." Working paper, Association for the Study of Religion, Economics and Culture. **Read in full** on 13 September 2026; stored in `research/incorporated/Lembke_nd/`. Used in the notes above for the reading of AA's entry cost as stigma rather than sacrifice.

**Cited at a remove:**

Jellinek, E. M. (n.d.). Personal communication to Maxwell, quoted in Maxwell (1950). The judgment about ideological distinctiveness quoted in the text.

Blair, H. W. (1888). *The Temperance Movement; or, The Conflict Between Man and Alcohol.* Boston: William E. Smythe. **Now read at source**; saved as `research/incorporated/Blair_1888/`. Used for the passage quoted above in full: the hundred and fifty thousand saved, the four hundred and fifty thousand who fell, the charge that the Washingtonians' opposition to legal restraint demoralised public sentiment, and the maudlin insanity line in its actual context. Blair was a United States senator and the author of a proposed prohibition amendment, so he is a hostile witness with a legislative motive, which is exactly why the passage is useful.

Fehlandt, A. F. (1904). *A Century of Drink Reform in the United States.* Cincinnati: Jennings and Graham. **Now read at source**; saved as `research/incorporated/Fehlandt_1904/`. His dating is blunter than Maxwell's and worth recording as the received view Maxwell was correcting: *By 1843, however, interest began to wane, and soon Washingtonianism had spent its force.* Maxwell's regional evidence shows this is too early and too uniform, and the disagreement is the point.

American Temperance Union (1840-1849). *Annual Reports of the Executive Committee.* New York: American Temperance Union.

Alcoholics Anonymous World Services (1957). *Alcoholics Anonymous Comes of Age*, p. 125. AA's own account, which this chapter declines to follow.

Iannaccone, L. R. (1992). "Sacrifice and Stigma: Reducing Free-Riding in Cults, Communes, and Other Collectives." *Journal of Political Economy* 100(2): 271-291. The formal theory of costly screening; the account under which the Sons of Temperance should have beaten the Washingtonians, and did.

Encyclopaedia entries on the Sons of Temperance (Case Western *Encyclopedia of Cleveland History*; *Encyclopedia.com*), consulted for corroboration; superseded by Maxwell where they differ.

**What was not read:**

Blumberg, L. U. (1980). "The Significance of the Alcohol Prohibitionists for the Washingtonian Temperance Societies, with Special Reference to Paterson and Newark, New Jersey." *Journal of Studies on Alcohol* 41(1): 37-77. The specific test of this chapter's political-entanglement argument. Largely relieved by Marsh 1866, Blair 1888 and Grosh 1842, all read at source, but not replaced by them: Blumberg would add the local detail none of those carry.

Alcoholics Anonymous World Services publications on the Washingtonians, including *Alcoholics Anonymous Comes of Age* and the twelve *Grapevine* articles Kurtz counts between 1945 and 1976. AA copyright, and not obtained. The 1953 commentary was read in full on 10 August 2026 and says nothing about the Washingtonians, so AA's own account of the movement still reaches this chapter through Kurtz and Maxwell rather than directly.

How widely the Utica model constitution was actually adopted. Grosh urges societies to procure a copy; whether they did is not in the manual and I have found no source that settles it.

# Chapter Three: The Man Who Was the Movement

There are two relapses in this chapter, two years apart, in the same man. He described both himself, in detail, in print. What differs is not the illness. What differs is what the world around him did about it, and the difference is the entire argument of this book in miniature.

---

In April 1843, John Bartholomew Gough had been sober about five months, and he was working himself into the ground. He had come off years of heavy drinking into a schedule of more than thirty consecutive speaking engagements, and his body was failing: constant distress in the stomach, no appetite, no sleep. A physician in Dudley gave him tincture of Tolu with ether in it, which he said affected him very strangely.

Then something happened that anyone who has watched this illness will recognise. On the road back to Worcester he began to feel sensations he could not define. The old wound on his skull, where a spade had struck him as a boy, began to throb, and he could not stop pressing his hands to his head. And there came over him a restlessness he was completely unable to subdue.

His own description of it is the best thing in the book:

> It appeared to me that I must be going somewhere, I knew not and cared not whither; but there was a certain impulsive feeling which I could not restrain, any more than an automaton can remain motionless when its machinery is wound up.

His landlady, Mrs. Chamberlain, saw he was ill and urged him to go to bed. He could not sit still for five minutes. He left the house, wandered, heard the fifteen minute bell at the depot announcing the Boston train, and got on it with no aim or object whatever.

In Boston he walked the streets, went to the theatre to quiet himself, and fell in with old companions from his drinking years. They noticed he was talking strangely and asked what ailed him. They took him for oysters. Somebody offered him a glass, and he wrote: *Without thought, I drank it off.*

Then the horror, and then the arithmetic every drinker knows: he reasoned that having made one false step, matters could not be worse for another, and had three or four more.

What he did next is what matters. He went to Newburyport, spoke at a temperance meeting although he felt he had no claim to be heard, went back to Boston, drank again, and then returned to Worcester and immediately sent for two friends, Jesse Goodrich and Dr. Hunting. He told them everything. He re-signed the pledge. He announced he was leaving the state permanently, packed his books and clothes, took his little account-book of appointments and his letters, and burned everything connected with his public work, intending never to speak again.

His friends talked him out of leaving and asked him to attend the Monday meeting. He went. The hall was full. The local temperance paper reported what happened:

> Mr. John B. Gough, as soon as he was known to be in the hall, was called for in all directions, and received in a manner which showed the true spirit of Washingtonian sympathy, kindness, and charity.

He acknowledged his misfortune, said he had re-signed the pledge, and left the hall in tears.

That is a fellowship handling a relapse. It took about ten days from the first drink to the standing ovation. It was conducted almost entirely among people who had the same problem, in one town, and it ended with the man restored and back at work. Nobody investigated anything. There was nothing to investigate: he had told them.

---

By September 1845, twenty-nine months later, he was the most famous reformed drunkard in America, and he had been to Britain and back on the strength of it.

On Friday the fifth of September he arrived in New York at about half past six in the evening, checked into the Croton Hotel, took tea, arranged his dress and went out. He bought a watch-guard on Broadway. Coming out of a store, he was accosted by a man who greeted him by name and said he was Jonathan Williams, an old shopmate. Gough did not remember him.

The man asked whether the temperance business was a good business. Then he said: *I suppose you are so pious now, and have got to be so proud, that you would not drink a glass of soda with an old shopmate.*

They went to Thompson's, found a crowd at the fountain, and Williams said he knew a better place. They walked down Chambers Street to Chatham Street to a small shop with a pasteboard sign reading Best Soda. Williams ordered, asked what syrup Gough took, and suggested raspberry. And then, in Gough's account, the detail he could never let go of:

> This man took my glass, and handed it to me with his hand over the top of the glass. I noticed his hand, because I thought it was not a very gentlemanly way of handing a glass; however, I thought no more, but drank it.

They walked back up to Broadway and Williams left him. Shortly after, Gough felt a warm sensation about the lungs and chest, unusual exhilaration, and then a bewildering desire for something he could not name.

He then went into a grocery store and got brandy. He says so plainly. He does not remember paying for it. He remembers drinking it.

After that the account fragments. He remembers seeing the new white church at the upper end of Broadway. He remembers a woman dressed in black, and asking her, or being asked, about a night's lodging. He remembers a flight of stairs but not going up them. He remembers nothing distinctly except that he drank, and he does not know what or how much or how often. He does not remember eating, though the woman said he ate and asked a blessing and prayed. He does not remember buying a shirt, though he had a strange shirt on when they took him away.

He was there seven days. When a Mr. Camp came into the house and found him, Gough said: *Oh, take me away from this.*

He was taken by carriage to a friend's house, where he was very ill for some time. He noted, in a sentence that reads like a physician's observation, that throughout the illness he never called for liquor and did not remember craving it.

---

Here is the thing I got wrong before reading his own account, and it is worth correcting in full, because the correction makes the chapter's point harder rather than softer.

I had assumed, from his chapter headings, that Gough treated the 1845 episode defensively: as a charge to be rebutted rather than a relapse to be owned. That is not what he wrote. What he wrote, on the twenty-second of September, in a statement he insisted on drafting himself in his own hand while very weak, was this:

> I have fallen! and, keenly feeling this, I am willing to lie prostrate in the dust, where this fall has put me. I do not presume to say that I am not to blame. I was to blame, in going with a stranger.

He goes further. He accepts blame for the brandy specifically, for giving way to his desire for it. He tells the temperance movement he is willing to be called the meanest man in the cause and to bear its censure. He tells his church to do with him as it judges fit. And to the people who think he is lying, he says:

> I blame you not for disbelieving my statement; I blame you not for all that you may say against me.

That is not a man managing a scandal. That is close to a fourth and fifth step, written in 1845 and published in the newspapers.

So the difference between 1843 and 1845 is not in Gough. In both cases he was ill, he drank, he told the truth about it promptly and in detail, and he asked to be judged.

The difference is entirely in what the institutions around him did.

---

In 1843 he told two friends and re-signed a pledge.

In 1845 his church appointed an examining committee.

The committee was appointed on the seventeenth of September. It interviewed him on the twenty-second. His statement was read to a full church meeting on the twenty-sixth, whereupon the congregation formally voted to instruct the committee to inquire thoroughly into the case. The committee then spent over a month attempting to confirm or contradict a sick man's account of a week he could not remember.

They went to New York. They began at the Croton Hotel and interviewed its proprietor. They went to Thompson's, where he said they first stopped for soda. They walked Broadway and Chambers Street looking for the shop.

Read that again and hold it against the 1843 version. A man with a recognised disease had a recurrence of it, and the institutional response was a formal investigative committee travelling between cities to verify his movements, reporting to a congregation, with findings published.

Meanwhile the press did what the press does. Temperance papers defended him, hostile papers dwelt on the house and the women in it, and the argument ran for weeks. One paper had the lost star of temperance going down ingloriously between Venus and Alcohol.

Thirteen years later, in June 1858, Gough stood in the Court of Exchequer in Westminster as plaintiff in a libel action, *Gough versus Lees*, before Baron Martin and a special jury. His autobiography gives three chapters to it, out of thirty-five.

The trial was not about Walker Street. It grew out of a private letter Gough wrote in March 1857 to a friend, saying that the temperance cause in America was depressed and that the Maine Law was a dead letter, which was published without his intention and used against him by prohibitionists in Britain who thought he had betrayed the legislative campaign. He introduces those chapters by saying he would gladly bury the whole controversy in oblivion, but that suppressing it would lay him open to the charge of covering up, and so he will give a clear and truthful narrative from beginning to end.

But watch what happens to 1845 inside that courtroom. His own counsel takes him through his life: the bookbinding trade, the drinking, the pledge. And Gough says, under oath and without prompting:

> I signed the pledge the last Monday night in October, 1842, and violated that pledge in the beginning of 1843.

He states the first relapse plainly, in open court, thirteen years on. Then counsel reaches September 1845, and the exchange is this, in full:

> In 1845, I believe, you had a short illness? Yes.

A short illness. That is the entire treatment of the week that convulsed the American press, delivered by his own advocate and assented to by the man himself.

Nothing about 1843 needed managing, so it could be spoken. Everything about 1845 had become a contested public asset, so it had to be compressed into four words that were true and disclosed nothing. The euphemism is not evasion by a dishonest man; he had, after all, published every particular in 1845 over his own signature. It is what happens to a fact when it stops being a fact about a person and becomes a position in an ongoing argument.

In 1869, twenty-four years after the week on Walker Street, he was still explaining himself in print, and he wrote this about it:

> any man can turn to the blotted pages, and pointing to them say, "Behold his record!" And what is more bitter, more stinging, when a man has carefully striven, and is striving, to live down the past, than to know that the record is read, and can be used as a weapon for wounding his tenderest sensibilities?

He adds, carefully: *I do not complain of this; I only say it is so.*

---

Nothing about Gough's illness changed between 1843 and 1845. What changed was that his name had become an asset, and an asset does not get to be sick privately.

Maxwell, writing in 1950 with the whole case in front of him, drew the conclusion this book is built on. A comparison with the Washingtonian experience, he wrote, underscores *the sheer survival value* of the principle of anonymity in Alcoholics Anonymous. At the height of his popularity, Gough either slipped or was tricked into a relapse; opponents of the movement seized on it with glee and made the most of it to hurt both the man and the cause; and public confidence in the movement was impaired.

Then Maxwell added the sentence that generalises it, and it is the most important line in his paper:

> This must have happened frequently to less widely known but nevertheless publicly known Washingtonians.

Gough is the case we can see, not the mechanism. The mechanism was running on every Washingtonian whose name and face were known in his own town, every time one of them went out, at a scale no newspaper recorded.

A movement of a hundred thousand people, in which any member's relapse can become a public event, carries an enormous and invisible liability. Not because relapse is shameful, but because relapse is *normal*, and a structure that converts a normal recurrence into a credibility crisis will generate credibility crises continuously, forever, at exactly the rate at which the illness recurs.

Which is often.

Compare what an anonymous fellowship offers a member who goes out. There is no statement to publish, because there is no public position to defend. There is no committee, because there is no institution whose reputation rests on this particular man's continence. There is no record to be turned to twenty-four years later. The group loses a member for a while and gets him back, and no newspaper in the country has an opinion about it.

The 1843 response was that, roughly. The Washingtonians in Worcester handled a relapse the way an AA group would: quickly, internally, among people with the same problem, and with sympathy, kindness and charity. They were entirely capable of it.

They simply could not do it for a famous man, and by 1845 they had made several.

---

There is a coda, and I want to keep it because it complicates the moral.

Gough came back. Over the following forty years he gave something like nine thousand six hundred lectures to perhaps nine million people. When he died in 1886 the *New York Times* judged him probably better known in America and Britain than any other public speaker. His church kept him, his wife kept him, his movement kept him. He is buried in Worcester, where he first got sober.

The man survived. Handsomely.

It was the movement that could not metabolise what had happened to him. Gough took a blow from the Washingtonians and outlived them by nearly forty years. The Washingtonians took a blow from Gough and never fully recovered, because they had built themselves so that his sobriety and their credibility were the same quantity.

Nobody designed that. It emerged from a series of individually sensible choices: put your best speaker on the platform, use his real name, let the papers print it, let the crowds come.

The next part of this book is about a mathematical result, published in 2010, that describes precisely what goes wrong in a group organised that way.

But the setup was already complete in 1845. A movement had concentrated its credibility in a handful of named men. One of them got sick, in the specific way that this illness is defined by recurring. And the structure shook.

---

## The Machinery

### 1. What the model says

The model treats a group as members who weight each other's judgment. Each member has an *influence weight*: the share of the group's eventual view traceable to that member. The weights sum to one.

The result in Chapter Seven says that such a group gets reliably closer to the truth as it grows if and only if the largest single influence weight shrinks toward zero. If one person permanently holds a fixed share of the outcome, adding members stops helping, because that person's errors never average away.

Gough is a historical analogy for what concentrated public prominence can look
like, not a measurement of a stationary influence weight.

He was not a member of a deliberating committee, so this is an extension past the model's literal setting and I want to flag that rather than slide it past you. But the extension is natural. A movement's public credibility is a collective belief, held by outsiders, about whether the thing works. The Washingtonians had concentrated a large share of that belief in a few named speakers. When the largest holder failed, the aggregate failed, and a thousand quiet successes elsewhere could not average it out.

The dynamical model does not supply a state-free ratio for damage moving from a
member to a group and back. Group resources are nonlinear summaries of member
states, while their effects on members also depend on capacities, gates, remaining
headroom and the current population. It therefore cannot establish that Gough
survived the Washingtonians for a single directional reason.

And there is a design implication. If you want to stop any member acquiring a large influence weight, you can either manage prominence after it appears, which means arguing with newspapers, as the temperance press spent October 1845 doing and losing; or you can remove the raw material from which prominence is built, which is surnames, occupations, titles and public identification. The second is much easier. It is what Tradition 12 does.

The two relapses give a revealing same-person contrast, not a natural experiment.
Same man and illness, twenty-nine months apart; a small internal response in 1843,
then investigation, press war and eventually a court case in 1845. Prominence is a
plausible mechanism, but the episodes differ in circumstances besides the man and
do not identify influence weight as the cause.

### 2. The technical version

Let A be the row-stochastic matrix of trust weights among N members and s the influence vector, normalised so that the entries sum to one. The simulation in Chapter Seven compares four governance regimes as N grows:

| Regime | max influence, N=10 | N=500 |
|---|---|---|
| Flat, equal weights | 0.100 | 0.002 |
| One dominant member holding 35% | 0.350 | 0.350 |

At N = 10 the two are hard to tell apart, which is why a small group cannot detect the problem by introspection. At N = 500 flat weighting has fallen by a factor of fifty and the dominant-member regime has not moved.

Accuracy, as mean absolute distance between consensus and truth when each member gets the truth plus independent unit noise:

| Regime | error, N=10 | N=500 |
|---|---|---|
| Flat, equal weights | 0.252 | 0.036 |
| One dominant member | 0.328 | 0.280 |

These are exact rather than simulated. If each member receives the truth plus independent noise of standard deviation sigma, the consensus is s . b, which is normally distributed about the truth with standard deviation sigma the length of s, so the mean absolute error is sigma the length of s sqrt(2/pi). Under flat weighting the length of s = 1/sqrt(N) and the error falls as exactly sigma * sqrt(2/pi) / sqrt(N).

The flat group becomes about seven times more accurate as it grows. The dominated group improves by about fifteen per cent and stops. Both reach consensus equally readily, which is the trap. The other governance arrangements, rotation and the collective forms of concentration, belong to Part Two, where they are the subject rather than the background.

**On direction.** The model contains no pair of reciprocal linear weights. Member
states enter resource capacities through means, counts, sums, dispersion and
saturation; resources enter growth through normalized bundles, beta, gates and
state. A directional comparison would require a named perturbation, state,
outcome and derivative. None is estimated here.

**Limits of the extension.** The theorem concerns members averaging beliefs about a shared question. Public reputation is not that. I claim a structural analogy, not an application. It would fail if outsiders' beliefs about a movement were formed by some process very unlike weighted averaging over its visible members. I think that is unlikely and I have not shown it.

### 3. Notes on sources

**This chapter has been substantially rewritten after reading Gough's own account.** An earlier draft characterised his framing of the 1845 episode from his chapter headings, since the relevant chapters were unread, and concluded he had treated it as a charge to be rebutted rather than a relapse to be owned. Having now read Chapters X and XIII in full, that was wrong. His September 1845 statement contains the words *I have fallen*, an explicit acceptance of blame for going with a stranger and for the brandy, a submission to his church's judgment, and an explicit statement that he does not blame anyone for disbelieving him. The error was mine and it ran in the direction of making my own argument easier, which is the direction errors usually run.

**The corrected reading is stronger.** With both relapses documented in his own words, the chapter no longer depends on any claim about Gough's character. It depends on the difference between the institutional responses, which is documented on both sides: the Washingtonian meeting at Worcester in April 1843, reported in the *Cataract and Washingtonian*, and the Mount Vernon Church examining committee of September and October 1845, whose report Gough reproduces.

**What is now first-hand.** The 1843 relapse in full, including the Tolu and ether, the spade wound, the automaton passage, the depot bell, the oyster room, the three or four further drinks, the burning of his appointment book, and the newspaper report of his reception. The 1845 statement in full, including the Croton Hotel, Jonathan Williams, Thompson's, the walk to Chatham Street, the hand over the glass, the brandy from the grocery store, the woman in black, the strange shirt, Mr. Camp, and the absence of craving during his illness. The church committee's appointment, the congregational vote, and the New York investigation. The 1869 passage about the blotted pages. The libel trial's date, court and judge.

**What remains second-hand.** The *National Police Gazette* account and its role in finding him, which reaches me through a twentieth-century book about the *Gazette*. The *Newburyport Daily Herald* front page of 4 October. The Venus and Alcohol line. The specific claims that no Jonathan Williams could be identified and that there were no soda shops on Chatham Street: note that Gough's own statement says there *are* two or three such establishments in that vicinity and that he believes he could identify the shop, so the sceptical claim and his account are in direct conflict and I have not resolved it. The contemporary newspaper record would settle it.

**On the drugging.** Maxwell writes that Gough either slipped or was tricked and declines to decide. I follow him. Gough admits drinking brandy on his own initiative after the soda, so the question is only whether the first drink was administered without his knowledge. His account of the preceding two years shows a man who had already relapsed once without any villain available to blame. He did not need to be drugged in order to drink. But the church committee investigated for over a month and did not repudiate him, and I cannot show he was not drugged. It does not affect the argument: what damaged the movement was not the truth of the matter but that the matter was public and contestable at all.

**A correction found by reading the trial chapters.** An earlier draft of this chapter said the libel action arose because the 1845 accusations had followed Gough to Britain and were still being printed. That is wrong. *Gough versus Lees* grew out of the so-called Dead Letter controversy of 1857, concerning a private letter about the failure of Maine Law prohibition in America, published without his consent. The 1845 episode was not the subject of the action. What the trial record does show, and what is now in the text, is that under examination the 1843 relapse was stated openly and 1845 was rendered as "a short illness". That is a better fact than the one I had, and I would not have found it without reading the chapters.

**On the numbers.** Every figure in section 2 was regenerated from the current model in a single session rather than carried over from earlier runs. The influence weights verified exactly. The accuracy figures did not: they had been Monte Carlo estimates quoted to three decimals, and they moved between runs by more than the last digit implied. They have been replaced with the closed-form expression, which is exact and reproducible. This is a small correction with a general lesson: a simulated number quoted to a precision the simulation does not support is a claim the author has not actually checked.

**On treatment.** Gough died in 1886 and his autobiography is a public document he wrote to be read. I have nonetheless tried to write about his drinking as an illness rather than an exposé, because that is what it was, and because a book arguing that anonymity protects sick people would be poorly served by treating a sick man as material.

### 4. References

**Read in full:**

Gough, J. B. (1869). *Autobiography and Personal Recollections of John B. Gough, with Twenty-Six Years' Experience as a Public Speaker.* Springfield, Mass.: Bill, Nichols & Co. Public domain; full text via the Internet Archive. Chapters I to V for the early life; Chapter X for the 1843 relapse in full; Chapter XIII for the 1845 episode, the September 22 statement, and the Mount Vernon Church committee report of October 31; Chapters XXVII to XXIX for the Dead Letter controversy of 1857, Gough's stated reasons for publishing the whole record, and the trial transcript of 21 June 1858 including the examination quoted in the text; the contents apparatus for the structure discussed in the text.

*Cataract and Washingtonian* (April 1843). Report of the Worcester and Westborough meetings, quoted in full by Gough at Chapter X.

Report of the Examining Committee, Mount Vernon Congregational Church, Boston, 31 October 1845. Reproduced by Gough at Chapter XIII.

Maxwell, M. A. (1950). "The Washingtonian Movement." *Quarterly Journal of Studies on Alcohol* 11: 410-452. The assessment of anonymity's survival value; the judgment that opponents seized on the lapse and that public confidence was impaired; the generalisation to less prominent but publicly known Washingtonians.

**Cited at a remove:**

*National Police Gazette* (1845), via Van Every, E. *The Sins of New York as "Exposed" by the Police Gazette*, ch. 4.

*Newburyport Daily Herald*, 4 October 1845.

Museum of Old Newbury, "The Mysterious Disappearance of John B. Gough" (2024). The placards, and the sceptical case against Gough's account.

**What was not read:**

The Gough scrapbook of clippings on the 1845 episode, held at the American Antiquarian Society, Worcester. This is Gough's own dossier on the affair and is the outstanding primary source for this chapter.

New York and Boston newspaper coverage, September and October 1845.

# Chapter Four: Akron, 1935

A stockbroker with no money stood in the lobby of the Mayflower Hotel in Akron, Ohio, in May of 1935, and did arithmetic that most drinking people will recognise.

He had come out on a proxy fight for control of a rubber company. The fight had collapsed. He was broke, in a strange city, with a hotel bill he could not comfortably pay, and at one end of the lobby there was a bar with people laughing in it. He had been sober about five months. He had got that way inside the Oxford Group, a Christian fellowship that emphasised confession, restitution, and surrender, and he had spent those five months trying with total commitment and total failure to sober up other alcoholics. Not one of them had stayed sober.

What he did next is the founding act of Alcoholics Anonymous, and it is worth being precise about why it worked, because it was not charity.

He went to a church directory in the lobby and started making calls, looking for another drunk to talk to. Not to save the other man. To save himself. He had noticed, in five months of failure, that the hours he spent talking to alcoholics were the hours he did not drink, and standing in that lobby he needed those hours more than he needed anything else.

The calls eventually reached a woman named Henrietta Seiberling, and through her a proctologist named Robert Smith, an Akron surgeon who had been drinking for years and who had come to Oxford Group meetings for two and a half years without getting sober. Smith agreed to fifteen minutes. The conversation ran several hours.

He drank again, once, in early June, on the way to a medical convention. His last drink was a beer to steady his hand for surgery on the morning of the tenth. Alcoholics Anonymous dates itself from that day.

---

The thing that made the Akron conversation different from five months of failures in New York was not technique. It was symmetry.

Wilson had been approaching alcoholics as a man who had recovered, offering to help. He had been, in effect, a missionary. What he did with Smith, standing in a stranger's house with his own sobriety hanging on the outcome, was different: he needed the conversation. He was not extending charity downward, he was asking for help while appearing to give it.

The alcoholics who preceded him in the Oxford Group had noticed that the group's methods worked on some drinkers. Wilson noticed something narrower and more useful: that the work itself was the medicine, and that its therapeutic value accrued to the person doing it. That is what the Washingtonians had discovered in Baltimore in 1840 and what the Sons of Temperance quietly dropped when they added sick pay and ranks. Wilson rediscovered it in a lobby, under pressure, for the most self-interested reason imaginable.

By 1937 the two groups, Akron and New York, could count about forty sober members between them, and Wilson and Smith sat down and counted. Twenty or so people had stayed dry for a meaningful stretch. It had taken two years to produce forty. At that rate the thing would reach a few thousand alcoholics in a century, and there were, they believed, hundreds of thousands of them.

They decided they had a communication problem, and this decision produced everything that followed, including the crisis that produced the Traditions.

---

The proposed solutions were ambitious. Paid missionaries. Alcoholic hospitals. A chain of recovery centres staffed by people who had recovered. All of it required money, and none of the people involved had any.

In late 1937 Wilson's brother-in-law made an introduction that reached Willard Richardson, who worked for John D. Rockefeller Jr., and a meeting was arranged for late December in Rockefeller's private board room. Wilson, Smith, Dr. William Silkworth, the physician who had treated Wilson, and alcoholics from both New York and Akron came to tell their story to a room of wealthy men. It began badly. The drunks, who were never at a loss for words, sat silent, awed by the room as much as by the money in it, until somebody suggested that each of them simply tell his story.

That is the moment the whole institution turned, and it turned twice, on two sentences spoken by a man who was not an alcoholic and had no stake in the outcome.

Albert Scott, who chaired the board of trustees of Riverside Church, had chaired the meeting. When the last man finished, Scott stood up at the head of the table and said: why, this is first century Christianity, what can we do to help?

Wilson, in his own phrase, went for broke. He asked for money, paid workers, a chain of hospitals, and above all literature. His companions, including the Akron men who had come with no such intention, backed him enthusiastically, watching the rich men nod. And then Scott asked his second question:

> Won't money spoil this thing?

What happened next is contested, and the contest is worth more than a tidy version would be. Frank Amos, a Rockefeller associate and an advertising man, went to Akron in February 1938 to look at the group in person, interviewing members, their wives and mothers, and a retired judge who chaired the board of the city hospital. In Wilson's memory Amos came back convinced and recommended that Rockefeller give the movement fifty thousand dollars, a very large sum in the money of the time, and it was Rockefeller himself who refused, repeating Scott's objection. In Henrietta Seiberling's memory it was she and the Akron people who persuaded Amos that money would spoil the thing, and Amos who carried that verdict back. Kurtz records both and does not choose. The difference matters because one version has the fellowship saved from money by a rich man's restraint and the other has it saved by its own members, and the second is the more flattering, which is a reason to hold it loosely.

What is not in dispute is the outcome. Rockefeller refused, on the ground that money would spoil any attempt at living out first century Christianity. He put five thousand dollars into the Riverside Church treasury, to be drawn out at thirty dollars a week to keep Wilson and Smith personally afloat, and that was all. In 1940 he gave a dinner and invited his wealthy friends to hear about AA, which produced publicity and almost no money, apparently by design.

Bill Wilson did not want this. He had gone looking for millions. He wanted the missionaries and the hospitals, and he was, by his own later account, disappointed. He would eventually credit Rockefeller with the idea that AA should be nonprofessional, which is a generous way of describing being refused.

The most distinctive financial rule in American mutual aid, the rule that AA declines outside contributions and supports itself entirely from the basket, did not originate in the fellowship's spiritual insight. It originated in a rich man's refusal, over the objections of the founder, in 1938.

---

With no money for missionaries, the communication problem had to be solved some other way, and the answer was a book.

Wilson began writing in 1938. The chapter containing the actual programme was drafted in one sitting, on a yellow pad, in bed. When he finished he had written down twelve steps. Four hundred copies of the working manuscript went out for comment, and the fellowship argued fiercely over the religious language: one contentious result of that argument was the softening of "you must" to "we ought" in various places, which is a small change with an enormous long-run effect on who can walk into a room and stay.

*Alcoholics Anonymous* was published in April 1939. It sold badly. The venture was rescued at one point by a member who mortgaged his tailor shop to pay the printer. The first board minutes of the Alcoholic Foundation record a treasury of 2,150, which was what remained of Rockefeller's five thousand.

Then, in the autumn of 1939, *Liberty* magazine ran an article, and about eight hundred desperate calls came in. In 1941 the *Saturday Evening Post* sent Jack Alexander, a sceptical reporter, who came away convinced and published a long piece in March. The response was overwhelming: thousands of appeals, and a fellowship that had taken four years to reach a few hundred members began growing at a rate nobody had planned for.

That is where Part One's argument reconnects with its beginning, and it does so at a point I did not anticipate before building the model.

The Washingtonians in 1840 had exactly one way for a new person to arrive: an existing member went and got him. There was no medical consensus that alcoholism was treatable, no treatment system to refer out of, no courts assigning attendance. Every arrival was produced by member activity.

AA in 1939 was in the same position. And then, between the *Liberty* piece and the *Saturday Evening Post*, it acquired a second channel: people who arrived because they had read something, or because a doctor or a wife or eventually a court sent them, independent of whether any member had gone out looking. In the model that runs underneath this book, that second channel is the difference between a group that can die from a quiet decline in member energy and one that cannot.

AA got that channel in 1941. The Washingtonians never had it.

And the growth it produced is what broke the fellowship's informal arrangements and forced somebody to write down rules, which is Chapter Five.

---

## The Machinery

### 1. What the model says

The model has two ways a newcomer arrives: **attraction**, proportional to how much twelfth-step work members are currently doing, and **referral**, an exogenous stream arriving independent of member activity.

Chapter One noted that the Washingtonians ran on attraction alone, and that the model treats a one-channel group as structurally fragile: explosive growth is available, but there is no floor, because nothing arrives on its own.

AA ran on attraction alone from 1935 to 1939. The 1939 book, the *Liberty* article and above all the 1941 *Saturday Evening Post* piece created the second channel. A person who read Jack Alexander's article and wrote to a post office box in New York had not been recruited by anybody. In model terms, AA acquired a non-zero referral floor in 1941, and it has never lost it: the modern equivalents are treatment programmes, courts, hospitals, and doctors.

Running the corrected model at a thirty-year horizon over four hundred paired random seeds, with everything else held at full adherence:

- Both channels intact: 98.5 per cent finish above five members, none close, and mean endpoint size is 17.80.
- Attraction lost, referrals intact: the same 98.5 per cent finish viable, none close, and mean size is 12.38.
- Referrals lost, attraction intact: 2.75 per cent finish viable, 10.5 per cent still exist, 89.5 per cent close, and mean size is 0.51 counting closures as zero.
- Both lost: none finish viable; one run in 400 still contains one member and 399 close.

The asymmetry is the point. A group with only referrals becomes small and stays alive. A group with only attraction stays large while its members are working and then has nothing underneath it.

I want to be careful about what this does and does not establish. It does not show that AA survived *because* of the *Saturday Evening Post*. It shows that a structural difference between AA after 1941 and the Washingtonians ever is exactly the difference that the model treats as decisive, and that this was not built into the model to produce the result: the two-channel inflow was added for an unrelated reason, to stop the simulation predicting that a struggling group receives no arrivals at all.

### 2. The technical version

Arrivals are drawn from a Poisson process with rate

> lambda = lambda_exog + lambda_0 * (sum over members of x_12) * T_11

where x_12 is a member's twelfth-step practice level, T_11 is adherence to the attraction principle, and lambda_exog is the referral floor. Setting lambda_exog = 0 recovers the pre-1941 condition and the pre-1848 Washingtonian condition.

With lambda_exog = 0, expected arrivals are strictly proportional to current aggregate member activity, so the population dynamics have an absorbing state at zero with no restoring force: if activity falls, arrivals fall proportionately, which lowers future activity. With lambda_exog > 0 the origin is no longer absorbing, and a group reduced to near-zero members still receives a trickle. That is what produces the stable remnant in the second scenario above.

The parameter values used are lambda_exog = 0.12 arrivals per week and lambda_0 = 0.05. Neither is estimated from data. They were originally chosen to target a group near 45 members with an experienced core near 9, but the corrected model no longer meets that calibration. Across all 400 runs its mean endpoint size is 17.80 ± 0.88. Among the 394 viable endpoints, the mean established count above 0.1 is 14.13 ± 0.79 and the experienced count above 0.5 is 1.25 ± 0.20. Every quantitative claim in this section inherits from these author-chosen rates and from the failed original calibration; no real meeting-size estimate should be read from them.

### 3. Notes on sources

**This chapter is the least well sourced in Part One, and I want that on the record.** Chapters One to Three rest on documents I read in full: Maxwell's 1950 study and Gough's 1869 autobiography. This chapter rests on a scholarly work I have not yet obtained, plus a set of secondary accounts that mostly derive from AA's own copyrighted histories.

**What is well attested across independent sources.** The Mayflower Hotel lobby and the church directory; the Seiberling introduction; Smith's Oxford Group attendance without sobriety; the June 1935 founding date; the 1937 count of about forty members; the Rockefeller approach; Frank Amos's February 1938 Akron investigation and his fifty-thousand-dollar recommendation; Albert Scott's question about money spoiling the thing; Rockefeller's refusal and the five thousand dollars at thirty dollars a week; the 1940 dinner; the 1939 publication; the *Liberty* article and roughly eight hundred responses; Jack Alexander's March 1941 *Saturday Evening Post* article and the flood that followed; the tailor-shop mortgage; the 2,150 first-meeting treasury.

**What I am reporting at one or more removes.** Nearly all of it. The Amos report, the Scott question and Rockefeller's reasoning are quoted in AA's own *Alcoholics Anonymous Comes of Age* and *Dr. Bob and the Good Oldtimers*, and reach me through secondary sites that quote those books. Wilson's disappointment at being refused, and his later crediting of Rockefeller with the nonprofessional principle, come from secondary accounts of his own recollections.

~~**The acquisition that would fix this** is Ernest Kurtz, *Not-God*.~~ **Obtained and read, 2 August 2026**, in the expanded 1991 edition. The narrative spine of this chapter is now first-hand: the failed Akron proxy fight of early May 1935; Wilson pacing the Mayflower lobby on Saturday 11 May, the day before Mother's Day, with the bar filling at one end of his track and the hotel church directory standing at the other; the thought *God, I am going to get drunk* and the panic that followed it, which Kurtz calls the final founding moment; and Dr Bob Smith's last drink on 10 June 1935, followed the same day by his rounds of confession and restitution to creditors and others he had harmed.

**One thing Kurtz changes rather than confirms.** This chapter, like most accounts, treats the Akron meeting as *the* founding. Kurtz names four founding moments: Jung's 1931 conversation with Rowland H.; Ebby T.'s visit to Wilson in late November 1934; Wilson's experience at Towns Hospital in mid-December 1934 and his discovery of William James; and the Wilson-Smith interaction across May and June 1935. The June date is, in his phrase, the enshrined one rather than the only one. This chapter keeps the June founding because that is what AA's own Landmarks record, but it should not be read as claiming a single origin.

**The board room scene has since been rebuilt on Kurtz, and it was in the wrong order.** This chapter had Amos's Akron visit and his fifty-thousand-dollar recommendation coming first, and Scott's question arriving afterwards as the thing that stopped it. Kurtz has Scott's question at the December 1937 meeting itself, immediately after Wilson's appeal, with Amos sent to Akron afterwards. So the objection preceded the investigation rather than answering it. Kurtz also records that the outcome is contested: Wilson remembered Amos recommending the money and Rockefeller refusing it; Henrietta Seiberling remembered persuading Amos in Akron that money would spoil the thing. The chapter now carries both.

**What is still at a remove.** The Amos report itself and Rockefeller's reasoning still reach this chapter through AA's copyrighted histories, and Kurtz is drawing on those same histories alongside the correspondence for parts of this episode. The chapter is no longer a well-corroborated outline, but it is not yet uniformly first-hand either.

**A note on the 1939 first edition.** Its US copyright appears not to have been renewed and facsimile reprints are commercially available, so the text itself is probably usable as a primary source. It contains the Steps. It does not contain the Traditions, which were written seven years later, so it does not help with Chapter Five.

### 4. References

**Read in full:**

Kurtz, E. (1979; expanded edition 1991). *Not-God: A History of Alcoholics Anonymous.* Center City, Minn.: Hazelden. A Harvard doctoral dissertation by the first researcher granted full access to AA's archives, published by a non-AA press. Used here for the proxy fight, the Mayflower lobby, the founding moment and its date, Dr Bob's restitution rounds, the four-founding-moments framing, and the December 1937 board room: the attendance, the silence, the suggestion that each man tell his story, Scott's two questions, Wilson going for broke, and the two incompatible memories of why the fifty thousand dollars was refused. **In copyright; the full text is not stored in the repository.** See `research/SOURCES.md`.

Maxwell, M. A. (1950). For AA's early structure and his contemporaneous description of the fellowship as small, informal, poor and unpretentious in its first years.

Various AA area and intergroup historical compilations, used only where two or more agreed and where the claim traced to a named AA publication.

**Cited at a remove:**

Alcoholics Anonymous World Services (1957). *Alcoholics Anonymous Comes of Age.* One of Kurtz's sources for the 1937 Rockefeller board room and for Scott's questions. Not read.

Alcoholics Anonymous World Services (1980). *Dr. Bob and the Good Oldtimers*, pp. 128 to 130. Source of the Frank Amos Akron investigation and report.

Minutes of the first meeting of the Alcoholic Foundation board. Source of the 2,150 figure.

**What was not read:**

*Alcoholics Anonymous*, 1st ed. (1939). New York: Works Publishing.

Alexander, J. (1 March 1941). "Alcoholics Anonymous." *Saturday Evening Post.*

# Chapter Five: Twelve Points to Assure Our Future

By 1945 the mail was the problem.

Jack Alexander's article had done what the founders spent 1937 failing to buy: it had made Alcoholics Anonymous national, and it had done so without missionaries, without hospitals, and without a dollar of Rockefeller money. The two thousand members who had watched that article appear in 1941 were more than fifteen thousand by 1945. Groups were forming in cities where nobody from New York had ever set foot. There was no organisation to speak of, no charter, no permission required. Two or three alcoholics could call themselves an AA group and did.

And they wrote to New York. Most of the letters wanted literature, or the address of another drunk in the next county. But a good many asked questions of procedure and practice, and a few asked questions of theory, and Wilson answered them himself, for hours, one at a time. Ernest Kurtz, who read the files, reconstructs the house style of those replies:

> If I understand correctly, your problem sounds similar to. . . . On that occasion, these good people, now years sober, tried. . . . Of course, it is for you and your group to work this out: I can only relate to you what we seem to have learned from past experience. Perhaps you and your group will choose to follow this, but whether you do or not, please let us know how it comes out.

Read that as a piece of governance rather than as correspondence. The man with more standing than anyone else in the fellowship is telling a group of strangers that the decision is theirs, that he can report experience and not issue instructions, and that he wants to hear the result whichever way they go. Two of the Traditions this chapter is about were being practised in the second person singular, in a letter, years before anyone wrote them down. And a third was being practised by omission, because the obvious solution to a repetitive mailbag is a rule book with an office behind it, and that is the solution nobody took.

Kurtz states the problem of those years more precisely than I would have dared to:

> From 1941 through 1945, the primary concern was how to share effectively the rapidly accumulating wisdom of experience without establishing a central authority, the very existence of which might stifle further experience and greater wisdom.

That is this book's argument about the ninth Tradition, written by AA's historian in 1979, with no theorem in front of him and no interest in one. Hold it for Part Two, where the condition it describes turns out to have a name.

---

Wilson did not want to write the Traditions.

By 1945 the questions had begun to repeat, which suggested to him that the whole mass of experience might be codified into a set of principles offering tested solutions to the problems of living and working together. He could see it. He hesitated anyway, and the reason he gives is the interesting one: he feared losing the personal touch, which was itself the thing that kept the experience flowing to him. A codebook answers the letter and ends the correspondence. Kurtz's summary of what finally overcame the hesitation is a sentence I would hang in any institution about to write its constitution. Writer's cramp, the scantness of staff assistance, and the repetitive nature of some concerns won out.

The matters he listed as by then settled by consistent and at times painful experience were membership, group autonomy, singleness of purpose, nonendorsement of other enterprises, professionalism, public controversy, and anonymity in its several aspects. Seven headings, every one of them a fight that had already happened somewhere, and between them they account for most of the twelve points that followed.

And then, before publishing, he disclaimed the genre:

> a code of traditions could not, of course, ever become rule or law [,] but might serve as a guide for our Trustees, Headquarters people, and especially for groups with growing pains

An earlier draft of this chapter called the Traditions a set of rules, four times over. Wilson's own framing sentence says they are not rules and cannot become rules, and the distinction is not modesty. A rule is enforced by whoever holds the authority to enforce it, and the entire problem of 1941 to 1945 was that creating such an authority would stop the experience arriving. What he wrote instead was a report of findings addressed to people with growing pains. That is a weaker instrument than a rule and, on this book's argument, a stronger one.

The long form went into the *A.A. Grapevine* in April 1946, headed "Twelve Suggested Points for A. A. Tradition". Its first three sentences are the thesis of this chapter, and I did not know they existed when I wrote the chapter. They are quoted here from the article rather than from a historian's account of it:

> Nobody invented Alcoholics Anonymous. It grew. Trial and error has produced a rich experience.

The text was cut soon after, to sit closer to the two hundred words of the Twelve Steps, and that short form appeared in November 1949. The fellowship adopted the Traditions officially in June 1950.

One edit made during the shortening is worth more than its size. Tradition Three had required an *honest* desire to stop drinking. The qualifier was dropped in 1949, on the published ground that it is nearly impossible to determine what constitutes an honest desire to stop as against the other forms in which the desire arrives. A fellowship that had just spent four years codifying its experience was still amending the code on the evidence three years later, which is what it looks like when a document is a record rather than a founding charter.

---

The specific crises are worth naming, because the Traditions are answers and each one has a fight behind it.

The one with the best documentation is professionalism, and it happened in 1937, nine years before anything was written down.

Charles Towns owned the hospital where Wilson had been detoxified and where he now walked the corridors looking for prospects. Towns met him there one day and made him an offer. Kurtz gives it close to verbatim: a hunch that this AA business was someday going to fill Madison Square Garden, an observation that the drunks around Wilson were getting well and making money while he gave the work full time and stayed broke, and then the proposal. An office. A decent drawing account. A very healthy slice of the profits. Perfectly ethical. You could become a lay therapist, and more successful than anybody in the business.

Wilson, by his own account, was bowled over. He felt a few twinges of conscience about how pleased he was, and Towns's stress on the word *ethical*, along with his own guilt about what his wife had been carrying, disposed of them.

That evening happened to be meeting night at Clinton Street. He came in and told the group about his opportunity, and as he laid out the details his enthusiasm drained away against their silence. His own record of it is that with waning enthusiasm his story trailed off to the end, and that there was a long silence. Then somebody spoke for the room:

> We know how hard up you are, Bill . . . it bothers us a lot. . . . [But] don't you realize that you can never become a professional? . . . You tell us that Charlie's proposal is ethical. Sure, it's ethical. But what we've got won't run on ethics only; it has to be better. Sure, Charlie's idea is good, but it isn't good enough. This is a matter of life and death, Bill, and nothing but the very best will do.

Wilson declined the offer. Kurtz's gloss is that this was the first time he heard the voice of what he would later call the group conscience, and that he obeyed it.

Two things about that scene are load-bearing here, and they point in opposite directions. The first is that the eighth Tradition and the second Tradition arrive together, in one room, in the same five minutes: the fellowship discovers that it will not be professionalised, and discovers the mechanism by which it decides such things, and the mechanism is a group of unimpressive men outvoting their founder by saying nothing until he stops talking. The second is that this cuts against any account in which the Traditions were composed by Wilson. He was on the losing side of the first one.

John Hawkins had faced a version of the same offer a century earlier and taken it, becoming the paid secretary of the Massachusetts Temperance Society in 1841. I flagged that sentence in Chapter One and asked you to hold it. This is where it lands.

The money question had been settled the same way and against Wilson's wishes, in Rockefeller's board room at the end of 1937, and Chapter Four tells that story. What the refusal did not settle is what an individual group should do when somebody offers it a building, or leaves it a bequest, or when a hospital wants to pay a member to work with its patients. Those are group-level questions and they were still arriving in the mail in 1945.

Publicity was the third pressure. Members were giving interviews under their own names, and some were using the AA connection to advance careers or causes. Whether the early members knew the Gough case specifically I cannot say and have not found. What they certainly knew was that any member publicly identified as AA carried the fellowship's reputation on his own sobriety, permanently.

Outside causes were the fourth, and the ground was well prepared: AA had arrived in a country where the temperance movement was living memory and prohibition had been repealed only a decade earlier. The invitation to take a position was constant and the precedent was catastrophic. Chapter Two shows Wilson reaching for that precedent in print in August 1945, eight months before the Traditions were published, and saying so.

---

Maxwell, writing in 1950 with AA's own 1947 booklet in front of him, catalogued what the groups had actually done in the years before the Traditions were written. Membership had been limited. The conduct of groups had been undemocratic. Leaders had exploited groups for personal prestige. The principle of anonymity had been violated. Personal and jurisdictional rivalries had developed. Money, property and organisational difficulties had disrupted groups.

Every one of those is a Tradition, stated as a failure that had already happened.

Which is the point about method, and it is a point about method rather than content.

The Traditions were not designed. They were recorded.

Wilson did not reason from first principles about what a decentralised mutual-aid organisation ought to look like. He answered eleven years of letters, noticed which failures kept recurring, and wrote down what the groups that had not blown up were doing. Nothing in Part Two depends on his having foreseen anything. What it depends on is that a long and painful selection process, running across thousands of independent groups, can arrive at an arrangement that turns out to be provably right. A design can be correct before anybody can say why.

Which is also why the mechanism is worth checking rather than assuming. Selection under real conditions produces adaptations, but it also produces superstitions, and both arrive wearing the same clothes. The first fellowship in this story wrote down a code of its own within two years of founding, as Chapter One shows, and it did not save them.

---

There is one Tradition where the historical record is unusually clear about the cost, and it is the one economists would flag first.

Tradition 7 says an AA group declines outside contributions and supports itself from the basket. Combined with Tradition 4, which makes each group autonomous, and Tradition 9, which forbids organising into a hierarchy, this closes the system: there is no party outside a group that can put resources into it or direct it.

Bernard Holmström proved in 1982 that in team production where individual effort cannot be observed, no budget-balanced sharing rule attains the efficient outcome. To get there you need an outside party who absorbs the residual, a budget breaker. Tradition 7 forbids precisely that party.

So AA is not merely autonomous. It is operating at a knowing second best, and it has been since Albert Scott asked his question in a room in 1937. The fellowship pays for its independence in efficiency, permanently, and the model in Part Five puts a number on part of the cost: a group's ability to carry newcomers is bounded by what its established members can supply, with nothing available from outside when that runs short.

---

That is where Part One's history ends. A fellowship had been founded on an insight that another fellowship had discovered ninety-five years earlier and lost. It had acquired, almost by accident, a second inflow channel its predecessor never had. And between 1946 and 1950 it wrote down twelve points, drawn from its own catalogue of disasters and disclaimed as rules by the man who wrote them out, whose net effect was to forbid nearly everything the Washingtonians' successor organisation had added.

Whether those points are why AA is still here is the question the rest of this book exists to examine. But it is not a question I get to ask first.

Somebody asked it in 1950, and got most of the way to the answer.

---

## The Machinery

### 1. What the model says

The model divides the Traditions into two functional classes, and the division was derived rather than assumed. In Part Four I describe how: by writing down what resources a group produces that a member's step work actually consumes, then asking which Traditions govern the supply of each resource, without at any point mapping Traditions to Steps directly.

Five Traditions come out of that derivation governing no resource that any Step consumes: autonomy, no endorsements, self-support, no hierarchy, and no opinion on outside issues. They cannot help a member directly. Their entire function is to protect the Traditions that can. In the model they are implemented as multipliers on the others, and when they are degraded, what falls is the effectiveness of unity, group conscience, the open door, attraction and anonymity.

This is exactly the shape of Wilson's 1946 problem. He was not writing to make individual members recover. He was writing to stop groups destroying themselves, so that the conditions under which members recover would still exist next year. The Traditions are a guard on the Steps, and the derivation says so in a way I did not put in by hand. His own description of the intended audience says the same thing from the other side: trustees, headquarters people, and especially groups with growing pains. Not members.

The chapter's other model connection is Tradition 7 and the closed system. Because no resource can enter a group from outside, everything a newcomer needs must be produced by the members present. The model makes this concrete: carrying capacity is supplied by the members already practising, discounted by the newcomer load it is carrying, with the identification resource drawing on the established count and the demonstration, confidentiality and counsel resources on the smaller experienced one. There is no external term. A group whose core is thin cannot import one.

### 2. The technical version

Protective Traditions enter as multipliers on effective adherence, applied once each with no compounding:

> T2_effective = T2 * (0.6 + 0.4 * mean(T9, T12))
> T5_effective = T5 * (0.6 + 0.4 * mean(T6, T10))
> external_factor = 0.7 + 0.3 * mean(T4, T7)

with the external factor multiplying all of them. The functional forms are chosen, not estimated. The one substantive constraint is that they are additive within each bracket and applied once, because an earlier version of the model multiplied adherence terms repeatedly and produced an artefact: a group at uniform 0.8 adherence collapsed in every parameterisation tested, because a twenty per cent shortfall compounded through four or five multiplications into something closer to fifty.

Under common random numbers with **four hundred** paired replications, degrading each Tradition singly from 0.85 to 0.50 and measuring membership at a twenty-year horizon against a reference group of 13.10 members:

| Tradition | Tier | Members lost | 95% half-width | t |
|---|---|---|---|---|
| T3 mixed adherence | enabling | 2.99 | 0.65 | 9.1 |
| T11 mixed adherence | enabling | 1.88 | 0.60 | 6.1 |
| T1 unity | enabling | 1.65 | 0.65 | 4.9 |
| T12 anonymity | enabling | 0.99 | 0.58 | 3.3 |
| T5 one purpose | enabling | 0.96 | 0.61 | 3.1 |
| T4 autonomy | protective | 0.88 | 0.62 | 2.8 |
| T7 self-support | protective | 0.88 | 0.62 | 2.8 |
| T2 group conscience | enabling | 0.48 | 0.62 | 1.5 |
| T6 no endorsement | protective | 0.23 | 0.46 | 1.0 |
| T10 no outside opinion | protective | 0.23 | 0.46 | 1.0 |
| T9 no organisation | protective | 0.02 | 0.43 | 0.1 |
| T8 non-professional | enabling | -0.20 | 0.51 | -0.8 |

Seven of the twelve have intervals excluding zero. Five are unresolved and are reported as unresolved rather than ranked on point estimates the variance does not support. The T3 and T11 rows are mixed adherence interventions affecting both of each Tradition's executable paths; the release-gate factorials report those paths separately.

**This table replaced an earlier one computed from thirty replications, and the ordering changed completely.** The thirty-replication version reported that only Traditions 4 and 7 cleared significance, at 5.5 members each with t = 2.6, with unity tied on the point estimate and six comparisons unresolved. That put the two protective Traditions at the top, and the paragraph beneath it noted the coincidence with their derived role while warning that it was not strong evidence, because a multiplier on several things will tend to matter.

The caution was right and the table was wrong. Under the corrected mean-one capability model, the top of the table is enabling rather than protective. Mixed Tradition 3 adherence leads, followed by mixed Tradition 11, unity, anonymity and singleness of purpose. Autonomy and self-support remain resolved and tied below them.

So the honest reading of this comparison is the opposite of what it was: **the Traditions that supply something to a member directly matter more, in this model, than the ones that protect the supply**, and the earlier appearance to the contrary was a small-sample artefact. That does not touch the derivation in Part Four, which is about which Traditions govern which resources and is exact algebra; it touches only what the simulation says about degrading them one at a time.

### 3. Notes on sources

**This chapter has been rewritten against Kurtz and is no longer provisional.** The previous version was built from Maxwell's 1950 summary plus secondary accounts, and its own notes said so. Kurtz, *Not-God*, read in full, supplies the composition history at first hand from AA's archives and the Wilson correspondence, and it corrected the chapter in five places.

**The date was wrong.** The chapter opened with 1944 as the year the mail became the problem. Kurtz puts the repetition of questions, and Wilson's conclusion that the experience could be codified, in 1945. Corrected, along with the membership figures, which Kurtz gives as two thousand in 1941 and over fifteen thousand by 1945.

**The word "rules" was wrong, and this is the correction that matters most.** The chapter called the Traditions rules, in the main text and in its closing paragraph. Wilson's own framing, quoted by Kurtz from the material he circulated before publication, is that a code of traditions could not ever become rule or law but might serve as a guide. The chapter now says what he said, and the distinction does real work: the difficulty the Traditions answer is precisely that a rule needs an authority to enforce it, and creating that authority was the outcome AA was trying to avoid.

**Two sources disagree about when the Traditions appeared, and I follow Kurtz.** Maxwell, writing in 1950, says the statement emerged in 1947 and 1948 in the Twelve Points of Tradition, elaborated in *Grapevine* editorials and subsequently published as a booklet. Kurtz, working from the archive thirty years later, dates the long form to April 1946, the short form to November 1949, and official adoption to June 1950. Maxwell is contemporary and Kurtz had the files; where they conflict on a date of publication I take the archive. Maxwell's 1947 and 1948 are a fair description of the *elaborating* editorials and of the booklet, which is the 1947 *A.A. Tradition* he cites as his own source.

**A citation problem inside Kurtz, now half resolved.** He cites the April 1946 publication twice with different details: once as "Alcoholics Anonymous Tradition: Twelve Points to Assure Our Future," *AAGV* 2:10 (April 1946), 7-9, described as the first public presentation of the Twelve Traditions, and once as the long form published in *AAGV* 2:11 (April 1946), 2-3. Same month, different issue number, different pages.

The article itself has since been read, and it explains the two titles rather than the two issue numbers. Its *Grapevine* headline is "Twelve Suggested Points for A. A. Tradition, By Bill". Inside the body, Bill introduces the list under a heading of his own: "An Alcoholics Anonymous Tradition of Relations, Twelve Points to Assure Our Future". Kurtz is citing that internal heading, AAWS's own pamphlet uses the same phrase, and this chapter takes its title from it. So the two names are one article and neither citation is wrong about the title. **The issue numbers remain unadjudicated**: the scan consulted carries no issue or page markers, so one of 2:10 and 2:11 is still a slip and I still cannot say which.

**The chapter previously said the Traditions were formally adopted at the fellowship's first international convention in 1950.** Kurtz says they were officially adopted in June 1950, and separately describes the Cleveland gathering of 1950 as the fifteenth anniversary convention, which Wilson labelled A.A.'s Coming of Age party. He does not connect the adoption to that meeting. I have dropped the connection rather than assert it.

**The Towns episode is new and is the best-documented thing in the chapter.** Kurtz gives the offer, Wilson's reaction, the meeting at Clinton Street and the group's reply, quoting Wilson's own later telling throughout. Two cautions. It is Wilson recalling a scene in which he is corrected, decades later, for an audience that had come to believe in the correction, which is the kind of story institutions polish. And the dating is Kurtz's: the financial crisis at Clinton Street in mid-1937, the Towns offer following, and the Rockefeller board room some six months after that.

**A claim dropped.** The chapter had said the 1938 trust agreement establishing the Alcoholic Foundation contained a provision requiring an alcoholic trustee to resign immediately on drinking, and that this happened within months. I have not found the provision in Kurtz, and it entered this chapter from a secondary account. Dropped rather than carried.

**What remains at one or more removes, and one remove that has since been shortened.** The 1949 *Grapevine* short form; *Alcoholics Anonymous Comes of Age*, which is where Kurtz's citations for the adoption date and for both forms lead; and the 1947 *A.A. Tradition* booklet, which is Maxwell's source for the catalogue of early failures. So the catalogue in this chapter reaches the reader through a sympathetic sociologist reading an AA booklet, and the composition history reaches it through an independent historian reading AA's files. Those are different qualities of remove and the chapter should not be read as though they were the same.

The 1946 long form is now the exception. AA's own pamphlet *A.A. Tradition: How It Developed*, obtained in its July 2024 edition, reproduces the "Twelve Points to Assure Our Future" in Bill W.'s foreword, and its text has been read directly and checked against the page images rather than taken from Kurtz. **This shortens that remove without closing it**: a 2024 AAWS pamphlet is a reproduction, not the April 1946 *Grapevine*, and it therefore says nothing about which of Kurtz's two conflicting issue numbers is the slip. What it does settle is the wording, which is what this chapter's argument actually rests on.

It also supplies a fact the chapter needed and did not have. The pamphlet states that in all but the Second Tradition the original language has been modified or shortened. That is AA's own account of the cutting described above, and it means the familiar short forms are not simply compressions of the 1946 text but revisions of it, with one exception. Tradition 2, the one that carries the group conscience and the phrase about leaders who do not govern, is the only one that reaches a reader today in the words Wilson first published.

**The Holmström application is mine.** The 1982 result is real and I have read the argument; the application to Tradition 7 is my own reading and, as far as I know, novel. It should be treated as an interpretation rather than a finding.

### 4. References

**Read in full:**

Kurtz, E. (1979, expanded 1991). *Not-God: A History of Alcoholics Anonymous.* Center City, Minn.: Hazelden. **Read at source.** Chapter Five and its notes, and the 1937 material in Chapter Three. Used here for the 1941 to 1945 statement of the problem, the membership figures, the reconstructed house style of Wilson's replies, his hesitation and what overcame it, the seven matters he listed as settled, his disclaimer that a code of traditions could never become rule or law, the April 1946 long form and its opening sentences, the November 1949 short form and the dropping of "honest" from Tradition Three, the June 1950 adoption, the Towns offer and the Clinton Street meeting, and the identification of that meeting as Wilson's first encounter with the group conscience. **In copyright; the full text is not stored in this repository.** See `research/SOURCES.md`.

Alcoholics Anonymous World Services. *A.A. Tradition: How It Developed.* Pamphlet P-17, July 2024 edition, written by Bill W. **Read in full**; obtained from AAWS's official distribution on 4 August 2026, and the two passages this book relies on were checked against the rendered page images rather than the OCR. Source for the text of the 1946 "Twelve Points to Assure Our Future" as AAWS reproduces it, and for the statement that in all but the Second Tradition the original language has been modified or shortened. **The document is deliberately not stored in this repository**: it is copyrighted AA literature and this repository is public, so the record under `research/incorporated/AAWS_2024_P17/` keeps the citation, the official URL, the file hash and the verified quotations instead. **Note what it is not.** It is a 2024 reproduction, not the April 1946 *Grapevine*, so it cannot adjudicate the conflicting issue numbers recorded above, and a claim turning on 1946 typography would still need the original.

Maxwell, M. A. (1950). "The Washingtonian Movement." *Quarterly Journal of Studies on Alcohol* 11: 410-452. **Read in full**; the original project PDF and text are stored in the Maxwell subdirectory of `research/incorporated/`, in a retyped copy whose transcription errors are listed in `research/SOURCES.md`. Source here for the catalogue of early AA organisational failures, taken by Maxwell from the 1947 *A.A. Tradition* booklet; for the observation that in AA there is actually no overhead authority and that wherever two or three alcoholics gather on the basis of the Twelve Step programme they may call themselves a group; and for the dating discussed above.

Holmström, B. (1982). "Moral Hazard in Teams." *Bell Journal of Economics* 13(2): 324-340. The budget-breaker impossibility result applied to Tradition 7.

**Cited at a remove:**

Wilson, W. (1946). "Twelve Suggested Points for A. A. Tradition." *AA Grapevine*, April 1946; cited by Kurtz as "Alcoholics Anonymous Tradition: Twelve Points to Assure Our Future," 2:10, 7-9. **Read at source.** A scan of the article was consulted on 10 August 2026 and is recorded in `research/incorporated/Grapevine_1946/`. Source for the three opening sentences quoted above, for the two titles the text carries, and for the twelve points in their original wording. **The document is not archived in this repository**: it is A.A. Grapevine copyright, the located scan is a third-party reproduction with unverified posting authorization, and the project's rights review directs that it be cited and quoted within limits rather than stored. The scan carries no issue or page markers and so cannot settle Kurtz's conflicting issue numbers.

Wilson, W. The long form of the Twelve Traditions, *AA Grapevine* 2:11, April 1946, 2-3, and the short form, *AA Grapevine* 6:6, November 1949, 16-17. Both as cited by Kurtz. Not read. The two April 1946 citations conflict and the conflict is recorded above.

*A.A. Tradition* (1947). New York: Works Publishing. Maxwell's source for the catalogue of failures. Not read.

Alcoholics Anonymous World Services (1957). *Alcoholics Anonymous Comes of Age.* Kurtz's source for the adoption date and for the texts of both forms. Not read.

**What was not read:**

Rockefeller Archive Center. Correspondence relating to the 1937 to 1940 approaches, the Frank Amos report, and the 1940 dinner. Kurtz has narrowed what this would settle: he records two incompatible memories of why the fifty thousand dollars was refused, and the archive is where that would be resolved. See Chapter Four.

# Chapter Six: The Sociologist

In 1950, an assistant professor of sociology at State College of Washington, in Pullman, published a forty-two page study of a fellowship that had been dead for a century.

Milton Maxwell had reasons beyond antiquarian interest. He said so in his first paragraph. A number of observers, he wrote, had noticed certain similarities between the Washingtonian movement and Alcoholics Anonymous. Why the older movement declined so fast was therefore still of concern to AA members, who might wonder whether the same fate was waiting for them.

That is the question the whole paper is written to answer. A fifteen-year-old fellowship of alcoholics was looking at a dead one that had reached perhaps six hundred thousand people and vanished inside a decade, and asking whether it was looking in a mirror.

Maxwell's answer was no, and his reasons are this book's thesis, stated seventy-five years before this book.

---

He worked through the comparison methodically. The similarities he granted freely: alcoholics helping each other, the needs of alcoholics kept central, weekly meetings, the sharing of experience, the fellowship of the group constantly available, reliance on a power greater than oneself, total abstinence. On those seven points the two movements are nearly the same organisation.

Then the differences, and these are what he thought decisive.

**Exclusively alcoholic membership.** The Washingtonian societies admitted anyone, and Maxwell saw clearly what that cost. His argument was not about atmosphere. It was that the greatest long-run value of an exclusively alcoholic membership is that it *permits and reinforces exclusive attention to the rehabilitation of alcoholics*. He had the Vermont numbers in front of him: 42,273 pledged members across eighty-two towns in 1844, of whom 518 were reformed drunkards. One and two-tenths per cent. A society composed overwhelmingly of people without the problem will not, over time, keep working on the problem.

**Singleness of purpose.** He identified the moral-suasion split as the thing that stranded the Washingtonians inside the temperance movement. AA, he noted, refuses to endorse or oppose any cause, and will not take a position on temperance itself. That refusal avoids the greatest handicap its predecessor had.

**A clear programme.** The Washingtonians, he wrote, understood nothing about alcoholism beyond the hope of recovery through love and sympathy. They had no programme for changing a person. And they had no way to state what they were doing, so that a new group could copy it. Work with other alcoholics was not required, and its therapeutic value was not explicitly recognised. They had discovered the mechanism and never wrote it down, so it could not be transmitted, and it decayed.

**Anonymity.** Here is the sentence this book exists to formalise. A comparison with the Washingtonian experience, Maxwell wrote, underscores *the sheer survival value* of the principle of anonymity in Alcoholics Anonymous.

He gave three reasons. It protects the fellowship's reputation from public criticism of relapses, failures, internal tensions and deviant behaviour. It stops groups exploiting prominent names for prestige, and stops individuals exploiting their AA connection for personal fame, which encourages the placing of principles above personalities. And it has direct therapeutic value. It makes AA easier to approach, it relaxes the new member, and it encourages honest disclosure. It also hides fumbling and failure from the critical eyes of acquaintances, while a person tries out a new way of living.

**Hazard-avoiding traditions.** And then, the one that matters most for what follows. Maxwell singled out one tradition as perhaps as important as any other: *keeping authority in principles rather than letting it become vested in offices and personalities*. Two related ideas support it, he said. Leadership rotates, and leaders are trusted servants.

Read that again with Part Two in mind. Keeping authority out of persons. Rotation. Servant leadership. Anonymity. He listed the exact mechanisms, and he listed them together, as a functional group.

---

What Maxwell did not have was any way to say why those particular mechanisms, out of everything AA does, should be the ones that matter.

His argument is comparative and historical. Two movements, one dead and one alive, differing in these respects, and here is a plausible story about how each difference contributed. That is a good argument. It is the argument a careful sociologist could make in 1950 and it has held up for more than seventy-five years.

But it cannot distinguish a mechanism from a correlate. AA differs from the Washingtonians in dozens of ways, and Maxwell picked five. He picked well, I think, but the picking was judgment. Nothing in his method tells you whether anonymity is doing structural work or whether it merely accompanies something else that is. Nothing tells you what would happen to a group that kept anonymity and dropped rotation, or kept both and grew ten times larger.

And there is one thing his method could not have reached at all, because the result did not exist.

The mathematics describing when a group that decides by discussion can be relied upon to be right was published in 2010, sixty years after his paper. It says that such a group converges on the truth as it grows if and only if no single member retains a fixed share of the group's aggregate attention. It names the failure modes: prominent individuals who receive disproportionate attention, imbalance between attention given and received, and insufficient dispersion across the group.

Anonymity, rotation and servant leadership are three independent mechanisms for satisfying that condition. Maxwell grouped them correctly and called them hazard-avoiding. They are more specific than that. They are the conditions under which a group conscience is trustworthy at all.

---

There is a coda about Maxwell himself that belongs here, because this book has been strict elsewhere about who wrote what and why.

He was not a disinterested party. His doctoral dissertation, completed the previous year, was a study of Alcoholics Anonymous. His paper was written partly to reassure AA members, and it ends by doing so. In his judgment, based on systematic study, there was no inherent reason why AA should not last indefinitely. The proviso was that members kept reaching out to other alcoholics, kept practising the rest of the programme, and kept close to the traditions.

So the man who demolished AA's own account of Washingtonian history, and who repeatedly contradicted the movement literature where it had invented a tidy moral, was himself sympathetic to AA and writing partly for its comfort. Both things are true. His analysis is better than the institution's, and he was not neutral.

He also closed with a recommendation that nobody appears to have taken up. Careful objective research on the conditions determining AA's future, he wrote, would give the fellowship another asset the Washingtonians never had.

Seventy-five years later, that research still has not been done in any systematic way. What follows is not that research either. It is something more modest: an attempt to state Maxwell's central claim precisely enough that somebody could test it.

---

## The strongest objection, and what happened in 1944

There is an objection to everything Part One has argued, and it is good enough that the book should meet it here rather than hope nobody raises it.

The objection is that the comparison is confounded by timing.

The Washingtonians were absorbed by the temperance movement. They were absorbed because temperance was the dominant American reform cause of the 1840s, it was hungry for a revival after the shift to teetotalism thinned its ranks, and it had the money, the press and the platforms. There was something powerful standing by to absorb them.

Alcoholics Anonymous was founded in 1935, two years after the repeal of Prohibition, when temperance was not merely weaker but publicly discredited. On this account AA survived not because its Traditions protected it from capture but because nothing tried to capture it. The field was empty. Tradition 10, which keeps AA out of public controversy, would then be a scar rather than a shield, and the central comparison of Part One would be measuring an accident of chronology.

It is a serious objection. It also turns out to be testable, because something did try, and it happened in 1944.

---

In April of that year, an AA member named Marty Mann moved to New Haven and founded the National Committee for Education on Alcoholism. Its first offices were at Yale. Its sponsor was the Yale group around E. M. Jellinek, the same Jellinek whose one-line judgment about the Washingtonians' lack of a distinctive ideology Maxwell quoted six years later. Its message had three points: alcoholism is a disease and the alcoholic a sick person; the alcoholic can be helped and is worth helping; alcoholism is a public health problem and therefore a public responsibility.

Every one of those propositions was to AA's benefit. Mann was a member in good standing, the first woman to achieve long-term sobriety in the fellowship, and Bill Wilson was her sponsor.

And AA said yes.

The *Grapevine*, four months old, endorsed the new committee enthusiastically. Wilson wrote a piece in October 1944 explaining and supporting the arrangement. Jellinek had come to them, he reported. Yale was sponsoring a programme of public education entirely noncontroversial in character, and an AA member had been made its executive director. The names of both AA co-founders, Wilson and Smith, appeared on the committee's letterhead. Mann began speaking across the country under her own name, breaking her anonymity, as the organisation's public face.

Then the committee solicited funds, and at some point the solicitation went out to AA members.

That is the moment. Three years earlier the fellowship had accepted that money would spoil it. Now its founders' names sat on the letterhead of an organisation asking its members for money, with its own magazine's endorsement attached. The public could not tell where one organisation ended and the other began.

Wilson and Smith withdrew. Mann agreed to stop publicly identifying herself as an AA member. And the conclusion the founders drew, in the words of AA's own account, was that total non-affiliation was the only answer.

Twelve Points to Assure Our Future was published in the *Grapevine* in April 1946, eighteen months later.

---

So the timing objection fails, and it fails in a way that strengthens the argument rather than merely surviving it.

The claim that nothing tried to capture AA is false. Something did, and it was structurally identical to what happened to the Washingtonians. In both cases a fellowship of recovered drinkers proved to be extraordinarily good evidence for a larger cause. In both cases the larger cause was the dominant reform movement of its day, staffed by serious people with real institutional resources, who admired the fellowship and wanted to use it. In both cases the fellowship's own most prominent members found the larger cause more interesting than the parish work, and drifted toward it. Hawkins and Gough moved toward general temperance advocacy. Mann moved toward public health education.

The difference is not that AA faced no threat. The difference is that AA had eleven years of accumulated wreckage to read, wrote the rules down eighteen months after the incident, and then held to them.

And the fellowship kept holding. In 1954 Yale offered Bill Wilson an honorary doctorate. He wanted it; he had never graduated from college. A trustee mentioned that Theodore Roosevelt had refused personal honours, and Wilson declined. He wrote to an old friend that turning it down would act as a terrific restraint on big shots and power seekers in AA. He was declining for that reason, he said, and not because he was noble.

That is a man applying a rule against his own interest nine years after he wrote it, having watched what happened when he did not.

---

Three weaker objections deserve naming, since none of them is fully answered by the above.

**The disease concept and the medical alliance.** AA arrived alongside a scientific reframing of alcoholism that the Washingtonians never had, and benefited from it enormously. This is true and Part One does not dispute it. But note that the alliance was available precisely because of the Yale group, and note what nearly happened when AA got close to it.

**The referral stream.** Chapter Four already concedes that AA acquired an inflow channel the Washingtonians never had, and the model treats that channel as decisive for survival. A critic could reasonably say that treatment centres and courts, not the Traditions, are what keep AA alive. The honest answer is that both matter, and that the model ranks them. Losing referrals damages a group more than losing attraction does. On endpoint viability that held in 323 of 334 draws when every number was allowed to move by up to twelve and a half per cent, in 269 of 334 at twenty-five per cent, with a single reversal at each amplitude, and in 201 of 334 at fifty per cent, where 117 draws tie and sixteen reverse. It also held at 931 of the 944 points at which each parameter was moved alone, which is the more demanding test. Single-tradition degradations, by contrast, mostly cannot be resolved at all. How much more, the model cannot say with any confidence. If anything this objection deserves more weight than the book currently gives it.

**Survivorship bias.** We are examining the one mutual-aid movement that lasted and reasoning backward from its features, which is exactly the procedure that produces spurious explanations. The defence is not that Part One escapes this. It is that Part Two does not depend on it: the argument there is that three Traditions satisfy a criterion provable in advance, not that they correlate with survival after the fact.

---

## The Machinery

### 1. What the model says

This chapter is about the limits of comparative history, so the relevant model result is one about limits.

Maxwell listed five differences between AA and the Washingtonians and argued each contributed. The natural next question is: which mattered most? The simulation can ask that question directly, by degrading one Tradition at a time and measuring what happens to the group over thirty years.

It can answer it partly, and the size of the sample decides how much.

At four hundred paired replications under common random numbers, seven of the twelve single-Tradition comparisons have intervals excluding zero and five do not. Mixed Tradition 3 adherence is largest, costing 2.99 members against a reference group of 13.10, followed by mixed Tradition 11 at 1.88 and unity at 1.65. Anonymity, singleness of purpose, autonomy and self-support also resolve. Group conscience, no endorsement, non-professionalism, no organisation and no outside opinion are unresolved. The T3 and T11 rows each move both of that Tradition's executable paths, so they are not path-specific effects.

**This paragraph read the opposite way until 2 August 2026 and the reason is worth more than the result.** At thirty replications only two comparisons cleared significance, six were indistinguishable from nothing, and the two that cleared were the protective Traditions rather than the enabling ones. I drew a methodological moral from that: if a simulation with no measurement error cannot rank these mechanisms, then comparative history certainly cannot. The moral was sound and the premise was a small sample. At four hundred replications the ranking resolves, and it resolves the other way up.

So the honest version of the methodological point is narrower and less comfortable. The instrument was not blunt; I was reading it at thirty replications and reporting what a blunt instrument would have shown. That is precisely the error Chapter Twenty-Three catalogues three other instances of, and it survived here longer than any of them because the result it produced was a modest one and modest results do not invite checking.

What remains true, and it is the part that bears on Maxwell, is that a comparative study of two historical movements has no replications at all. It has one of each. Whatever this model can or cannot resolve at four hundred runs, the historical method cannot resolve any of it, and that asymmetry is the chapter's actual subject.

What the model does establish is narrower and I think more useful. It shows that the mechanisms Maxwell grouped as hazard-avoiding have explicit functions in the authored model, and that loss of outside referrals produces the highest closure rate among the tested decline paths. Conditional practice can mask that decline, though room-size loss is visible. Those are claims that can be checked against real groups. What the comparison no longer supports is the suggestion that the guard Traditions dominate the ranking.

### 2. The technical version

Common random numbers means running every configuration on the identical sequence of random seeds, so that differences between configurations are not contaminated by differences in the random draws. At four hundred replications the cross-seed standard deviation of final membership at the reference adherence level is 5.67 members, and the paired standard error under CRN runs from 0.22 to 0.33 members depending on the comparison. The pairing improves precision, but it does not reduce the replication count.

The full table is in Chapter Five's Machinery and is asserted in `model/book-calculations.ipynb`, computed by `model/tradition_paired.py`. Seven comparisons have |t| above 2.5, from 9.1 down to 2.8; five are unresolved.

Final membership at a twenty-year horizon remains a high-variance quantity in a model with stochastic arrivals, stochastic dropout and individual heterogeneity in growth capability. The earlier version of this section concluded from thirty replications that the model was a poor instrument for ranking similar effects. **That conclusion was drawn from the sample size rather than from the model.** At four hundred replications the instrument resolves seven of twelve. The unresolved set crosses the enabling/protective distinction, so the results do not support the earlier claim that only protective mechanisms remain uncertain.

One methodological note that generalises beyond this project. An earlier version of this analysis, run without common random numbers, produced an apparent complete ranking of all twelve Traditions. It was noise. The ranking was stable enough across a handful of seeds to look real, and it disappeared entirely when the variance was properly measured. That is the kind of error that is invisible unless you go looking for it, and the only defence is to measure the noise floor before reporting any comparison.

### 3. Notes on sources

**This chapter rests almost entirely on a document I have read in full**, which makes it the best-sourced chapter in Part One after Chapters One and Two. Every claim about what Maxwell argued comes from the paper itself.

**Quotation practice.** I have quoted Maxwell's phrase *sheer survival value* directly because the exact wording is the point. Elsewhere I have paraphrased his argument closely and identified it as his.

**What Maxwell cites that I have not read.** The 1947 *A.A. Tradition* booklet, on which his account of AA's traditions depends, and his own 1949 doctoral dissertation, *Social Factors in the Alcoholics Anonymous Program*, University of Texas. The dissertation would be worth obtaining: it is the systematic study he refers to when he offers his judgment about AA's prospects.

**On the 1944 material.** The Marty Mann episode is reported here from secondary accounts and from Wilson's own October 1944 *Grapevine* article as quoted in AA-affiliated archives. I have not read the article at source, nor AA's own account in *Pass It On*, which is the origin of the letterhead and withdrawal details. The founding date of the NCEA, its Yale sponsorship, its offices opening on 2 October 1944, Mann's role, and the three-point message are attested independently, including in National Institutes of Health historical material. The specific sequence of endorsement, letterhead, solicitation and withdrawal comes from AA sources and should be verified against Kurtz and against Mann's own biography before Part One is final. The 1954 Yale degree refusal and Wilson's letter about big shots and power seekers are widely reported but likewise reach me second-hand.

**The seventy-five year problem.** Maxwell's paper is old, and the field has moved. I do not currently know whether later scholarship has revised his account of the Washingtonian decline, and Part One should not be considered finished until that is checked. The places to look are the Alcohol and Drugs History Society, the *Points* research community, and the work of historians including Ian Tyrrell and Leonard Blumberg.

### 4. References

**Read in full:**

Maxwell, M. A. (1950). "The Washingtonian Movement." *Quarterly Journal of Studies on Alcohol* 11: 410-452. The entire chapter. Specifically: the introduction stating the paper's motivation; the seven-point similarity list; the five-point difference analysis covering exclusively alcoholic membership, singleness of purpose, programme content, anonymity and hazard-avoiding traditions; the three arguments for anonymity's value; the identification of authority in principles rather than offices, with rotating leadership; the Vermont membership figures; the concluding prognosis and the call for objective research.

Golub, B. and M. O. Jackson (2010). "Naive Learning in Social Networks and the Wisdom of Crowds." *American Economic Journal: Microeconomics* 2(1): 112-149. The 2010 result described at the end of the chapter and proved in Part Two.

**Cited at a remove:**

Wilson, W. (October 1944). Untitled *Grapevine* piece on the National Committee for Education on Alcoholism. Quoted in AA archival compilations.

Alcoholics Anonymous World Services (1984). *Pass It On*, p. 320. Source of the letterhead, the anonymity break, the solicitation to AA members, and the withdrawal of Wilson and Smith.

Brown, S. and D. R. Brown (2001). *A Biography of Mrs. Marty Mann: The First Lady of Alcoholics Anonymous.* Center City, Minn.: Hazelden. Identified but not obtained.

National Institute on Alcohol Abuse and Alcoholism historical material on the founding of the NCEA and the Yale Research Council. Independent corroboration of the institutional setting.

**What was not read:**

Maxwell, M. A. (1949). *Social Factors in the Alcoholics Anonymous Program.* Doctoral dissertation, University of Texas.

*A.A. Tradition* (1947). New York: Works Publishing.


\clearpage
\thispagestyle{empty}
\vspace*{0.32\textheight}
\begin{center}
{\Large\bfseries Part Two}\\[0.6em]
{\large\itshape The Condition}
\end{center}
\clearpage

# Chapter Seven: How a Room Decides

An AA group has no boss.

That is not a figure of speech or an aspiration. There is no president with a casting vote, no board that can overrule the meeting, no headquarters that can send instructions, and no appeal to anybody above. The Traditions say the group conscience is the final authority and that leaders are trusted servants who do not govern, and the fellowship means it literally enough that a group can decide almost anything about its own affairs and nobody, anywhere, can tell it otherwise.

Which raises a question that ought to be asked more often than it is. **How does a room like that ever decide anything?**

Organisations without authority are supposed to deadlock. That is most of what political theory is about. Put thirty people in a basement with a genuine disagreement, no chairman who can end debate, no vote that settles it, and no higher power to appeal to, and the obvious prediction is that they argue until somebody leaves.

They mostly do not. Groups settle things every month, all over the world, in a process that looks from the outside like nothing much: people talk, other people talk, somebody says something that lands, and after a while there is a sense in the room, and the sense becomes the decision. Nobody calls a vote in the ordinary sense. What is being sought is not a majority but something closer to substantial agreement, and the remarkable thing is that they usually get there.

This chapter is about what is actually happening while that occurs, because it turns out to be a specific process with specific properties, and once you can see it clearly you can ask when it works and when it does not.

---

Start small. Five people, one question, and some way of measuring the answer. Say the group has to decide how much of its money to keep in reserve, and the views range from nine months of expenses down to two.

Ann arrives thinking nine. Ben thinks two. Cara thinks six, Dan four, Eve seven.

Now they talk. Nobody is trying to win. Everybody listens to everybody, and everybody adjusts a bit, and how much each person adjusts depends on whose judgment they have come to trust. Ann respects Cara's caution about money and moves toward her. Ben has been coming three months and moves toward almost anyone. Cara listens too, but less, because she has thought about this before.

Run that for one round of conversation and the spread has already collapsed. Ann has come down from nine to six. Ben has come up from two to five and a quarter. The others have converged toward the middle. After a second round they are within a tenth of each other, and by the third round they have all arrived at the same number, and it is 5.74.

Nobody proposed 5.74. Nobody argued for it. It is not anyone's original view and it is not a compromise anybody negotiated. It is where the room goes when people who trust each other unequally keep adjusting toward each other.

That process is the group conscience, described mechanically. It has a name in the mathematics, after the statistician Morris DeGroot, who wrote it down in 1974: everyone holds a view, everyone updates toward a weighted average of the views around them, repeat until nothing moves.

I am not claiming this is a complete account of what happens in a meeting. It plainly is not. But it captures the one feature that matters here, which is that a room settling on a shared view is a process of repeated mutual adjustment, and processes like that have properties you can work out in advance.

---

Here is the first property, and it is the one that answers the question this chapter opened with.

**The room settles fast.** Three rounds, in the example above, from a spread of seven points down to agreement. Not because anybody surrendered, but because mutual adjustment converges, and it converges quickly once everybody is at least somewhat connected to everybody else.

That is why a group with no authority does not deadlock. Authority is one way to end a discussion. Mutual adjustment is another, and it is a great deal more reliable than political theory would predict, provided one condition holds.

The condition is that the room is not actually two rooms.

Take the same five people and split them: two who listen only to each other, three who listen only to each other, no attention crossing between them. Run the same process and it does not converge at all. Each faction settles internally, one camp at nine and the other at one, and there they sit forever. More discussion does not help, because no information passes between the halves. Each side is talking, adjusting, reaching agreement, and doing all of it inside a sealed compartment.

That is a schism in slow motion, and it is worth noticing that the mathematics sees it coming before anybody in the room does. Both factions are having what feels like a productive conversation. Both are converging. What has failed is not any individual's willingness to listen; it is the connectivity of the whole.

---

Now the second property, which is where this chapter earns its place.

The room landed on 5.74. But the plain average of the five starting views is 5.6.

That gap is small and it is not an accident. The room did not land on the average of what people thought. It landed on a *weighted* average, and the weights are not equal.

Cara's view carried about a third of the outcome. Ann's carried a fifth. Dan and Eve carried about a seventh each, which is less than half of Cara's. Nobody decided this. Nobody would have said, going in, that Cara's opinion counted twice as much as Eve's. But that is what the room did, and if you asked afterwards, everyone would have described it as a group decision arrived at together, which it also was.

Call that fraction a person's **influence weight**: the share of the final answer traceable to their starting view. The weights always add up to one, because the group ends up somewhere, and everybody's contribution to that somewhere has to sum to the whole of it.

Here is what makes influence worth a name of its own. **It is not the same as talking, and it is not the same as listening.**

Look at who did what in that room. Dan and Eve were the most open-minded people present; they placed the most weight on other people's views and the least on their own. They also had the least influence, by a distance. Cara was the least movable, and she had by far the most.

Influence is not about how much you speak, or how hard you try, or how much you care. It is entirely about how much weight *other people* place on you. It is conferred, not taken. Which means the person with the most influence in a room is often not the person who appears to be running it, and is sometimes not aware of it at all. He is the man who says one sentence near the end and watches everybody nod.

---

So a group conscience is a specific thing: a room of people adjusting toward each other, converging quickly provided they are all connected, and landing on a weighted average of where they started, with weights nobody chose and few could name.

Which raises the obvious question, and it is the question the whole of this book turns on.

**When can you trust the answer?**

Not whether it is arrived at honestly. Assume it is. The question is whether this process, run by sincere people, actually finds the right answer, or whether it just produces agreement, which is a different thing and much easier to obtain.

You already have most of what you need to see why it might not. The room lands on a weighted average. If the weights are even, that is a blend of many people's judgment. If one person holds a third of the weight, it is mostly that person's judgment wearing a group's clothes, and the group would have no way of telling the difference from the inside, because the conversation looks identical either way.

There is an exact answer to when it can be trusted, and it was proved in 2010. That is the next chapter.

---

## The Machinery

### 1. What the model says

The process described in this chapter is DeGroot updating, and it is the foundation for everything in Part Two. Three properties do the work.

**Convergence.** A room settles, and settles fast, provided attention flows through the whole group rather than pooling in sealed compartments. In the five-member example the spread collapses from seven points to under a tenth in two rounds and to identity in three. This is a general feature rather than a property of the example: mutual adjustment among connected agents converges geometrically.

**Weighted, not plain, averaging.** The settling point is the influence-weighted average of the starting views, not their arithmetic mean. In the example the room lands on 5.74 while the plain average is 5.60. The gap is small here because the weights are only moderately uneven. It grows with the unevenness, and Chapters Eight and Nine are about what happens when it grows a lot.

**Influence is conferred.** A member's influence weight is determined by how much others weight them, not by how much they speak or how much they weight others. In the example the two members who placed the most weight on others, 0.80 each, ended with the two smallest influence weights, 0.147 and 0.138. The member who placed the least weight on others, 0.65, ended with the largest at 0.333. Open-mindedness and influence are close to inversely related, which is worth knowing before deciding that a group's most receptive member is also its most important one.

### 2. The technical version

Let A be a row-stochastic N by N matrix, where A(i,j) is the weight member i places on member j's view. Beliefs update by

> b(t+1) = A b(t)

If A is strongly connected, meaning attention flows from every member to every other by some path, and aperiodic, then b(t) converges to a consensus in which every member holds the same value, and that value is

> the influence-weighted average of the starting beliefs

where the influence vector s is the normalised left dominant eigenvector of A, and the s(j) sum to one.

The worked example uses this matrix, rows in the order Ann, Ben, Cara, Dan, Eve:

| | Ann | Ben | Cara | Dan | Eve |
|---|---|---|---|---|---|
| Ann | 0.30 | 0.20 | 0.30 | 0.10 | 0.10 |
| Ben | 0.15 | 0.25 | 0.35 | 0.15 | 0.10 |
| Cara | 0.20 | 0.15 | 0.35 | 0.15 | 0.15 |
| Dan | 0.15 | 0.15 | 0.35 | 0.20 | 0.15 |
| Eve | 0.20 | 0.15 | 0.30 | 0.15 | 0.20 |

Starting beliefs 9, 2, 6, 4, 7. Successive rounds give 6.00, 5.25, 5.85, 5.60, 5.90; then 5.75, 5.69, 5.76, 5.74, 5.76; then agreement at 5.74 to two decimal places.

Influence weights: Ann 0.204, Ben 0.178, Cara 0.333, Dan 0.147, Eve 0.138. The weighted average of the starting beliefs under these weights is 5.74, matching the simulated settling point exactly, which is the check that the eigenvector calculation and the iteration agree.

The split-room example uses a block-diagonal matrix with no cross-block attention. It has two dominant eigenvalues rather than one, the chain is not strongly connected, and the iteration converges to two distinct values, 9 and 1, rather than to a consensus.

### 3. Notes on sources

**Nothing in this chapter is reported at a remove.** DeGroot's paper is read at source. The examples are constructed and the arithmetic computed rather than cited.

**The five-member example is invented**, not observed. It is chosen to make three points visible at once: fast convergence, the gap between weighted and plain averaging, and the inverse relation between open-mindedness and influence. A different matrix would give different numbers. What does not depend on the choice is the structure: convergence to a weighted average, with weights given by how others attend to you.

**DeGroot averaging is a simplification of a group conscience and I want to be plain about how large a one.** Real members argue rather than average. They defer on some questions and not others, change how much they trust someone mid-discussion, abstain, arrive late, and occasionally harden rather than converge. Some rooms have a member whose contribution is to say the thing nobody wants to say, which is not weighted averaging at all. The model captures a room converging toward a shared view and captures nothing of the texture of how.

**On the description of AA practice.** I have described the group conscience generically rather than quoting AA's own account of it, since that material is copyright. The characterisation of the fellowship as having no governing authority, with leaders as trusted servants, is a paraphrase of Tradition 2.

### 4. References

**Read in full:**

DeGroot, M. H. (1974). "Reaching a Consensus." *Journal of the American Statistical Association* 69(345): 118-121. The updating model, the convergence conditions, and the identification of the consensus with the influence-weighted average of initial beliefs.

Golub, B. and M. O. Jackson (2010). "Naive Learning in Social Networks and the Wisdom of Crowds." *American Economic Journal: Microeconomics* 2(1): 112-149. Referenced forward; the subject of Chapter Eight.

**Cited at a remove:**

Nothing.

**Referenced but not reproduced:**

The Twelve Traditions of Alcoholics Anonymous, paraphrased. The text is copyright Alcoholics Anonymous World Services, Inc. and is not reproduced here.

**Internal, and reproducible from this repository:**

The five-member worked example, its iteration to consensus, and its influence vector; the split-room counterexample. Code in the companion notebook.

**What was not read:**

Any empirical literature on how AA groups actually reach decisions. The chapter's account of a group conscience working by mutual adjustment is built from the DeGroot updating model and from the text of Tradition 2, not from any observation of a business meeting. I have not found a study of AA group decision-making of any kind, and if one exists this chapter should be checked against it before it is trusted.

# Chapter Eight: The Condition

Suppose a group has to decide something real.

The meeting has outgrown its room. There is a bigger hall available across town, cheaper, but on a bus route that runs badly after nine at night. Some members think the move is obvious. Some think it will kill the meeting for the people who need it most. Nobody has data. Everybody has a view, and each view is built out of something real: one person knows the bus schedule because she rides it, another has watched two meetings die after moving, a third has been coming eleven years and has a feel for what this particular room can absorb.

There is no vote in the ordinary sense, or if there is, it comes at the end of a long conversation that has already done the work. What happens instead is that people talk, and listen, and adjust. A man who came in certain leaves less certain. A woman who had not thought about the bus at all now thinks about it. Round and round until the room settles.

That is a group conscience, and the question this chapter answers is: **when can you trust the answer it produces?**

Not whether the people are sincere. Assume they are. Not whether they are wise. Assume ordinary. The question is structural. Given a room of well-meaning people who each know something and none of whom knows everything, under what conditions does talking until you agree actually land on the right answer?

It turns out there is an exact answer, and it is not the one most people would guess.

---

Start with one person. She has a view about the hall, and her view is partly right and partly wrong. That is not an insult; it is the condition of having a view. She has real information, the bus schedule, and she is also missing things, the eleven-year feel for the room. Call the wrongness her error.

The critical thing about her error is that it points in a particular direction. She overestimates the bus problem, say, because she rides that route on bad nights and it looms large. Somebody else underestimates it, because he drives. A third has never considered it.

Now put them in a room and let them average.

If the errors point in different directions, blending them cancels some of the wrongness. She was too pessimistic, he was too optimistic, and halfway between is closer to the truth than either. Add a fourth person and a fifth and the cancellation improves, because you are adding more independent directions of wrongness to be cancelled against.

This is the entire case for group decision-making, and it is a strong one. It does not require anybody to be clever. It requires only that people be wrong in different ways, and that the blending be even.

Here is the arithmetic, and it is worth having exactly, because the exactness is the point. If everybody's view counts equally, the group's expected error shrinks in proportion to one over the square root of the number of people.

Put numbers on that. Say a person deciding alone is typically off by ten. Four people, averaging evenly, are off by five. Twenty-five people are off by two. A hundred people are off by one, and it takes four hundred to get down to a half.

Notice the shape of it. To halve the error you have to quadruple the room. The returns are real and they are slow.

Not because anybody got smarter. Because errors cancel.

---

Now change one thing. Leave everything else alone: same people, same sincerity, same information, same conversation. But suppose that one member's view reliably accounts for a third of wherever the room lands.

He is not a tyrant. Nobody has appointed him. It is subtler than that and much more common: he has twenty-two years, he was here when the meeting started, he speaks last, and when he speaks the room settles. People genuinely change their minds when he talks, which is exactly what makes his weight real rather than nominal.

What happens to the cancellation?

A third of the group's answer is now his view, which means a third of his error is now permanently in the answer. It does not cancel against anybody, because it is not being averaged with the others. It is being *added* to whatever the others work out.

And here is the part that should stop you. **Adding more people does not fix it.** Double the meeting and the other members' errors cancel each other slightly better, but his third is still a third. Grow to five hundred and his third is still a third. The group gets larger and larger and its accuracy stops improving, because the same fixed slab of one man's wrongness sits in every answer the room produces.

The result, stated properly, is this. A group that decides by talking until it agrees converges on the truth as it grows **if and only if** the largest share held by any single member shrinks toward nothing as the group grows.

Nobody may keep a fixed piece of the answer.

That is the condition. It was proved in 2010 by two economists, Benjamin Golub and Matthew Jackson, who were studying how beliefs spread through social networks and were not thinking about Alcoholics Anonymous or about anything like it.

---

Take a room where everyone counts equally. At ten members the largest share anybody holds is a tenth. At fifty it is a fiftieth. At two hundred and fifty it is four thousandths, and at five hundred it is two thousandths. The largest voice in the room gets quieter and quieter, relative to the room, simply because the room is bigger.

Now take the same room with one member holding thirty-five per cent. At ten members his share is 0.35. At fifty it is 0.35. At two hundred and fifty it is 0.35, and at five hundred it is 0.35.

One of those falls by a factor of fifty. The other does not move at all.

That is the condition being met, and not being met.

And here is what it costs. One person deciding alone is off by about 0.80, so any group beats going it alone. The question is by how much, and whether the advantage keeps growing.

At ten members the two rooms are almost indistinguishable: 0.25 for the flat room against 0.33 for the dominated one. That near-identity is worth dwelling on. **A small group cannot detect this problem by looking at itself.** Everything feels fine, and everything largely is fine, because with ten people even a dominant member is not far from an equal share.

Then the paths separate. By fifty members the flat room has halved its error to 0.11 while the dominated room sits at 0.29. By five hundred the flat room is down to 0.04, seven times better than where it started. The dominated room has crawled to 0.28, an improvement of about fifteen per cent, and there it stops. Permanently. At a level roughly eight times worse than the room beside it.

The full figures are in the Machinery.

Both rooms reached agreement every time. Neither had an argument it could not resolve. On any given evening, from a chair in the room, they behave identically.

One of them is getting better at deciding things. The other stopped years ago and has no way of knowing.

---

The instinct most people have about group decisions is that they are safer than individual ones because more heads are better. That instinct is right, but it is right for a specific reason, and the reason has a condition attached that the instinct does not include.

More heads are better *because errors cancel*. If the errors do not cancel, more heads are not better, and the extra heads can even hurt, because they lend the appearance of collective judgment to what is functionally one person's opinion.

That last part is the trap, and it deserves stating plainly. A group with a dominant member does not look like one person deciding. It looks like a group deciding. There is discussion. There is genuine disagreement, aired. There is a sense of the room, arrived at collectively. People leave feeling they participated, and they did participate. It is just that the participation did not do the thing participation is supposed to do.

The failure is invisible from inside precisely because the visible parts of the process are all working.

---

Now put the condition beside AA's Traditions.

The condition says: no member may hold a fixed share of the group's judgment, and the share must shrink as the group grows.

**Tradition 2** puts final authority in the group conscience and casts anyone holding a position as a servant of it rather than a director of it. Formally, that means office confers no weight. Being the secretary or the treasurer or the general service representative does not make your view count for more when the room is deciding something. The role is administrative, not epistemic.

**Tradition 9** says the fellowship is never to be organised into a hierarchy, and that service positions rotate. This attacks the same problem from a different direction: even if weight starts to gather somewhere, it does not get to stay there. The person who chaired last year does not chair this year. Nothing accumulates.

**Tradition 12** says anonymity is the spiritual foundation of all the Traditions, and that principles come before personalities. This is the strangest of the three and the most interesting. It does not regulate weight at all. It removes the raw material weight is built out of.

Think about what unequal influence actually attaches to in an ordinary room. It attaches to surnames, to jobs, to money, to titles, to reputation earned somewhere else. The surgeon's view weighs more than the janitor's, not because anyone decided it should, but because everyone knows which is which. Strip out the surnames and the occupations and the outside status, and the substrate that unequal weighting grows on is simply not present.

Three rules. Three different mechanisms. One condition.

The first says office does not buy weight. The second says weight cannot accumulate over time. The third says the things weight would attach to are not visible in the first place. Belt, braces, and no trousers.

---

That is the argument, and the fellowship's own book says something that damages it.

In 1953 AA published *Twelve Steps and Twelve Traditions*, a chapter of commentary on each of the twenty-four rules, written by Bill Wilson. It is the closest thing the fellowship has to an authoritative statement of what the Traditions mean. Until late in the writing of this book I had not read it, on the grounds that it is copyright and the project does not acquire what it cannot hold. That was a bad reason and it cost me something, because the chapter on Tradition 2 contains both the strongest support for the argument above and the strongest objection to it, and I would rather have found the objection myself.

The support first, since it is easy to state. Wilson's chapter ends the story of a group's first election with a sentence that is this book's thesis in his words: the group conscience, well advised by its elders, will in the long run be wiser than any single leader. He arrives at it the way he arrives at everything, by telling what happened. A hospital owner offers him a salaried job as a lay therapist. It is ethical, he needs the money badly, and on the train home he receives what he takes to be divine guidance telling him to accept. He puts it to the group that evening and they tell him no. He obeys. The most influential man in the fellowship is overruled by a room, records that the room was right, and prints the story as the reason the rule exists.

Now the objection.

Two pages earlier, the same chapter explains what becomes of a founder after the election that removes him. Some sour into what Wilson calls bleeding deacons. The rest mature into elder statesmen, and of those he says: they become the real and permanent leadership of AA, they are the voice of the group conscience, and when a group is sorely perplexed it inevitably turns to them for advice.

Read that against the condition. Permanent. A fixed set of people whose judgment the group returns to whenever a question is hard. They hold no office, so there is nothing for them to rotate out of, and the passage is not a warning. It is the chapter's account of how a healthy group is supposed to work.

That is a concentration of influence that does not shrink as the group grows, which is the one thing the condition forbids.

---

It is worth pricing rather than conceding, because how much it costs turns out to matter more than whether it exists.

Put three such people in a room and give them, between them, a tenth of the attention in every member's row. That is a modest assumption, well short of the dominant old-timer at thirty-five per cent, and it describes something most people who have sat in a long-running meeting will recognise.

At ten members this arrangement is invisible. The group's error is 0.255 against 0.252 for a room where everyone counts equally, a penalty of about one per cent, which no one could detect from a chair. At fifty it is 0.121 against 0.113. At two hundred and fifty, 0.068 against 0.051. At a thousand, 0.053 against 0.025, and the group is now twice as inaccurate as it could be.

The three elders' largest share settles at 0.034 and stops moving, against a flat benchmark of 0.001 at that size. The predicted floor is a tenth divided by three, which is 0.033. The computation lands on it.

So the elder statesmen are an obstruction in the exact technical sense, and the damage follows the same curve as everything else in this part of the book: nothing at all while the group is small, and unbounded relative cost as it grows.

---

There is a second and worse consequence, which Chapter Ten takes up properly.

The same chapter of the Twelve and Twelve that describes the elder statesmen also describes the committee, and it is blunt about how little the committee matters. Its members are sharply limited in authority. In no sense whatever can they govern or direct the group. They are servants, not senators, and their work is looking after the chores.

So the fellowship rotates its offices faithfully, and the offices it rotates are the ones its own commentary says carry no weight, while the people the commentary says carry the weight hold no office and rotate out of nothing. If that is right, then rotation is aimed at the wrong target, and widening the rotation, which is Chapter Ten's prescription, cannot help. A pool is only a remedy for a concentration that is inside the pool.

The arithmetic agrees, and it is not close. Take a group following Chapter Ten's recommendation exactly, rotating a quarter of its members through service, and give it three elder statesmen at a tenth. At fifty members its largest share is two and a half times the flat benchmark. At two hundred and fifty it is nine times. At a thousand it is thirty-four times, and climbing, in a group doing the recommended thing correctly.

---

I do not think this sinks the argument, and I want to say precisely why not, because the temptation to rescue one's own thesis is strongest exactly here.

The condition is a claim about what a rule does, not a claim that the fellowship obeys it. Traditions 2, 9 and 12 satisfy the criterion; a group that also maintains a permanent advisory class does not, and both of those can be true at once, because AA's practice is not identical to AA's rules. That is not a dodge. It is the difference the whole book turns on, and Part Six is about how easily the two get confused.

What the passage does establish is that the failure this book describes is not hypothetical and not rare. It is described approvingly in the fellowship's own literature, which means any group following that literature faithfully will build one. A reader who wanted to argue that the Traditions are self-defeating in practice now has the better evidence for it, and it came from the movement rather than from me.

The honest summary is that AA wrote down three rules that satisfy the condition and one paragraph of commentary that undoes a good deal of their effect, and did not notice, because there was no reason to expect anyone would ever put the two beside a theorem.

---

I want to be careful here, because this is the centre of the book and it would be easy to say more than the evidence carries.

**The claim is that these three Traditions satisfy a mathematical condition for reliable group deliberation.** That is not an interpretation or an analogy. The condition is precisely stated, the Traditions map onto it precisely, and the mapping can be checked by anyone.

**The claim is not that Bill Wilson anticipated a theorem.** He plainly did not. He wrote the Traditions in 1946 out of eleven years of correspondence, as Chapter Five describes: complaints in, patterns noticed, the practice of the groups that lasted written down. The Traditions are a record of failure modes, not a derivation.

**The claim is not that this is why AA has lasted.** A correspondence is not a cause. Showing that a rule satisfies a criterion does not show that satisfying the criterion is what kept the institution alive, and Part Six of this book is largely about the difference.

What the correspondence does establish is narrower and, I think, more interesting than a causal claim would be. It says the Traditions are not arbitrary. They are not merely good manners, or humility for its own sake, or the cultural residue of 1940s American Protestantism. Three of them, at least, are doing identifiable structural work, and we can now say exactly what work.

A fellowship of drunks arrived at the answer by watching groups fall apart. It took economists sixty-four more years to prove it.

---

## The Machinery

### 1. What the model says

The result in this chapter is not mine and it is not simulated. It is a theorem, published in the *American Economic Journal: Microeconomics* in 2010, and everything in the main text follows from it directly.

What my own model contributes is the tables. The theorem tells you that maximum influence must vanish; it does not tell you how fast concentration hurts in a group of any particular size, or how the damage compares between a single dominant member and a small clique. Those are computed from constructed trust matrices, and the computation is simple enough to be checkable by hand for small groups.

The one substantive thing the model adds to the theorem is the small-group observation: at ten members, all four governance arrangements produce similar accuracy. That has a practical implication the theorem does not state. **A group cannot audit its own governance by introspection while it is small, because while it is small the governance barely matters.** By the time the difference is visible in outcomes, the structure that produced it has been in place for years.

### 2. The technical version

Let A be an N by N row-stochastic matrix, where A(i,j) is the weight member i places on member j's view. Beliefs update by repeated averaging:

> b(t+1) = A b(t)

If A is strongly connected and aperiodic, then b(t) converges to a consensus the influence-weighted average of the starting beliefs, where s is the normalised left dominant eigenvector of A, called the influence vector. Member j's influence weight is s(j), and the sum of s(j) = 1.

Computed values, with sigma = 1 throughout:

| N | max influence, flat | max influence, dominant | error, flat | error, dominant |
|---|---|---|---|---|
| 10 | 0.100 | 0.350 | 0.252 | 0.328 |
| 50 | 0.020 | 0.350 | 0.113 | 0.289 |
| 250 | 0.004 | 0.350 | 0.050 | 0.281 |
| 500 | 0.002 | 0.350 | 0.036 | 0.280 |

**Golub and Jackson (2010).** Suppose member *j*'s initial belief is

> b(j) = mu + e(j)

where mu is the truth and the errors e(j) are independent with mean zero and variance sigma squared. Then the consensus converges in probability to mu as N grows **if and only if** the largest s(j) goes to zero.

The error is available in closed form, which is how the second table was computed. The consensus is the influence-weighted average of the starting beliefs, which is

> consensus = mu + sum over j of s(j) e(j)

and that weighted sum of errors is normally distributed with mean zero and standard deviation sigma times ||s||, the Euclidean length of the influence vector. For a normal variable with mean zero, the expected absolute value is its standard deviation times sqrt(2/pi). So

> E | consensus - mu | = sigma * ||s|| * sqrt(2/pi)

Under equal weighting s(j) = 1/N for all j, so the length of s is one over root N and the error is exactly sigma * sqrt(2/pi) / sqrt(N). That is the one-over-root-N result in the main text, and it is exact rather than approximate.

The single-person baseline quoted in the text is the same expression at N = 1: sigma * sqrt(2/pi) = 0.798 for sigma = 1. So the tables and the baseline are the same formula evaluated at different points, which is why the comparison is meaningful rather than a change of units.

Under a dominant member holding share alpha with the remainder split evenly, the squared length of s is alpha^2 + (1-alpha)^2/(N-1), which converges to alpha squared rather than to zero. The error therefore approaches sigma * alpha * sqrt(2/pi) and stays there. With alpha = 0.35 and sigma = 1 that limit is 0.279, which is what the table shows at N = 500.

Golub and Jackson identify three obstructions to the vanishing condition: prominent agents receiving non-vanishing attention from the whole society; imbalance, where some parties receive far more attention than they give; and insufficient dispersion, where subgroups do not attend to the wider society. The three map respectively onto the dominant old-timer, the member whose sponsorship lineage listens to him but who listens to nobody, and the clique.

**That mapping was stated here for some time without being computed, and computing it changed it.** The three obstructions are properties of *sequences* of societies as they grow, not properties of a room. Take the clique and the imbalanced member at fixed magnitude and neither obstructs anything. Take a clique of three that gives a tenth of its attention outward. Between them the three hold 0.750 of the influence in a group of ten. In a group of fifty it is 0.375, in a group of two hundred and fifty 0.107, and in a group of a thousand 0.029. A member who receives twenty times the attention he gives holds 0.690 in a group of ten and 0.020 in a group of a thousand. Both shares vanish, so both satisfy the condition and neither is an obstruction at all.

Now let the same two practices grow with the group. A clique whose inwardness approaches one as the group expands holds 0.167 of the influence at every size tested from ten to a thousand. A member whose attention advantage grows in proportion to the group runs from 0.182 at ten to 0.168 at a thousand, converging to a positive share rather than settling on one exactly. Neither is falling toward zero, and that is the whole of what makes them obstructions.

So what makes a practice dangerous is not its severity but whether it scales. A fellowship with one very prominent member in every room of thirty is in a different position from a fellowship with one very prominent member however large the room gets, and the difference is not a matter of degree. It is the difference between a share that vanishes and a share that does not.

That is the same finding this book reaches from another direction when it comes to rotation, and it is worth carrying forward as the general form of the argument: the question a group should ask about any concentration of attention is not how large it is but whether it would still be there if the group doubled.

**The elder-statesman structure, added 10 August 2026.** A non-rotating class of *e* members holds share alpha of every row between them; the rest of the group attends flat. This is not the dominant-member family with a different label, because the share is held collectively and because nothing rotates: there is no office and therefore no cycle to average over. Maximum influence converges to alpha over *e*.

| N | max influence, 3 elders at 0.10 | flat benchmark | error, elders | error, flat |
|---|---|---|---|---|
| 10 | 0.1233 | 0.1000 | 0.2552 | 0.2523 |
| 50 | 0.0513 | 0.0200 | 0.1214 | 0.1128 |
| 250 | 0.0369 | 0.0040 | 0.0681 | 0.0505 |
| 1000 | 0.0342 | 0.0010 | 0.0525 | 0.0252 |

The predicted floor is 0.10 / 3 = 0.0333 and the computed value at N = 1000 is 0.0342, approaching it from above. The error ratio runs 1.01, 1.08, 1.35, 2.08 across those four sizes, which is the invisible-while-small pattern again and is why no group detects this by introspection.

**Whether Chapter Ten's prescription helps.** It does not, and this is the practically important row. Setting the rotation pool to twenty-six per cent of the group at every size, as Chapter Ten recommends, and giving the officeholder a deliberately small share because the source text says the committee cannot govern or direct:

| structure | N = 50 | N = 250 | N = 1000 |
|---|---|---|---|
| rotation only, pool at 26 per cent | 2.0 | 2.0 | 2.0 |
| plus 3 elders at 0.10 | 2.5 | 9.2 | 34.2 |
| plus 3 elders at 0.20 | 4.1 | 17.4 | 67.4 |
| plus 5 elders at 0.20 | 2.7 | 10.7 | 40.7 |

Entries are maximum influence as a multiple of the flat benchmark. The first row holding at exactly 2.0 is a self-consistency check rather than a finding, since twenty-six per cent was *defined* in Chapter Ten as the pool that comes within a factor of two. The rows below it are the finding: the prescription is necessary and nowhere near sufficient, and the gap it leaves grows with the group.

And on severity, one correction to what the table above suggests. The illustration uses a dominant member at 0.35, which is a lot, and a reader could take from it that only substantial dominance matters. It does not take much. A member holding five per cent of every row floors the consensus error at 0.0465 against a flat 0.0252 at a thousand members, which is a factor of 1.84, and that factor grows without bound as the group grows because the flat error keeps falling and the other does not. At ten per cent the factor is 3.3. The dose-response is in the appendix and it starts hurting almost immediately.

### 3. Notes on sources

**The theorem is read at source**, not reported. Golub and Jackson's paper is the origin of every formal claim in this chapter.

**The mapping to the Traditions is mine**, and it is an interpretation rather than a finding. Someone could reasonably argue that Tradition 2's "trusted servants" language is about humility rather than about weighting, or that anonymity is primarily protective of individuals and only incidentally structural. I think the structural reading is correct and I have argued for it, but a reader should know it is a reading.

**That objection is no longer hypothetical, and it has a name.** Richard Rohr's *Breathing Under Water* is a book-length devotional reading of the Steps that treats anonymity exactly as the protective reading has it: as confidentiality, as a discipline against gossip, as the principle that not everybody has a right to know everything. He asks in so many words whether that is part of why the word appears in AA's title. He is a serious reader arriving at a different answer, and the fair thing is to say so rather than to keep the objection abstract where it is easier to dismiss.

The two readings turn out not to compete, which I did not expect. The Twelve and Twelve's own chapter on Tradition 12 describes both functions and treats them as separate lessons learned at different times: first that a member's name and story had to be confidential, which is Rohr's reading, and later, after the fellowship's first taste of national publicity, that anonymity had to be absolute at press, radio, film and television so that no self-appointed member could present himself as a messiah representing AA. The second is the structural reading, and it is in the source text. What this chapter should not claim is that the structural function is the *only* one, or the original one. It is neither.

**Reading the Twelve and Twelve changed this chapter rather than confirming it**, which is worth recording because the reverse would have been suspicious. It supplied the thesis in Wilson's own words and, three pages away, the best objection anyone has raised to it.

**DeGroot averaging is a strong simplification of how a group conscience works.** Real members argue rather than average. They defer selectively, on some questions and not others. They abstain. They update out of order, and sometimes they harden rather than converge. The model captures a room settling toward a shared view and captures nothing about the texture of how that happens. Golub and Jackson's result is a statement about naive averaging specifically, and a group that deliberated some other way would need a different analysis.

**Nothing in this chapter is reported at a remove.** The theorem is read at source, the updating model is read at source, and the numbers are computed rather than cited. This is the only chapter so far with no outstanding acquisitions, which is a property of the material rather than a virtue of the research: the whole argument rests on one paper and some arithmetic.

**Exchangeability is an idealisation.** Proposition 1 in the underlying paper assumes trust weights are genuinely uniform under full adherence to the three Traditions. Real trust is never exactly uniform, even in a perfectly run group. The claim is asymptotic and approximate: the Traditions push maximum influence toward 1/N, not exactly to it.

### 4. References

**Read in full:**

Golub, B. and M. O. Jackson (2010). "Naive Learning in Social Networks and the Wisdom of Crowds." *American Economic Journal: Microeconomics* 2(1): 112-149. The wisdom criterion; the three obstructions; the convergence conditions.

DeGroot, M. H. (1974). "Reaching a Consensus." *Journal of the American Statistical Association* 69(345): 118-121. The updating model.

Alcoholics Anonymous World Services (1953). *Twelve Steps and Twelve Traditions*. Read in full 10 August 2026, from the per-chapter files AAWS publishes free at aa.org. The chapters on Traditions 2, 9 and 12, at printed pages 132 to 138, 174 to 178, and 187 to 191. Source of the group-conscience claim, the founding story of Tradition 2, the elder statesmen and bleeding deacons, the description of the committee as sharply limited, the warning against entrenched power, and the two functions of anonymity. Copyright AAWS; held as a record with no document, and paraphrased rather than quoted at length.

Rohr, R. (2011). *Breathing Under Water: Spirituality and the Twelve Steps*. Cincinnati: Franciscan Media. Read in full 10 August 2026. Cited only for its reading of anonymity as confidentiality, and for containing no discussion of the Traditions.

**Cited at a remove:**

Nothing.

**Referenced but not reproduced:**

The Twelve Traditions of Alcoholics Anonymous, paraphrased. The text is copyright Alcoholics Anonymous World Services, Inc. and is not reproduced here. The same applies to the 1953 commentary on them: the passages above are paraphrased or quoted in fragments short enough to identify the claim, and a reader who wants the argument in Wilson's words should read the chapters, which AAWS gives away.

**Internal, and reproducible from this repository:**

Influence weights and consensus errors for flat, rotating, dominant and clique regimes at N = 10, 50, 250 and 500. The elder-statesman family and the twenty-six-per-cent contrast, added 10 August 2026, in `model/part2_influence.py`, sections 5b and 5c, cached to `research/part2_influence.json` under the keys `elders` and `elders_vs_prescription`. Influence vectors computed as left dominant eigenvectors of constructed trust matrices; errors from the closed form above rather than by simulation. Code in the companion notebook.

**What was not read:**

Nothing in the mathematics is at a remove; the theorem was read at source. What has not been read is any work testing whether real deliberating groups behave like DeGroot updaters. Golub and Jackson prove a result about a model, this chapter applies it to a fellowship, and the step between the two is an assumption about how people in a room revise their views. That assumption is not tested here or anywhere else in the book.

Nor has anything been read on whether real groups in fact maintain an elder-statesman class, how large it is, or how much attention it attracts. The 1953 commentary says such people exist and are turned to; it does not count them, and neither has anyone else that I can find. The three-elders-at-a-tenth figure above is an illustration chosen to be modest, not an estimate, and Chapter Twenty-Four's proposed survey would be the way to replace it with one.

# Chapter Nine: Confident and Wrong

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

**Nothing in this chapter is reported at a remove.** The theorem is Golub and Jackson, read at source. The trust matrices are constructed and the figures computed rather than cited. The Gough material is from his own 1869 autobiography, read at source, and is treated at length in Chapter Three.

**The closed-core result is new to this project** in the sense that I had not computed it before writing this chapter. It is not new to the literature: it is a direct consequence of Golub and Jackson's imbalance condition, and the fact that a closed subgroup captures all influence in the limit is standard for absorbing states in Markov chains. What is worth reporting is the magnitude, which is much starker than the other two failure modes and which I would not have guessed.

**The extension from group deliberation to public reputation, in the Gough passage, is an analogy and not an application.** The theorem concerns members averaging beliefs about a shared question. What the outside world believed about the Washingtonians was not formed that way. I have flagged this in the text rather than relying on the reader to notice.

**The dependence index rests on a hand-written matrix.** It is a normalized
summary of the author's resource assignments and inherits their uncertainty.

### 4. References

**Read in full:**

Golub, B. and M. O. Jackson (2010). "Naive Learning in Social Networks and the Wisdom of Crowds." *American Economic Journal: Microeconomics* 2(1): 112-149. The three obstructions to the wisdom condition: prominent agents, insufficient dispersion, and imbalance.

Gough, J. B. (1869). *Autobiography and Personal Recollections of John B. Gough.* Springfield, Mass.: Bill, Nichols & Co. The September 1845 episode; treated in Chapter Three.

**Cited at a remove:**

Nothing.

**Referenced but not reproduced:**

The Twelve Traditions of Alcoholics Anonymous, paraphrased. The text is copyright Alcoholics Anonymous World Services, Inc. and is not reproduced here.

**Internal, and reproducible from this repository:**

Influence weights and consensus errors for four governance regimes at N = 10, 50, 250 and 500, with the analytic limits. Per-step group-dependence coefficients from the model module. Code in the companion notebook.

**What was not read:**

Any measurement of attention or influence inside a real mutual-aid group. The three regimes in this chapter are constructed matrices, not observed ones, and appendix A8 sets out what would have to be measured to know whether any of them resembles a meeting. Chapter Twenty-Four lists that measurement and admits it may not be obtainable ethically in an anonymous fellowship.

# Chapter Ten: Rotation Has to Be Wide

The Traditions say that service positions rotate. They do not say how many people should be in the rotation, and it turns out that this is the number that matters.

The instruction is more explicit than the short form of the Traditions suggests. The long form of Tradition 9 states in five words that rotating leadership is the best, and then describes the shape of it: the small group elects its secretary, the large group its rotating committee, the metropolitan area its intergroup committee. The 1953 commentary adds the reason, warning the fellowship away from the dangers of great wealth, prestige and entrenched power. Entrenched is the right word and it is theirs, not mine.

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

Before that number gets used, it has to survive an objection that would make it beside the point, and the objection comes from AA's own commentary on the Tradition.

Chapter Eight sets it out with the source and the arithmetic, so I will not repeat either. The short form is that AA's own 1953 commentary denies the premise this chapter starts from. It says the committee that rotates cannot govern or direct anything, and it puts the fellowship's real influence in a class of former officeholders it calls elder statesmen, who hold nothing and therefore rotate out of nothing.

The fellowship's fullest statement on service structure says something adjacent to this chapter's claim, and the gap between them is the point. The Twelve Concepts for World Service, adopted in 1962, are where AA sets out how its service bodies should be composed, and Concept 4 establishes what it calls the Right of Participation: voting representation in reasonable proportion to the responsibility each part of the structure discharges. So AA does hold a proportionality principle about service, explicitly and in its own words, and I had assumed it held none. But it proportions a different pair. Concept 4 proportions voting weight to responsibility discharged. This chapter's result concerns the size of the rotating pool relative to the size of the group being served. A structure could satisfy Concept 4 exactly, every body weighted precisely to what it is answerable for, and still rotate twelve people through a fellowship of eight hundred, which is the configuration the arithmetic above shows to be a permanent oligarchy. The claim I started with was that AA never says how many people. The claim I can defend after reading the Concepts is narrower and more interesting: AA has the instinct for proportion and applies it to representation rather than to the pool.

If that is accurate, this chapter has been measuring the wrong quantity. A pool is a remedy for influence held inside it.

So I priced the combination, and the result is in Chapter Eight's Machinery rather than here. What it comes to is this: a group that adopts the recommendation below in full, and also defers to a small permanent advisory class, diverges from an evenly weighted room anyway, and diverges faster the larger it gets. Following the advice correctly does not close the gap, because the advice does not reach what is opening it.

Two conclusions follow, and I would rather state both than the comfortable one.

The twenty-six per cent stands as far as it goes. A group that rotates a dozen people is worse off than a group that rotates a quarter of itself, and that comparison is unaffected by anything above. What does not stand is the implication a reader would reasonably draw, that a group meeting the proportion has dealt with the problem this book is about. It has dealt with one channel. The commentary describes another, larger one, running through people the rotation never touches.

And the practical advice has to change shape accordingly. Counting names on a service roster is still worth doing, and it is still the most checkable thing in this book. But a group that wanted to know whether it satisfies the condition would have to ask a second question, which no roster can answer: when something difficult comes up, how many different people does this room turn to, and is that number growing as the room does?

I do not know how to measure that without asking members, which is why Chapter Twenty-Four's survey now has a second thing to ask about.

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

**That paragraph stood for weeks before I read the source that answers it, and the answer is worse than the guess.** I supposed the weight would concentrate in a few of the rotating positions. AA's own commentary says the rotating positions carry no governing weight at all, and puts the influence with a class of people who hold no position. So the refinement I described would not have found the problem, because it varies the share across offices and the structure that matters has no office in it. The elder-statesman family in `model/part2_influence.py` section 5b is the construction that does reach it, and the twenty-six-per-cent contrast in section 5c is what it costs. Both are reported in Chapter Eight rather than duplicated here.

**The elder-statesman parameters are illustrative and are not estimates.** Three people at a tenth was chosen to be modest rather than fitted to anything, because there is nothing to fit it to: no one has counted how many people a group turns to on hard questions, or measured how much attention they get. The qualitative result does not depend on the choice, since alpha over *e* fails to vanish for any positive alpha, but every specific multiple quoted in Chapter Eight does depend on it and should be read as an illustration of a mechanism.

**The twenty-six per cent is a property of my parameter choices**, specifically alpha = 0.35 and the within-a-factor-of-two criterion. Both are judgement calls. What does not depend on them is the qualitative result, that a fixed pool floors while the benchmark falls, and that the required pool scales with the group rather than being a fixed headcount. Treat the proportion as an order of magnitude, not a threshold.

**On the historical claim.** The suggestion that this failure mode is absent from the Traditions because AA had few very large groups in 1946 is my inference, not something I have found stated anywhere. It is consistent with the account in Chapter Five of how the Traditions were compiled, but I have not verified it against the record of what groups actually wrote to New York about.

### 4. References

**Read in full:**

Golub, B. and M. O. Jackson (2010). "Naive Learning in Social Networks and the Wisdom of Crowds." *American Economic Journal: Microeconomics* 2(1): 112-149. The vanishing-influence criterion, and the requirement that maximum influence go to zero as the society grows, which is what a fixed rotation pool fails.

Alcoholics Anonymous World Services (1953). *Twelve Steps and Twelve Traditions*. Read in full 10 August 2026. The long form of Tradition 9, at printed page 177, for the statement that rotating leadership is best and for the secretary, committee and intergroup structure; the chapter on Tradition 9, at 174 to 178, for the warning against entrenched power; the chapter on Tradition 2, at 132 to 138, for the committee's limited authority and for the elder statesmen. Copyright AAWS; held as a record with no document.

W., Bill. *The Twelve Concepts for World Service* (Short Form), SMF-114. Adopted 1962. Read at
source on 17 August 2026 from the fellowship's own free posting and held as record only under
`research/incorporated/TwelveConcepts_1962/`. Used here for Concept 4, the Right of
Participation, and for Concept 9 on the passage of primary service leadership from the founders
to the trustees. The long-form Concepts and the essays accompanying them in the Service Manual
were not read; if a rule about the size of a rotating pool exists anywhere, the Concept 4 essay
is where it would be.

**Cited at a remove:**

Nothing.

**Referenced but not reproduced:**

The Twelve Traditions of Alcoholics Anonymous, paraphrased, and the 1953 commentary on them. Both are copyright Alcoholics Anonymous World Services, Inc. and neither is reproduced here beyond fragments short enough to identify the claim.

**Internal, and reproducible from this repository:**

The pool sweep at N = 400; the fixed-pool scaling series from N = 50 to 800; the required-pool calculation at each size. Code and assertions in `model/book-calculations.ipynb`, section 2. The elder-statesman family and the twenty-six-per-cent contrast quoted above are computed in `model/part2_influence.py`, sections 5b and 5c, and cached to `research/part2_influence.json`.

**What was not read:**

Anything about how AA groups in fact rotate service, and anything about how many people a group turns to on a hard question. The claim that rotation must scale with the group is derived from the theorem and from a constructed matrix; whether real groups rotate a fixed dozen or a fixed proportion is an empirical question I have not investigated and that Chapter Twenty-Four proposes as a survey. The elder-statesman question is the second thing that survey would have to ask, and it is harder, because a service roster records offices and nothing records deference.

Nothing further on the Concepts. They were read on 17 August 2026 and are now discussed above rather than listed here as a gap.

# Chapter Eleven: What the Washingtonians Lacked

Part One left a question standing. Six drunks in a Baltimore tavern built something that worked, reached a great many people with it, and were effectively gone within eight years. Ninety-five years later a nearly identical fellowship did not go. The obvious explanation, that AA had rules and the Washingtonians did not, is the right shape but too vague to be worth much. Rules against what?

Part Two has now supplied three specific answers, and applying them to 1840s Baltimore turns out to be more interesting than I expected, because the Washingtonians had one of the failure modes badly, and it was not the one everybody blames.

---

Start with the one everybody blames, since it is real.

The movement concentrated its public credibility in a small number of named men. John Hawkins, the hatter, was on the platform within months of signing and eventually gave upward of five thousand speeches. John Gough became the most famous reformed drunkard in America. When Gough disappeared for a week in September 1845 and was found in a house on Walker Street, the aggregate moved with him, and a thousand quiet recoveries in a thousand other towns could not average it out.

That is the prominent agent from Chapter Nine, and it does real damage. But notice what it does not explain. Gough relapsed in 1843 as well, and nothing happened, because in 1843 he was nobody. The prominent-agent problem is a consequence of how the movement had grown, not a cause of anything. Something had made a handful of men load-bearing. The question is what.

---

Here is the answer, and it is the failure mode from Chapter Nine that I found most surprising when I computed it.

Consider how a Washingtonian meeting actually worked in 1840 and 1841. Members stood up and described their own drinking. Everybody in the room could speak and most did. Attention flowed in every direction: the man testifying tonight listened to somebody else last week and will listen again next week. Whatever else you say about it, that is a structurally flat arrangement, and it is very close to what an AA meeting still looks like.

Now consider how the movement *grew*. It grew by sending speakers out. Pollard and Wright worked New York, New Jersey and Pennsylvania and collected twenty-three thousand signatures. Vickers and Small opened Pittsburgh, then Wheeling, then Cincinnati. Teams fanned out from there. Missionaries were in the field continuously, and the Pittsburgh correspondent quoted in Chapter One could not think of a kind of building they had not reached.

A lecture is not a meeting. Attention runs one way. Five thousand people listen to Hawkins; Hawkins listens to nobody. He cannot; that is what a platform is.

And Chapter Nine showed what happens to a group in which a small set of people receive a great deal of attention and return almost none. It is not merely that they hold a large share. In the limit they hold **all** of it. A movement of a hundred thousand people, whose attention structure is dominated by a few dozen touring speakers, decides and believes approximately what those few dozen speakers decide and believe. The other ninety-nine thousand-odd are talking, and are genuinely being heard by each other in their own rooms, and are not entering the aggregate.

So the Washingtonians did not have one failure mode with a famous man attached. They had the worst of the three, and they had it structurally, built into the only mechanism they possessed for growing.

---

That last clause matters, and it is the point at which I want to be fair to them rather than clever about them.

**They had no other way to scale.** There was no treatment system to refer people, no medical consensus that this was a condition anyone treated, no courts sending anybody. Chapter One made this point about inflow and it applies again here: every Washingtonian arrived because another Washingtonian went and got him. When the movement wanted to reach beyond one city, the platform was the instrument available. Print existed, but print in 1841 meant a temperance newspaper edited by somebody with his own agenda, which is how John Marsh came to curate what later historians would know.

Growing through named speakers was not a mistake the Washingtonians made. It was the only door in the building.

Now put AA's equivalent beside it. When AA faced the same problem in 1937, forty members after two years and no way to reach the hundreds of thousands they believed were out there, they wanted paid missionaries and hospitals. They were refused the money, as Chapter Four described. What they did instead was write a book.

And the book went out with no author's name on it. Not as a modest gesture: the fellowship's own name was the byline. The most important artefact the movement produced in its first decade carried the message with no man attached to it, so that no man's subsequent drinking could take it down.

Two movements, the same problem, two instruments. One scaled through named men on platforms, which is structurally the worst arrangement in Chapter Nine. The other scaled through an anonymous book, which is structurally no arrangement at all: a book confers no influence weight on anybody, because there is nobody there to confer it on.

I am not claiming anyone reasoned it out that way. Nobody did. But when Tradition 11 was written in 1946, saying the fellowship's public relations rest on attraction rather than promotion, and Tradition 12 placed anonymity at the foundation, they were forbidding precisely the growth mechanism that had built and then broken their predecessor.

---

Now the limits, and there are four that matter.

**The theorem is about members averaging beliefs, and public reputation is not that.** Golub and Jackson describe people in a group updating toward each other about a shared question. What the American public believed in 1845 about whether temperance worked was not formed by that process. I have argued a structural analogy: a quantity that should have been an average over many independent contributions was in fact dominated by a few, so when the few failed there was nothing to cancel against. The analogy is close and I think it holds. It is still an analogy, and if outsiders' beliefs about a movement are formed some other way entirely, this chapter's central application fails while Chapters Seven through Ten stand.

**DeGroot averaging is a simplification of a group conscience.** Members argue rather than average, defer selectively, abstain, and sometimes harden. Everything in Part Two is a statement about naive repeated averaging, and a room that deliberated some other way would need a different analysis.

**The exchangeability in Chapter Eight is exact only in the limit.** Real trust is never perfectly uniform, even under flawless adherence. The Traditions push maximum influence toward one over N; they do not deliver it.

**And the objection raised in Chapter Six has not gone away.** A critic can say that treatment centres and courts keep AA alive, not the aggregation properties of its governance, and that this book has spent five chapters on the less important variable. The simulation does not refute that. It ranks the two, and the ranking favours the critic.

I think both matter and I think the honest position is that the model cannot rank them. What the model can say is that the two do different work. Inflow determines whether a group survives. Influence structure determines whether the decisions it makes on the way are any good. A group can have plenty of the first and still spend twenty years deciding things badly, and nothing in its experience will tell it so.

---

Which brings this part back to where Part One ended.

Chapter Six ended on Milton Maxwell, who in 1950 named anonymity, rotating leadership and keeping authority out of persons as a functional group, and said the first of them had sheer survival value. He got there by the route this part has just retraced: through Gough, and through what a movement risks when its credibility sits in named men.

What he could not do was say why those mechanisms and not others. His method was comparison, and comparison cannot separate a mechanism from a correlate. Part Two can, because the three he named turn out to be three ways of satisfying one stated condition, and the condition has a proof behind it.

That is the whole of what Part Two adds to him. Not a discovery, and not the research he called for at the end of his paper, which still has not been done. Something smaller and prior to it: his claim, stated precisely enough that somebody could go and check it.

The group half of this book now rests on a theorem rather than on an analogy between two fellowships. Whether the rest of it should be believed is a different question, and Part Six is about that.

---

## The Machinery

### 1. What the model says

This chapter applies Chapter Nine's three failure modes to a historical case, so the model contributes a classification rather than new numbers.

**The Washingtonian meeting was structurally flat.** Everyone testified, attention ran in every direction, and on the model's terms a room like that satisfies the condition well.

**The Washingtonian growth mechanism was structurally imbalanced**, which Chapter Nine showed to be the most damaging of the three. A touring speaker receives attention from thousands and returns none, and a movement whose attention structure is dominated by such figures concentrates effectively all of its influence in them. The computation behind that claim is in Chapter Nine: a group of two hundred and fifty with a closed core of five has error 0.357, exactly the error of a five-member group, because the influence of everyone outside the core is identically zero.

**The prominent-agent problem was downstream of this, not independent of it.** Gough's 1843 relapse produced nothing and his 1845 relapse produced a national controversy. The variable that changed was the weight the growth mechanism had placed on him.

**AA's contrasting instrument carries no influence weight at all.** A book has no node in the trust matrix. This is the sharpest structural difference the model can point to between the two movements' methods of scaling, and unlike most of Part One's comparisons it does not depend on any parameter I chose.

### 2. The technical version

No new computation. The figures referenced are from Chapter Nine, section 2, and are asserted in `model/book-calculations.ipynb`, section 2: closed core of five in a group of two hundred and fifty holds influence 1.000 in aggregate with 0.000 outside it, and error 0.357, matching the square root of two over pi divided by the square root of five.

The classification claim can be stated formally. A movement's attention structure can be modelled as a bipartite arrangement: within-group attention, which was flat, and cross-group attention flowing through touring speakers, which was one-directional. As the proportion of total attention carried by the second channel rises, the influence vector converges on the speakers regardless of how many members the movement has. The Washingtonians' expansion from 1841 to 1843 was precisely a rise in that proportion.

~~I have not simulated this bipartite structure.~~ **It has now been simulated, and it turns out to have an exact closed form.**

Let each member give a fraction of their attention to the touring speakers and let the speakers give a fraction of theirs back to the general membership. Then the speakers' total influence is

> speakers' share of influence = outward / (outward + back)

and this is exact to twelve decimal places, **independent of how many members the movement has and independent of how many speakers there are**. Five speakers receiving three tenths of the movement's attention and returning two tenths of their own hold six tenths of the influence in a movement of ten and in a movement of a thousand alike.

That is stronger than the argument this chapter was making. It is not that the influence vector converges on the speakers as the proportion rises; it is that the speakers' share is fixed by a ratio and does not move with the size of the movement at all. The Washingtonians could have grown to any size whatever and the touring speakers would have held the same fraction of the movement's attention, because growth adds members to the denominator of the local channel and to the numerator of the speaker channel in equal measure.

One caution about the construction, because the first version of it was degenerate. If the speakers give *nothing* back, they are a closed communicating class, the chain is not strongly connected, Golub and Jackson's theorem does not apply, and the speakers hold all of the influence at every size and every level of attention including a tenth. That is a true statement about an absorbing set and a useless one about a fellowship, and it is not the result quoted above.

### 3. Notes on sources

**The historical material is from Part One and carries Part One's sourcing.** Maxwell 1950, read in full, for the touring teams, the signature counts, the Pittsburgh correspondent, Hawkins's career, and the closing call for research. Gough 1869, read at source, for both relapses. The 1937 Rockefeller episode reaches this chapter through Chapter Four, which was rebuilt on Kurtz, *Not-God*, read at source: the December 1937 board room is now first-hand, and the Amos report and Rockefeller's reasoning are still at a remove. The publication of the 1939 book remains at a remove.

**The claim that the 1939 book was published without an author's name** is well attested and easily checked: the work was issued by Works Publishing and attributed to the fellowship rather than to Wilson. I have not examined a first edition directly.

**The application of the imbalance failure mode to the lecture circuit is mine**, and it is an interpretation rather than a finding. It is the strongest new claim in this chapter and it rests on a structural argument, not on a computation of the actual 1840s attention network, which nobody can reconstruct.

**On fairness to the Washingtonians.** I have tried to make the point that the platform was the only instrument available to them rather than a mistake they made. Maxwell's own judgment is harsher on the movement than mine, and a reader who wanted to argue that the Washingtonians were simply careless with their famous men would find support in the AA literature. I think that reading is unfair and I have said why.

### 4. References

**Read in full:**

Maxwell, M. A. (1950). "The Washingtonian Movement." *Quarterly Journal of Studies on Alcohol* 11: 410-452.

Gough, J. B. (1869). *Autobiography and Personal Recollections of John B. Gough.* Springfield, Mass.: Bill, Nichols & Co.

Golub, B. and M. O. Jackson (2010). "Naive Learning in Social Networks and the Wisdom of Crowds." *American Economic Journal: Microeconomics* 2(1): 112-149.

**Cited at a remove:**

The 1937 approach to Rockefeller, the Albert Scott question, and the decision to write a book rather than fund missionaries. See Chapter Four, which was rebuilt on Kurtz, *Not-God*, read at source; the board room scene there is first-hand and the Amos report is still at a remove.

**Referenced but not reproduced:**

The Twelve Traditions of Alcoholics Anonymous, paraphrased. The text is copyright Alcoholics Anonymous World Services, Inc. and is not reproduced here.

**What was not read:**

Blumberg and Pittman (1991), *Beware the First Drink!*, which is the only book-length modern treatment of exactly the comparison this chapter makes and is the source most likely to have anticipated or contradicted it. Not obtained. Also unread: any contemporary account of how attention actually flowed within a Washingtonian society, as against between societies and their touring speakers, which is the distinction the whole chapter turns on and which the surviving record may simply not contain.


\clearpage
\thispagestyle{empty}
\vspace*{0.32\textheight}
\begin{center}
{\Large\bfseries Part Three}\\[0.6em]
{\large\itshape The Member}
\end{center}
\clearpage

# Chapter Twelve: Twelve Dials

There is a question people in AA ask each other that sounds like small talk and is not. Where are you in the steps?

The expected answer is a number. I am on four. I finished my ninth last spring. It is a natural way to talk, and it treats the programme as a list with boxes down the side. You work through them, you tick them off, and the tick stays ticked.

Everyone who has been around a while knows this is not quite how it goes. People who finished all twelve years ago come back looking like they have not done any of them. People stuck on the fourth for a decade are plainly doing something, and the something is working. A man who made his amends in 1994 has not, in any useful sense, still made them. The list-with-boxes account cannot express that, and the rooms have a whole vocabulary for working around it: you are as sick as your secrets, it works if you work it, we do not graduate.

This chapter takes that vocabulary seriously enough to write it down. The proposal is small and everything in Part Three rests on it. **A person is not a position in a list. A person is twelve quantities, each of which can be high or low, and each of which moves.**

Saying "I did Step Four" and saying "Step Four is at 0.8" are different kinds of statement. The first is about the past and is permanent. The second is about now and is perishable. If the second is the right description, three consequences follow immediately, and the rest of the chapter is those three consequences.

---

The first is that everything leaks.

Left alone, a dial falls. This is not a moral claim and it is not about willpower. It is the standard structure of every model of accumulated human capability since Ben-Porath wrote his in 1967, and it is there because it is obviously true of skills, languages, fitness and relationships. A thing you built and then stopped doing does not stay where you left it.

In the model each dial loses about six per cent of its current value per week when nothing is holding it up. That gives a half-life of a bit under three months: a practice at 0.8, entirely unattended, is at 0.4 in twelve weeks. I want to be clear that six per cent is a number I chose. What I did not choose is the shape, which is proportional decay, because that is what depreciation looks like in every literature that has measured anything like it.

The nearest measurements I have found do not rescue the number, and they are worth stating, because after the ordering exponent the decay rate is the most consequential value in the model. Both measure skills rather than practices. Greek teachers kept waiting years for a post lose teaching skill at something like four per cent a year, perhaps more once they have taught; German workers out of a job for up to three years lose no measurable cognitive skill at all. Six per cent a week is one to two orders of magnitude faster than either. I do not think that makes it wrong, because a practice is not a skill. A person can keep for years the ability to write an inventory while the habit of writing one lapses in a month, and the one thing in those studies that did fall, the unemployed workers' own sense of their conscientiousness and patience, looks more like a practice than a skill. But the number now rests on that distinction and nothing else, since I have found no measurement of how fast a practice lapses. If it lapses much more slowly than I assumed, groups in the model grow larger and healthier across the board, and some of the book's comparisons change with them, which the Machinery sets out.

The immediate payoff is that the model can distinguish two people who would score identically on a checklist. Both have done all twelve steps. One is doing them; one did them. In a list the two are the same person. In twelve dials they are nowhere near each other, and the model will predict quite different futures for them, which is the minimum you would want from a description of a programme whose members insist on exactly this distinction.

There is a second decay term, smaller and stranger. A dial falls faster when the dial *after* it is low. Practice on the ninth step erodes more quickly in someone whose tenth is empty. That is a modelling choice with a clear intuition behind it, which is that the later steps are partly what maintains the earlier ones, and it is worth flagging as a choice rather than a finding.

---

The second consequence is that the steps are gated.

A dial cannot rise much while the one before it sits near zero. In the model the growth of each step is multiplied by the level of its predecessor, raised to a power. Set that power high and the gate is strict: nothing moves until the previous step is well established. Set it low and the gate is loose, and a person can make progress on the eighth while the fourth is barely started.

This is the assumption most likely to be wrong, and it is also the one doing the most work, which is an uncomfortable combination. Chapter Thirteen is entirely about whether it is true, and states plainly that nobody has tested it, so Chapter Twelve should not pretend the matter is settled. What this chapter contributes is only that the folk rule is expressible: the claim that you cannot skip a step is a claim about the value of one exponent, and writing it that way is what makes it checkable.

There is also a fact about that exponent I did not expect, which comes from the sensitivity work rather than from any argument. Of the hundred and eighteen numbers in this model, the step-ordering exponent is the one with the largest single influence on how a group ends up, and it holds that position on all three outcomes the sweep scores. Moved alone by a quarter in either direction, it swings the group's daily practice by about one and a quarter times its own baseline value, its maintenance by five and a half times, and its final membership by two and a half times, which is more than the decay rate does and more than anything else does. The strictness of the ordering is the most consequential thing in the apparatus and it is a number nobody has measured. That is worth saying plainly, and it is a better argument for Chapter Thirteen's research programme than anything Chapter Thirteen says on its own behalf.

---

The third consequence is the one that connects a person to a room, and it is where the chapter has something genuinely non-obvious to report.

Some steps need other people and some do not. That much is obvious from reading them. What is not obvious is how uneven the difference is, or which steps fall where.

In the model this is not a judgement. It is derived. I asked, for each step, what a person actually needs from a group in order to do it. Somewhere to walk in. Other people who identify themselves as alcoholic, and visible evidence that recovery happens. Confidentiality, and counsel from someone further along. Somebody to help. Continuity week to week, and a certain amount of gentle pressure. Eight things. Each step consumes some combination of them, and a step's dependence on the group is just how much it consumes in total.

Run that through and the answer is a spread of about six to one, from the least social step to the most. The two that need a group most, both at the maximum, are the first and the last: admitting the problem, and carrying the message. Everything in the middle needs less, and the least social of all is the seventh, at about a sixth of the maximum, which in most tellings is the one conducted alone and in silence.

That is a claim about what a meeting is for, and it is worth stating in the form a member might recognise. **The group is most necessary at the two ends and least necessary in the middle.** You need a room to arrive in and you need a room to be useful to. In between there is a stretch of work that is largely yours, done in your own time, and the room's job during that stretch is mostly to still be there when you come back.

I have some confidence in the shape of that result, because it fell out of asking what each step requires rather than out of deciding what the answer should be. I have much less confidence in the exact coefficients, and the honest position is that the ordering of the twelve is more trustworthy than any individual value in it.

---

Now a correction that matters for Part Four.

A person's practice contributes to what the group can supply, and what the group
supplies contributes to a person's practice. I had described those flows as two
linear weights, one upward and beta downward. The code does not contain that pair.
Member states enter through means, threshold counts, sums, dispersion and
saturation. The return path passes through resource capacities, normalized
bundles, beta, sequential gates, maintenance capacity and remaining headroom.

Beta is still useful as a within-model dependence index: it controls the blend of
autonomous and resource-supported peer growth for each Step. Its reciprocal is not
a transmission ratio. Any directional comparison would have to name a state,
perturbation and derivative, or use a paired trajectory contrast.

---

I should be exact about what this apparatus is, because the preface promised a proper description and because everything in Parts Three, Four and Five is downstream of it.

A member is twelve numbers between zero and one. A group is a collection of members, plus eight supply quantities computed from their states, plus the twelve Traditions expressed as levels of adherence between zero and one. Members arrive from two channels and leave through two. Time runs in half-weeks for thirty years. Steps grow at a rate that is a product of four things: a top speed for that step, the gate, the group's supply of what that step needs, and the person's own maintenance capacity, which is Chapter Fourteen's subject. Against growth runs the leak.

That is the central machine. It has **one hundred and eighteen registered numeric
values**: twenty-two scalar defaults, twelve Step speeds, forty-nine nonzero
entries in the consumption matrix and thirty-five nonzero entries in the
governance matrix. That is not every simulation-effective choice. Functional
coefficients, founder and arrival states, horizons, the time step, the viability
threshold, perturbation ranges and the one hundred and eight structural zeros are
separate choices. None was fitted to AA group data.

Two things follow that a reader should hold onto.

The first is that a model like this can show a set of ideas is consistent. It cannot show they are true. Everything Part Three claims is of the form *if the world works like this, then that follows*, and the antecedent has not been checked against a single real person.

The second is methodological. The expanded one-at-a-time screen moves each of
those 118 registered values in both directions at ten, twenty-five, fifty and
seventy-five per cent, producing 944 parameter-direction-distance endpoints. It
uses only three stochastic seeds per endpoint and cannot establish universality
or test structural zeros. Its strict orderings, ties, reversals and unresolved
comparisons must be reported separately. Confirmatory claims in this revision use
400 paired seeds and named mechanism contrasts.

---

One last observation, which is the strangest thing the sensitivity work turned up and which belongs here rather than anywhere else, because it is a fact about the apparatus rather than about recovery.

Thirty-five of those hundred and eighteen numbers record which Traditions govern the supply of which group resource. All of Part Four is built on them. And they have no effect at all on a group that follows the Traditions completely.

This is arithmetic and not a result. Each column of that matrix is scaled to sum to one before it is used, so at full adherence the scaling undoes the entries exactly and every resource comes out at quality one, no matter what I put in the cells. Those thirty-five numbers begin to bite only when adherence is partial, and even then a quarter's change in any one of them shifts nothing you could measure.

This cancellation is scenario-specific, not reassurance that the governance
matrix is unimportant. At partial adherence its magnitudes matter, and Part Four's
semantic-overlap claims also depend on them. The blank pattern is authored too,
and multiplicative sensitivity cannot test whether a blank should be filled.

---

## The Machinery

### 1. What the model says

A member is a vector x of twelve step-practice levels in [0, 1]. Growth in each step is the product of four terms and is opposed by depreciation. The three properties the chapter rests on are all in that one equation: depreciation makes practice perishable, the gate term makes it ordered, and the group-supply term makes it social to a degree that varies by step.

The group-dependence coefficients are calculated from, but not independently
validated against, the authored consumption matrix. Each Step's row in S is
summed and normalized by the largest row sum. Steps 1 and 12 are 1.00, Step 7 is
0.17, and the mean is 0.53.

These coefficients blend autonomous and resource-supported peer growth. The code
does not implement their reciprocals as member-to-group weights, so no one-to-six
transmission claim follows.

### 2. The technical version

Per-step growth, in full, for member *m* and step *i*:

> dx(i)/dt = h(m) * a(i) * gate(i) * peer(i) * Cm(i) * (1 - x(i))  -  d(i) * x(i)

with

> gate(i) = x(i-1) ^ p_gate,  and gate(1) = 1
>
> peer(i) = (1 - beta(i)) + beta(i) * G(i),  G = Snorm * R
>
> Cm(i) = 1 - w(i) * (1 - C),   w(i) = 0.05 + (i - 1) * (1 - 0.05) / 11
>
> d(i) = delta0 * (1 + psi * (1 - x(i+1))) for i < 12,  d(12) = delta0

Two terms in that equation belong to other chapters and are written here so this one is
complete rather than referring outward. **C is the maintenance capacity** and Chapter Fourteen
derives it; all that matters here is that it lies in [0, 1] and is the same number for every
step of a given member. **w(i) is the per-step exposure to it**, rising linearly from 0.05 at
Step One to 1.00 at Step Twelve, so that Cm(1) is essentially 1 whatever C is and Cm(12) is C
itself. That weighting is the formal content of the claim that an arrival has nothing to
maintain and a veteran has a great deal. **h(m) is member heterogeneity**, a lognormal draw
parameterized as exp(N(-het_sd^2/2, het_sd)) and fixed after arrival. Its arithmetic mean is
one, so changing het_sd changes dispersion without mechanically changing average capability.

**Parameters.** delta0 = 0.06 per week, giving an unattended half-life of 11.6 weeks. psi = 0.20 is the backward complementarity. p_gate = 1.5 is the ordering exponent. Top speeds a run from 0.15 at Step 9 to 0.30 at Step 1.

**The eight group resources:** somewhere to be admitted, others who identify as alcoholic, visible proof of recovery, confidentiality, counsel, somebody to help, week-to-week continuity, and gentle pressure.

**Derived group-dependence, beta:**

| Step | beta | Step | beta |
|---|---|---|---|
| 1 admit | 1.00 | 7 ask | 0.17 |
| 2 believe | 0.71 | 8 list harms | 0.33 |
| 3 decide | 0.29 | 9 amends | 0.62 |
| 4 inventory | 0.33 | 10 daily | 0.62 |
| 5 tell someone | 0.71 | 11 connect | 0.33 |
| 6 willing | 0.25 | 12 carry it | 1.00 |

Maximum 1.00 at Steps 1 and 12, minimum 0.17 at Step 7, mean 0.53, ratio of extremes 6.0.

**Registered sensitivity inventory:** 22 continuous scalars, 12 step speeds, 49 non-zero cells in S, 35 in the governance matrix. These 118 values are not every authored model choice; fixed constants, structural zeros, equations and experiment-design settings are inventoried separately. None is fitted.

**One dial per step is an assumption, and the measurement literature does not support it.** Greenfield and Tonigan (2013) gave 130 new AA affiliates two instruments at intake and at three, six and nine months. The two disagreed about whether step-work had happened for nine of the twelve steps, which is a caution about the whole enterprise of putting a number on a step. More awkwardly for this chapter, their factor analysis found step-work is not one thing. It came apart into behavioural step-work and spiritual step-work, and the two behaved differently: the behavioural component held steady over time and was predicted by having a sponsor, while the spiritual component declined over time and was the one that predicted percent days abstinent. Behavioural step-work predicted nothing about later substance use.

This model gives each step a single level. It therefore cannot represent the member their data describes, whose behavioural practice holds while the spiritual part falls away, and it collapses into one number the only component that predicted an outcome. That is a limitation of the representation and not a detail of calibration, and no sensitivity analysis in this book can reach it, because every design here perturbs the values of the dials rather than the decision to have one dial. Their study is small, nine months long and observational, so it is not a refutation. It is a well-aimed objection to the shape of the apparatus, and Chapter Thirteen's research programme should include it.

**From the multi-level sweep** (`research/oat_full.json`, notebook section 9): 118 registered values, each moved alone by 10, 25, 50 and 75 per cent in each direction, three common seeds per endpoint, 944 perturbation points. Against a full-adherence baseline of 0.0431 maintenance, 0.2261 practice and 18.67 members, the ordering exponent `p_gate` has the largest single influence on every scored outcome. At plus or minus 25 per cent it swings maintenance from 0.0027 to 0.2373, a range of 5.45 times baseline; the decay rate `delta0` is second at 3.27 and the step-10 speed third at 2.22. Across the whole four-level ladder the `p_gate` maintenance range is 14.64 times baseline, `delta0` 12.98 and member heterogeneity 4.69. All 35 governance cells produce zero change in every outcome and every scenario, to floating-point precision, because the sweep runs at full adherence and the column-normalised governance quality is then identically 1 whatever the underlying cell magnitudes are. That is a property of the reference point, not evidence that governance is inert, and it is why the Morris and Sobol designs sit at 0.85 adherence instead.

### 3. Notes on sources

**The functional forms are borrowed; the values are not.** Depreciating human capital with endogenous investment is Ben-Porath (1967), read at source. The production of a stage from several inputs, and the idea that early stocks condition later growth, are from Cunha and Heckman (2007) and Cunha, Heckman and Schennach (2010), also read at source. They combine the inputs with a constant-elasticity-of-substitution aggregator. The product used here is my choice, not theirs: it resembles that family's Cobb-Douglas case, which Cunha and Heckman give, but its terms and exponents are this book's, and Chapter Thirteen returns to their aggregator when it asks about substitutability. The saturation form used for the participatory resources is Iannaccone's (1992), read at source.

**Nothing here is calibrated to AA data**, because none exists at the required resolution. Inflow, dropout and churn were originally set to target a steady state near forty-five members with an experienced core near nine, roughly a healthy urban meeting. After correcting the lognormal capability draw to have mean one, 400 runs deliver 17.80 ± 0.88 members overall. Among the 394 viable endpoints, the established count above 0.1 is 14.13 ± 0.79 and the experienced count above 0.5 is 1.25 ± 0.20. The calibration therefore fails rather than merely undershooting. I report that failure instead of retuning after seeing the results; absolute levels should not be interpreted as estimates of AA groups.

**The resource list is mine.** The eight group resources were arrived at by asking what each step requires from other people, and no source proposes this list. Someone who knows the programme better would produce a different eight, and the group-dependence coefficients would move with it. What I would expect to survive is the shape: the entry step and the service step depending most, the interior steps depending least.

**The decay rate against the only estimates I have found.** Two papers on adult skill depreciation were read on 13 September 2026, and neither measures anything the model's dials represent. Dinerstein, Megalokonomou and Yannelis use the quasi-random order in which Greek graduates wait for teaching posts and estimate that teaching skill depreciates at about four per cent a year in early-career teachers, and at about seventeen per cent in more experienced ones with a standard error larger than the estimate; they describe both as lower bounds if age itself adds skill, and their district-level estimates rest on a weak first stage. Cohen, Johnston and Lindner follow newly unemployed German workers for up to three years and find no decline in cognitive skills or in the noncognitive skills that predict earnings, although self-assessed conscientiousness, risk tolerance, trust, patience and reciprocity fall by between a fifth and three fifths of a standard deviation. The model's six per cent a week compounds to a loss of about 96 per cent a year, a half-life of 11.6 weeks against roughly sixteen and four years for teaching skill. Read as skill, the rate is one to two orders of magnitude too fast. Read as practice, which is what the dial is, it is untested: these papers bound how fast a capability fades, not how fast the habit of using it lapses, and the one declining measure in them is closer to a habit than a skill. I have left the value unchanged, because replacing an authored number with another authored number chosen after reading two papers about something else would not be an improvement, and I report instead how much rides on it.

**How much rides on it.** The decay rate is second only to the ordering exponent in the multi-level sweep, the Morris screen and the Sobol decomposition, where its membership total-order index is 0.373. Chapter Fourteen's 400-seed sweep takes it from 30 per cent below its value to 50 per cent above, and at 30 per cent below the full-adherence group ends with 57.71 members against 17.80, close to the room's capacity. In the one-at-a-time screen, run at three common seeds per endpoint, the referral-starved group, which closes at the default rate, is endpoint-viable at every seed once the rate is a quarter lower, and large downward moves of this rate are among the few that reverse the ordering between losing referrals and losing attraction on final membership (Chapter One; appendix A7.5). A rate anywhere near the skill literature's lies far outside every range tested. The comparisons the book reports are therefore conditional on practice lapsing at roughly the assumed rate, and a measurement of how fast a practice lapses would be worth nearly as much to it as a measurement of the ordering exponent.

**The numbers are computed, not cited**, and are asserted against these printed values in the companion notebook.

### 4. References

**Read in full:**

Ben-Porath, Y. (1967). "The Production of Human Capital and the Life Cycle of Earnings." *Journal of Political Economy* 75(4): 352-365. The depreciation structure and the treatment of a capability as a stock with investment and decay.

Greenfield, B. L. and J. S. Tonigan (2013). "The General Alcoholics Anonymous Tools of Recovery: The Adoption of 12-Step Practices and Beliefs." *Psychology of Addictive Behaviors* 27(3): 553-561. **Read in full**; the NIH author manuscript, PMCID PMC3707937, obtained 10 August 2026 and stored with its citation and metadata in `research/incorporated/Greenfield_Tonigan_2013/`. Source for the disagreement between two step-work instruments on nine of twelve steps, for the two-factor structure separating behavioural from spiritual step-work, for their different time paths and predictors, and for spiritual step-work rather than behavioural step-work predicting percent days abstinent. Used here as an objection to this chapter's one-dial-per-step representation. **Note the copy**: this is the author manuscript, so its pagination is not the journal's, and the staged record that preceded it gave the issue and end page incorrectly as 27(2): 553-560.

Cunha, F. and J. J. Heckman (2007). "The Technology of Skill Formation." *American Economic Review* 97(2): 31-47. Self-productivity, and the conditioning of later growth on earlier stocks.

Cunha, F. J. J. Heckman, and S. M. Schennach (2010). "Estimating the Technology of Cognitive and Noncognitive Skill Formation." *Econometrica* 78(3): 883-931. The stage technology whose substitution parameter is Chapter Thirteen's subject.

Iannaccone, L. R. (1992). "Sacrifice and Stigma." *Journal of Political Economy* 100(2): 271-291. The saturation form for goods produced by participation.

Dinerstein, M., R. Megalokonomou and C. Yannelis (2022). "Human Capital Depreciation and Returns to Experience." NBER Working Paper 27925, revised September 2022. **Read in full** on 13 September 2026 apart from its online appendix, which is not held; stored in `research/incorporated/Dinerstein_2022/`. The depreciation of teaching skill during time without formal employment, its separation from forgone experience, and the caveats on precision, age effects and the weak district-level first stage.

Cohen, J. P., A. C. Johnston and A. S. Lindner (2023). "Skill Depreciation during Unemployment: Evidence from Panel Data." NBER Working Paper 31120. **Read in full** on 13 September 2026 apart from its appendices; stored in `research/incorporated/CohenJohnstonLindner_2023/`. No measurable decline in cognitive or earnings-relevant noncognitive skills over up to three years of unemployment, the decline in several self-assessed traits, and the decline in the same measures after retirement.

**Cited at a remove:**

Nothing.

**Internal, and reproducible from this repository:**

The derived group-dependence coefficients, the transmission ratio, the parameter inventory, and the sweep results quoted above. Code and assertions in `model/book-calculations.ipynb`.

**What was not read:**

The literature on how fast practices and habits lapse, as distinct from how fast skills fade, which is where the evidence for the decay rate would have to come from and which was not searched. The two skill papers above are the only part of the depreciation literature read.

# Chapter Thirteen: Can You Skip a Step?

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

It is also a question that has been answered once, somewhere else, and the answer was not a single sign. When Cunha, Heckman and Schennach estimated their version of the parameter for children, it came out positive in early childhood for cognitive skills, where investment can make up for a poor start, and strongly negative later on, where it cannot; for the social and emotional skills it was negative at both stages. Nothing about the steps follows from children's test scores. But the one place anyone has measured this found that the answer depends on the stage and on the kind of capability, and a study of the steps should be built to find that rather than to assume one sign for all twelve.

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

Each step is written as a production stage combining four inputs: the person's own accumulated practice of that step, their practice of the preceding step, what the group supplies for that step, and their maintenance capacity. The functional form is the constant-elasticity-of-substitution aggregator used by Cunha, Heckman and Schennach for skill formation, with a single parameter rho governing how substitutable the inputs are. They write that parameter as phi and use rho for something else, the weight of cognitive skill in an adult outcome; rho is this book's notation, kept because this chapter and the paper use it throughout.

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

**The unsolved obstacle.** Group input is endogenous to member state. Groups direct attention toward members who are struggling, and members who are doing well attract sponsees. Estimating this technology without handling that will attribute to the technology what is really selection. Cunha, Heckman and Schennach face the identical problem with parental investment and address it: they let family income move investment without moving skill directly, and identify the technology under parametric assumptions they state. Adapting that approach is necessary before any of this touches real data, and I have not done it, nor is it obvious what would play the part of family income for a group.

### 3. Notes on sources

**The empirical literature has now been read in full, and it did not qualify what the abstract stated.** Greenfield and Tonigan's study previously reached this chapter through its abstract and secondary summaries, and this note recorded that the full paper should be read before the chapter was final. It was obtained and read on 10 August 2026. Every specific claim used here survives: the two-factor structure, the differing predictors and time trends of the two factors, the finding that only spiritual step work predicted percent days abstinent, and the discrepancy between instruments on nine of twelve steps. What full reading adds is scale and design rather than correction, and both are worth stating beside the findings: 130 new AA affiliates, assessed at intake and at three, six and nine months, observationally. That is a small sample over a short horizon, so the two-factor result is a finding to build on rather than a settled fact.

**Cloud and colleagues' definition of twelve-step affiliation** as attendance plus self-identification plus sum of steps completed reaches me through a later methodological paper citing it, not from the original.

**Carroll (1993) on adherence to the steps has not been consulted**, and it is the most likely place for a prior treatment of sequencing. It should be checked before this chapter is final.

**I have not established that no experimental test of sequencing exists**, only that none appeared in a reasonable search and that the standard measurement instrument could not support one. Those are different claims and the chapter states the weaker one.

**The formal apparatus is read at source.** Cunha and Heckman (2007) and Cunha, Heckman and Schennach (2010) for the technology and the identification strategy. Both were read in full on 13 September 2026 in their working-paper versions, whose pages `research/SOURCES.md` records.

**The one estimate of the analogous parameter.** Cunha, Heckman and Schennach's estimates allowing for unobserved heterogeneity, their Tables 4 and 5, put the cognitive-skill parameter above zero in the first stage of childhood and well below it in the second, and the noncognitive parameter below zero at both. The sign therefore varies with stage and skill in the one literature where it has been estimated. Their inputs are a child's skills, investment and the parents' skills, and their stages are years of childhood, so this is an analogy for the design of a study and not evidence about the steps.

**The numbers are computed, not cited**, and are asserted against these printed values in the companion notebook.

### 4. References

**Read in full:**

Cunha, F. and J. J. Heckman (2007). "The Technology of Skill Formation." *American Economic Review* 97(2): 31-47. Self-productivity and dynamic complementarity.

Cunha, F. J. J. Heckman, and S. M. Schennach (2010). "Estimating the Technology of Cognitive and Noncognitive Skill Formation." *Econometrica* 78(3): 883-931. The CES stage technology, the measurement system, anchoring, and the treatment of endogenous investment.

**Cited at a remove:**

Greenfield, B. L. and J. S. Tonigan (2013). "The General Alcoholics Anonymous Tools of Recovery: The Adoption of 12-Step Practices and Beliefs." *Psychology of Addictive Behaviors* 27(3): 553-561. **Read in full**; the NIH author manuscript, PMCID PMC3707937, obtained 10 August 2026 and stored in `research/incorporated/Greenfield_Tonigan_2013/`. Source for the two-factor structure, the predictors and time paths of each factor, spiritual step-work predicting percent days abstinent where behavioural step-work did not, the instrument discrepancy on nine of twelve steps, and the sample of 130 affiliates over nine months. **Note the copy**: the author manuscript's pagination is not the journal's.

Cloud, R. N. and colleagues (2004). The definition of twelve-step affiliation as attendance, self-identification and sum of steps completed. Reached through a later methodological review; the original has not been located and the co-authors are therefore not named here, which is a defect in this entry rather than a house style.

Schennach, S. M. (2004). "Estimation of Nonlinear Models with Measurement Error." *Econometrica* 72(1): 33-75; and Hu, Y. and S. M. Schennach (2008). *Econometrica* 76(1): 195-216. The identification results underlying the measurement strategy, known through their application in Cunha, Heckman and Schennach. Hu and Schennach's abstract, introduction and assumptions were read on 13 September 2026 and match that use; Schennach (2004) was not read.

**Internal, and reproducible from this repository:**

The substitution table and cross-partial series are checked in `model/book-calculations.ipynb`; both are exact algebra on a fixed functional form and carry no sampling error. The 3,200 proxy-averaging jobs, 400 replications for each of four true values and two proxy counts, are in `research/ch13_reps.json`, generated by `model/ch13_reps.py`. Those replications do carry sampling error, and the fractions below are proportions over 400 replications with 95 per cent Wilson intervals. At rho = 0 the estimated effect is nonpositive in 53.5 per cent of the one-proxy designs, interval 48.6 to 58.3, and in 55.5 per cent of the three-proxy designs, interval 50.6 to 60.3. At rho = -4 and rho = -1 it is nonpositive in every replication, interval 99.0 to 100.0, and at rho = 0.5 in 0.2 per cent of the one-proxy designs, interval 0.0 to 1.4, and none of the three-proxy designs, interval 0.0 to 1.0.

**What was not read:**

Any work estimating a substitution parameter for a sequential practice of this kind. The one estimate of an analogous parameter, for children's skills, is described in the notes above; it concerns stages of childhood, not a practice. The chapter's central move is to say that the folk rule is the limiting case of a family indexed by rho, and that rho is estimable in principle; nobody has estimated it for the steps, and the chapter should not be read as implying that anybody has.

Carroll, S. (1993). On adherence to the twelve steps.

# Chapter Fourteen: The Leaky Bucket

The people who go out are often not the ones who looked worst.

Anyone who has been around a group for a few years has watched this happen. Someone with real time, who knows the programme better than most of the room, gets busy. They stop sponsoring. The morning routine goes first, then the evening one. They still come on Tuesdays. For a while nothing visible changes at all, and if you asked them how they were they would tell you the truth, which is that they were fine. Then, some months later, they are not.

The folk description of this is that he was drunk before he drank. It is meant as a claim about sequence: the drinking is the last event, not the first. What it does not say is why the collapse should be sudden. If practice simply wears away when you stop practising, you would expect a slope. What people describe is a floor giving way.

This chapter asks whether that shape falls out of the model, what would have to be true for it to be real, and how much of it I am entitled to claim. The release audit changed the answer. The equation can produce a cliff under a sufficiently supportive frozen group environment, but the corrected model's typical endpoint environment usually does not. The old chapter demonstrated a conditional mechanism and reported it as a baseline result. That claim is retired here rather than preserved by retuning.

---

Start with what maintenance is, in the model's terms.

Nine of the twelve steps are things you do. You admit something, you write something down, you tell somebody, you go and apologise. They have a beginning and an end. Three of them do not. Steps Ten, Eleven and Twelve are the ones with no completion state: keep taking inventory, keep the practice of attention or prayer, keep carrying it to somebody else. They are what a person does on an ordinary Tuesday when nothing is wrong.

In the model these three are averaged into a single quantity called maintenance capacity, and that quantity does something the other nine do not. It does not sit alongside them. It multiplies them.

Every step in the model grows at a rate that is scaled by maintenance, and the scaling is not applied evenly. Step One barely feels it: an arrival with nothing to maintain cannot be penalised for failing to maintain it. The weight rises across the twelve, and by the back end it binds completely. Making amends, in the model, is something you can only get better at while the daily practice is alive.

That is the leak and the bucket in one. The nine event steps are the water. The three daily ones are not more water. They are whether the bucket holds.

---

Now the part that makes the shape.

Maintenance does not scale the other steps in proportion to itself. It passes through a gate: an S-shaped curve, near zero for small values, near one for large, with a short and steep transition between. This is a Hill function, borrowed from biochemistry, where it describes reactions that switch rather than ramp. Everything below the transition is effectively off. Everything above it is effectively on.

And maintenance is one of the things maintenance gates. Steps Ten, Eleven and Twelve are themselves near the top of the range where the gate binds hardest. So the loop closes on itself. A person with a live daily practice is well placed to keep having one. A person whose daily practice has fallen below the transition is not merely doing less; the machinery that would rebuild it is the thing that has gone.

A loop like that can have two resting places rather than one. The old diagnostic fixed group resources at constants taken from the capability-inflated model. Under those obsolete constants, a high start settled with maintenance near 0.32 and a low start near zero.

Both were genuine equilibria of that frozen diagnostic. They are not two typical equilibria of the corrected released model. Re-estimating the environment from 400 corrected full-adherence endpoints finds this high-start/low-start separation in seven, or 1.75 per cent. In the mean corrected environment both starts converge to maintenance of about three times ten to the minus eight.

---

The old frozen-environment diagnostic also produced a distinctive collapsed profile, which is retained here as a record of the proposed mechanism rather than as a release result.

The collapsed member has not lost everything. Averaged over all twelve dials they are at 0.27 against the healthy member's 0.50, which is a bit under half. That sounds like a person in obvious trouble. Look at the dials one at a time and it is stranger than that.

Step One, the admission, sits at 0.758 in the collapsed state against 0.766 in the healthy one. It is essentially untouched. Step Two and Step Three are down by a few per cent. Step Four, the inventory, has gone from 0.56 to 0.44, which you would have to be looking for. From there it falls off a shelf: Step Eight from 0.46 to 0.06, Step Nine from 0.36 to 0.01, and the three daily steps to nothing at all.

Under that obsolete environment the collapse was back to front: early Steps remained high while the back end disappeared. The current model does not establish that as a typical trajectory.

The profile came from the gate weighting, but it also depended on a hand-copied resource vector and group-capacity constant. Calling it emergent without naming those frozen inputs was an error. At most it shows what the architecture can generate under one supportive environment.

It still suggests a prediction that could be checked: early recognition items should move less than daily-practice items before relapse. But that prediction now comes from a conditional mechanism demonstration and outside literature, not from the corrected baseline simulation.

---

Where is the edge?

This is the question everybody wants answered and it is the one I have to refuse.

The divide between the two basins could be located precisely inside the old frozen diagnostic. Scaling its healthy state uniformly put the boundary near seventy-four per cent, or maintenance near 0.24 against 0.32. The corrected mean endpoint environment has no corresponding pair of basins and therefore no such boundary to locate.

Those numbers are worth nothing, and I need to say why with some force, because they are the most quotable thing in this book and they are the thing I would least like to see quoted.

The diagnostic contains a decay rate, a single number setting how fast an unpractised step wears away. I chose it. Under the old frozen inputs, raising it by under three per cent destroyed the high equilibrium and lowering it by a fifth raised that equilibrium to 0.56. Those are sensitivity facts about the diagnostic, not thresholds for the released baseline or for people.

That is not a caveat. It is a statement that the model has no quantitative content on this question whatever. The distance between a world where a typical person can maintain a recovery and a world where nobody can is smaller than my ability to guess a parameter, and I would not claim to know that number to within twenty per cent, let alone three.

The plan for this chapter, written before the first sweep, said five per cent. The old diagnostic returned under three. The release audit found the larger failure: after updating its state-dependent environment, a typical high equilibrium is already absent in 393 of 400 endpoint environments.

---

So what is left, and is it enough for a chapter?

What is left is the shape, and the case for the shape is different in kind from the case for the numbers.

A self-gating loop can create two stable states and a divide between them, but it does not do so for every set of inputs. The old text slid from possibility to necessity. The corrected environment check is the counterexample inside this project: the loop remains in the code while the two-attractor result is rare.

The remaining claim is more conditional. If maintenance gates its own recovery strongly enough, and if the surrounding resource environment is sufficiently supportive of a high state, then the system may have a threshold and hysteresis. Whether either premise holds for people is empirical, and the corrected baseline simulation does not supply it.

There is outside support for the shape, and it is a great deal better than it was when I drafted this chapter.

The older strand is Hufford and colleagues, who in 2003 fitted a cusp catastrophe model to relapse data from patients with alcohol use disorders and reported that it predicted better than the linear models standard in the field. A cusp catastrophe is a canonical mathematical object for a system that responds smoothly to a pressure until it responds abruptly. Witkiewitz and Marlatt subsequently argued the broader case, that post-treatment drinking is a nonlinear dynamic process rather than a linear response to risk factors, and that treating it as linear is why so much of the prediction literature has done badly. The honest size of that warrant is two preliminary samples, fifty-one inpatients and forty-three outpatients, six months of follow-up.

The newer strand is much stronger and I want to set it out carefully, because it is the closest thing in the literature to what this chapter describes, and because it does not support everything the chapter says.

In 2025 Fatimah, Hunter and Bornovalova published a **double-well potential model** of relapse. Substance use is treated as a dynamical system with two stable equilibria, one of use and one of non-use, and a continuous latent state that sits in one well and can be pushed into the other. Their image is a steel ball on a table with two magnets of unequal strength beneath it. They fitted it to timeline followback data from a hundred and thirty-nine adults with a substance use disorder returning to the community after residential treatment.

Three things in that paper bear directly on this chapter.

**The two wells are not an assumption they impose; they are a model that fits.** The parameters carry information. They call the ease of moving between wells steepness and the relative depth of the two tilt, and those parameters predicted outcomes at long follow-up, including life satisfaction and criminal behaviour, **over and above the standard measures of proportion of days used and time to first use**. A description that adds predictive power beyond the usual metrics is doing more than redescribing them.

**Their central quantity is the one this chapter calls the separatrix.** They describe the relapse process in terms of separation energy: the amount of disturbance required to move the system from abstinence to relapse, and, separately, from relapse back to abstinence. Two different energies, one each way. That asymmetry is the hysteresis this chapter argues for, arrived at by people fitting curves to real drinking histories rather than by me building a mechanism.

**And they find real between-person variation in it.** Steepness and relapse risk varied significantly across participants, and the variation was predictable from demographics, baseline psychopathology and treatment history. I chose the spread of member capability hoping it would convert individual cliffs into a group slope, rather than from a measured quantity. The corrected audit does not recover that intended mechanism in most endpoint environments. The paper supports heterogeneity in relapse landscapes, not this parameter value or this implementation.

Now the limits, and they are not small.

Their object is not my object. They model substance use behaviour; I model practice on twelve steps, of which maintenance is three. The shapes are analogous and the things being shaped are not the same, and nobody has fitted a double well to step practice because nobody has the data.

Their model is descriptive and mine is generative. They fit a potential landscape to observed behaviour and read its parameters. I claim a mechanism, that maintenance gates its own recovery, and derive a landscape from it. Their result supports the landscape. It says nothing about my mechanism, and a different mechanism producing the same landscape would fit their data equally well.

Their sample is not an AA meeting. It is a criminal-justice-involved, largely polydrug population leaving residential treatment, about a quarter from minoritised groups, measured by retrospective recall that the authors themselves say gives weekly rather than truly daily resolution over long windows.

And one finding of theirs cuts against the dramatic reading of this chapter: non-use was the predominant stable state across their participants. Most people's landscape is tilted toward staying well. The two wells exist; they are not of equal depth.

So the position is this. The external case for a nonlinear, person-specific relapse landscape now rests on a fitted double-well model with a hundred and thirty-nine people behind it. That is a real upgrade in the literature. It does not rescue the model result: the object, mechanism and environment differ, and the corrected simulation rarely produces the typical-member bistability this chapter originally claimed.

---

There is one more property of a system like this, and it is the one with the sharpest practical edge.

Suppose the pressure that pushed somebody over is removed. They come back to the group. The meetings are the same meetings, the sponsor is available again, the circumstances are restored exactly. Does the person come back with them?

In the old frozen diagnostic, no, and there was a clean line. Remove support from its high state and restore it five years later: eight or eleven weeks away recovered; twelve did not. The transition occurred near eleven and a half weeks.

That is hysteresis in the diagnostic. It is also the formal version of something the rooms say constantly without the vocabulary: the door out and the door back in are not the same width. The outside literature supports taking that shape seriously. The corrected simulation does not establish that its typical member occupies a high basin from which this experiment can begin.

The eleven weeks is retired as a model result. The asymmetry remains a property of a two-basin system and a hypothesis supported more directly by the fitted double-well literature than by this release.

---

Now the correction that matters most, because it changes the chapter rather than qualifying it.

The old calculation drew capability from an uncentred lognormal distribution and froze group support at values produced by that inflated population. Correcting the draw to arithmetic mean one reduces the experienced core and the resource environment sharply. A new audit takes the endpoint resources and group capacity from each of 400 full-adherence runs, then places the same capability-one test member at high and low initial practice in each frozen environment.

Only seven environments, 1.75 per cent, retain two attractors separated by more than 0.05 maintenance. Across environments the median high-start maintenance is 1.4 times ten to the minus nine, indistinguishable in substance from the low start. In the mean environment the two endpoints agree to displayed precision. The chapter's typical-member cliff is therefore not a result of the corrected baseline.

The full group still responds smoothly to the decay-rate sweep. From thirty per cent below baseline through fifty per cent above, endpoint viability is 1.000, 1.000, 0.9925, 0.985, 0.980, 0.980, 0.9175 and 0.8675. Mean maintenance falls monotonically from 0.226 to 0.006. That smoothness no longer supports the story that it averages many individual cliffs: the released audit finds few such cliffs for a capability-one member in its own endpoint environments.

What remains useful is methodological. A structural story must be tested under the state-dependent environment produced by the same released model. Freezing old inputs can create a clean mechanism that the full system no longer occupies. The group slope is real model output; the explanation previously attached to it is not established.

---

A last thing, which is not a result and is the reason for the whole chapter's caution.

Nobody should try to locate themselves on any of these curves. None of the numbers apply to a person, not approximately and not as a rough guide. The model has never been compared against a single real person, and the parameter that would set where your threshold sits is a number I chose because it made a simulation behave. Anybody who tells you they can locate you on a curve like this is selling something, and if the person telling you is a book, it is still selling something.

What the chapter offers is smaller and I think worth having. The outside literature gives a reasonable case for nonlinear relapse dynamics and hysteresis. This model contains one possible self-gating mechanism, but its corrected typical environment rarely produces the claimed pair of attractors. The discrepancy is a result, not an embarrassment to hide: structural plausibility does not establish that a simulated system actually occupies the regime the story requires.

---

## The Machinery

### 1. What the model says

Maintenance capacity is the mean of the practice levels on Steps Ten, Eleven and Twelve. It enters every step's growth rate through a Hill gate, weighted by step index so that it barely touches Step One and fully binds Step Twelve. Because Steps Ten to Twelve are themselves at the heavy end of that weighting, maintenance gates its own accumulation. Such a loop can be bistable; the corrected model usually is not bistable for a capability-one member in its own endpoint environments.

Two findings replace the old claims.

**The old frozen-environment demonstration is not the released baseline.** Its high state, separatrix and hysteresis are reproducible under its recorded constants, but those constants came from the retired capability-inflated population.

**The environment-matched test mostly has one low attractor.** Across 400 corrected full-adherence endpoint environments, only seven yield a high-start/low-start maintenance difference above 0.05 for a capability-one member. The mean environment yields maintenance of approximately 0.00000003 from either start.

**The group response is smooth but its old explanation is unsupported.** The decay sweep produces a monotone decline in mean maintenance and endpoint viability remains 0.8675 or higher over the registered range. The current test does not show that this smoothness is an average of individual cliffs.

### 2. The technical version

The gate is

> C(M) = M^n / (k^n + M^n),  with n = 3.0 and k = 0.12, M the mean of Steps 10 to 12

extended for group support as

> C = C(M) + (1 - C(M)) * omega * Gcap,  omega = 0.75

with Gcap the mean own-capacity C(M) across living members, so that a member whose own
maintenance has collapsed still retains a fraction of capacity as long as the group around them
has not. The multiplier that actually enters each step's growth is not C but

> Cm(i) = 1 - w(i) * (1 - C),   w(i) = 0.05 + (i - 1) * (1 - 0.05) / 11

so the gate phases in linearly by step index, from 0.05 at Step One to 1.00 at Step Twelve. At
Step One the gate is almost inoperative whatever C is; at Step Twelve it binds fully. Chapter
Twelve states the same two lines, because each chapter's Machinery is meant to be readable
without the other.

**Retired frozen-environment diagnostic**, capability 1.0, obsolete resource vector and Gcap = 0.245. These values reproduce the prior chapter but are not current baseline outputs:

| quantity | healthy | collapsed |
|---|---|---|
| maintenance (mean of Steps 10 to 12) | 0.3205 | 0.0003 |
| mean of all twelve steps | 0.5003 | 0.2698 |
| Step 1 | 0.766 | 0.758 |
| Step 4 | 0.559 | 0.441 |
| Step 8 | 0.459 | 0.056 |
| Step 12 | 0.250 | 0.000 |

**Retired separatrix.** Under those obsolete constants only, scaling the high state uniformly gives recovery for f >= 0.742 and collapse below; maintenance at the boundary is 0.2378.

**Retired diagnostic's fragility in the decay rate**, baseline 0.06:

| delta0 | change | healthy state | bistable |
|---|---|---|---|
| 0.0480 | -20% | 0.5569 | yes |
| 0.0570 | -5% | 0.3987 | yes |
| 0.0600 | 0 | 0.3205 | yes |
| 0.0612 | +2% | 0.2718 | yes |
| 0.0617 | +2.79% | collapses | no |
| 0.0630 | +5% | 0.0001 | no |

The failure is asymmetric within that diagnostic. It is retained to document how the conditional mechanism behaved, not as a statement about the current endpoint environment.

**Retired hysteresis diagnostic.** Total withdrawal of its frozen group support for D weeks, then restoration and five years:

| D | maintenance at end of absence | after five years back |
|---|---|---|
| 8 | 0.2397 | 0.3205 |
| 11 | 0.2132 | 0.3204 |
| 12 | 0.2047 | 0.0003 |
| 26 | 0.1060 | 0.0003 |

Critical absence 11.50 weeks by bisection under the retired constants. This is not a current model threshold.

**Environment-matched test.** Each of 400 corrected full-adherence endpoints supplies its own resource vector and mean group capacity. A capability-one member is integrated from 0.95 and 0.02 on every Step with that environment held fixed. Seven of 400 environments produce a maintenance separation above 0.05. High-start maintenance has tenth, median and ninetieth percentiles approximately 0.0000000002, 0.0000000014 and 0.0000071; the low-start quantiles are the same to displayed precision. Mean resource supply is [1.000, 0.556, 0.191, 0.233, 0.191, 0.532, 0.520, 0.717] and mean group capacity is 0.0451. Code and raw environments are in `model/ch14_individual.py` and `research/ch14_individual.json`.

**Group simulation**, 400 seeds, thirty years, full Tradition adherence, decay rate swept from -30 to +50 per cent. Endpoint viability is 1.000, 1.000, 0.9925, 0.985, 0.980, 0.980, 0.9175 and 0.8675 across -30, -20, -10, 0, +5, +10, +30 and +50 per cent. Mean endpoint membership is 57.71, 47.47, 29.07, 17.80, 14.67, 13.52, 10.48 and 8.91, with 95 per cent half-widths from the cross-run standard error of 0.40, 1.37, 1.53, 0.88, 0.65, 0.52, 0.39 and 0.34. All-run mean maintenance is 0.2262, 0.1468, 0.0761, 0.0380, 0.0258, 0.0234, 0.0094 and 0.0062. The maintenance decline is monotone.

The group sweep is a sensitivity curve, not evidence for individual bistability. At +50 per cent, 2.75 per cent of groups close and 86.75 per cent remain viable; existence, viability and maintenance are separate outcomes.

### 3. Notes on sources

**The empirical warrant for the shape improved substantially after this chapter was drafted, and the chapter has been revised rather than left standing.** It originally rested on Hufford and colleagues (2003) alone, read via abstract. Fatimah, Hunter and Bornovalova (2025) is now the primary support and is read in full from the author manuscript.

**On Fatimah and colleagues.** Read at source. Their double-well potential model is fitted to timeline followback data from N = 139 adults leaving residential treatment, using the `dynr` package; code is deposited at osf.io/tkg9s. What I take from it: that a two-well landscape fits and validates; that their separation energy is asymmetric between the two directions, which is this chapter's hysteresis; and that steepness and relapse risk vary significantly between people and are predictable from baseline characteristics, which is the empirical counterpart of the heterogeneity this chapter assumes. **What I do not take from it:** support for the mechanism. They fit a landscape to behaviour; I derive one from a claim about maintenance gating its own recovery. A different mechanism would fit their data as well. Nor is their outcome my outcome: they model substance use, this model runs on step practice, and nobody has fitted a double well to step practice.

**A finding of theirs that qualifies this chapter.** Non-use was the predominant stable state across their sample. The two wells are not of equal depth for most people, and the chapter should not be read as saying they are.

**Hufford and colleagues (2003) reaches me through its published abstract and through a later paper's citation of it, not through the full text.** It is now corroborating rather than load-bearing, and the 2025 paper cites it as one of the calls for exactly this kind of model, which at least confirms the chain is real. What the abstract states is that two preliminary studies, fifty-one inpatients and forty-three outpatients followed for six months, indicate a cusp catastrophe model has more predictive utility than traditional linear models. **The comparison statistics themselves I have not seen.** An earlier draft of the chapter plan said the model outperformed "linear and logistic" specifications; the abstract says linear, and I have removed the stronger word rather than keep a claim I cannot support.

**Witkiewitz and Marlatt (2007) is also read via abstract only.** It is cited here for the general argument that post-treatment drinking is nonlinear, not for any specific result. A passage of theirs quoted in Hunter-Reel and colleagues (2009) describes relapse as a feedback loop running until a steady state of drinking or not drinking is reached, which is bistability in their own words; I have that quotation at two removes and have not used it in the main text for that reason.

**The Hill function is borrowed, not fitted.** Its use for switch-like behaviour is standard, and n = 3 gives a moderately sharp switch. Neither n nor k was chosen from data. Sensitivity of the retired frozen-environment diagnostic does not establish bistability in the corrected baseline environment.

**No part of this chapter has been tested against a person.** There is no longitudinal dataset of step practice with the resolution this would need, which is the same gap Chapter Thirteen ran into from the other direction.

**The numbers are computed, not cited.** The corrected environment test is generated by `model/ch14_individual.py`; the group sweep by `model/ch14_sweep.py`. The retired constants remain displayed so the superseded calculation can be reproduced and distinguished from the release result.

### 4. References

**Read in full:**

Fatimah, H. M. D. Hunter, and M. A. Bornovalova (2025). "Modeling the Dynamics of Addiction Relapse Via the Double-Well Potential System." *Journal of Psychopathology and Clinical Science* 134(1): 69-80. doi:10.1037/abn0000960. Read from the author manuscript; saved as `research/incorporated/Fatimah_2025/`. The two stable equilibria, the separation energy in each direction, the person-specific steepness and tilt, the between-subject variance in steepness and relapse risk, and the criterion validity against life satisfaction and criminal behaviour beyond proportion of days used and time to first use.

Golub, B. and M. O. Jackson (2010). "Naive Learning in Social Networks and the Wisdom of Crowds." *American Economic Journal: Microeconomics* 2(1): 112-149. Used here only for the contrast drawn at the end of the chapter, between influence failure and aggregation blindness.

Cunha, F. J. J. Heckman, and S. M. Schennach (2010). "Estimating the Technology of Cognitive and Noncognitive Skill Formation." *Econometrica* 78(3): 883-931. The stage technology into which maintenance enters. The depreciation structure is not theirs, since their technology carries a stock forward without a separate decay term; it is Ben-Porath's, below.

**Cited at a remove:**

Hufford, M. R. K. Witkiewitz, A. L. Shields, S. Kodya, and J. C. Caruso (2003). "Relapse as a Nonlinear Dynamic System: Application to Patients with Alcohol Use Disorders." *Journal of Abnormal Psychology* 112(2): 219-227. Read via abstract; full text not obtained.

Witkiewitz, K. and G. A. Marlatt (2007). "Modeling the Complexity of Post-Treatment Drinking: It's a Rocky Road to Relapse." *Clinical Psychology Review* 27(6): 724-738. Read via abstract; full text not obtained.

Hunter-Reel, D. B. McCrady, and E. Hildebrandt (2009). "Emphasizing Interpersonal Factors: An Extension of the Witkiewitz and Marlatt Relapse Model." *Addiction* 104(8): 1281-1290. The source of the Witkiewitz and Marlatt quotation described in the notes above.

Ben-Porath, Y. (1967). "The Production of Human Capital and the Life Cycle of Earnings." *Journal of Political Economy* 75(4): 352-365. The ancestry of the depreciation structure, described in Chapter Twelve rather than here.

**Internal, and reproducible from this repository:**

`model/ch14_individual.py` and `research/ch14_individual.json` for the 400 corrected endpoint environments and frozen-member tests. `model/ch14_sweep.py` and `research/ch14_sweep.json` for the corrected group curve. The companion notebook reports these caches and labels the older fixed-environment calculations as retired.

**What was not read:**

Hufford et al. (2003), the earlier nonlinear-dynamics treatment of relapse, which remains unobtained and which would say how much better the double-well fit does than the alternatives. The chapter now rests on Fatimah, Hunter and Bornovalova (2025), read in full, so this is corroboration rather than foundation. Also unread: the wider clinical literature on relapse trajectories, which this chapter engages only through those two papers and which may well contain results that bear on the bistability claim in either direction.

# Chapter Fifteen: Helping Is Not the Reward

The twelfth step is the one that sounds like a graduation.

Eleven steps of difficult interior work, and then, having had a spiritual awakening as the result of these steps, you carry the message to other alcoholics. It reads like an afterword. You get well, and then, because you are well and because you are grateful, you go back and help somebody else. Service as the thing you do once the work is finished.

Almost everyone outside the rooms reads it that way, and a fair number of people inside them do too. It is the natural reading and I think it is exactly backwards.

The strongest clinical clue discussed in this chapter says so, and it is not mine. The paper has now been obtained and read in full, so what follows is taken from it rather than from its abstract.

---

In 2004 Maria Pagano and three colleagues went back to the data from Project MATCH, one of the largest clinical trials ever run in alcohol research, and asked a question the trial had not been designed to answer. Among people who had been through three months of treatment, did it matter whether they had helped other alcoholics?

It mattered a great deal. Of those who had done such helping, forty per cent avoided drinking entirely across the following twelve months. Of those who had not, twenty-two per cent did. Roughly twice as likely to stay sober, and the effect held independently of how many meetings a person attended, which is the comparison that matters, because otherwise you are only measuring who showed up.

Two things about that finding deserve stating before anything else is built on it.

The first is that it is observational. Project MATCH randomised people to treatments, not to helping. Nobody assigned half the participants to sponsor somebody. So the comparison is between people who chose to help and people who did not, and those are different people in ways that plausibly bear on staying sober. Somebody well enough to sponsor is, by that fact, somebody already doing better. The finding cannot rule that out, and Pagano and her colleagues do not claim it can.

The second is that the idea was not new even in 1965, when Frank Riessman gave it a name. He called it the helper therapy principle: that in a relationship where one person helps another with a shared condition, the helper is often the one who benefits most. Riessman was writing about self-help groups generally, and he was describing something practitioners had noticed for decades without writing it down.

So this chapter is not reporting a discovery. The observation belongs to the rooms, the name belongs to Riessman, and the best evidence belongs to Pagano. What the model contributes is smaller and more specific: an account of the mechanism by which it could be true, and a prediction about when it would stop being true.

---

Here is the mechanism, and it is almost embarrassingly simple.

In the model, service is not a separate activity bolted onto recovery. It is a step like the others, with a practice level that rises when worked and falls when not, and it feeds the same maintenance capacity that Chapter Fourteen showed holds everything else up. Steps Ten, Eleven and Twelve are averaged into that capacity. Take the twelfth away and you have removed a third of the thing keeping the other nine off the floor.

You can test that inside the model by simply switching it off: set the growth rate of the twelfth step to zero, so that members can never build any service practice at all, change nothing else, and run four hundred groups for thirty years.

The corrected result is smaller than the earlier draft reported but still clear on membership. Mean endpoint size falls by 5.33 members, from 17.80 to 12.48, a paired reduction of 30 per cent with a 95 per cent interval of 4.44 to 6.21 members. Average practice falls by 0.015 and maintenance capacity by 0.0135.

The more ambitious cross-step claim does not survive correction. Step Nine is lower by 0.0055, about twelve per cent of its baseline value, but its paired 95 per cent interval runs from a decrease of 0.0125 to an increase of 0.0015. Making amends has no direct dependence on carrying the message, and this experiment is too imprecise to say that disabling Step Twelve degrades it specifically. What is resolved is the aggregate maintenance change: 0.0135 with a paired interval of 0.0079 to 0.0192.

That is weaker than the result I wanted. Inside this model Step Twelve is load-bearing for membership and the maintenance aggregate. The evidence does not isolate damage to a particular Step with no direct connection to it.

And notice what does *not* happen within the thirty-year experiment. The same 394 of 400 runs finish endpoint-viable in the baseline and with Step Twelve disabled. That is a finite-horizon result, not proof that a group with no service practice persists indefinitely. Within the modeled horizon it looks smaller without changing the estimated viability fraction.

---

Now the part that connects this chapter to the rest of the book, and it is the reason the twelfth step is different in kind from the other eleven.

Everything else on the list you can do alone or with one other person. You can take an inventory in a room by yourself. You can make amends to somebody who wants nothing to do with the programme. But you cannot carry the message to a person who is not there.

The twelfth step requires a recipient, and a recipient is not something a person can supply for themselves. The model approximates that opportunity with low-practice members already in the population; it does not establish that they are new arrivals.

The model treats this as a resource like any other, but its name needs care. It
stores no tenure, sponsorship or matching. The numerator counts members at or
below the low-practice threshold and the denominator counts members above the
high-practice threshold. The ratio is therefore **opportunity per potential
helper**, not newcomer supply or helper capacity. Forty low-practice members and
two high-practice members produce a high value; two and forty produce a low one.
The formula does not model overload, match quality or whether any pair actually
works together.

You can check whether this capacity is doing real work by forcing only it to one
while holding the consumption matrix, beta and the realized group process fixed.
Across 400 paired seeds, final membership rises by 1.03 members, but the 95 per
cent interval runs from -0.26 to 2.31. The clean ablation is unresolved. The older
8.7 per cent claim came from deleting a consumption cell, renormalizing the rest
of Step Twelve and changing beta at the same time; it could not identify the
recipient mechanism.

That is the recipient-opportunity hypothesis, and it is more limited than the
earlier wording. A group with few low-practice members per high-practice member
has less modeled opportunity for Step Twelve. Whether real helpers are short of
recipients, overloaded by them or matched at all is an empirical question the
model cannot answer.

---

Which returns me to where the book started, and to the difference between the two inflow channels.

Chapters One and Four distinguished attraction, arrivals generated by members' practice, from referrals sent by courts, hospitals and treatment programmes regardless of what the group does. One repeatedly supported within-model ordering is that referral loss and attraction loss have different consequences. The corrected analysis reports closure, endpoint viability and membership separately and does not turn finite sensitivity ranges into a universal claim.

This chapter says why, and the reason is not the obvious one. It is not simply that referrals are more numerous. It is that referrals are the channel that does not depend on the group's own health. Attraction is generated by members' twelfth-step practice, so a group whose practice is slipping attracts fewer people, which supplies fewer recipients, which degrades practice further. That loop closes on itself. Referral does not run through the loop at all. It is the term that keeps arriving when the group has stopped deserving anybody.

The Washingtonians, as Chapter Four set out, had only the first channel. Everything depended on the movement continuing to be impressive.

---

A last thing, and it is a caution about how to read all of this.

The model says the twelfth step is load-bearing. Pagano's data says helpers stayed sober at twice the rate of non-helpers. Neither of those is advice, and the distance between them and advice is larger than it looks.

Pagano's finding is observational, so it cannot tell you that a struggling person would do better if they started sponsoring. It is at least as consistent with the reverse, that people who are already doing better take on sponsees. Establishing the direction would take an experiment nobody has run, and possibly nobody should. And the model cannot help, because the model is not evidence about people. It is a demonstration that a certain set of assumptions has a certain consequence.

What the two together do support is narrower and still worth having. If you are describing what a group is for, the account in which service is the reward for recovery is probably the wrong shape. Service looks more like part of the mechanism, and a group with nobody to hand to its established members is missing something structural, not something decorative. That is a claim about institutions. It is not a claim about you, and nothing here licenses anyone to tell a person in difficulty that they would be well if only they helped more.

---

## The Machinery

### 1. What the model says

The twelfth step consumes seven of the eight group resources and has the maximum
group-dependence coefficient, 1.00, tied with Step One. It is the only Step that
consumes the **recipient opportunity** proxy, a ratio computed from low- and
high-practice member counts.

Three results, all at 400 seeds, thirty-year horizon, full Tradition adherence.

**Service is load-bearing rather than terminal inside the model.** Setting the twelfth step's growth rate to zero costs 5.33 members [4.44, 6.21], or 30 per cent of baseline membership, and lowers maintenance capacity by 0.0135 [0.0079, 0.0192]. Average practice falls by 0.0150, with paired interval [0.0076, 0.0223].

**Losing it does not change endpoint viability in these runs.** In each condition 394 of 400 runs finish above five members. The result is a smaller group over thirty modeled years; it is not proof of permanence or survival forever.

**The clean recipient override is unresolved.** Forcing recipient capacity to one
raises final membership by 1.03 members relative to baseline, with paired 95 per
cent interval [-0.26, 2.31]. It changes no matrix weight or beta. The former 8.7
per cent estimate came from a compound structural change and is retired.

### 2. The technical version

**The recipient resource.** Supply is

> R(recipient) = sat(n_low / max(n_high, 1), k_recip) * q(recipient),  sat(c, k) = c / (c + k)

with k_recip = 2.0, n_low the members at or below the established-practice
threshold and n_high those above the experienced-practice threshold. Half capacity
is reached at two low-practice members per high-practice member; nine tenths needs
eighteen. Lower helper count increases the ratio rather than reducing it, so this
is opportunity per potential helper and not helper capacity.

Four traditions govern its supply, with column-normalised weights: single purpose 0.375, open membership 0.333, attraction 0.250, unity 0.042.

Step 12 is the only consumer: S[12, recipient] = 1.0, which is 0.417 of that step's normalised resource bundle.

**Results**, 400 paired seeds each. Endpoint viability is a fraction; means show 95 per cent half-widths:

| Configuration | Endpoint viable | Mean N | Practice | Step 1 | Step 9 | Step 12 | Maintenance |
|------------------------|------------|-------------|---------------|-------|-------|--------|--------------|
| Baseline | 0.985 | 17.80 ± 0.88 | 0.2198 ± 0.0054 | 0.7135 | 0.0471 | 0.0347 | 0.0380 |
| Twelfth step disabled | 0.985 | 12.48 ± 0.35 | 0.2049 ± 0.0055 | 0.7046 | 0.0416 | 0.0026 | 0.0245 |
| Recipient capacity forced to one | 0.9875 | 18.83 ± 1.05 | 0.2198 ± 0.0054 | 0.7136 | 0.0458 | 0.0371 | 0.0382 |

Because conditions use common random streams, uncertainty is computed on paired differences. Baseline minus disabled membership is 5.33 [4.44, 6.21]. Forced-capacity minus baseline membership is 1.03 [-0.26, 2.31] and is unresolved. The Step Nine change under disabled service is likewise unresolved; the membership and maintenance effects are not.

**Sensitivity.** The expanded release suite varies `k_recip` at four distances in the multi-level OAT design and includes it in the global, tiered and Morris screens. A weak effect on one endpoint, especially referral-starved viability, would not establish that the recipient mechanism is structural or untuned. The clean recipient override is the direct mechanism comparison; the sensitivity designs describe dependence on its authored parameters.

**What is not claimed.** The 30 per cent figure is a within-model quantity and inherits every caveat in the appendix. A lower endpoint size in this authored system is not evidence that helping causes recovery in people, and the specific cross-Step propagation claim is unresolved.

### 3. Notes on sources

**The Pagano result is now read in full, and the two percentages check out.** The paper is Pagano, Friend, Tonigan and Stout (2004) in the *Journal of Studies on Alcohol*. Earlier drafts of this chapter took the forty and twenty-two per cent from a 2011 Case Western Reserve University news release and said so, because a press release is a weak place to take two numbers from and the full text had not been obtained. It has been. The paper's own results section gives the same two figures: among those helping other alcoholics 40 per cent avoided taking a drink in the year after treatment, and among those not helping, 22 per cent. The independence from meeting attendance is the paper's own framing, established by proportional-hazards regression controlling for the number of AA meetings attended, and the difference appears in both study arms.

**What reading it added is a limitation the press release did not carry.** The authors' first stated limitation is that only 8 per cent of the sample were coded as helping, on a measure they describe as crude, and they note the rate would probably be higher under a more refined instrument. So the contrast is between a small helping group and a large non-helping one, which widens the interval around any effect and makes the selection worry above harder to dismiss rather than easier. The sample is the Project MATCH cohort, and the outcome is individual drinking after formal treatment, which is a different object from anything this model simulates.

**The observational limitation is mine to state, not theirs to answer.** Project MATCH randomised treatment, not helping. Nothing in the design supports a causal reading, and the direction of effect is genuinely open.

**Riessman (1965) is cited for the name and the idea, not read at source.** It is behind a subscription at *Social Work*. The principle as stated here, that the helper in a shared-condition relationship often benefits most, is not in dispute and is reported in many places, but I have not read the original article.

**The recipient resource is my construction.** No source proposes measuring opportunity to help as low-practice members per high-practice potential helper. The ratio form follows from asking what a person needs in order to do twelfth-step work, and the saturation form is borrowed from Iannaccone's treatment of participatory goods, but the object itself is an invention of this model and should be read as such. The nearest thing in print is Lembke's application of Iannaccone to AA, which counts as a free-rider the sober member who never works the steps, because such members do not sponsor and so shrink the pool of people who can. That is the same resource described from the helper's side and without a measure, so it supports the idea rather than the ratio.

**The numbers are computed, not cited**, and are asserted against these printed values in the companion notebook.

### 4. References

**Read in full:**

Iannaccone, L. R. (1992). "Sacrifice and Stigma: Reducing Free-Riding in Cults, Communes, and Other Collectives." *Journal of Political Economy* 100(2): 271-291. The saturation form for goods produced by participation.

Cunha, F. J. J. Heckman, and S. M. Schennach (2010). "Estimating the Technology of Cognitive and Noncognitive Skill Formation." *Econometrica* 78(3): 883-931. The stage technology through which the degradation propagates.

Lembke, A. (n.d.). "Sacrifice, stigma, and free-riding in Alcoholics Anonymous (AA): A new perspective on behavior change in self-help organizations for addiction." Working paper, Association for the Study of Religion, Economics and Culture. **Read in full** on 13 September 2026; stored in `research/incorporated/Lembke_nd/`. The sober member who does not sponsor as a free-rider who shrinks the pool of possible sponsors. The paper is theoretical, and its two cases are clinical vignettes.

**Cited at a remove:**

Pagano, M. E., K. B. Friend, J. S. Tonigan, and R. L. Stout (2004). "Helping Other Alcoholics in Alcoholics Anonymous and Drinking Outcomes: Findings from Project MATCH." *Journal of Studies on Alcohol* 65(6): 766-773. **Read in full**; the NIH author manuscript, PMCID PMC3008319, obtained 10 August 2026 and stored with its citation and metadata in `research/incorporated/Pagano_2004/`. Source for the forty and twenty-two per cent figures, which earlier drafts took from a 2011 news release and which the paper's own results section confirms, for the independence from meeting attendance, and for the eight per cent helping rate the authors give as their first limitation. **Note the copy**: this is the author manuscript, so its pagination is not the journal's and a page-specific citation would need the published version.

Riessman, F. (1965). "The 'Helper' Therapy Principle." *Social Work* 10(2): 27-32. Cited for the naming of the principle; not read at source.

**Internal, and reproducible from this repository:**

The three configurations and the recipient saturation curve. Code and assertions in `model/book-calculations.ipynb`, raw runs in `research/ch15_service.json`.

**What was not read:**

Pagano, M. E. and colleagues (2009). The follow-up analysis on sustained helping and depression, also from Project MATCH, referred to in the same news release.

Zemore, S. E. and colleagues on giving and receiving help in recovery settings, which appears to be the nearest contemporary literature and which I have not surveyed.


\clearpage
\thispagestyle{empty}
\vspace*{0.32\textheight}
\begin{center}
{\Large\bfseries Part Four}\\[0.6em]
{\large\itshape Where the Two Halves Meet}
\end{center}
\clearpage

# Chapter Sixteen: The Pairing That Isn't

There are twelve Steps and there are twelve Traditions, and for more than seventy years they have been printed on facing pages.

So the thought arrives on its own, usually within a week of somebody first seeing the two lists together. If there are twelve of each, perhaps they go together. Step One and Tradition One. Step Two and Tradition Two. A programme for the person and a matching programme for the room, aligned all the way down.

It is not a stupid thought. Numbered lists of equal length invite pairing, the two documents share an author and a vocabulary, and there are places where the correspondence looks real. Step Twelve is about carrying the message and Tradition Five is about carrying the message, which is not a pairing but is close enough to keep the idea alive.

For a long time this chapter said that AA's own literature gestures at the parallel without asserting it, and admitted in its notes that it could not say how strongly, because the literature in question was copyright and unread. It has now been read, and the answer is that it does not gesture at all.

The book to check is the obvious one. *Twelve Steps and Twelve Traditions*, published in 1953, is the only work that treats both lists at length, one chapter each, bound together, by the same author. If the pairing were intended by anyone it would show up there.

Across the twelve Tradition chapters, not one refers to the Step of its own number. Not once in twelve. Across the twelve Step chapters, the word *Tradition* does not appear at all, in any of them, at any point. The single indexed cross-reference in the whole book runs the wrong way for the conjecture: the chapter on Tradition Eight mentions the Twelfth Step, and mentions it to explain that a paid worker's job is not to do Twelfth Step work but to make Twelfth Step work possible.

That is a stronger result than the chapter previously claimed and it costs nothing to obtain. The man who wrote both lists wrote a book about both lists and never once connected them by number.

This chapter is a test of that thought, and the test comes out negative on every count. But the count is not twelve, whatever the summary says, and getting from twelve to the number it actually is turns out to be the most useful thing in the chapter.

---

The test is worth something only because of when the two matrices were built.

Part Three has already described the first of them. Each Step consumes things a group produces: a way in, someone to identify with, the demonstration that recovery happens, confidentiality, counsel, somebody to help, continuity, and the pressure of other people's expectations. Eight resources. Twelve Steps. That gives a table of what each Step needs and how much, and Part Three spent a chapter on it without once mentioning the Traditions.

The second matrix asks a different question: which Traditions govern the supply of each of those same eight things. Open membership governs whether there is a way in. Anonymity governs confidentiality. Group conscience governs counsel. Singleness of purpose governs whether there is somebody to help, because a room whose newcomers are not alcoholics supplies that resource to nobody. Unity governs continuity, because a group that splits stops being the same room next week.

Neither table has a column for Steps and Traditions together. Nothing in either one asks what serves what. The coupling is what you get when you multiply them, and the multiplication is the whole method: for each Step, add up what it consumes weighted by which Tradition governs the supply, and the largest number in that Step's row names its principal supplier.

That is a derivation rather than a fit. It could have come out the other way, and if it had, this chapter would have been a short one saying that the numbering was right after all.

---

It does not come out the other way. No Step's principal supplier is its own index-mate. Twelve for twelve, or rather zero for twelve, depending on which way you like to count.

And now the deflation, which I would rather deliver myself than have a reader find.

Five of those twelve counts are arithmetic, not evidence.

Five Traditions govern no resource that any Step consumes. They are the fourth, sixth, seventh, ninth and tenth: group autonomy, the refusal to endorse, the refusal of outside money, the refusal to organise, and the refusal to hold an opinion. That is a finding, and it is the subject of another chapter in this part. But once it is in hand, Steps Four, Six, Seven, Nine and Ten cannot possibly be served by their index-mates, because their index-mates govern nothing at all. Their entries are exactly zero. Index-pairing fails for those five the way a horse fails to win a race it did not enter.

So the twelve counts are not twelve independent tests. They are seven tests and one previously established structural fact wearing five hats. Every robustness figure in the rest of this chapter is carried entirely by the seven, which I have checked directly: at every level of disagreement I tried, the proportion of draws in which index-pairing fails on all twelve is identical, to the last draw, to the proportion in which it fails on the seven that could have gone either way. The five contribute nothing because they cannot.

The honest headline, then, is that index-pairing fails on all twelve counts, of which five follow from the two-tier split and seven are the actual result. I have written "all twelve" elsewhere in this book without that qualification, and it should be read with it.

That is where this chapter stood when it was drafted, and Chapter Eighteen has since improved on it, so the paragraph above is not quite the last word. What is arithmetic about those five counts is that *multiplying* the matrix entries cannot reach them. There is another test, which asks instead how strongly a Tradition would have to govern before index-pairing held, and that test does reach them and finds they fail by margins comparable to the other seven. Chapter Eighteen runs it, because it is really a test of the two-tier split rather than of index-pairing. So the deflation stands as a statement about *this chapter's designs* and is repaired as a statement about the claim.

---

Here is how the seven fail, because they do not all fail the same way.

Step One, admitting powerlessness, is the near miss and the only one. Its principal supplier is open membership, at 1.22, and its index-mate unity comes second at 0.99. A reader who thought I had overweighted the admission resource by a fifth could flip it. That is one count of seven where the result is close enough to argue about, and I would not want the chapter to rest on it.

That guess turns out to be measurable, and it is right. Delete each of the eight resources in turn, then merge each pair, then delete each pair, which is sixty-four different resource lists, and ask which Steps get their index-mates back. Two do. Step One in fifteen of the sixty-four, and Step Two in one. The other five non-trivial counts never break under any of it, and every one of the fifteen Step One failures involves removing or merging the admission resource, which is precisely the thing that gives the open door its lead there. So the chapter's weakest count is weak in exactly the way and for exactly the reason I guessed, and the other six are not.

The other six are not close. Step Two, coming to believe, is supplied principally by attraction rather than by group conscience, and its index-mate ranks seventh of twelve. Step Three's index-mate ranks seventh, with an entry of 0.01. Step Eight's ranks fourth. Step Eleven's ranks fourth. Step Nine's index-mate is one of the five that govern nothing.

Then there are the two that make the point vivid, and they are inversions rather than misses.

Step Five is telling another human being the exact nature of one's wrongs. It is served principally by Tradition Twelve, anonymity, at 1.08, with its own index-mate fifth. The route is confidentiality. Step Five consumes confidentiality more heavily than any other Step consumes any other resource, and anonymity is what supplies it. A man does not describe the worst thing he has done to a room that might repeat it.

Step Twelve is carrying the message to other alcoholics. It is served principally by Tradition Five, singleness of purpose, at 1.25, with its own index-mate sixth. The route is the recipient resource. A twelfth-step call needs somebody to make it to, and singleness of purpose is what keeps a supply of newcomers who are actually alcoholics.

The two most quotable pairings in the programme, the ones anyone would guess at, are not merely wrong. They are swapped.

---

The chapter would be finished there if I were willing to report one robustness number, and I am not, because a single percentage at a level I chose is exactly the kind of figure this book has been wrong about before.

Take the two matrices and multiply every entry by a random factor, so that a reader who would have written 0.7 where I wrote 0.9 is represented in the draws. Do that two thousand times at each of four levels of disagreement, and then do something harder: throw the magnitudes away entirely, keep only which cells are empty, and fill every non-empty cell with a fresh random number.

At plus or minus fifteen per cent, index-pairing fails on all counts in 98.8 per cent of draws, and the Step Twelve inversion holds in 89.7. At thirty per cent the figures are 85.5 and 67.3. At fifty per cent, 72.5 and 52.9. At seventy-five per cent, 65.2 and 43.8. Under structural randomisation, where only the sparsity survives, index-pairing fails on all counts in 40.6 per cent of draws, which is less often than it holds, and the Step Five inversion survives in 17.5 per cent.

Read the whole curve rather than any row of it. What it says is that the result is robust to a reader who disagrees with me moderately about the magnitudes and is not robust to a reader who thinks the matrices are essentially arbitrary. That is a real claim and a bounded one. It is also a different kind of claim from the ones in Parts One and Three, which survive the structural test at a hundred per cent and may therefore be defended as resting on structure rather than on my judgement. Part Four cannot borrow that defence. It rests on the magnitudes, the magnitudes are judgement, and the argument for them is the derivation itself, chapter by chapter, and not a robustness statistic.

The unevenness inside those figures matters as much as the levels. The Step Five inversion holds at 99.5 per cent at thirty per cent jitter, and the Step Twelve inversion at only 67.3. The reason is visible in the numbers: for Step Twelve, open membership is a close second at 1.10 against singleness of purpose at 1.25, because both govern the recipient resource, and a modest perturbation flips them. So the sentence about Step Five is firm and the sentence about Step Twelve is a two-in-three proposition, and I would rather say that than average them.

---

There is a second fragility, separate from the first, and it cuts in a direction that helps rather than hurts.

The identity of a Step's principal supplier is often decided by a hair. Step Four's top two, group conscience and unity, are separated by less than a hundredth. Step Six's by one hundredth. Step Three's and Step Seven's by four. Change my numbers slightly and the winner changes for four of the twelve Steps.

But the *loser* does not change, because the index-mate is not in contention. For those four Steps, the index-mate's entry is 0.00, 0.00, 0.01 and 0.00. The argmax is a poor instrument for telling you which Tradition serves a Step, and a good one for telling you that it is not the one with the matching number, because the gap between first place and the index-mate is enormous in exactly the cases where the gap between first and second is not.

That distinction is the difference between the claim this chapter makes and a claim it does not make. It does not say that Step Four is governed by group conscience. It says that Step Four is not governed by Tradition Four, and it says that with a margin of the whole distribution.

---

One more number, offered here and taken up properly later in this part.

Add each Tradition's column and you get how much of the total demand across all twelve Steps that Tradition is carrying. Unity comes first at 6.52. Group conscience is second at 3.89 and singleness of purpose third at 3.88, close enough to be a tie. Nothing else exceeds 2.7.

Unity is carrying about two-thirds again as much as its nearest rival, and it does so without being the principal supplier of very much. It is the second-place finisher almost everywhere. That is a different kind of importance from the one this chapter has been measuring, and it deserves its own treatment.

---

The obvious objection to this chapter is that it is numerology.

It computes a twelve-by-twelve coupling between two lists of twelve things and reports patterns in it, and that is a shape which has embarrassed better arguments than this one. I take the objection seriously enough to state the defence precisely rather than confidently.

The defence is not that the numbers are objective. They are not; I chose them. It is that both matrices were built to answer other questions, months before anyone multiplied them, and that the test could have failed. If the coupling had put Tradition Five under Step Five and Tradition Twelve under Step Twelve, the numbering would have been vindicated and this chapter would have said so. It did not, and it did not in a way that inverts the two pairings a person would have guessed at first.

What I cannot offer is an independent check. There is no second person who built these matrices, and there is no dataset that would adjudicate them. The strongest available test is the one this chapter has already run and failed to pass cleanly: strip the magnitudes and keep only the pattern of empty cells, and the result goes away. A reader who wants to reject Part Four has a principled place to stand, and it is only fair to point at it.

---

## The Machinery

### 1. What the model says

The coupling is not a separate construction. It is the product of the two matrices the simulation already runs on, and it is used nowhere in the simulation itself.

The consumption matrix S is twelve Steps by eight resources, and Part Three derives it. The governance matrix G is twelve Traditions by the same eight resources, and it is the object every Tradition-related result in the book depends on. The coupling is

> B = S G'

so that B[i][j] is the total demand Step *i* places on resources that Tradition *j* governs. The principal supplier of Step *i* is argmax over *j* of B[i][j]. The load on Tradition *j* is the column sum of B.

Two things follow that are worth separating. The first is that B is a *derived* object: no entry of it was chosen. The second is that being derived does not make it robust, because it inherits every judgement in S and G. Those are different properties and this chapter needed both stated.

### 2. The technical version

**These are exact calculations, not simulations.** B is a matrix product of two fixed matrices; the principal suppliers and the loads below are deterministic and carry no sampling error. The robustness figures that follow *are* Monte Carlo, over 2,000 random draws each, and are reported with 95 per cent Wilson intervals.

Principal supplier of each Step, with its own index-mate for comparison. All values are exact.

| Step | Principal | Value | Runner-up | Value | Index-mate | Value | Its rank |
|---|---|---|---|---|---|---|---|
| 1 admit | T3 | 1.22 | T1 | 0.99 | T1 | 0.99 | 2 |
| 2 believe | T11 | 0.82 | T5 | 0.72 | T2 | 0.13 | 7 |
| 3 decide | T2 | 0.31 | T1 | 0.27 | T3 | 0.01 | 7 |
| 4 inventory | T2 | 0.35 | T1 | 0.35 | T4 | 0.00 | 8 |
| 5 tell someone | T12 | 1.08 | T1 | 0.65 | T5 | 0.12 | 5 |
| 6 willing | T1 | 0.25 | T2 | 0.24 | T6 | 0.00 | 9 |
| 7 ask | T1 | 0.17 | T2 | 0.13 | T7 | 0.00 | 10 |
| 8 list harms | T2 | 0.43 | T1 | 0.29 | T8 | 0.07 | 4 |
| 9 amends | T2 | 0.90 | T1 | 0.48 | T9 | 0.00 | 11 |
| 10 daily | T1 | 0.94 | T2 | 0.43 | T10 | 0.00 | 12 |
| 11 connect | T1 | 0.47 | T2 | 0.21 | T11 | 0.11 | 4 |
| 12 carry it | T5 | 1.25 | T3 | 1.10 | T12 | 0.12 | 6 |

Load per Tradition, exact: T1 6.52, T2 3.89, T5 3.88, T3 2.69, T11 2.69, T12 2.62, T8 1.11, and exactly zero for T4, T6, T7, T9 and T10.

**The trivial-count decomposition.** T4, T6, T7, T9 and T10 have identically zero rows in G, so Steps 4, 6, 7, 9 and 10 have index-mate entries of exactly zero and index-pairing cannot hold for them under any perturbation that preserves sparsity. Both perturbation designs below preserve sparsity, one by construction and one by definition. The consequence is checkable and I checked it: at every level, the proportion of draws in which index-pairing fails on all twelve equals the proportion in which it fails on the seven non-trivial Steps to the last draw. 98.75 and 98.75 at fifteen per cent, 85.50 and 85.50 at thirty, 72.45 and 72.45 at fifty, 65.15 and 65.15 at seventy-five, 40.60 and 40.60 structurally. The five trivial counts are not evidence and no design used here could have made them so.

**Design one, multiplicative jitter.** Every entry of S and every entry of G is multiplied by an independent uniform draw on [1-L, 1+L], for L in {0.15, 0.30, 0.50, 0.75}. 2,000 draws per level, seeded at 3. This represents a reader who disagrees with the magnitudes by up to L and agrees about which cells are empty.

**Design two, structural randomisation.** Every non-zero entry of S and G is replaced by an independent uniform draw on [0.05, 1.00]; zeros stay zero. 2,000 draws, seeded at 23. This represents a reader who accepts only the pattern of which Tradition touches which resource and rejects every magnitude I chose. It is the same test the survival claims of Parts One and Three pass at 100 per cent.

| Design | T1 most load-bearing | Index-pairing wrong on all counts | Step 5 to T12 | Step 12 to T5 |
|---|---|---|---|---|
| jitter ±15% | 100.0 [99.8, 100.0] | 98.8 [98.2, 99.2] | 100.0 [99.8, 100.0] | 89.7 [88.3, 91.0] |
| jitter ±30% | 100.0 [99.8, 100.0] | 85.5 [83.9, 87.0] | 99.5 [99.1, 99.7] | 67.3 [65.3, 69.4] |
| jitter ±50% | 98.0 [97.3, 98.5] | 72.5 [70.5, 74.4] | 88.7 [87.2, 90.0] | 52.9 [50.7, 55.1] |
| jitter ±75% | 86.8 [85.3, 88.3] | 65.2 [63.0, 67.2] | 71.5 [69.5, 73.4] | 43.8 [41.6, 45.9] |
| structural | 75.4 [73.5, 77.2] | 40.6 [38.5, 42.8] | 17.5 [15.9, 19.2] | 27.6 [25.7, 29.7] |

Intervals are Wilson at 95 per cent on n = 2,000. The two 100.0 entries are 2,000 of 2,000 and their intervals are one-sided in effect; they should be read as "not observed to fail", not as certainty.

**Why Step 12 is the weak row.** In the unperturbed coupling, Step 12's top two are T5 at 1.25 and T3 at 1.10, a margin of 0.15 on a value of 1.25. Both Traditions govern the recipient resource, T5 at 0.9 and T3 at 0.8, so a perturbation that moves them in opposite directions flips the winner. The margin, not the level, is what makes the row fragile.

**What no design here can test.** Neither perturbation can move a structural zero, so no figure in this chapter is evidence about the two-tier split. Neither can test whether a differently-minded person would place the zeros where I placed them. Those are the threats named in appendix A7.1 and neither is addressed here.

**The eight resources have since been tested and the result is in the main text.** Appendix A7.6 deletes each resource, merges each pair and deletes each pair, sixty-four variants in all, and finds that only Step 1 and Step 2 ever regain their index-mates, in fifteen and one variants respectively. That establishes the list is no *finer* than it needs to be. It cannot establish that the list is fine *enough*, because inventing a ninth resource requires a judgement about what it contains and cannot be done by rearranging the eight.

### 3. Notes on sources

**Everything in this chapter is computation on two matrices I built.** There is no external source and there is nothing to verify against. The matrices are printed in full in `model/aa_group_model.py` and every figure above is reproduced by section 11 of `model/book-calculations.ipynb`, with assertions against the printed values.

**A provenance note that belongs in the record.** The 85.5 per cent figure was carried in `research/PARAMETERS.md` for some time before it could be reproduced from the book's own repository; the code lived only in the working paper the book grew out of. It was ported into the notebook so that the claim stands on the book's own files, and the port is what produced the degradation curve and the structural test, neither of which existed before.

**The claim this chapter softens, and how far Chapter Eighteen unsoftens it.** The book's summary of its own three headline results says that index-pairing is wrong on all twelve counts. That is true, and under the designs run here it is not twelve independent counts, for the reason given in the main text. Chapter Eighteen then supplies a design that can reach the five and finds them failing by comparable margins, which restores most of what this chapter gave away. The settled wording, used in `README.md` and `BOOK-PLAN.md`, is that index-pairing fails on all twelve, that five of the twelve are invisible to multiplicative perturbation, and that a threshold test which can see them finds no difference worth the name.

**What would change my mind.** A second person building a governance matrix from the twelve Traditions, without seeing mine, and putting the zeros in different rows. That is not a computation and no amount of further perturbation substitutes for it. It is the reader pass named in `plans/PART-4-PLAN.md` section 5, and it remains outstanding.

### 4. References

**Read in full:**

Golub, B. and M. O. Jackson (2010). "Naive Learning in Social Networks and the Wisdom of Crowds." *American Economic Journal: Microeconomics* 2(1): 112-149. Not used for any result in this chapter; named because the governance matrix was built for Part Two's argument and not for this one, which is what makes the test here meaningful.

Alcoholics Anonymous World Services (1953). *Twelve Steps and Twelve Traditions*. Read in full 10 August 2026. All twenty-four chapters, for the cross-reference count in the main text. Copyright AAWS; held as a record with no document.

Rohr, R. (2011). *Breathing Under Water: Spirituality and the Twelve Steps*. Cincinnati: Franciscan Media. Read in full 10 August 2026. Cited for containing no discussion of the Traditions.

**Cited at a remove:**

Nothing.

**Internal, and reproducible from this repository:**

`model/aa_group_model.py`, matrices S and GOV. `model/book-calculations.ipynb`, sections 11 and 11b for every figure above, 17 for the resource-list test, and 11c for the threshold test that reaches the five counts this chapter's designs cannot. `appendix/APPENDIX.md`, sections A5.4 and A7.1, for the perturbation designs and for what they cannot reach. `plans/PART-4-PLAN.md` section 1, which records that this part's central claim was found to be non-structural after the plan had asserted the opposite.

The cross-reference count is not internal and not a simulation. It is a search of the twenty-four chapters, and anyone can repeat it in a few minutes from the files AAWS publishes free at aa.org. The method is stated in the main text so that it can be checked rather than believed: count, in each Tradition chapter, references to the Step of that chapter's own number, and count, in each Step chapter, occurrences of the word *Tradition*.

**What was not read:**

There is still no literature on the coupling between AA's Steps and its Traditions, because as far as I can find nobody has proposed one to be tested. I searched for a prior statement of the index-pairing conjecture strong enough to quote and did not find one, which is why the main text says the conjecture arrives on its own rather than attributing it. So this chapter refutes a thing people believe rather than a thing somebody published, and a reader is entitled to think that a weaker target.

**The previous version of this paragraph said something I have had to withdraw.** It said the AA literature gestures at the parallel, and that I could not judge how strongly because the literature was copyright and unacquired. Having read the one book that treats both lists, the honest statement is that it does not gesture at all, and I should not have characterised the contents of a source I had not opened. The conjecture appears to be entirely a reader's inference from the two lists having the same length, which makes it a weaker target than the old wording implied and a cleaner one.

What remains genuinely unread is the rest of the AA canon: the Twelve Concepts, the service manual, and seventy years of *Grapevine*. Any of those could contain an assertion of the pairing, and the claim here is about the 1953 book rather than about everything AA has ever printed.

# Chapter Seventeen: What a Tradition Carries

Chapter Sixteen read the coupling one row at a time and asked, of each Step, which Tradition supplies it. Read the same table one column at a time and a different question appears: how much is each Tradition carrying?

Add a Tradition's column and you get the total demand placed on everything it governs, summed across all twelve Steps. It is a crude measure and I want to say so before using it. It treats a unit of demand for confidentiality as interchangeable with a unit of demand for somebody to help, which is not obviously right. What it does capture is exposure: how much of the programme stops working if this Tradition stops working.

The answer is lopsided, and the shape of the lopsidedness is the chapter.

Unity carries 6.52. Group conscience carries 3.89 and singleness of purpose 3.88, which is a tie in everything but the third decimal. The open door and attraction carry 2.69 each, anonymity 2.62, non-professionalism 1.11. And five carry nothing at all, for the reasons Chapter Eighteen sets out.

So the most exposed Tradition in the programme is the first one, by a margin of two-thirds over its nearest rival.

---

The obvious objection arrives immediately, and it is correct.

Unity is not top because it is strong anywhere. It is top because it is everywhere.

Look at how often it actually wins. Unity is the principal supplier of four Steps. Group conscience is also the principal supplier of four. On that measure they are level. What separates them is second place: unity is the runner-up for six more Steps, so it sits in the top two for ten of the twelve, and group conscience for eight. And unity is the only Tradition in the set that governs all eight resources. Nothing else governs more than six.

That is a Tradition which supplies a little of almost everything and the most of not very much.

I think the objection is right and that it is the finding rather than a problem with it. Consider what the alternative would look like. A Tradition that carried a lot by governing one thing intensely would be a Tradition whose failure has a symptom: lose it, and one specific thing stops. Group conscience is close to that shape, taking sixty-nine per cent of its load from a single resource, counsel. Anonymity takes fifty-seven per cent from confidentiality. Attraction takes forty-nine per cent from the demonstration that recovery happens. Those are Traditions with a failure mode you could name.

Unity is not shaped like that, and the consequence is uncomfortable. A group losing its unity does not present with a specific symptom. Everything gets slightly worse at once, which is the hardest kind of decline to notice from inside and the reason Part Five treats it separately.

---

That is the flattering version. Here is the part that qualifies it.

Unity is not as diffuse as I have just made it sound. Twenty-nine per cent of its load comes from continuity, the group being the same room next week, and twenty-eight and a half from pressure, the expectations other people place on a member. Those two together are fifty-seven and a half per cent of the total. The remaining six resources supply the rest between them.

So unity is carrying two heavy things and six light ones, and its lead over the field depends on the two. Strip continuity and pressure out and unity falls to 2.77 and to third place, behind group conscience and singleness of purpose and still narrowly ahead of the open door. I first wrote that it falls to fourth, and the assertion I had put in the notebook for that sentence failed before anyone read it. The claim that unity is the most exposed Tradition is, on inspection, the claim that group continuity and social pressure are heavily demanded and that unity is what governs them.

Which is a much more specific claim than "unity is important", and it is the one a critic should attack.

---

A critic has, in a sense, already attacked it, and the attack is a hundred years old and comes from inside the fellowship's own historiography.

Ernest Kurtz, in a note to his fifth chapter, records that in some later AA literature the concept properly conveyed by the term *single-purposed* was obfuscated by substituting the term *unity* as its supposed exact equivalent, and that after Wilson's death AA itself at times fell into this. He is not speculating. The sentence he is glossing is Wilson's own, from the *Grapevine* of August 1945, where Wilson writes that AA must make everlastingly certain that it will always be strong enough and single-purposed enough from within to relate itself rightly to the world without. That is the sentence Wilson wrote eight months before publishing the Traditions, and the thing it calls single-purposed is close to what the First Tradition would later be called on to mean.

If the two terms were run together in the literature I absorbed, then some of what I have assigned to unity may belong to singleness of purpose, and this chapter's finding would be an artefact of a semantic drift rather than a result about the Traditions. That objection is good enough that I would not have drafted the chapter without answering it.

The answer is a test, and it is one division at a time.

Take each of the eight resources in turn. Hand unity's governance of that resource over to singleness of purpose, wholesale, so that single purpose acquires unity's coefficient and unity keeps nothing. Then ask which Tradition leads.

For six of the eight resources, unity still leads. Give singleness of purpose the admission resource and unity leads 6.32 to 3.98. Give it identification, or the demonstration that recovery happens, or confidentiality, or counsel, or somebody to help, and unity still leads, by margins from 1.44 to 2.54.

For two of the eight, the lead changes hands. Move continuity and single purpose leads 5.14 to 4.63. Move pressure and it leads 5.12 to 4.66.

So the finding is exactly as secure as one judgement, stated plainly: that it is unity rather than singleness of purpose that governs whether the group is still the same group next week, and whether it exerts expectations on the people in it. Nothing else in the matrix can flip it.

I think that judgement is right, and I think it is the most defensible cell in the whole governance matrix, because it is close to a paraphrase of the sentence. The First Tradition says that common welfare comes first and that personal recovery depends on AA unity. That is a claim about the group persisting and cohering. The Fifth says each group has one primary purpose, to carry its message to the alcoholic who still suffers. That is a claim about what the group does while it persists. Continuity belongs to the first and the recipient resource, which is what carrying the message needs, belongs to the second, and the matrix assigns them that way.

But I want to be exact about what has and has not been established. Kurtz's charge is that the terms were conflated in some later literature, and my defence is that my assignment tracks the published wording rather than the later usage.

That defence has since acquired a second leg, and the source is Wilson himself. *Twelve Steps and Twelve Traditions* gives each Tradition a chapter, and the two chapters keep the terms apart about as cleanly as prose can. The chapter on Tradition 1 is about the fellowship holding together: unity is the most cherished quality the Society has, without it the heart of AA would stop, the group must survive or the individual will not. The chapter on Tradition 5 opens with the shoemaker sticking to his last and argues that a group should do one thing supremely well rather than many badly. Counting the words is cruder than reading them and says the same thing: the Tradition 1 chapter uses "unity" five times and "purpose" once, and the Tradition 5 chapter reverses it exactly.

So in the fellowship's own commentary the First Tradition is about persisting and the Fifth is about what you do while you persist, which is the distinction the matrix encodes.

I do not want to overstate what that settles. Kurtz named a specific passage in a different book, *Alcoholics Anonymous Comes of Age*, pages 97 to 98, as the place where the clarification occurs, and I still have not read it. What I have is Wilson making the same distinction elsewhere, at length, in the year the commentary was published, which is good evidence that he held it and not proof about the passage Kurtz cited. The objection is now answered by a sensitivity test, by the short text of the Traditions, and by the 1953 commentary, and still not by the document Kurtz named.

---

There is one more thing worth reporting, and it is the reason this chapter might reasonably be read before Chapter Sixteen rather than after.

Unity's primacy is the most robust claim in Part Four, and it is the only one that survives the hardest test at better than even odds.

Under multiplicative disagreement about the magnitudes, unity leads in every one of two thousand draws at fifteen per cent, every draw at thirty per cent, 98.0 per cent at fifty, and 86.8 per cent at seventy-five. Then take the structural test Chapter Sixteen describes, in which every magnitude is discarded and only the sparsity survives. Unity still leads in 75.4 per cent of draws.

Compare that with the rest of the part on the same test: 40.6 per cent for index-pairing, 17.5 for the Step Five inversion, 27.6 for the Step Twelve inversion. Those are results that depend on my magnitudes. Unity's primacy depends on them much less, because three-quarters of the time a random matrix with the same sparsity pattern puts unity first anyway.

That is not a hundred per cent and I will not round it up. A quarter of the time it does not. But it is the difference between a claim that rests mainly on structure and a claim that rests mainly on judgement, and Part Four contains one of the first and several of the second.

A second design agrees, and it agrees on the interesting part. Appendix A7.6 rebuilds the coupling on sixty-four alternative resource lists, formed by removing resources singly and in pairs and by combining pairs into one, and unity leads on sixty-three of them. **The one failure is the variant that removes continuity and pressure together**, which is precisely the pair the reassignment test above identifies as the only two whose transfer can flip the result. Two tests built for different purposes, one moving a resource from one Tradition to another and one deleting resources outright, converging on the same two columns of the matrix, is worth more than either on its own. It means the finding has one point of failure and both instruments can see it.

---

What this means for the rest of the book is a handover rather than a conclusion.

A Tradition that supplies something to nearly every resource is a Tradition whose failure has no signature. It does not break the room in a way anyone can point at in the month it happens. It lowers the ceiling on everything, and the group carries on looking like itself, and the decline is legible only in the aggregate and only later.

That is precisely the failure this book opened with. The Washingtonians did not lose a specific capability on a specific date. They were absorbed, gradually, into something adjacent, and the record of the absorption is a set of small changes none of which looked fatal at the time. Part Five is about what that looks like from inside a group and what, if anything, would show up in the numbers first.

---

## The Machinery

### 1. What the model says

The load on Tradition *j* is the column sum of the coupling B = S G', which is the total demand every Step places on resources that Tradition *j* governs. It is a summary of the same object Chapter Sixteen reads row-wise, and it is used nowhere in the simulation itself.

The load has a useful decomposition. Because B = S G', the contribution of resource *r* to Tradition *j*'s load is the total demand for that resource across all Steps, times *j*'s governance coefficient for it. That factorisation is what makes the reassignment test below one multiplication rather than a re-derivation, and it is why the test is exact.

The model does not use the load. What it uses is the effective-adherence machinery, in which unity is one of the seven enabling Traditions and its degradation is one of the twelve comparisons reported in Part One's last chapter. Those figures come from paired simulation and carry sampling error; everything in this chapter is deterministic matrix algebra and does not.

### 2. The technical version

**These are exact calculations.** No figure in sections 1 or 2 of this Machinery comes from a simulation, except the robustness proportions, which are Monte Carlo over 2,000 draws and carry Wilson intervals.

Load per Tradition, exact, with the concentration of that load across resources. The share is the largest single resource's contribution as a fraction of the total; HHI is the sum of squared shares, so a Tradition drawing equally on all eight would score 0.125 and one drawing on a single resource would score 1.

| Tradition | Load | Resources governed | Largest resource | Its share | HHI | Principal for | Runner-up for |
|---|---|---|---|---|---|---|---|
| T1 unity | 6.52 | 8 | continuity | 0.29 | 0.204 | 4 | 6 |
| T2 group conscience | 3.89 | 4 | counsel | 0.69 | 0.520 | 4 | 4 |
| T5 singleness of purpose | 3.88 | 6 | proof | 0.24 | 0.197 | 1 | 1 |
| T3 open door | 2.69 | 4 | admission | 0.37 | 0.297 | 1 | 1 |
| T11 attraction | 2.69 | 4 | proof | 0.49 | 0.335 | 1 | 0 |
| T12 anonymity | 2.62 | 5 | confidential | 0.57 | 0.387 | 1 | 0 |
| T8 non-professional | 1.11 | 4 | confidential | 0.41 | 0.290 | 0 | 0 |
| T4, T6, T7, T9, T10 | 0.00 | 0 | none | - | - | 0 | 0 |

Unity is the only Tradition governing all eight resources and the only one in the top two for ten of the twelve Steps. It is **not** the most diffuse by HHI: singleness of purpose scores 0.197 against unity's 0.204, marginally lower. The claim in the main text is breadth of coverage, eight resources against six, and not minimum concentration.

Unity's load by resource, exact: continuity 1.89, pressure 1.86, identification 0.85, counsel 0.60, the demonstration that recovery happens 0.57, confidentiality 0.45, admission 0.20, somebody to help 0.10. Continuity and pressure are 57.5 per cent of the total. Removing both leaves 2.77, which is third, behind group conscience at 3.89 and singleness of purpose at 3.88 and ahead of the open door at 2.69. An earlier draft said fourth; the notebook assertion caught it.

**The reassignment test.** For each resource *r*, set G[T5][r] to the maximum of its current value and G[T1][r], set G[T1][r] to zero, recompute the loads, and record which Tradition leads. This is the strongest form of the conflation objection: it does not merely move a share, it transfers unity's whole governance of that resource to singleness of purpose.

| Resource moved from T1 to T5 | T1 load | T5 load | Leader |
|---|---|---|---|
| admission | 6.32 | 3.98 | T1 |
| identification | 5.67 | 4.05 | T1 |
| proof | 5.95 | 3.88 | T1 |
| confidentiality | 6.07 | 4.33 | T1 |
| counsel | 5.92 | 4.48 | T1 |
| somebody to help | 6.42 | 3.88 | T1 |
| **continuity** | **4.63** | **5.14** | **T5** |
| **pressure** | **4.66** | **5.12** | **T5** |

Two of eight flip it. The finding is conditional on those two assignments and on nothing else in the matrix.

**Robustness of unity's primacy**, 2,000 draws per design, Wilson 95 per cent intervals:

| Design | Unity leads |
|---|---|
| jitter ±15% | 100.0 [99.8, 100.0] |
| jitter ±30% | 100.0 [99.8, 100.0] |
| jitter ±50% | 98.0 [97.3, 98.5] |
| jitter ±75% | 86.8 [85.3, 88.3] |
| structural, sparsity only | 75.4 [73.5, 77.2] |

The structural figure is the highest of any Part Four claim on that test, against 40.6 per cent for index-pairing on all counts, 17.5 for the Step Five inversion and 27.6 for the Step Twelve inversion. The two 100.0 entries are 2,000 of 2,000 and should be read as "not observed to fail".

**What the load measure assumes, and it is not innocuous.** Summing a column treats demand for one resource as commensurable with demand for another, which is a choice and not a derivation. A Tradition governing a resource that many Steps need a little of will score like one governing a resource that one Step needs a great deal of. Nothing in the model justifies that trade; the column sum is a summary statistic and the chapter uses it as one.

### 3. Notes on sources

**The conflation objection was raised in the plan before the chapter was written**, and it is Kurtz's, not mine. `plans/PART-4-PLAN.md` records it as something to settle before drafting, on the ground that it might make the chapter's central finding an artefact. The reassignment test above is the answer and it was run for that purpose.

**What the answer now includes, and what it still does not.** The 1953 commentary was read in full on 10 August 2026 and its chapters on Traditions 1 and 5 keep unity and singleness of purpose distinct, in the terms the main text describes. That is real corroboration and it did not exist when this chapter was drafted.

It is not the document Kurtz named. He points at Wilson's discussion of the First Tradition in *AA Comes of Age*, pages 97 to 98, and that book has still not been read. The difference matters: the 1953 chapters show that Wilson held the distinction, which is what the matrix needs, while the passage Kurtz cites is where he says it is *clarified*, which is a claim about a specific piece of text I cannot check. A reader who has *Comes of Age* to hand can close this in five minutes and I would want to know the result either way.

**The reason it remains unread has changed and should be stated accurately.** It is no longer that the project declines to read AA copyright material; it read the 1953 commentary and was better for it. It is simply that this particular book has not been obtained. That is a smaller and more embarrassing reason, and the correct one.

**A second thing I cannot check.** Kurtz says the conflation appears in *some later AA literature*. He does not say which, and I have not identified an instance. So I am answering a charge whose extent I have not been able to measure.

**Everything else here is computation on matrices I built**, printed in `model/aa_group_model.py`, with every figure reproduced and asserted in `model/book-calculations.ipynb` section 11d.

### 4. References

**Read in full:**

Kurtz, E. (1979, expanded 1991). *Not-God: A History of Alcoholics Anonymous.* Center City, Minn.: Hazelden. **Read at source.** Note 16 to Chapter Five, for the charge that the concept conveyed by *single-purposed* was obfuscated by substituting *unity*, and that AA itself at times fell into this after Wilson's death; and the main text of Chapter Five for Wilson's August 1945 *Grapevine* sentence about being strong enough and single-purposed enough from within. **In copyright; the full text is not stored in this repository.** See `research/SOURCES.md`.

Alcoholics Anonymous World Services (1953). *Twelve Steps and Twelve Traditions*. Read in full 10 August 2026. The chapters on Tradition 1 and Tradition 5, spanning printed pages 129 to 131 and 151 to 155, for Wilson keeping unity and singleness of purpose apart. Copyright AAWS; held as a record with no document.

**Cited at a remove:**

Wilson, W. (1945). "Modesty One Plank for Good Public Relations." *AA Grapevine* 2:3, August 1945, 1 and 4. Quoted here from Kurtz. Not read.

**Internal, and reproducible from this repository:**

`model/aa_group_model.py`, matrices S and GOV. `model/book-calculations.ipynb`, sections 11 and 11d, and section 17 for the resource-list corroboration. `appendix/APPENDIX.md` A5.4 for the perturbation designs. `plans/PART-4-PLAN.md` section 2, which raised the conflation objection.

**What was not read:**

Alcoholics Anonymous World Services (1957), *Alcoholics Anonymous Comes of Age*, pages 97 to 98. Kurtz names it as the passage that clarifies the distinction this chapter's central finding depends on. AA copyright; not acquired; not read. Also not read: whatever later AA literature Kurtz has in mind when he says the conflation occurred there.

# Chapter Eighteen: Two Kinds of Rule

Five of the twelve Traditions do nothing for anybody.

That is not an insult and it is not a complaint. It is what falls out of the derivation. Autonomy, no endorsement, self-support, no hierarchy, no opinion on outside issues: not one of those five governs the supply of any resource that any Step consumes. Put them into the coupling and their columns are exactly zero. A member working the Steps receives, directly, nothing from any of them.

The other seven are not like that. Unity, group conscience, the open door, singleness of purpose, non-professionalism, attraction and anonymity all govern something a Step actually needs. They are in the supply chain. The five are not.

Nobody decided this. It falls out of asking, one Tradition at a time, whether it governs any of the eight things a group produces for its members, and finding that five times the answer is no. That is the two-tier split, and this chapter is about whether it is a discovery or an artefact of how I read twelve sentences.

---

Start with why it looks like a discovery.

The five are a third of the code by count. They are also, by reputation, among the load-bearing ones: an AA member asked which Traditions matter would very likely name self-support and no outside opinion, and Part One spends two chapters on what happened to a movement that had neither firmly. If the derivation had been built to flatter the Traditions it would not have produced a result in which a third of them supply nothing.

And the split is not arbitrary in content. Read the five together and they are all about the group's relations with things that are not the group: other groups, outside enterprises, outside money, a structure above the group, the world's arguments. Read the seven together and they are all about what happens inside the room. That is a clean line and I did not draw it. I drew twelve rows of a matrix by asking a different question, and the line appeared.

The natural reading is that the five are second-order rules. They do not help a member; they protect the conditions under which the other seven can. In the simulation they are implemented exactly that way, as multipliers on the seven rather than as suppliers in their own right, and Part One's history is a case study in what their absence costs. A movement can have a functioning room and lose it to the world outside.

That is the chapter's claim, and now the difficulty.

---

The difficulty is that I cannot test it with the instrument I have used everywhere else, and for a while I did not notice.

Every robustness figure in this part comes from multiplying the entries of two matrices by random numbers. Do that to a zero and you get a zero. So when an earlier version of the notebook reported that the two-tier split survives a hundred per cent of perturbations, it was reporting that zero times a random number is zero, two thousand times, which is not a fact about the Traditions. It is a fact about multiplication.

This has happened twice in this project and both times it was caught late. The rule I have written for myself since is to ask, of any robustness figure, what result the design could in principle have produced instead. For the two-tier split under multiplicative perturbation the answer is none. There is no draw in which a protective Tradition acquires a resource, so there is no draw in which the split fails, so the hundred per cent means nothing at all.

The same trap sits underneath the previous chapter. Five of its twelve counts against index-pairing are the five Steps whose index-mates are these protective Traditions, and those five counts hold for the same empty reason. So the two chapters share one weakness, and if the split is an artefact then a good deal of Part Four goes with it.

---

There is a test that can move a zero, and it took writing this chapter to think of it.

Instead of multiplying, ask what would have to be true. Suppose Tradition Four did govern things. Suppose it governed every resource that Step Four consumes, at some uniform strength. How strong would that have to be before autonomy became Step Four's principal supplier?

The answer is exact, because it is one division. Step Four's current principal supplier reaches 0.35, and Step Four's total consumption across all resources is 0.80, so autonomy would need to govern at 0.438. Not a probability, not an average over draws. A number, and a number that can be compared against something.

The thing to compare it against is the governance matrix itself. It has thirty-five non-zero entries. Their mean is 0.374 and their median is 0.300. So for index-pairing to hold at Step Four, autonomy would have to govern everything Step Four consumes more strongly than a typical live entry in the matrix, and considerably more strongly than the median one.

Run the same division for the other four protective Steps and the thresholds are 0.417, 0.425, 0.600 and 0.627. Give each of the five protective Traditions the mean live strength, 0.374, across every resource its Step consumes, which is a generous concession since it means inventing thirty-five entries out of nothing, and all five still lose. Give them the median, 0.300, and they lose by more.

That is a design capable of returning the opposite answer. It returned this one.

---

It gets better, and the way it gets better is the part I did not expect.

Run the same division for the seven Steps whose index-mates do govern things. The thresholds are 0.443, 0.482, 0.508, 0.521, 0.538, 0.588 and 0.635, averaging 0.531. The five protective thresholds run from 0.417 to 0.627 and average 0.501.

I first wrote that the protective range sits inside the enabling one. It does not, and the assertion I had added to the notebook said so before anyone else could. The protective range extends slightly below the enabling range at both ends. So the protective Steps are not equidistant from index-pairing; they are marginally closer to it than the others, by three hundredths on the average threshold. That is the direction a sceptic would predict, and it is much smaller than the gap that would matter.

What survives is the substantive point. Index-pairing is about equally far from holding everywhere, whether the index-mate governs nothing or governs a great deal, and if you hand every Tradition the mean live strength across its own Step's needs, all twelve still lose. Across all twelve the threshold averages 0.518, against a matrix whose live entries average 0.374.

This repairs something in the previous chapter. Those five counts are not merely arithmetic after all. They are arithmetic under multiplicative perturbation, which is the only test that chapter ran, and they are ordinary results under a test that can reach them. The honest summary is now narrower and stronger than either version I have written before: index-pairing fails on all twelve counts, five of them cannot be tested by multiplying and can be tested by asking what strength would be needed, and under that test they fail by about the same margin as the seven.

I would rather have found this before writing the previous chapter than after. The correction is recorded there rather than hidden.

---

None of that touches the harder question, which is whether the five zeros belong where I put them.

A threshold test tells you how wrong a number would have to be. It cannot tell you whether the cell should have been empty in the first place, because it takes the emptiness as given and asks what filling it would cost. The only real test of the two-tier split is whether a differently-minded person, handed the twelve Traditions and the eight resources and told to mark which governs which, would leave the same five rows blank.

That is not a computation, and I want to put it to you directly rather than compute something adjacent to it and call it evidence.

I can offer one check that is independent of the model, and it half works.

If the split is real, it should show in the wording. The obvious criterion is prohibition: perhaps the five protective Traditions are the ones phrased as things a group must not do, and the seven enabling ones describe things a group does. That criterion fails. Only three of the five carry an explicit "ought never" or "has no opinion", and the other two are phrased as positive practices, while one of the enabling seven is phrased as a prohibition as flatly as any of them.

A second criterion does better. Read the twelve looking for people. Every one of the enabling seven mentions a person or persons: personal recovery, leaders who serve, a requirement for membership, the alcoholic who still suffers, special workers, personal anonymity, personalities before which principles are to be placed. Four of the five protective Traditions mention no person at all. They speak of groups, of the fellowship as such, of outside enterprises, of the name, of contributions, of issues. The fifth is arguable, because of a clause about boards being responsible to those they serve, and I will not pretend otherwise.

So the textual check gives four clean, one strained, and no false positives in the other direction. That is weaker than I would like and it is a different kind of evidence from the model, which is why it is worth having. The two tiers are not only two columns of a matrix. They are two grammars.

---

There is one more piece of evidence and it comes from a hundred years earlier.

Part One shows what the Washingtonians wrote down in 1842, in a manual they sold to anyone starting a society. Set that against the two tiers and the pattern is uncomfortable.

Of the five protective Traditions they had four in some written form. Each society independent and subordinate to none. Its money answerable to its own membership and nobody else. Nothing political or sectarian admitted to the movement's publications or meetings. Only the prohibition on endorsement is missing.

Of the seven enabling Traditions they had none. Not one is in the manual as a rule. Three are explicitly contradicted: the manual prefers publicity to secrecy in taking names, it prescribes elected officers with no rotation and a president who can order a member to sit down, and it claims all classes, sexes, ages and conditions for the movement rather than one purpose.

A movement that wrote down the guards and not the thing guarded. That is what the two-tier split predicts should fail, and it did, and the prediction was not available to me when I built the matrix because I had not read the manual. The weight it carries needs bounding. One movement is one case, and the Traditions were partly written by a man reading that movement's history, so the two documents are not independent in the way the argument would want. What can be said is that the direction is right and did not have to be.

---

What the split is, then, in the plainest terms I can manage.

Seven of the Traditions are about supply. They determine whether the room has the things a person needs in order to change, and if they fail, the room stops working for the people in it.

Five are about interference. They determine whether anything outside the room can reach in and take it over, and if they fail, the room is still working right up until it is no longer the same room.

Those are different failure modes and they show up on different clocks. A group that loses its open door is visibly worse next month. A group that takes outside money is fine next month and is something else in a decade. The Washingtonians are the second failure, and the reason the first fellowship in this book is so much harder to learn from than a collapse would be is that nothing went wrong in the room. It went wrong around it.

Whether the twelve sentences really divide that way is, in the end, a judgement about twelve sentences. I have given the number a person would have to disagree with me by, and the grammar that supports the division, and one historical case that fits. What I have not given, and cannot, is a second reader.

---

## The Machinery

### 1. What the model says

The two-tier split is a property of the governance matrix G, which is twelve Traditions by eight group resources. Five of its rows are identically zero: Traditions 4, 6, 7, 9 and 10. The consequence for the coupling B = S G' is that those five Traditions have zero columns, so they supply nothing to any Step.

They are not absent from the simulation. They enter it as multipliers on the effective adherence of the Traditions they guard, described in Part One's last chapter and specified in appendix A2. That is a modelling choice and not a derivation: the derivation says only that the five govern no consumed resource, and says nothing about how they should act instead. The multiplier form is the simplest thing that gives them a role, and it is the reason they appear near the top of the degradation comparison, which is noted there as consistent with their derived role rather than as evidence for it.

One consequence worth naming because it is algebra and not simulation: because the governance matrix is column-normalised, at full adherence to every Tradition it cancels exactly, and 35 of the model's 118 registered sensitivity values cannot affect a fully adherent group at all. The count is not a census of every authored choice. The split is therefore informative only away from the full-adherence corner; the model does not measure the adherence of real groups.

### 2. The technical version

**The threshold test.** For Step *i*, let *w_i* be the total consumption of Step *i* across all eight resources, that is the row sum of S, and let *b_i* be the largest entry in row *i* of B excluding the index-mate's own entry. If Tradition *i* governed every resource at a uniform strength *c*, its entry in row *i* would be *c w_i*. Index-pairing holds at Step *i* exactly when

> c > c*_i = b_i / w_i

This is one division per Step and carries no sampling error. It is the only design in this part that can turn a structural zero into a non-zero, which is why it is the only one that can say anything about the five protective Steps.

| Step | Index-mate | Beats | Row sum of S | c* | c* / mean live entry |
|---|---|---|---|---|---|
| 1 | T1 | 1.22 | 2.40 | 0.508 | 1.36 |
| 2 | T2 | 0.82 | 1.70 | 0.482 | 1.29 |
| 3 | T3 | 0.31 | 0.70 | 0.443 | 1.18 |
| **4** | **T4** | 0.35 | 0.80 | **0.438** | 1.17 |
| 5 | T5 | 1.08 | 1.70 | 0.635 | 1.70 |
| **6** | **T6** | 0.25 | 0.60 | **0.417** | 1.11 |
| **7** | **T7** | 0.17 | 0.40 | **0.425** | 1.14 |
| 8 | T8 | 0.43 | 0.80 | 0.538 | 1.44 |
| **9** | **T9** | 0.90 | 1.50 | **0.600** | 1.60 |
| **10** | **T10** | 0.94 | 1.50 | **0.627** | 1.67 |
| 11 | T11 | 0.47 | 0.80 | 0.588 | 1.57 |
| 12 | T12 | 1.25 | 2.40 | 0.521 | 1.39 |

Bold rows are the five protective Traditions. The governance matrix has 35 non-zero entries of 96 cells, with mean 0.374, median 0.300, minimum 0.10 and maximum 1.00. Every c* exceeds both the mean and the median. The protective range, 0.417 to 0.627, is not contained in the enabling range, 0.443 to 0.635; it extends below it at both ends. Mean c* is 0.501 for the five protective Steps, 0.531 for the seven enabling ones and 0.518 across all twelve. The protective Steps are therefore marginally closer to index-pairing holding, by 0.03 on the mean threshold, which is the direction an objector would predict and an order of magnitude smaller than the distance to the mean live entry.

Setting *c* to the mean live entry of 0.374 for every Step simultaneously, all twelve index-mates still lose, by margins from 0.02 at Step 7 to 0.44 at Step 5.

**What this test does and does not license.** It licenses the statement that index-pairing would require the index-mate to govern its own Step's needs more strongly than a typical entry in the matrix, uniformly across all twelve. It does not license any statement about whether the zeros are correctly placed, because it holds the sparsity pattern's origin fixed and prices only its consequences. It is a sensitivity analysis of a judgement, not a test of it.

**What the multiplicative designs cannot do, restated so it is not lost.** Multiplying a zero by a random number leaves a zero. Both perturbation designs used elsewhere in this part are multiplicative on the non-zero entries and preserve sparsity by construction. Therefore neither can produce a draw in which a protective Tradition supplies anything, and neither can be quoted as evidence about the two-tier split. The 100 per cent figure previously recorded for the split is vacuous and has been removed from `research/PARAMETERS.md` and appendix A5.4.

**The textual classification is a judgement and is recorded as one.** Criterion one, an explicit prohibition in the wording, matches three of the five and also matches one of the enabling seven; it fails. Criterion two, mentioning no individual person, matches four of the five cleanly, matches the fifth only if a clause about service boards being responsible to those they serve is read as referring to groups rather than to people, and matches none of the enabling seven. Reported as four clean, one strained, no false positives. No count here is a computation and none is asserted in the notebook.

### 3. Notes on sources

**An error caught by the notebook rather than by me.** The main text of this chapter first said the protective thresholds sit inside the enabling range. They do not; the protective range extends below the enabling range at both ends, and the protective mean threshold is 0.501 against 0.531. The assertion added for that sentence failed on its first run and the text was corrected before the chapter was saved. The corrected version is a weaker claim in the direction an objector would want, and it is in the main text rather than here.

**The threshold test is new to this chapter and it changed the previous one.** Chapter Sixteen reports that five of its twelve counts against index-pairing are arithmetic rather than evidence, because no sparsity-preserving perturbation can reach them. That is true of the designs Chapter Sixteen runs. It is not true in general, and the threshold test above reaches them and finds they fail by margins comparable to the seven. Chapter Sixteen now carries a pointer to this chapter at that paragraph rather than being silently amended.

**The historical parallel became available only in August 2026** and is not something the matrices were built against. Part One's account of what the Washingtonians wrote down rests on Grosh's *Washingtonian Pocket Companion* of 1842, read at source, and the mapping of its clauses onto four of the five protective Traditions is set out in Chapter One with the quotations. The mapping onto the *tiers* is mine and is new here. Two cautions travel with it. First, Wilson wrote his reading of Washingtonian history into the *A.A. Grapevine* eight months before publishing the Traditions and was, on Kurtz's account, explicitly seeking support for the Traditions he was formulating, so the Traditions and the Washingtonian record are not independent. Second, one movement is one case.

**What the reader is being asked to supply.** Whether the five rows should be empty. This is named in `plans/PART-4-PLAN.md` as the reader pass and it is still outstanding. It is the single largest unresolved item in Part Four and no further computation will close it.

**What has been done in the meantime, and what it is worth.** The elicitation form now exists at `research/GOVERNANCE-MATRIX-ELICITATION.md`, and so does the script that will analyse the completed forms, written before any came back so the analysis cannot be chosen after seeing the answers. Appendix A8 also prices disagreement in the abstract: flipping cells of the governance matrix at random, confined to the enabling rows so the split is held fixed, index-pairing survives 86 per cent of the time when four of fifty-six cells differ and 53 per cent when sixteen do. That says Part Four tolerates a reader who differs on a handful and not one who differs on a third. It does not say which cells a real reader would pick, which is the thing that matters and the thing only a reader can supply.

### 4. References

**Read in full:**

Grosh, A. B. comp. (1842). *Washingtonian Pocket Companion.* Second edition. Utica, N.Y.: B. S. Merrell. **Read at source**; saved in `research/`. Used here only for the four written analogues of protective Traditions and the three contradicted enabling ones. Full bibliographic detail and the quotations are in Chapter One.

Kurtz, E. (1979, expanded 1991). *Not-God: A History of Alcoholics Anonymous.* Center City, Minn.: Hazelden. **Read at source.** Used here for the dependence of Wilson's Washingtonian reading on the Traditions he was drafting. **In copyright; the full text is not stored in this repository.**

**Cited at a remove:**

The wording of the Twelve Traditions themselves. They are AA copyright, this project does not reproduce them in full, and the textual classification above therefore describes the wording rather than quoting it beyond the few phrases needed to make the criteria checkable.

**Internal, and reproducible from this repository:**

`model/aa_group_model.py`, matrix GOV, for the five zero rows. `model/book-calculations.ipynb`, section 11c, for the threshold table and the matrix statistics. `appendix/APPENDIX.md`, sections A2 for the multiplier specification, A5.3 for the exact cancellation at full adherence, and A5.4 for the perturbation designs and what they cannot reach.

**What was not read:**

Any discussion by AA of why these five Traditions are phrased as they are. *Alcoholics Anonymous Comes of Age* contains Wilson's own commentary on each Tradition and would be the obvious place to test whether he understood the five as second-order rules; it has not been obtained. *Twelve Steps and Twelve Traditions*, which was read in full on 10 August 2026, gives each Tradition a chapter and is the nearer parallel, but its chapters argue for each rule rather than classifying the rules against one another, so it does not test the split either. The claim that the split is visible in the grammar therefore still rests on my reading of twelve sentences and on nobody else's.


\clearpage
\thispagestyle{empty}
\vspace*{0.32\textheight}
\begin{center}
{\Large\bfseries Part Five}\\[0.6em]
{\large\itshape How Groups Die}
\end{center}
\clearpage

# Chapter Nineteen: You Cannot Close the Door

Eleven of the Twelve Traditions tell a group what to do. One tells it what it may not decide.

The third says the only requirement for membership is a desire to stop drinking. Read it as an instruction and it sounds welcoming. Read it as a constraint and it is something stronger: a group has no procedure for refusing membership, because it has been denied one. It cannot interview. It cannot decide that this particular person is not ready, or not really an alcoholic, or not the sort of person the meeting is for. Whoever wants to be a member is one.

I need to be careful with one word before going further, because the obvious objection to that paragraph is correct and the fellowship has a term of art that collides with mine.

**AA meetings are routinely closed, and this is not a violation of anything.** A closed meeting is one at which only people who have a desire to stop drinking are present, as against an open meeting which anyone may attend. The distinction is standard, it is published, and a group deciding to hold closed meetings is doing something entirely ordinary. So "a group cannot close its doors" is false as a statement about meetings.

The Tradition is about **membership**, not attendance at a particular gathering. It says who may be a member of Alcoholics Anonymous, and the answer is anybody who wants to stop drinking. A closed meeting excludes the curious and the professional and the family member; it cannot exclude an alcoholic who wants what the room has. That is the power the Tradition removes, and it is the only one this chapter is about.

For the rest of the chapter I will therefore say **unwelcoming** rather than closed, because the thing being modelled is a group's culture toward the people it cannot refuse, and using "closed" for it would import a meaning the fellowship has already assigned elsewhere.

That leaves the question the constraint raises. If a group cannot refuse a member, what does an unwelcoming group even look like?

The answer is that it looks like a room. Not a door.

---

Everything a gatekeeping group does, it does to someone already inside.

Nobody is turned away at the threshold because there is no threshold and no one standing at it. What happens instead is a hundred small things that are not decisions: the seat nobody moves along to make, the conversation that closes when the newcomer approaches, the shorthand that is not explained, the coffee rota that is already staffed, the phone list that is not offered. None of that is a policy. All of it is a message, and the message is received.

So the open door does not govern who arrives in the default model. It has two other paths.

One path changes the governance quality of four resources, including admission and recipient opportunity. The other adds dropout friction weighted by low practice. The model records practice but not tenure, so that second path cannot tell a person of two weeks from a long-tenured person whose practice is low. Earlier drafts called it newcomer weighting and described the whole intervention as retention. Both descriptions were too strong. The corrected analysis separates resource governance from dropout friction before combining them.

---

Now the price list has to be split in two.

Across four hundred paired seeds, the baseline ends at 17.80 members. Removing only the inverse-practice dropout protection costs 2.96 members, with a 95 per cent interval from 1.85 to 4.08. Removing only Tradition Three's resource governance costs 6.03, from 5.04 to 7.01. Removing both costs 11.05, from 10.03 to 12.06. The two losses do not add: their interaction is -2.06, with an interval excluding zero.

The event outcomes are sharper. Every baseline group still exists at thirty years and 98.5 per cent finish above five members. Under combined loss, 25.0 per cent are closed and only 54.8 per cent finish above five. Crossing the threshold is not permanent: 347 combined-loss runs cross to five or fewer and 340 later recover above five at least once. A crossing, a recovery, an endpoint below six and closure are different events.

---

The two paths also send different interior signals.

With friction loss alone, established-member practice rises from 0.265 to 0.289 even as membership falls. That is compatible with selection: losing low-practice members can make the remainder look stronger. Governance loss does something else. Established-member practice is nearly unchanged at 0.265, while the low-practice fraction rises from 0.235 to 0.406. Under combined loss, established practice falls to 0.225 and the low-practice fraction is 0.294.

So the old sentence that an unwelcoming group looks better was an artefact of treating two mechanisms as one. It describes the friction path and not the governance path or their combination. The model has no arrival dates, cohorts or sponsorship links, so the low-practice fraction must not be translated into a newcomer count.

What the factorial says, in one sentence, is that the Third Tradition is neither cheap nor one mechanism. One path can create a misleading improvement among those left; the other changes the resource environment; together they produce closure in one run out of four within the modeled horizon.

Compare that with the failure Part One documents. The Washingtonians were not unwelcoming. They defined themselves so broadly that the movement stopped being about drunkards at all, which is the opposite failure and, on this model's accounting, a far more dangerous one. Whether it is more dangerous is the subject of the next chapter, which sets this failure beside the two other ways a group can starve and asks which of the three anyone would see coming.

---

## The Machinery

### 1. What the model says

Tradition 3 enters the model through two separately controllable paths.

Arrivals are Poisson, with rate equal to an exogenous referral floor plus attraction generated by members' twelfth-step practice and scaled by Tradition 11. **Tradition 3 does not appear in that expression.** A group's welcome does not affect who turns up, because the Tradition denies the group any admission procedure. Whether the model should represent it that way is a substantive question and the answer here is that it should, because the alternative is a group exercising a discretion the Tradition removes.

Its first path is resource governance: its row contributes to four resource columns. Its second path is the dropout hazard. Each member's per-period hazard is a baseline that falls exponentially with early-step practice, plus a churn floor, with an additional friction term

> t3_friction = 1 + (1 - T3) * exp(-6 * mean practice)

so that at full adherence there is no additional friction, and at zero adherence the friction is largest for members whose practice is near zero and negligible for members whose practice is high. Because the weight uses practice rather than tenure, it must be called inverse-practice weighting rather than newness.

The release-gate factorial reports loss of the governance path, loss of the friction path, their combination and their interaction. The older five-level sweep varies both paths together and therefore describes a combined Tradition 3 intervention, not a retention-only treatment.

### 2. The technical version

Design: 400 paired seeds, all other Traditions at 1.0, thirty-year horizon, dt of half a week. Continuous entries are means with 95 per cent intervals; proportions carry Wilson intervals.

| Condition | Final N | Exists, N > 0 | Endpoint viable, N > 5 | Closed, N = 0 | Established practice | Low-practice fraction |
|----------------------|-----------|-----------|-----------|-----------|-----------|-----------|
| Baseline | 17.80 [16.92, 18.68] | 100.0% [99.0, 100.0] | 98.5% [96.8, 99.3] | 0.0% [0.0, 1.0] | 0.2645 [0.2587, 0.2703] | 0.2345 [0.2215, 0.2474] |
| Friction loss only | 14.84 [13.91, 15.76] | 99.2% [97.8, 99.7] | 94.0% [91.2, 95.9] | 0.8% [0.3, 2.2] | 0.2886 [0.2806, 0.2965] | 0.2225 [0.2073, 0.2376] |
| Governance loss only | 11.77 [11.15, 12.40] | 98.0% [96.1, 99.0] | 91.2% [88.1, 93.6] | 2.0% [1.0, 3.9] | 0.2648 [0.2553, 0.2743] | 0.4059 [0.3860, 0.4257] |
| Combined loss | 6.76 [6.17, 7.34] | 75.0% [70.5, 79.0] | 54.8% [49.9, 59.6] | 25.0% [21.0, 29.5] | 0.2246 [0.2086, 0.2406] | 0.2937 [0.2694, 0.3179] |

Paired final-N contrasts, baseline minus loss: friction 2.96 [1.85, 4.08], governance 6.03 [5.04, 7.01], combined 11.05 [10.03, 12.06]. The factorial interaction is -2.06 [-3.41, -0.70].

**Quality and low-practice fraction are conditional on endpoint population and this matters more here than it looks.** Closed runs contribute no members to either column. Conditioning can therefore make the remaining groups look stronger than the all-run population. Endpoint nonviability is not itself death: runs with one to five members are extant and are reported separately from closure in the release-gate analysis.

**What is not varied.** Everything else. This is a one-factor sweep at full adherence elsewhere, which is a best case: it asks what an unwelcoming culture costs a group that is otherwise doing everything right. An unwelcoming culture in a group already short of attraction or referrals is not tested here and there is no reason to assume the costs add.

**What the registered sweep cannot find.** The friction term's exponent of 6, which sets how quickly the added friction falls with practice, is hard-coded and not estimated. It is not one of the 118 registered sensitivity values and the old one-at-a-time sweep never varied it. It appears separately in the model-choice inventory. No robustness claim may be based on saying that all model choices were perturbed.

### 3. Notes on sources

**This chapter is model output and a reading of one sentence.** The sentence is the Third Tradition. The claim that it removes a power rather than granting one is mine, and it is the whole basis for modelling the open door as acting on retention rather than on arrival.

**The title is kept deliberately.** "You Cannot Close the Door" is the claim the chapter makes about membership, and the main text explains in its third paragraph why it is not a claim about meetings. Retitling would lose the point; leaving the ambiguity unaddressed would have been worse.

**The term of art was corrected here.** An earlier draft used "closed" throughout for a group with an unwelcoming culture. In the fellowship's own usage a closed meeting is one restricted to people with a desire to stop drinking, as against an open meeting anyone may attend, and it is an entirely ordinary thing for a group to hold. The chapter now says unwelcoming, and the main text sets out why Tradition 3 still removes the power it is described as removing: it governs membership rather than attendance at a given gathering. This is the second correction in the book to have come from anticipating what a reader inside the fellowship would object to, and I would rather have the objection than the phrasing.

**The behavioural description is not sourced and is offered as illustration.** The seat nobody moves along to, the conversation that closes, the phone list not offered: I have no study of AA group culture to cite for any of that, and it is in the chapter to make the mechanism concrete rather than to establish it. A reader who thinks gatekeeping in practice works some other way should discount the chapter's framing and keep its arithmetic, which does not depend on the particulars.

**What would test this properly.** Any longitudinal measurement of low-practice members and newcomer retention across groups differing in culture, with practice and tenure measured separately. I am not aware of one, and this is a place where the fellowship's own anonymity makes the research hard rather than merely undone.

**The proxy is the first thing to check.** The model predicts a larger low-practice fraction under the combined intervention. Whether that corresponds to first-ninety-day membership is unknown. Measuring both would test the translation rather than assuming it.

### 4. References

**Read in full:**

Nothing new to this chapter. The dropout and inflow structure is described in Part Three and specified in appendix A2, and the sources for its functional forms are given there.

**Cited at a remove:**

Nothing.

**Internal, and reproducible from this repository:**

`model/aa_group_model.py` for the resource and friction paths. `model/release_gate_analysis.py` for the paired factorial and `research/release_gate_results.json` for its 3,200 raw jobs and summaries. `research/RELEASE-GATE-RESULTS.md` is the generated human-readable report. `appendix/APPENDIX.md` gives the full specification, selection threat and sensitivity designs.

**What was not read:**

Any empirical literature on newcomer retention in mutual-aid groups. I searched for a study relating group climate to early attrition in AA specifically and did not find one I could read; the chapter's mechanism is therefore asserted from the Tradition's wording and from the model, and not from evidence about how meetings actually behave.

# Chapter Twenty: Three Ways to Starve

A group can fail to bring people in, or fail to have people sent to it, or fail to keep the people who arrive. Those are the three, and they are not variations on one thing.

Each of them starves the group of the same commodity, which is members, and each does it by a different route, on a different timetable, with a different set of symptoms. The corrected model makes all three visible in room size. What remains difficult to read is practice quality, because conditioning on groups that remain viable can make the most damaged populations look strongest.

I am going to give them names, because the model's names are ugly. Call them invisible, unreferred, and unwelcoming.

---

An **invisible** group is one whose members have stopped carrying the message.

Nobody outside hears about it. The twelfth-step work is not happening, or is happening privately and without effect, so the only people who arrive are the ones sent by somebody else. In the model this means setting only Tradition 11's attraction path to zero while leaving its resource-governance path intact: attraction produces nothing, and the referral floor is all that is left.

The result is a slow, visible, usually viable shrinkage. A group of twenty-five falls to 21.5 within a year, 18.6 by the second, 14.5 by the fifth, and finishes at 12.4. At year thirty all 400 groups still exist and 98.5 per cent have more than five members.

Established-member practice falls from 0.55 at founding to 0.352 at year five, 0.295 at year ten and 0.259 at year thirty. The matched healthy values are 0.322, 0.302 and 0.265. The old claim that the invisible group's members are distinctly worse no longer holds: the two trajectories are close after the first decade.

So an invisible group is small and thin and alive. It looks like what it is. Anyone attending would say the meeting has got quiet and the regulars are not what they were, and they would be right.

---

An **unreferred** group is one that nothing external feeds.

No courts sending people, no treatment centre discharging them, no doctor writing the address on a card. In the model this is the exogenous inflow set to zero, so every arrival has to be generated by a member out doing the work. Chapter One argues this was the Washingtonians' condition, not by choice but because in 1840 the second channel did not exist.

Now look at what happens, and look at the first five years before anything else.

At year one an unreferred group has 32.7 members. At year two, 30.4. At year five, mean membership across all runs is 21.6 and 97.0 per cent remain above five members. A healthy group at year five has 35.2. The unreferred group is already visibly smaller. Among its viable groups, established practice is 0.348 against a healthy 0.322, which is to say apparently *better*.

Five years in, a viable unreferred group is a smaller meeting full of apparently solid people.

By year ten, 66.0 per cent remain endpoint-viable and 94.8 per cent still exist. The viable groups average 16.5 members and sit at 0.348, above the healthy group. By year twenty, 17.3 per cent remain viable and 42.5 per cent exist; the viable subset averages 11.4 members at 0.355. By year thirty, only 2.75 per cent remain viable, 10.5 per cent exist at all, and 89.5 per cent have closed. The eleven viable groups average 12.3 members.

Read the viable-subset columns down and two things diverge. Membership falls from 22.1 at year five to 12.3 at year thirty, a visible warning. Practice goes the other way, from 0.348 to 0.364, while the viable subset shrinks from 388 groups to eleven. The corrected model therefore does not support the claim that nothing inside the room looks wrong. It supports the narrower claim that practice among selected survivors can look strong while the population of groups disappears.

The mortality is entirely in the groups that are no longer there to be asked.

---

An **unwelcoming** group here is one that loses both modeled Tradition 3 paths: resource governance and inverse-practice dropout protection.

The previous chapter set out what that costs and why its two mechanisms should not be conflated. The combined intervention costs 11.05 endpoint members [10.03, 12.06] relative to baseline, closes one group in four, and leaves 54.8 per cent viable at year thirty.

In trajectory the combined-loss group falls from 30.4 members at year one to 26.4 at year two, 14.5 at year ten and 6.8 at year thirty when closures count as zero. Viability falls from 90.5 per cent at year ten to 54.8 per cent at year thirty. Among viable groups, established practice is 0.360 at year ten and 0.321 at year thirty, above the corresponding healthy values, but that comparison is selected on remaining viable.

It is not the stable, slightly small meeting the earlier cache implied. Combined Tradition 3 loss is a serious closure and viability failure in the corrected model.

---

Put the three beside each other at year ten and the differences are obvious.

The invisible group's viable endpoints average 13.0 members and established practice 0.295. The unreferred viable subset averages 16.5 and 0.348. The combined Tradition 3-loss subset averages 15.7 and 0.360. A healthy viable group averages 29.4 and 0.302.

Membership warns in every failure mode. Practice does not. The two modes with the strongest-looking selected members are the unreferred and combined Tradition 3-loss conditions, which are also the modes producing substantial closure.

Every one of those quality figures is measured among the members of groups that are still alive, and that is not a technicality. It is why the numbers come out that way. A failure mode that kills weak groups leaves strong ones to be measured, and a failure mode that expels weak members leaves strong ones to be counted. Both mechanisms manufacture the appearance of health out of the fact of loss.

Which is the thing I want to be careful about, because this book has warned twice against exactly this reasoning and is now relying on it. The difference is only that the conditioning is stated. When I say an unreferred group's survivors look healthy, the sentence contains the word survivors, and the fraction surviving is printed next to it. The moment that fraction is dropped, the same table says that losing your referrals improves your meeting.

---

So here is the practical shape of it.

A group can measure two things about itself without any apparatus at all. It can count the room, and it can tell, roughly, how the regulars are doing.

Against the invisible failure, both instruments work. The room is small and the regulars are struggling, and the two agree.

Against combined Tradition 3 loss, the room count works and the practice reading can mislead. The group is much smaller; the selected established members can look stronger than baseline.

Against the unreferred failure, the room count registers decline early and the practice reading points the wrong way. The larger failure is still in the population of rooms: no surviving room can directly observe the 89.5 per cent that have closed.

That is the subject of the next chapter, because the correction weakens its original thesis. Selection still hides failure in the practice measure, but membership decline is visible inside the surviving groups, and the Washingtonian analogy has to be narrowed with it.

---

## The Machinery

### 1. What the model says

The three failure modes are three different interventions on the same simulation and they act at three different points in the loop.

**Invisible** sets only the Tradition 11 attraction path to zero. Arrivals fall to the exogenous floor while Tradition 11's resource-governance path remains at one.

**Unreferred** sets the exogenous inflow to zero, so arrivals become strictly proportional to the twelfth-step practice currently being done by current members. Chapter One's Machinery describes the consequence: a group on one engine has no floor underneath it. Its inflow is a function of its own state, which makes the population dynamics multiplicative rather than additive, and a multiplicative process with no floor has an absorbing state at zero.

**Unwelcoming** sets Tradition 3 to zero on both of its default paths. It removes resource governance and adds inverse-practice dropout friction without touching arrivals. The release factorial in Chapter Nineteen separates those paths; this trajectory combines them.

The distinct mortality profiles follow from that structure without being put in by hand. The referral floor prevents closure in the invisible condition. Unreferred groups are the only ones whose inflow can go to zero and stay there, and they close most often. Combined Tradition 3 loss also closes a substantial minority through its resource and dropout paths.

### 2. The technical version

400 paired seeds per condition, thirty-year horizon, dt of half a week, membership and practice recorded at every step and sampled yearly. Runs come from `model/part5_runs.py` and are cached in `research/part5.json`. Endpoint existence means N > 0; viability means N > 5; closure at N = 0 is permanent. **The quality column below conditions on viability, while all-run membership includes zeros. The viable fraction is printed beside it.**

Survival carries a 95 per cent Wilson interval; membership and quality carry a 95 per cent half-width from the cross-run standard error.

| Condition | Viable y10 | Members if viable, y10 | Established practice y10 | Viable y30 | 95% interval | Established practice y30 |
|-------------------------|--------|------------|--------------|--------|----------------|--------------|
| nothing wrong | 0.9975 | 29.40 ± 1.16 | 0.3016 ± 0.0052 | 0.985 | 0.968 to 0.993 | 0.2648 ± 0.0058 |
| invisible | 0.9925 | 12.98 ± 0.34 | 0.2949 ± 0.0079 | 0.985 | 0.968 to 0.993 | 0.2592 ± 0.0071 |
| unreferred | 0.660 | 16.47 ± 1.18 | 0.3475 ± 0.0084 | 0.0275 | 0.015 to 0.049 | 0.3642 ± 0.0443 |
| unwelcoming, combined T3 loss | 0.905 | 15.70 ± 0.82 | 0.3597 ± 0.0097 | 0.5475 | 0.499 to 0.596 | 0.3211 ± 0.0134 |

Only eleven unreferred runs are viable at year thirty. Their quality interval is correspondingly wide; the high conditional mean is evidence of selection, not population improvement.

Membership counted over all runs with deaths as zero, by year:

| Condition | y1 | y2 | y5 | y10 | y20 | y30 | half-width at y30 |
|------------------------|--------|--------|--------|--------|--------|--------|----------------------------|
| nothing wrong | 37.7 | 38.3 | 35.2 | 29.3 | 21.3 | 17.8 | ± 0.88 |
| invisible | 21.5 | 18.6 | 14.5 | 12.9 | 12.2 | 12.4 | ± 0.34 |
| unreferred | 32.7 | 30.4 | 21.6 | 11.7 | 2.5 | 0.51 | ± 0.23 |
| unwelcoming, combined T3 loss | 30.4 | 26.4 | 20.0 | 14.5 | 9.2 | 6.8 | ± 0.59 |

The unreferred row shown both unconditionally and conditioned on endpoint viability:

| Condition | y5 | y10 | y20 | y30 |
|---|---|---|---|---|
| unreferred, all runs | 21.55 ± 1.01 | 11.68 ± 1.02 | 2.50 ± 0.48 | 0.51 ± 0.23 |
| unreferred, viable runs only | 22.07 ± 1.00 | 16.47 ± 1.18 | 11.39 ± 1.37 | 12.27 ± 3.81 |
| viable fraction | 0.970 | 0.660 | 0.1725 | 0.0275 [0.015, 0.049] |

The unconditional series falls by 98 per cent from year two to year thirty. Even the viable-subset membership falls sharply, while its practice measure rises. The gap is selection, but the corrected model no longer makes the decline invisible on membership.

**Established-practice differences against a healthy viable group at year ten:** invisible is 0.0067 lower, unreferred is 0.0459 higher, and combined Tradition 3 loss is 0.0581 higher. Membership is lower in all three.

**What is not tested.** Combinations. Each condition switches one thing off at full adherence elsewhere. Real decline is unlikely to be so tidy and there is no reason to expect the costs to add. Appendix A7.1 lists this under what no design covers.

**What the trajectories are not.** They are not predictions of how long a real group lasts. The horizon, arrival rate and churn floor are authored choices, and the original forty-five-member calibration fails after the heterogeneity correction. The expanded sensitivity designs are screens of dependence within this model; they do not validate the durations or absolute sizes.

### 3. Notes on sources

**Everything quantitative here is model output.** There is no external dataset of group survival and none of the three failure modes has been observed in the way described. What the chapter offers is the internal logic of a set of assumptions, and the strongest claim it can support is that if the model is right about the mechanisms, then these three failures are distinguishable in principle and not in practice.

**The naming is mine and is not neutral.** Calling the exogenous-inflow condition "unreferred" imports a modern institutional world of courts and treatment centres. Chapter One argues the Washingtonians were in this condition permanently, which is a strong claim about 1840 and rests on the absence of institutions rather than on any record of a group starving.

**Where this could be checked.** AA's General Service Office publishes group counts by region and has done for decades. A region whose treatment-referral pipeline changed sharply, in either direction, would be a natural experiment on the unreferred condition, and group counts before and after would be a real test of the mortality profile above. I have not attempted it, and I do not know whether the group-count series is fine-grained enough to support it.

### 4. References

**Read in full:**

Nothing new to this chapter. The population dynamics and their sources are given in Part Three and specified in appendix A2.

**Cited at a remove:**

Nothing.

**Internal, and reproducible from this repository:**

`model/part5_runs.py` for the runs. `research/part5.json` for the raw output. `model/book-calculations.ipynb` section 14 for every figure with its assertion. `appendix/APPENDIX.md` A4 for the selection threat that this chapter turns into a finding, A7.1 for what no design covers, A6 for the calibration.

**What was not read:**

Any study of mutual-aid group mortality. I looked for a survival analysis of AA groups, or of any comparable voluntary fellowship, and found nothing I could read. So the mortality profiles here have no empirical counterpart at all, and the chapter's claim that they are distinguishable from outside is a claim about the model rather than a claim anyone has tested.

# Chapter Twenty-One: The Healthy-Looking Corpse

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
|--------|--------|--------|----------------|----------------|------------------------|
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

**The series has now been obtained and read, and it supplies one number.** The document is service material SMF-132, *Estimated Worldwide A.A. Individual and Group Membership*, published free by the General Service Office as a table of groups and members by year, 1935 to 2020. It was located on 2 August 2026, left unread on a policy ground that was itself corrected on 10 August, and read at source on 17 August 2026. Dividing reported members by reported groups gives a mean of 18.4 members per group across 2001 to 2020, ranging from 16.5 to 22.1 and falling steadily as groups are added faster than members. The model's endpoint membership at full adherence is 17.80, with a 95 per cent interval of [16.92, 18.68] on 400 seeds at thirty years. That sits inside the observed range and close to its mean, and the model was not fitted to it: room capacity, arrival and dropout were all set before this table was read, which is what makes the comparison out of sample at all. **It is a consistency check and not a validation, and the source says why.** AA keeps no membership lists, and these are reports from groups registered with general service offices. A ratio of two estimated aggregates is not a sample of group sizes: it carries no interval, and it says nothing about a distribution that is certainly skewed. The model produces a distribution and the table produces a point. They agree at the point, which is worth a sentence and not a chapter. Two limitations named earlier survive unchanged. The series is worldwide rather than regional, so the natural experiment this chapter proposes, a region whose referral pipeline changed sharply, still needs finer data than SMF-132 carries. And a count of groups is not a count of group deaths, because the total moves with births as well.

**Almost nothing here is validated.** The trajectories are model output and have never been compared against a real group. The one comparison that now exists, mean group size against SMF-132, touches a single endpoint number and not a trajectory, and is a consistency check rather than a test. The expanded sensitivity suite measures dependence on authored choices; it does not validate the durations, the absolute group sizes or the historical application.

### 4. References

**Read in full:**

Maxwell, M. A. (1950). "The Washingtonian Movement." *Quarterly Journal of Studies on Alcohol* 11: 410-452. Saved under `research/incorporated/Maxwell_1950/`; see Chapter One for the note on the retyped copy. Used here only for the character of the decline record, which is discussed at length in Chapter Two.

Krout, J. A. (1925). *The Origins of Prohibition.* New York: Alfred A. Knopf, chapter IX. Saved in `research/`. Used here for the same purpose.

Alcoholics Anonymous World Services. *Estimated Worldwide A.A. Individual and Group Membership*, SMF-132, Rev. 12/20. Read at source on 17 August 2026 and held as record only under `research/incorporated/SMF132_2020/`. Used here for the members-per-group ratio and for the method note that limits it.

**Cited at a remove:**

Nothing.

**Internal, and reproducible from this repository:**

`model/part5_runs.py`, `research/part5.json`, `model/book-calculations.ipynb` section 14. `appendix/APPENDIX.md` A4 for the selection threat, A7.1 for what no design covers, A11 threat 2 for the absence of external validation.

**What was not read:**

Also not read: any survival analysis of voluntary associations that would say whether bimodal group mortality is a real phenomenon or an artefact of this model's inflow structure. The chapter's central mechanism therefore has no empirical corroboration of any kind, and a reader should weigh it as an argument about a model rather than a claim about the world.

# Chapter Twenty-Two: What You Cannot Engineer

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
|----------------------|-----------|-----------|-----------|-----------|-----------|-----------|
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


\clearpage
\thispagestyle{empty}
\vspace*{0.32\textheight}
\begin{center}
{\Large\bfseries Part Six}\\[0.6em]
{\large\itshape What I Do Not Know}
\end{center}
\clearpage

# Chapter Twenty-Three: The Wrong Turns

This chapter is a list of everything I got wrong.

Not everything I am unsure about, which is Chapter Twenty-Four, and not everything the method cannot reach, which is Chapter Twenty-Five. This is the record of specific, identifiable errors that were in the work and are no longer, together with what each one took to find.

I am including it for a reason that is not modesty. The errors sort themselves into three kinds, and the three kinds were caught by three completely different instruments. That pattern is the most useful thing this book has to say about how to do work of this sort, and it would be invisible if I reported only the corrected version.

---

The first kind is a **modelling error**, and the distinguishing feature is that no amount of reading would have found it.

I built the model with a single equilibrium. Members' practice grew toward one attractor and, whatever you did to the group, it approached that attractor from wherever it started. This is a very natural thing to build and it makes collapse mathematically impossible, which I did not notice until I tried to simulate a group dying and found I could not. I added a Hill-function gate because the relapse literature motivates nonlinear dynamics. The release audit then found that the corrected model's actual endpoint environments rarely support the typical-member bistability I claimed for that gate. Chapter Fourteen now records both corrections.

I had the protective Traditions entering as multipliers that compounded. A group at uniform 0.8 adherence collapsed in every parameterisation I tried, which seemed like a finding until I worked out why: a twenty per cent shortfall passing through four or five multiplications comes out closer to fifty. The adherence terms are averaged within brackets now and applied once each, and Chapter Five's Machinery says so.

I had the recipient resource proportional to the raw number of newcomers, so that a room full of newcomers with nobody to help them registered as a room rich in the thing twelfth-step work consumes. It is now low-practice members per high-practice potential helper. That is still a proxy, not a newcomer or sponsorship measure, because the model stores neither tenure nor matching.

I had newcomer dependence bolted on as a term I inserted by hand, rather than falling out of what each step consumes. The eight-resource derivation replaced it, and the derived version is what Part Four is built on.

I keyed dropout to the mean across all twelve steps, which makes a member who has done Step One and nothing else look identical to a member who has done nothing at all. It is keyed to early-step practice now, which is why Chapter Nineteen's friction term is strongest at low practice. The model records no tenure, so it cannot identify newcomers or veterans.

I calibrated the baseline on a ten-year horizon and then reported thirty-year results from it, so the model was tuned to a group that had not yet finished settling.

I wrote a noise-floor check that used the same seeds on both sides of the comparison, so it measured nothing and reported zero, which looked like a very clean result.

And I quoted Monte Carlo figures to three significant figures from ten seeds. That error was real, but its first repair exposed another. The ten-seed referral-starved result of 0.20 viable and 2.9 members became 0.360 and 9.9 at four hundred seeds under the old model. Then the release audit found that individual capability had been drawn from an uncentred lognormal distribution, silently raising its mean above one. With the distribution corrected to mean one, the four-hundred-seed result is 0.0275 endpoint viability, 0.105 existence, 0.895 closure and 0.51 mean membership. The first change was sampling error; the second was a modelling error. Both are retained here because collapsing them into one correction would hide what each check found.

Every one of those was invisible until something was computed. Reading more history would not have touched any of them.

---

The second kind is a **research error**, and the distinguishing feature is the mirror image: no amount of computation would have found it.

I had the index-pairing conjecture in my head as something worth testing because there are twelve Steps and twelve Traditions. That is not an error, but the way I first framed the result was: I described the failure of index-pairing as a finding on twelve independent counts, when five of the twelve follow from a single prior fact about the governance matrix. Chapter Sixteen now says so and Chapter Eighteen repairs part of it.

I had Hawkins losing two wives, from a secondary site. Maxwell's account has his wife supporting him through withdrawal. She was there the whole time.

I had a Worcester statistic attributed to Maxwell that is not in Maxwell at all. He has better-documented equivalents from Cincinnati, Brattleboro and Vermont, and the Vermont figure is more dramatic than the one I had been using.

I treated Gough's account of his 1845 relapse as defensive, until I read it and found the sentence *I have fallen*.

I attributed the 1858 libel trial to the 1845 relapse. It arose from a dispute about prohibition enforcement, thirteen years later and about something else.

I cited Crothers's 1911 book for the founding rationale of the Sons of Temperance. He does not mention the Sons anywhere. That material is Eddy's, and the misattribution was caught by a checking script on its first run rather than by me.

I said the Washingtonians had no rule against outside issues and therefore no way to decline the temperance movement's turn to legislation. They had two, in print, within two years of founding. Their own manual contains them and I had not read their own manual.

I said Maxwell was precise about all three founding dates. He gives two and then says the pledge was signed the next day.

I said the period's vocabulary distinguished at least eight grades of drinker. Maxwell lists ten.

I said the Traditions were a set of rules. Wilson's own framing sentence says a code of traditions could never become rule or law.

I said the Traditions were adopted at a 1950 international convention. Kurtz dates the adoption to June 1950 and does not connect it to that gathering.

Every one of those became visible the moment a primary source was in front of me, and not one minute before.

---

The third kind is an **institutional error**, and I did not catch it at all.

I built a scenario in which an AA group closes its doors to newcomers. A reader with experience of the fellowship pointed out that Tradition Three makes this impossible: there is no membership decision to close off, because the Tradition removes it. Whatever an unwelcoming group does, it does after the person is already a member. A second correction to the same chapter came later and from anticipating the same reader: I had been using "closed" for that culture, and a closed meeting is a formal and entirely ordinary category in the fellowship, meaning one restricted to people with a desire to stop drinking.

That correction produced Chapter Nineteen, which is now a chapter about retention rather than admission, and it produced a structural test in the appendix showing that the alternative reading makes zero adherence equivalent to a group that admits nobody and dies in every run. The corrected version is better than the original in a way I could not have reached by myself, because the thing I was missing was not in any document.

---

Three kinds, three instruments, and the instruments do not substitute for each other.

The model errors were found by simulation. Specifically, by trying to make the model do something and failing, which is a different activity from checking that it runs.

The research errors were found by reading primary sources at length. Not by checking citations, which would have caught the Crothers misattribution and none of the others, but by reading whole documents and noticing that they did not say what I had them saying.

The institutional error was found by a person with standing I do not have.

If I had done only the first, I would have a well-tested model of a fellowship that does not exist. If I had done only the second, I would have a well-sourced history with a broken model underneath it. If I had done only the third, I would have neither.

---

There is a fourth category that I want to name separately, because it appeared late and it changed how I work.

Several of the errors above were caught by assertions rather than by me. The practice is simple: every number printed in the book is also written into a notebook cell with an assertion that it equals what the computation produces. The point is not that the assertions verify the numbers. It is that writing an assertion forces you to state the relationship you think holds, and stating it is what exposes the ones that do not.

Five errors in this book were caught that way, and every one was a claimed relationship rather than a modelling fault. I wrote that a range of thresholds sat inside another range; it did not, it extended below it at both ends. I wrote that a Tradition stripped of two resources fell to fourth place; it fell to third. I wrote a constant as 0.2769 when it was 0.2269. In each case the sentence was in a draft, the assertion failed on its first run, and the sentence was corrected before anyone read it.

An assertion detects drift, not error. It cannot tell you that a number is wrong, only that it has changed. But an assertion about a *relationship*, of the form "this range contains that one" or "these two figures are equal", is a different instrument, and it catches the thing you were sure of.

---

The last correction is the one I like least, and it is the most recent.

The single most robust comparison in the simulation is between a group starved of referrals and one that has lost only its attraction path. Earlier drafts said that comparison survived 236 quarter-step perturbations and four architectural changes. Those numbers belonged to the retired capability-inflated model and to a narrower sensitivity design.

I never said what worse meant.

The release audit retested five architectures at 400 paired seeds per condition: the base model, a flat step gate, Tradition Three moved to admission, capacity supplied by all members, and unsaturated resource counts. In the corrected model the referral-loss condition has lower existence, lower endpoint viability and lower mean final membership than pure attraction loss in all five. The former three-of-four size reversal does not reproduce. Parameter screens still report strict, tied and reversed draws separately, because agreement across five architectures is evidence over those architectures, not a universal theorem.

That correction is the argument for this whole chapter. A result can change because the model changed, because the estimand changed, or because the earlier audit sampled too narrowly. Keeping the old structural conclusion after changing the capability distribution would have been as misleading as never testing the architecture at all.

---

## The Machinery

### 1. What the model says

Nothing new. This chapter is about the model's history rather than its output, and every figure in it is quoted from the chapter where it belongs.

One structural observation is worth making here because it does not fit anywhere else. Of the nine modelling errors listed above, seven were errors in which the model was **too well behaved**: a single equilibrium so collapse was impossible, a resource that grew without a constraint, a dropout hazard that could not distinguish a beginner from a newcomer, a noise floor of zero. Only two, the compounding multipliers and the ten-seed sampling, made the model behave worse than it should.

That asymmetry is not an accident and it is a hazard worth naming. A model that misbehaves gets debugged, because it is annoying. A model that behaves smoothly is finished. Every one of the seven survived until something specific was demanded of it that it could not do.

### 2. The technical version

The corrections, with what found each one and where the corrected version lives.

| Error | Found by | Now in |
|---|---|---|
| Single equilibrium, collapse impossible | trying to simulate a death | Ch 14, appendix A2 |
| Adherence compounding multiplicatively | a group at 0.8 collapsing everywhere | Ch 5 Machinery, A2 |
| Recipient resource on raw newcomer count | Worcester not reproducing | Ch 1 Machinery |
| Newcomer dependence inserted by hand | the eight-resource derivation | Part Four |
| Dropout keyed to the twelve-step mean | Ch 19's retention question | A2 |
| Baseline calibrated on ten years, reported at thirty | horizon study | A3 |
| Noise floor using the same seeds twice | reading the check | A4 |
| Three significant figures from ten seeds | recomputing at 400 | Ch 1, 2, 4, 14, preface, A4 |
| Uncentred lognormal capability changed both mean and dispersion | release-gate distribution audit | Ch 4, Ch 12, appendix |
| Semantic overlap published as executable coupling | source-to-code trace | Parts Three and Four, paper, appendix |
| Recipient ablation changed several mechanisms | one-mechanism override | Ch 15, primer, appendix |
| T3 and T11 interventions mixed two paths | paired two-by-two factorials | Ch 19, Ch 20, paper |
| Endpoint viability described as survival or death | event-history audit | Ch 1, Ch 2, Part Five, paper |
| One-draw recovery exercise and overclaimed estimator | 25 then 400 replications, claim narrowed | Ch 13 |
| Frozen Chapter 14 environment came from the retired model | re-estimating 400 endpoint environments | Ch 14, paper |
| Composition null narrated as equality | paired intervals and estimand review | Ch 22, paper |
| Exact ties broken by ordinal ranking | competition-rank audit | Ch 16, primer, paper |
| Public notebooks and caches lacked complete dependency identity | release checker and notebook rebuild | both notebooks, all current caches |
| Index-pairing as twelve independent counts | the trivial-count decomposition | Ch 16, Ch 18 |
| Hawkins's two wives | Maxwell, read in full | Ch 1 |
| A Worcester statistic not in Maxwell | Maxwell, read in full | Ch 1 |
| Gough's 1845 account read as defensive | Gough, read at source | Ch 3 |
| The 1858 trial attributed to the 1845 relapse | Gough, read at source | Ch 3 |
| Crothers cited for the Sons of Temperance | the sources checker, first run | Ch 2 |
| The Washingtonians had no rule on outside issues | Grosh 1842, read at source | Ch 1, Ch 2 |
| Maxwell precise about three founding dates | Maxwell, read from a saved copy | Ch 1 |
| Eight grades of drinker | the same | Ch 1 |
| The Traditions described as rules | Kurtz, quoting Wilson | Ch 5 |
| Adoption at a 1950 convention | Kurtz | Ch 5 |
| A group closing its doors | a reader who had been in the rooms | Ch 19, A9 |
| Threshold range containment | a notebook assertion | Ch 18 |
| A rank stated as fourth | a notebook assertion | Ch 17 |
| A constant transcribed as 0.2769 | a notebook assertion | Ch 22 |
| "Worse" undefined in the book's strongest claim | structural variants, appendix A9 | preface, Ch 1, Ch 4, A9 |

The table no longer has the tidy count this chapter once reported. The release-gate audit added
distributional, semantic, estimand and reproducibility errors that cross the earlier categories.
That loss of neatness is itself accurate: code inspection, simulation, source reading,
institutional review and cross-artifact verification caught different classes of failure.

**A count I am not going to give.** How long each error was in the manuscript before it was caught. The progress log carries no dates, so any such claim would be unverifiable, and this project has already written two duration claims it could not support.

### 3. Notes on sources

**This chapter is sourced entirely from `research/progress-log.md`**, which is the running record of corrections, and every entry above is traceable to an entry there. Where the log and my memory disagree, the log wins, and it has won twice.

**Two claims about this project's own history were themselves wrong** and were removed rather than corrected, because there was nothing to correct them to. One asserted a number of shared phrases between two chapters that appears nowhere in the log. One asserted that an error had stood for months, which the log cannot support because it is undated. Both were written by me about my own work, which is the least reliable kind of testimony in this book and the kind a reader can least easily check.

**The institutional correction is reported at one remove and cannot be otherwise.** It came from a reader rather than a document. I have recorded what was said and what it changed, and there is nothing to cite.

### 4. References

**Read in full:**

Nothing new to this chapter. Every source named above is cited in the chapter where the correction landed.

**Cited at a remove:**

Nothing.

**Internal, and reproducible from this repository:**

`research/progress-log.md` for every entry in the table. `model/book-calculations.ipynb` for the assertions that caught three of them. `appendix/APPENDIX.md` A4 for the small-sample errors, A7.3 for the structural variants that split the final claim. `tools/check_book.py` for the sources check that caught the Crothers misattribution.

**What was not read:**

Nothing applicable; this chapter reads only its own project.

# Chapter Twenty-Four: What Would Settle It

The honest position of this book is that it has shown a set of ideas to be consistent and has not shown them to be true.

That is a real distinction and it is not a modest formula. A model with a hundred and eighteen chosen numbers, fitted to nothing, can demonstrate that a mechanism is *available*: that if groups work in a particular way, then certain things follow and certain other things cannot. It cannot demonstrate that groups work that way. No amount of further computation changes that, because the limitation is not computational.

So this chapter is a list of measurements that would. Each one is something somebody could actually do, each has a result that would tell against the book as well as for it, and each is described precisely enough that a reader could start.

They are in order of how much they would settle.

---

**One. A second governance matrix.**

Part Four rests on a table of twelve Traditions against eight group resources, marking which governs the supply of which. One person built it. Every perturbation design in the project takes its pattern of empty cells as given and prices the consequences of that pattern; none can test the pattern itself.

The measurement is this. Give three people the eight resource definitions and the twelve Traditions, without the original table and without Part Four, and ask them to mark which cells are non-zero. Twenty to forty minutes each. Then compare on three things: whether the same five rows come out empty, how many of the ninety-six cells agree, and whether Chapters Sixteen and Seventeen still hold when their computations are rerun on each respondent's matrix.

What would tell against the book: any respondent leaving a different set of rows empty. The two-tier split is what Chapter Eighteen is about and what five of Chapter Sixteen's twelve counts descend from, and if it is one person's reading of twelve sentences rather than a property of the sentences, then a third of Part Four goes.

The form exists, at `research/GOVERNANCE-MATRIX-ELICITATION.md`, and the comparison script does not. This is the cheapest large thing on the list and it has not been done.

---

**Two. Whether rotation breadth predicts anything.**

Chapter Ten's claim is that rotating service through a fixed pool of people gives a floor rather than a decline: as a group grows, a pool of twelve keeps the largest share of influence at roughly one thirty-second regardless of size, while an evenly weighted room's largest share keeps falling. The condition requires falling. So the practical form of the claim is that a group needs to rotate about a quarter of itself, not a fixed dozen, and that this proportion holds at every size tested.

The measurement is a survey of meetings that would take an afternoon per meeting. How many people have held a service position in the last two years, as a fraction of regular attendance. Then set that against something observable about the group: how long it has been running, whether it has split or died, how many of its members are in their first year.

What would tell against the book: no relationship, or a relationship with the headcount rather than the proportion. The second would be the more interesting failure, because the whole of Chapter Ten is the claim that the proportion is what matters.

The obstacle is not difficulty. It is that the quantity is defined at the level of a group and the outcome takes years, so the study is longitudinal and the unit is a meeting rather than a person, which is not how most research in this area is organised.

---

**Three. Whether the steps are worked in order.**

Chapter Thirteen argues from a model in which later steps are gated behind earlier practice, so that a member cannot make progress on Step Nine without Steps Four and Five having happened. The gate contributes to Chapter Fourteen's possible self-reinforcing loop, but the corrected baseline rarely produces the claimed typical-member bistability. It remains a structural choice that requires direct measurement.

The measurement exists in a partial form already. Greenfield and Tonigan asked members which practices they had adopted, using both direct and indirect instruments, and found substantially more people endorsing step work on the indirect measure for nine of twelve steps. What is missing is the ordering: whether the set of steps a member has worked is, as the model requires, an initial segment of the list rather than an arbitrary subset.

That is a simple thing to ask and I have not found it asked. Twelve binary items and a check of how often the answers form a prefix.

What would tell against the book: members commonly reporting later steps without earlier ones. The model's gate would then be describing an ordering that people do not in fact follow, and Chapters Twelve to Fourteen would need rebuilding rather than adjusting.

---

**Four. Group mortality against referral supply.**

Chapter Twenty-One's claim is stated as a mechanism rather than a finding: a group starved of external referrals loses groups and members while established practice among the selected viable remnants can remain high. The corrected trajectories do show shrinking rooms, so the stronger claim that the interior offers no warning has been withdrawn.

The measurement is a natural experiment. Somewhere, a region's treatment or court-referral pipeline has changed sharply, in either direction, within a period for which group counts exist. The prediction now has three separately scored parts: group closures should rise, surviving-room membership should fall, and established practice among remaining members may fall much less or rise through selection. A single average cannot test all three.

The instrument is AA's own service material SMF-132, which reports groups and members by year. Two problems with it, both stated in Chapter Twenty-One. It is worldwide rather than regional, and a count of groups nets births against deaths. What is needed is a regional series with formation and dissolution separated, which area committees hold and nobody has assembled.

What would tell against the model: no differential change in closure or membership after a referral shock, or member-practice measures deteriorating in the same proportion as membership with no selected-remnant pattern. Either result would reject the proposed mechanism more directly than a mismatch in its modeled timing.

---

**Five. Whether the three obstructions look like the three failure modes.**

Appendix A8 established something I had not computed before: whether a concentration of attention obstructs group learning depends on how it scales with the group rather than on how severe it looks. A clique of three giving a tenth of its attention outward holds three per cent of the influence in a group of a thousand and is not an obstruction. The same clique tightening as the group grows is one.

So the empirical question is not "do AA groups have dominant members" but "does the dominance scale". In a room of eighty, does the most-attended person hold roughly what the most-attended person in a room of twenty holds, or roughly a quarter of it?

That is measurable by sociometric survey, which is intrusive and is the wrong instrument for an anonymous fellowship, and I do not have a good suggestion for how to do it ethically. It is on the list because it is the single measurement that bears most directly on the book's central claim, and because saying so is more useful than leaving the claim looking testable when the test is not available.

---

**Six. Anything at all about the model's trajectories.**

Threat two in the appendix says no output of this model has ever been set beside a real group. That is true and it is the largest gap, and it is worth separating what would help from what would not.

Comparing the model's thirty-year membership curve against a real meeting's roll would not help much. The horizon, the arrival rate and the churn floor are three of the hundred and eighteen chosen numbers, and a match would mostly show that three numbers can be chosen to produce a match.

What would help is comparing a prespecified *ordering* against real data. The strongest candidate is the comparison between referral loss and pure attraction loss, scored separately on closure, endpoint existence, endpoint viability and final membership. In the corrected model the referral-loss condition is worse on all three endpoint outcomes in the base architecture and four variants. The expanded parameter screens include ties and reversals, so the empirical study must name its outcome rather than inherit a blanket robustness claim. Chapter Twelve adds a reason to hold it loosely: the few reversals the one-at-a-time screen finds come mostly from large downward moves of three values, and one of them is the decay rate, which nothing measures for a practice. A study that could record how fast practice lapses in the groups it follows would test the ordering and its most fragile assumption together. That is the comparison in item four, and it uses the same measurement.

---

**One case arrived without being asked for.**

Every item above is a measurement somebody would have to go and take. While this book was being finished, a case turned up that nobody took, because it happened on its own and was written down afterwards by the people it happened to.

Recovery Dharma is a Buddhist recovery fellowship whose program book was published in 2023 and read for the comparison in appendix A12. It exists because of a split. Its predecessor was organized around a single named founding teacher, and it fractured in 2019. The account in the book is given by people who held office in the predecessor, including its executive director and a member who ran its retreats and conferences for five years. Her description of the collapse is that the community was heavily influenced, in her words, by "inequities among leaders", and that people were harmed and a sangha was fractured.

What the survivors then built is the part that bears on this book. The executive director's account of the founding says they meant to be deliberate about the framework and that it had to be peer-led. The commitment appears first in the meeting script every group reads aloud: the fellowship is peer-led and follows no one leader or teacher, and the person running the meeting says plainly that they hold no particular authority. A fellowship that had just watched authority concentrate in one figure responded by abolishing the office that concentrated it.

That is Tradition Two and Tradition Nine arrived at independently, eighty-four years after AA, by people who had never heard of this argument and had no reason to care about it. It is the closest thing to a live test the book has, and it is worth being exact about how little it settles. It is a single case. It is testimony rather than measurement, written by participants in their own founding literature, which is the genre most likely to make a decision look more principled in hindsight than it was. It does not touch the mathematics, and it says nothing at all about item five's real question, which is whether dominance *scales* with the size of the room. What it does is remove one specific comfort: the objection that no group has ever actually restructured itself around this problem, and that the reading of Traditions Two and Nine is therefore a pattern I imposed on a text. At least one fellowship did restructure itself around this problem, at considerable cost, and reached for the same two answers.

I would have preferred to find this before the argument was written rather than after. Its full treatment, including the parts that cut the other way, is in appendix A12.

---

There is a pattern in the six and it is worth naming.

Four of them require data about *groups*, not about people: which cells a reader marks, what proportion of a group rotates, how many groups exist in a region and for how long, how attention is distributed in a room. Almost all research on AA is about members, because members are who show up in clinical trials and who can be followed.

The book is about the group. The literature is about the member. That mismatch is why so much of this book is a model rather than an analysis, and it is the single most useful thing a researcher could change about the field it sits in.

---

## The Machinery

### 1. What the model says

Nothing new here, and that is the point of the chapter. Every item above is a place where the model makes a claim that the model cannot check.

One thing the model does contribute is the *form* of the claims, and the form matters for testability. Some claims are endpoint orderings, some are deterministic matrix comparisons, and the rotation result is a scaling condition from a theorem. They do not share one sensitivity result. An ordering can be cheaper to test than a magnitude because it may require only a monotone instrument, but its outcome and conditioning still have to be fixed in advance.

### 2. The technical version

For each item, the claim, the design, and the result that would falsify it.

| # | Claim | Design | Falsified by |
|---|---|---|---|
| 1 | Five Traditions govern no consumed resource | three independent elicitations of the 12 by 8 matrix | any respondent leaving a different set of rows empty |
| 2 | Rotation must scale with the group, at about a quarter | cross-sectional survey of rotation proportion against group age and survival | a relationship with headcount rather than proportion, or none |
| 3 | Step practice is an initial segment, not a subset | twelve binary items, tested for prefix structure | later steps commonly reported without earlier ones |
| 4 | Referral loss raises closure and shrinks viable remnants while selected established practice changes less | regional formation, dissolution, room-size and practice series around a referral shock | no differential closure or membership effect, or proportional practice deterioration with no selected-remnant pattern |
| 5 | Concentration obstructs only when it scales | sociometric attention shares across rooms of different sizes | the largest share roughly constant in absolute terms across sizes |
| 6 | The orderings hold outside the model | any of the above | any reversal |

**Item 1 is the only one that could be done this month**, needs no institution, no funding and no access, and directly tests the thing three chapters rest on.

**Items 2, 4 and 5 need a unit of analysis the field does not use.** Groups rather than members.

**Item 3 is closest to being already done.** Greenfield and Tonigan's instrument would need one additional analysis rather than a new study. The paper has now been read in full, so this chapter's description of it no longer rests on an abstract, and reading it strengthens the case: their two-factor structure means the additional analysis is not merely possible but has an obvious form, since behavioural and spiritual step-work already separate and could be scored per step rather than summed.

### 3. Notes on sources

**This chapter proposes rather than reports and should be read as a research agenda.** Nothing in it is a finding. The Recovery Dharma case added at the end is the one piece of reported material, and it is testimony rather than measurement: a single fellowship's account of its own founding, written by participants, in its own program literature. It corroborates and cannot confirm. It is placed in this chapter rather than in the argument chapters precisely because this is where the book says what it has not established.

**One claim here still rests on material I have not read.** SMF-132 is described from AA's own catalogue entry and has not been obtained; its structure is inferred from the title and description rather than from the document. Greenfield and Tonigan (2013) was in the same position until 10 August 2026 and has since been read in full, which is what allows this chapter to say what could be added to the instrument rather than only that the instrument exists.

**One item has no method.** Item five names the measurement that would bear most directly on the book's central claim and then says I do not know how to take it ethically in an anonymous fellowship. I would rather have a gap on the list than an item that pretends to be actionable.

**What I have not done.** I have not searched systematically for existing work on any of the six. The literature searches behind this book were driven by specific chapter needs, and a proper review might well find that items three and four have been partly answered by somebody. If they have, this chapter is wrong to list them.

### 4. References

**Read in full:**

Recovery Dharma Global (2023). *Recovery Dharma: How to use Buddhist practices and principles to heal the suffering of addiction.* Second edition. Recovery Dharma Inc. CC BY-NC-SA 4.0. Stored in `research/incorporated/RecoveryDharma_2023/`. Source of the 2019 split described above, which is reported in the personal recovery stories of Section II by people who held office in the predecessor organization, and of the peer-led commitment in the meeting script at printed pages 147 and 151. The named individual at the centre of the predecessor's collapse is named in that source and is deliberately not named here; the structural point does not require it and this book has no way to adjudicate an allegation about a living person. Appendix A12 carries the full comparison, including the material that cuts against this chapter's use of it.

**Cited at a remove:**

Greenfield, B. L. and J. S. Tonigan (2013). "The General Alcoholics Anonymous Tools of Recovery: The Adoption of 12-Step Practices and Beliefs." *Psychology of Addictive Behaviors* 27(3): 553-561. **Read in full**; the NIH author manuscript, PMCID PMC3707937, obtained 10 August 2026 and stored in `research/incorporated/Greenfield_Tonigan_2013/`. Used here for the existence and structure of the instrument and for what a further analysis of it could yield.

Alcoholics Anonymous World Services, SMF-132, "Estimated Worldwide A.A. Individual and Group Membership." Located, not acquired. See `research/SOURCES.md`.

**Internal, and reproducible from this repository:**

`research/GOVERNANCE-MATRIX-ELICITATION.md` for item one. `appendix/APPENDIX.md` A7 for the threats each item addresses, A8 for the scaling result behind item five, A9 for the structural variants behind item six.

**What was not read:**

Any systematic review of research on mutual-aid group survival, rotation of service, or attention structure. The six items are drawn from what this book needs rather than from what the field has already tried, and that is a real weakness of the chapter.

# Chapter Twenty-Five: What a Model Cannot Tell You

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

---

There is a person who answered this book's question before I asked it, and answered it differently, and he had better standing to do so than anyone.

Ernest Kurtz wrote the history of Alcoholics Anonymous. He had the archives in New York and Akron, he interviewed the surviving old-timers, he listened to the tapes. In a talk given about 1984 he says that at the end of those interviews the old-timers would turn the question back on him: how long will AA last, is it changing so that in another fifty years it will no longer be AA, is it still AA now.

That is Maxwell's question and it is mine. Kurtz's answer contains no structure at all.

He says AA lasts so long as somewhere a sober alcoholic, meeting another alcoholic, drinking or sober, sees not a believer or an unbeliever, not a Baptist or a Catholic, not a man or a woman, but another alcoholic he has to reach out to in order to stay well himself. That is the whole of it. No Traditions, no rotation, no anonymity as a structural device. The historian with the fullest access anyone has had to the record locates the fellowship's survival in the character of a single encounter.

I do not think he is wrong, and I do not think it contradicts anything computed here. A model of resource supply and influence weighting is a description of the conditions under which that encounter keeps being available to people, and Kurtz is describing the thing the conditions are for. Both can be true.

But I notice that his answer is the one that would console someone and mine is not, and that this is not an accident of temperament. He was asked by people who had built the thing and wanted to know if it would survive them. I was asking whether a theorem applies. Those questions have different right answers, and a reader who came here for his and got mine should know that the substitution happened and that it was mine, not his, that narrowed.

---

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

Kurtz, E. (about 1984). "A Talk About the History of Alcoholics Anonymous From the Letters of Bill Wilson." Undated recorded talk; transcript restored by historyofrecovery.com. Read in full 10 August 2026. Source of the closing question put to Kurtz by the old-timers and of his answer to it. The year is inferred from internal evidence and must always be given as "about"; the basis is recorded at `research/incorporated/KurtzTalk_c1984/citation.md`.

**Cited at a remove:**

Wilson's letters, throughout the Kurtz talk. Kurtz quotes them from memory and without page citations, so nothing attributed to Wilson through that talk has been checked against a letter.

**What was not read:**

**The previous version of this paragraph is withdrawn.** It said that nothing written by the fellowship about itself for its own members had been read, that the project does not acquire such material, and that at no point does the institution speak here in its own voice. That was true when written and is no longer. *Twelve Steps and Twelve Traditions* was read in full on 10 August 2026, and it changed Chapters Eight, Ten and Sixteen: it supplied the book's own thesis in Wilson's words, the best objection to that thesis, and the disproof of the index pairing. The institution now speaks in its own voice in three chapters, and the book is better for it.

The lesson is not that the earlier policy was cowardly but that it was imprecise. A rule against *holding* copyrighted material is a copyright rule and this project keeps it: nothing is stored, nothing is committed, nothing is quoted at length. A rule against *reading* it was never a copyright rule at all, and it cost the argument three chapters' worth of evidence, including the one finding that most damages the book's own case.

What genuinely remains unread is most of the canon: the Twelve Concepts of World Service, the service manual, the daily reflections, and seventy years of *Grapevine*. Each is available and none has been opened.


\clearpage
\thispagestyle{empty}
\vspace*{0.32\textheight}
\begin{center}
{\Large\bfseries Appendices}
\end{center}
\clearpage

# Technical Appendix

*Nobody in Charge.* Released model specification, estimands, numerical checks, sensitivity
designs, source boundaries, and reproduction instructions.

Author: Anonymous. Released to the public domain under The Unlicense. See `../LICENSE`.

This appendix describes the release-gate model identified by SHA-256:

```text
c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952
```

The executable source `model/aa_group_model.py` and hash-linked JSON caches are authoritative.
This document and the PDF are derived artifacts. No simulation parameter is estimated from AA
data.

Part Two uses a published theorem and deterministic arithmetic over authored matrices. The
stochastic group model supports Parts Three and Five and some comparisons in Part Four; it is
not evidence about an individual person's recovery.

---

## A1. Claim classes and scope

The project contains three objects that must not be collapsed.

1. `B = S GOV^T` is raw semantic overlap between two author-coded matrices. It describes which
   Step-resource and Tradition-resource codes overlap.
2. `C = Snorm GOVW^T` is the normalized, no-capacity linear map from effective adherence to Step
   resource bundles.
3. The executable response adds effective-adherence rules, member-side capacity, clipping,
   nonlinear growth gates, stochastic entry and exit, and the current member state.

Neither `B` nor `C` is a transition matrix or a simulated trajectory effect. Part Four's
historical interpretation of the matrices is an authored operationalization, not a theorem and
not something the simulation discovered.

The modeled room has capacity 60. The release did **not** increase membership to 400 or 1,000.
Confirmatory stochastic comparisons use 400 seeds, paired when conditions share a seed.
Robustness was increased by adding parameter points, perturbation distances, structural
variants, horizons, integration steps, and screening trajectories.

---

## A2. Executable model

### A2.1 State and initial condition

At time `t`, `X` is a `cap x 12` matrix with entries in `[0,1]`; row `i` holds one living
member's twelve practice states. `alive` marks occupied rows. Each member has a fixed positive
growth multiplier `h_i`.

The default run begins with 25 founders, all twelve states equal to 0.55. Arrivals enter with
all states equal to 0.02. Time is integrated by explicit Euler in half-week steps. The reported
horizon is 1,560 weeks, or thirty years.

The practice scale is cardinal only inside the model. It has no validated clinical unit and
does not measure sobriety, harm, tenure, sponsorship, or recovery quality.

### A2.2 Step-resource matrix

The eight resources are admission, identification, living proof, confidentiality, counsel,
recipient opportunity, continuity, and gentle pressure. Rows are Steps 1 through 12.

```text
S =
0.8 1.0 0.3 0.0 0.0 0.0 0.2 0.1
0.0 0.4 1.0 0.0 0.1 0.0 0.2 0.0
0.0 0.0 0.2 0.0 0.3 0.0 0.1 0.1
0.0 0.1 0.0 0.0 0.3 0.0 0.0 0.4
0.0 0.1 0.0 1.0 0.3 0.0 0.2 0.1
0.0 0.0 0.1 0.0 0.2 0.0 0.0 0.3
0.0 0.0 0.1 0.0 0.1 0.0 0.0 0.2
0.0 0.0 0.0 0.1 0.4 0.0 0.0 0.3
0.0 0.0 0.0 0.3 0.9 0.0 0.1 0.2
0.0 0.0 0.0 0.1 0.2 0.0 0.5 0.7
0.0 0.0 0.1 0.0 0.1 0.0 0.2 0.4
0.2 0.1 0.1 0.0 0.1 1.0 0.6 0.3
```

For Step `j`, `Snorm[j,:]` divides its row by the row sum. Group dependence is

```text
beta[j] = row_sum(S[j,:]) / max_k row_sum(S[k,:]).
```

Both are re-derived after any perturbation to `S`.

### A2.3 Tradition-governance matrix

Rows are Traditions 1 through 12 and columns are the eight resources in the same order.

```text
GOV =
0.2 0.5 0.3 0.3 0.2 0.1 0.9 0.6
0.0 0.0 0.0 0.1 0.9 0.0 0.2 0.2
1.0 0.4 0.0 0.0 0.0 0.8 0.1 0.0
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
0.1 0.4 0.5 0.0 0.0 0.9 0.3 0.2
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
0.0 0.1 0.1 0.3 0.1 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
0.0 0.2 0.7 0.0 0.0 0.6 0.2 0.0
0.1 0.3 0.0 1.0 0.1 0.0 0.1 0.0
```

`GOVW` divides each column by its positive column sum. Consequently, at full adherence the
governance quality of every resource is exactly one whatever the 35 nonzero magnitudes in
`GOV`. That cancellation is algebra. It does not apply at partial adherence and says nothing
about whether the structural zeros belong where the author placed them.

### A2.4 Effective adherence

Traditions 4, 6, 7, 9, and 10 have zero rows in `GOV` and act only as protective modifiers.
Using one-based Tradition labels:

```text
Te[2] = T[2] * (0.6 + 0.4 * mean(T[9], T[12]))
Te[5] = T[5] * (0.6 + 0.4 * mean(T[6], T[10]))
ext   = 0.7 + 0.3 * mean(T[4], T[7])
Te    = clip(Te * ext, 0, 1)
q     = GOVW^T Te
```

Protective effects are applied once. They are not repeatedly multiplied through the model.

### A2.5 Member-side resource capacity

Let `lv_i` be member `i`'s mean over the twelve states. Established members satisfy
`lv_i > act_thr`; experienced members satisfy `lv_i > exp_thr`. Define

```text
sat(c,k) = c / (c+k)
unity    = clip(1 - 2 * sd(lv among established members), 0, 1)
```

The eight capacity terms are

```text
admission       1
identification  sat(n_established, k_ident) * unity
proof           sat(n_experienced, k_proof)
confidential    sat(n_experienced, k_conf)
counsel         sat(n_experienced, k_couns)
recipient       sat(n_low_practice / max(n_experienced,1), k_recip)
continuity      (0.45 + 0.55 * solvent) * unity
pressure        unity
```

`R = clip(capacity * q, 0, 1)`. Solvency is established-member contributions divided by rent,
clipped at one.

The recipient term is opportunity per high-practice potential helper. Low-practice and
high-practice are state thresholds, not newcomer and veteran cohorts. The model has no tenure
or matching state. The clean recipient experiment replaces only this capacity term.

### A2.6 Step growth and depreciation

For member `i` and Step `j`:

```text
bundle_j = Snorm[j,:] R
order_gate_1 = 1
order_gate_j = X[i,j-1]^p_gate, j > 1
peer_j = (1-beta_j) + beta_j * bundle_j

own_i = M_i^hill_n / (hill_k^hill_n + M_i^hill_n)
M_i   = mean(X[i,9:12])              zero-based slice: Steps 10 through 12
group_capacity = mean(own_i among living members)
capacity_i = own_i + (1-own_i) * omega * group_capacity

w_j = linear sequence from 0.05 at Step 1 to 1 at Step 12
capacity_gate_ij = 1 - w_j * (1-capacity_i)
growth_ij = a_j * order_gate_ij * peer_j * capacity_gate_ij * h_i

decay_ij = delta0 * (1 + psi * (1-X[i,j+1])) for j < 12
decay_i12 = delta0
dX_ij/dt = growth_ij * (1-X_ij) - decay_ij * X_ij
```

Capability uses the mean-one lognormal draw

```text
h_i = exp(N(-het_sd^2/2, het_sd)).
```

Changing `het_sd` therefore changes dispersion without mechanically changing arithmetic mean
capability. The previous uncentred draw did both and all caches from it are retired.

### A2.7 Membership flow and split Tradition paths

Exit hazard is

```text
early_i = mean(X[i,0:3])              zero-based slice: Steps 1 through 3
low_practice_weight_i = exp(-6 * mean(X[i,:]))
t3_friction_i = 1 + (1-dropout_T3) * low_practice_weight_i
hazard_i = drop0 * exp(-drop_k * early_i) * t3_friction_i + churn.
```

Arrivals are Poisson with half-week mean `lambda * dt`, where

```text
lambda = lam_exog + lam0 * sum_i X[i,12] * attraction_T11.
```

Tradition 3 has distinct resource-governance and inverse-practice dropout-friction paths.
Tradition 11 has distinct resource-governance and attraction paths. The main factorials change
each separately and jointly. The headline referral comparison uses pure attraction loss with
Tradition 11 governance held intact.

Exit is evaluated before arrival. Once membership reaches zero, the group closes permanently
and no same-step exogenous arrival can reopen it.

---

## A3. Default values and authored choices

| Quantity | Default |
|---|---:|
| Step speeds `a` | 0.30, 0.25, 0.25, 0.18, 0.22, 0.20, 0.20, 0.18, 0.15, 0.25, 0.20, 0.22 |
| `delta0`, `psi`, `p_gate` | 0.06, 0.20, 1.5 |
| `hill_n`, `hill_k`, `omega` | 3.0, 0.12, 0.75 |
| `k_ident`, `k_proof`, `k_conf`, `k_couns`, `k_recip` | 3, 3, 2, 3, 2 |
| `act_thr`, `exp_thr` | 0.10, 0.50 |
| `lam0`, `lam_exog` | 0.050, 0.12 per week |
| `churn`, `drop0`, `drop_k` | 0.004, 0.035, 4.0 |
| `cap` | 60 |
| `cost`, `contrib` | 50, 2 per week |
| `het_sd` | 0.55 |

The registered sensitivity set contains 22 scalar defaults, 12 step speeds, 49 nonzero `S`
cells, and 35 nonzero `GOV` cells, for 118 values. These are **registered sensitivity values**,
not all parameters or all choices. The separate inventory also records fixed coefficients,
108 structural zeros, equations, thresholds, initial conditions, and experiment-design choices.

The original inflow and exit values were selected to target approximately 45 members and 9
experienced members. That target fails under the corrected capability distribution: mean final
membership is 17.80; among viable endpoints, the mean established count is 14.13 and the mean
experienced count is 1.25. The parameters were not retuned after observing the failure.

---

## A4. Estimands and uncertainty

The release distinguishes:

- endpoint existence: `N > 0`;
- endpoint viability: `N > 5`;
- permanent closure: `N = 0`;
- final membership, with closed runs contributing zero;
- first crossing at or below five members;
- first recovery above five after a crossing;
- all-member practice;
- established-member practice, conditional on the stated population.

A run may cross below viability and recover. Endpoint nonviability is not closure. A statement
about members in viable groups is selected on the group remaining viable and is printed beside
the viable fraction.

Principal stochastic estimates use seeds 0 through 399. Continuous condition means use normal
95 per cent intervals. Paired continuous contrasts retain common random numbers. Binary
condition intervals are Wilson intervals; paired binary contrasts use paired risk differences
and exact McNemar tests in the cache. Three- and five-seed parameter points are screens, not
independent replications and not confirmatory estimates.

---

## A5. Confirmatory results

### A5.1 Conditions and mechanism factorials

| Condition | Final N, mean [95% interval] | Exists | Viable | Closed |
|---|---:|---:|---:|---:|
| Baseline | 17.800 [16.917, 18.683] | 1.000 | 0.985 | 0.000 |
| T3 friction loss only | 14.838 [13.910, 15.765] | 0.9925 | 0.940 | 0.0075 |
| T3 governance loss only | 11.773 [11.149, 12.396] | 0.980 | 0.9125 | 0.020 |
| T3 combined loss | 6.755 [6.170, 7.340] | 0.750 | 0.5475 | 0.250 |
| T11 attraction loss only | 12.380 [12.038, 12.722] | 1.000 | 0.985 | 0.000 |
| T11 governance loss only | 15.515 [14.809, 16.221] | 1.000 | 0.980 | 0.000 |
| T11 combined loss | 11.920 [11.584, 12.256] | 1.000 | 0.985 | 0.000 |
| Recipient capacity forced to one | 18.828 [17.782, 19.873] | 1.000 | 0.9875 | 0.000 |

Paired final-membership losses from baseline are 2.962 [1.848, 4.077] for T3 friction,
6.027 [5.043, 7.012] for T3 governance, and 11.045 [10.030, 12.060] jointly. The T3 factorial
interaction is -2.055 [-3.414, -0.696], so path effects are not additive.

The T11 losses are 5.420 [4.515, 6.325] for pure attraction, 2.285 [1.214, 3.356] for
governance, and 5.880 [4.972, 6.788] jointly. The interaction is 1.825 [0.755, 2.895].

Forcing only recipient capacity to one changes final membership by 1.028 [-0.259, 2.314]. The
interval crosses zero, so the clean recipient ablation is unresolved.

### A5.2 Service, composition, and the Tradition ranking

Disabling Step 12 lowers final membership by 5.325 [4.437, 6.213], established practice by
0.01497 [0.00765, 0.02229], and maintenance capacity by 0.01351 [0.00788, 0.01915]. The isolated
Step 9 change is 0.00550 with an interval from -0.00149 to 0.01249 and is unresolved.

The founder-composition experiment holds total initial practice at 13.75 and compares even,
concentrated, and split allocations. Relative to even founders, paired final-membership
differences are 0.2925 [-0.898, 1.483] and -0.3475 [-1.472, 0.777]. No equivalence margin was
specified, so this is unresolved rather than evidence of equality. The model has no mentoring,
sponsorship, clique, or sorting mechanism.

At twenty years with all Traditions at 0.85 and one lowered to 0.50, reference membership is
13.0975 with cross-seed SD 5.666. Seven of twelve paired contrasts exclude zero. Tradition 3
and Tradition 11 are mixed adherence interventions in this ranking; mechanism-specific results
come from the factorials above.

### A5.3 Chapter 14 correction

The original typical-member bistability result used a frozen environment from the retired
capability-inflated model. Recomputed from 400 corrected full-adherence endpoints, capability-one
high and low starts separate by more than 0.05 in only 7 environments, or 1.75 per cent. In the
mean corrected environment both starts converge to negligible maintenance. The architecture can
generate bistability in some environments; typical-member bistability is not a released baseline
result.

### A5.4 Trajectories and selection

Under referral loss, all-run membership is 21.55 at year 5, 11.68 at year 10, 2.50 at year 20,
and 0.51 at year 30. Endpoint viability falls from 0.970 to 0.660, 0.1725, and 0.0275. Membership
among viable groups also falls, from 22.07 to 16.47, 11.39, and 12.27. The last mean is based on
only eleven viable runs and has half-width 3.81. The corrected model therefore shows visible
room-size decline as well as closures. Established practice among selected viable remnants stays
high; that selected quantity is not evidence that the interior has no warning signal.

---

## A6. Numerical resolution and horizon

At the baseline thirty-year horizon, mean final membership is 17.80 at `dt=0.5`. In 200 paired
seeds, changes relative to that step are 1.535 plus or minus 1.777 at `dt=1`, 0.865 plus or minus
1.836 at `dt=0.25`, and -0.405 plus or minus 1.742 at `dt=0.125`. All intervals cross zero. This
supports the tested half-week resolution for the reported comparisons; it does not prove
convergence at arbitrary resolution.

Mean final membership is 29.34 at 10 years, 21.14 at 20, 17.80 at 30, 16.43 at 50, and 15.64 at
100. The 100-year series includes one closure in 200 runs. Because the horizon series continues
to move, the release makes no steady-state or indefinite-persistence claim.

---

## A7. Expanded sensitivity and structural robustness

### A7.1 Design registry

| Design | Size | Seeds per parameter point | Purpose |
|---|---:|---:|---|
| Global simultaneous perturbation | 1,002 draws, 334 at each amplitude | 3 | broad joint screen at 12.5%, 25%, and 50% |
| Tiered perturbation | 1,000 draws | 3 | ranges tied to evidential status |
| Randomized nonzero matrices | 1,000 draws | 3 | magnitude test with sparsity fixed |
| Multi-level one-at-a-time | 944 points | 3 | 118 values, two directions, four distances |
| Morris | 20 trajectories, 2,380 points | 5 | factor screen; interaction or nonlinearity not separated |
| Sobol | 1,024 base rows, 11,264 points | 5 | conditional decomposition on eight Morris leaders |
| Structural variants | 10,000 simulations | 400 | five architectures by five scenarios |

Multiplicative designs cannot move structural zeros. A full-adherence outcome cannot reveal the
35 `GOV` magnitudes because they cancel. The randomized-matrix design holds sparsity fixed and
therefore tests magnitudes, not where zeros belong.

### A7.2 Global screen

Counts are strict/tied/reversed for pure-attraction-loss minus referral-loss outcomes.

| Amplitude | Final N | Endpoint viability | Existence | Full model viable in all 3 seeds |
|---|---:|---:|---:|---:|
| 12.5% | 301/0/33 | 323/10/1 | 318/16/0 | 302/334 |
| 25% | 251/1/82 | 269/64/1 | 262/72/0 | 291/334 |
| 50% | 213/17/104 | 201/117/16 | 215/117/2 | 256/334 |

The comparison is most stable on existence and least stable on final membership. Even at the
mildest amplitude, no blanket statement that every outcome survives is correct.

### A7.3 Structural variants

Four one-choice variants are compared with the base architecture: a flat rather than
step-phased capacity gate; Tradition 3 moved from retention friction to admission; capacity
supplied by all living members; and a piecewise-linear, clipped capacity response in place of
the hyperbolic response. The last variant still saturates at one despite its historical
`no_saturation` filename.

| Architecture | Attraction loss N / exists / viable | Referral loss N / exists / viable |
|---|---:|---:|
| Base | 12.380 / 1.000 / 0.985 | 0.510 / 0.105 / 0.0275 |
| Flat gate | 6.613 / 0.870 / 0.6575 | 0.745 / 0.120 / 0.0550 |
| T3 on admission | 12.380 / 1.000 / 0.985 | 0.510 / 0.105 / 0.0275 |
| Capacity from all members | 14.730 / 1.000 / 1.000 | 2.003 / 0.2575 / 0.1225 |
| Piecewise-linear capacity | 13.038 / 1.000 / 0.995 | 1.020 / 0.145 / 0.0575 |

Referral loss is worse on final membership, existence, and endpoint viability in all five
tested architectures. The earlier three-variant size reversal came from the retired uncentred
capability model and does not reproduce. Five architectures are not every possible architecture.

### A7.4 Tiered and randomized-matrix screens

| Design | Final N | Endpoint viability | Existence | Full viable in all 3 seeds | Full exists in all 3 seeds |
|---|---:|---:|---:|---:|---:|
| Tiered, 1,000 draws | 783/10/207 | 818/165/17 | 821/177/2 | 833/1,000 | 943/1,000 |
| Random nonzero matrices, 1,000 draws | 1,000/0/0 | 1,000/0/0 | 999/1/0 | 784/1,000 | 1,000/1,000 |

Counts are strict/tied/reversed for pure-attraction-loss minus referral-loss. Randomizing every
nonzero matrix magnitude while preserving the zero pattern leaves the comparison intact on all
three outcomes. The tiered design, which also varies scalar defaults and Step speeds over wider
ranges, produces substantial final-membership reversals and smaller numbers of viability and
existence reversals. These are different robustness questions.

### A7.5 Multi-level OAT, Morris, and Sobol results

All three caches are complete and match both the model hash and their generating-script hashes.
The generated tables live in `research/ROBUSTNESS-RESULTS.md`; this section states what they mean
and what they do not license.

**Multi-level one-at-a-time screen** (`research/oat_full.json`). Each of the 118 registered values
is moved alone by 10, 25, 50 and 75 per cent in each direction, giving 944 perturbation points,
with three common seeds per endpoint. This is a screen, not a confirmatory design. Across the 944
points the pure-attraction-loss minus referral-loss ordering is strict in 931, tied in 2 and
reversed in 11 on final membership; 934/10/0 on endpoint viability; and 933/11/0 on existence.
Full adherence is endpoint-viable in all three seeds at 893 of 944 points and exists in all three
at 936. The eleven membership reversals are not scattered: nine are large downward moves of
`p_gate`, `delta0` and `churn` at the 25, 50 and 75 per cent distances, and the remaining two are
the `S:11,5` and `S:11,6` cells. Twenty-six of the 118 values move the referral-starved endpoint
viability on their own, and 32 move the full-adherence endpoint viability.

Against a full-adherence baseline of 18.67 members, 0.2261 practice and 0.0431 maintenance, the
ordering exponent `p_gate` has the largest single influence on all three outcomes. At plus or
minus 25 per cent its maintenance range is 5.45 times baseline, `delta0` 3.27 and the step-10
speed 2.22; over the whole four-distance ladder the figures are 14.64, 12.98 and, for `het_sd`,
4.69.

All 35 governance cells return zero change in every outcome and every scenario, with a maximum
absolute deviation of 5.6e-17. This is a property of the reference point and not evidence of
inertness: the OAT scenarios run at full adherence, where the column-normalised governance quality
is identically 1 regardless of the underlying magnitudes. A multiplicative screen also cannot move
a structural zero. Both facts are why the Morris and Sobol designs are sited at 0.85 adherence.

**Morris screen** (`research/morris.json`). Twenty trajectories over all 118 factors at plus or
minus 25 per cent, four levels, delta 2/3, five common random numbers per point, 2,380 model
evaluations, reference adherence 0.85. Effects are output change per unit proportional change in
the parameter. The membership `mu_star` leaders are `p_gate` 52.44, `delta0` 51.21, `churn` 33.48,
`drop_k` 24.30, `lam_exog` 23.46, `het_sd` 18.90, `a:5` 18.54 and `a:11` 15.87. The ninth factor,
`lam0`, is 14.34, so the eight-factor cut is untied. By share of total membership `mu_star`, the
22 scalars carry 44.9 per cent, the 49 `S` cells 33.7, the 12 step speeds 18.2 and the 35 `GOV`
cells 3.3. Five of the eight leaders have `sigma/mu_star` above one, which indicates interaction
or curvature without separating them; that separation is what the Sobol design is for.

This screen corrects the retired ten-trajectory result. Three of the factors previously carried
into the Sobol design do not survive: `a:8` now ranks fifteenth, `a:4` twenty-seventh and `omega`
thirty-seventh. They are replaced by `lam_exog`, `a:5` and `a:11`.

**Sobol decomposition** (`research/sobol.json`). Saltelli first-order and Jansen total-order
estimators on a 1,024-row base design over the eight Morris membership leaders at plus or minus
25 per cent, reference adherence 0.85, five common random numbers per point. The executed cache is
11,264 evaluations: 1,024 each for A, B and the noise replicate, plus 8,192 cross-matrix rows.
Intervals are 2,000-resample percentile bootstraps over base rows. The noise-replicate total-order
floor is 0.0429 for membership and 0.0728 for practice.

Membership total-order indices are `p_gate` 0.576 [0.510, 0.643], `delta0` 0.373 [0.320, 0.428],
`drop_k` 0.171 [0.145, 0.199], `churn` 0.132 [0.111, 0.155], `het_sd` 0.079 [0.064, 0.095],
`lam_exog` 0.058 [0.049, 0.068], `a:11` 0.038 [0.031, 0.046] and `a:5` 0.029 [0.024, 0.034]. The
last two lie at or below the noise floor and are not separated from Monte Carlo error. The
total-order indices sum to 1.456 for membership and 1.464 for practice; the excess over one is
interaction counted once per participating factor, so interaction is present and is not dominant.

The eight-fold increase in base sample repairs the membership first-order column and not the
practice column. On membership no factor has `S1` above `ST` and the first-order indices sum to
0.693, so the column is admissible: `p_gate` resolves at 0.404 [0.288, 0.525] and `delta0` at
0.238 [0.156, 0.327], and the other six have intervals covering zero and are unresolved rather
than zero. On practice `delta0` returns `S1 = 0.421` against `ST = 0.417`, violating the identity
`ST >= S1`, and the practice first-order indices sum to 1.074, which a first-order sum cannot do.
The practice first-order column is therefore still withheld and no number from it is quoted.

The decomposition is conditional on these eight factors and these ranges. The other 110 registered
values are held at nominal, so this is the variance those eight generate between them and not the
model's total variance. The `mu_star` shares above remain the right place to look for the latter.

### A7.6 Resource-list test

The eight group resources are an author-coded list: admission, identify, proof, confidential,
counsel, recipient, continuity, and pressure. No source proposes them, so the question is whether
Part Four's conclusions depend on that particular eight. `model/resource_list_test.py` rebuilds the
raw semantic overlap `B = S @ GOV.T` under 64 alternative lists and re-runs the index-pairing test
on each, using competition rank and complete maximizing sets. The object is semantic overlap, not
executable coupling, and the test is deterministic, so it carries no interval.

| Variant family | Count | All-twelve rejection holds | Unity leads | Protective set unchanged |
|---|---:|---:|---:|---:|
| Leave one resource out | 8 | 7 | 8 | 8 |
| Merge a pair of resources | 28 | 20 | 28 | 28 |
| Drop two resources | 28 | 21 | 27 | 28 |

Unity leads on 63 of the 64 variants. The single failure is the drop-two variant that removes
continuity and pressure together, which is the same pair the reassignment test in A8 identifies as
the only transfer able to flip the result. Two instruments built for different purposes fail on the
same two columns, which is worth more than either alone because it localizes the point of failure.

The all-twelve rejection of index-pairing survives in 48 of the 64 variants. The five protective
Traditions keep empty governance rows in all 64, which is a structural consequence of the authored
zeros rather than an independent confirmation. Where the all-twelve rejection fails it is almost
always Step 1 regaining its index-mate, in 15 variants across the three families. The finding is
therefore that the pairing verdict is not an artifact of any single resource, and not that the list
is correct.

---

## A8. Part Two and deterministic coupling tests

Golub and Jackson's theorem concerns the maximum stationary influence weight in a sequence of
networks. Under its regularity conditions, naive learning aggregates information if and only if
that maximum influence vanishes as group size grows. The theorem is published mathematics. The
claim that Traditions 2, 9, and 12 operationalize its assumptions is this project's unverified
reading.

The deterministic Part Two notebook checks finite-group influence, scaling of rotation pools,
the three obstruction constructions, and random-network controls. These are not runs of the
stochastic membership model. The matrices in Part Four reject index-pairing on the authored
values, but five of the twelve rejections are forced by structural zeros. Threshold and sparsity
tests are required where multiplicative perturbation is blind. Under wholesale randomization of
nonzero coupling magnitudes, the all-twelve index-pairing rejection holds in 40.6 per cent of
draws. The magnitude claim therefore needs substantive defense and independent elicitation.

---

## A9. Source and corpus boundary

`research/SOURCES.md` is the current evidence ledger. Maxwell (1950) and Golub and Jackson
(2010) were already used by the project and are stored under `research/incorporated/`. The
Maxwell copy remains a retyped reproduction with visible transcription errors, not a journal
scan; moving it did not upgrade its source status.

`research/staged/` is a supplied next-round corpus. Its remaining items have intentionally not
been incorporated into the manuscript or paper. File presence is not evidence that a source was
read or used. A verifier may mark a finding `deferred corpus may resolve`, but must not silently
use staged material to repair this release or recommend it as an accidentally overlooked source.

---

## A10. Reproduction and release gate

Principal files:

```text
model/aa_group_model.py                    canonical model
model/book-calculations.ipynb              book verification notebook
paper/anonymity-as-an-aggregation-condition.ipynb
                                           paper verification notebook
research/RELEASE-GATE-RESULTS.md           generated confirmatory report
research/ROBUSTNESS-RESULTS.md             expanded-sensitivity report
research/model-choice-inventory.json       values, zeros, and constants
tools/check_release.py                     fail-closed release gate
```

From the repository root, after every cache is complete. All three PDFs are built before the
release check, because that check requires each rendered artifact to postdate every source that
feeds it:

```bash
python3 tools/summarize_robustness.py
python3 tools/regenerate_notebooks.py
python3 tools/run_notebook.py
python3 tools/run_notebook.py --paper
python3 tools/check_book.py
python3 tools/check_chapter.py reference/PRIMER-steps-and-traditions.md
python3 tools/check_portability.py
python3 tools/build_book.py
tectonic --outdir paper \
  paper/anonymity-as-an-aggregation-condition.tex
python3 tools/build_primer.py
python3 tools/check_release.py
```

`build_book.py` and `build_primer.py` each report an overfull-box count, and release requires
zero from both. A nonzero count means text is sitting outside the type block. All three PDFs use
one inch margins, the book at 1.05 inches.

Release also requires rendering all three PDFs to page images and inspecting them for overflow,
clipped tables, broken references, duplicated headings, blank pages, and stale text.

### A10.1 Renumbering note

This appendix was consolidated during the release-gate round and several section identifiers used
by earlier drafts no longer exist. Manuscript, paper, and primer references were retargeted. The
docstrings of completed analysis scripts still carry the old identifiers, because those scripts are
hash-linked to caches that would be invalidated by editing them, so the mapping is recorded here
instead.

| Retired identifier | Current location |
|---|---|
| A3.3, A3.3b, A3.4 | A4, estimands, seed counts, and the selection threat |
| A4.6, A5.5 | A7.5, Morris and Sobol |
| A5.4b, A5.4c, A5.4e | A8, threshold, reassignment, and sparsity-pricing tests |
| A5.4d | A5.2, the degradation ranking |
| A5.6 | A7.1, the design registry and what no design covers |
| A9 as structural variants | A7.3 |
| A9.5 | A7.6, the resource-list test |

---

## A11. Threats to validity

1. No simulation parameter is fitted to longitudinal AA group data, and the original calibration
   fails after the mean-one correction.
2. The `S` and `GOV` matrices are author judgments. Their magnitudes and sparsity need independent
   elicitation.
3. The mapping from three Traditions to the Golub-Jackson conditions is an interpretation, not a
   theorem or historical fact.
4. The model has no tenure, sponsorship, pair matching, cliques, attendance networks, relapse
   outcome, harm measure, competing organization, or regional ecology.
5. The practice scale is internal and unvalidated. Threshold names such as established and
   experienced do not create empirical categories.
6. Finite-horizon persistence is not indefinite survival; endpoint viability is not closure;
   selected member quality is not a population outcome.
7. Sensitivity screens cover stated ranges and architectures only. Low-replication parameter
   points rank robustness; they do not estimate real-world probabilities.
8. The staged corpus is deliberately outside this release's evidence record.
9. The decay rate `delta0` is authored and, after the ordering exponent, the most influential
   registered value. The only estimates read for anything comparable, on 13 September 2026,
   measure skills rather than practices and are one to two orders of magnitude slower. Large
   downward moves of `delta0` are among the few that reverse the pure-attraction-loss minus
   referral-loss ordering in A7.5. The released value is unchanged, because no source measures
   how fast a practice lapses.

The model's proper use is to make assumptions and comparisons explicit enough to test against
real group data. It cannot evaluate or advise any individual person's recovery.

---

## A12. A second fellowship: Recovery Dharma read against the model

This section answers a question put to the project from outside it, rather than one the model was
built for. It is deterministic and textual. It adds no cache, no seed, no interval, and no
stochastic claim, and nothing elsewhere in the release depends on it. The source is
`research/incorporated/RecoveryDharma_2023/`, read in full in two passes: Section I, Section II
with its fourteen personal stories, the meeting format, the glossary and the dedication of merit
on 16 August 2026, and the selected meditations and the inquiry questions on 13 September 2026.

### A12.1 The question, and what the model cannot answer

The question was whether the model shows the Twelve Steps simplified into the Dharma. It does not,
and three separate obstacles stand in the way before any evidence is weighed.

The first is chronology. The Eightfold Path predates the Twelve Steps by roughly two and a half
thousand years. The source dates Siddhartha to about 2,500 years ago and the writing down of the
teachings to the centuries after his death in the fifth century BCE, and it presents its program as
an application of early Buddhist teaching rather than as a rewriting of anything. A claim that one
document is a simplification of the other is available in neither direction, and in the direction
asked it is ruled out by dates alone.

The second is that the model has no parameterization for this fellowship. Applying it would require
a step-resource matrix and a governance matrix elicited for Recovery Dharma. Neither exists. A11
item 2 already records that the two matrices the project does have are author judgments in need of
independent elicitation, so authoring two more here, for a fellowship the author does not belong
to, would compound the existing weakness rather than test anything.

The third is that the model contains no object corresponding to a comparison of fellowships. A11
item 4 records the absence of a competing organization, and there is no comparative estimand, no
second room, and no shared population.

What remains available is a structural reading: taking the model's eight resources as a vocabulary
and asking, of each program's own documents, where each resource is carried. That is a coding
exercise on text, and it is registered here as a reading rather than a result.

### A12.2 The count test

The count comparison that makes simplification look true is eight against twelve, and it compares
one Recovery Dharma list against one AA list.

| Program | Enumerated lists | Items |
|---|---:|---:|
| AA as this model codes it: Steps and Traditions | 2 | 24 |
| Recovery Dharma: jewels, Noble Truths, path factors, precepts, heart practices, foundations of mindfulness, commitments of The Practice | 7 | 35 |

The Recovery Dharma items are three jewels, four Noble Truths, eight path factors, five precepts,
four heart practices, four foundations of mindfulness, and seven commitments in the section called
The Practice. On count the program is larger, not smaller, and its commitments are distributed
across seven enumerated lists rather than concentrated in two.

There is a real simplification in the source, and it is of grouping rather than of count. The eight
path factors are gathered under three headings, wisdom, ethics and concentration, and the Path is
not worked in sequence. The Steps are numbered and ordered. That difference is genuine and is not
what the word simplification is usually taken to mean.

### A12.3 Where the eight resources are carried

The model's own structure first, computed from the canonical `S` and `GOV` and carrying no
interval. Group dependence `beta` is maximal and equal at 1.000 for Steps 1 and 12. Step 12 is the
only Step with a nonzero recipient-opportunity entry, so it is the sole carrier of that resource.
Step 1 holds 0.800 of the admission column and 0.588 of the identification column, Step 5 holds
0.667 of the confidentiality column, and the two diffuse resources, counsel and gentle pressure,
are spread across eleven Steps each with top shares of 0.300 and 0.226. In `GOV`, recipient
opportunity carries the largest governance mass of the eight columns at 2.40.

| Resource | AA carrier in `S` | Recovery Dharma carrier, with printed page |
|---|---|---|
| admission | Step 1, 0.800 of column | First Noble Truth, "Addiction **is** suffering" (9); Renunciation in The Practice (xv) |
| identify | Step 1, 0.588 of column | made optional by design: introductions need no identification beyond a name (150); no requirement to identify yourself in any way (43) |
| proof | Step 2, 0.526 of column | the fourteen personal stories (57-121); those who have made it to the other side (2, 48) |
| confidential | Step 5, 0.667 of column | the closing of the meeting script (151) |
| counsel | diffuse, Step 9 top at 0.300 | Wise Friends and Mentors (49-50); Reaching Out (46-48); the inquiry questions, which suggest working through them with a mentor, wise friend or group and ask whether the reader has one to turn to (136, 139, 143) |
| recipient | Step 12, sole carrier | Sangha, Wise Friends, Mentors in The Practice (xvi, 148); Service and Generosity (50-52); the newcomer question in the closing (151) |
| continuity | Step 12 top at 0.286 | Meetings and Growth in The Practice (xv-xvi); the announcements (151) |
| pressure | diffuse, Step 10 top at 0.226 | the Five Precepts (29); cut against by the group-sharing rule that shares carry no advice (151) |

Two things follow. The carriers scatter across four documents rather than one, so the counterpart of
the Twelve Steps is not the Eightfold Path but the union of the Path, The Practice, the Sangha
chapter and the meeting script. And three of the eight resources, confidentiality, recipient
opportunity and gentle pressure, are not carried in the Eightfold Path at all. A reading that sets
the Path beside the Steps and counts eight against twelve is comparing a practice taxonomy with a
document that does a different job.

One entry deserves separate notice because it runs opposite to the model's coding. Identification
is the resource AA loads most heavily onto Step 1, and Recovery Dharma removes the ritual that
carries it, twice and explicitly. The model gives that resource a column mass of 1.70 and a
governance mass of 1.90. It cannot say what removing the ritual would do, because there is no
parameterization, but it locates the question precisely, which is the most this exercise supports.

### A12.4 Governance, the sangha, and a schism

This book's argument is about the Traditions rather than the Steps, so this is the section that
matters most, and it is the one a first pass got wrong. That pass claimed the fellowship had no
Traditions-equivalent object at all. It has one. Correcting the error is what produced the strongest
finding in this section.

**The sangha is the group-conscience analogue, and it is constitutional rather than procedural.**
The meeting script has every member affirm that they "trust in the wisdom of" the Buddha, the
Dharma, and the Sangha, glossed there as the community of wise friends (147). Refuge in the three
jewels is doctrinal, recited at every meeting, and is not among the things the script invites a
meeting to edit. The Sangha chapter states that the fellowship is "decentralized and peer-led" and
that its own advice is offered "in the spirit of friendly guidance rather than direction" (42),
which is close in both content and tone to Tradition 2's account of leaders who do not govern. AA
locates ultimate authority in a group conscience; Recovery Dharma locates trust in a sangha. Those
are the same move.

| Function in AA's Traditions | Recovery Dharma location |
|---|---|
| ultimate authority in the group, Tradition 2 | refuge in the Sangha and trust in its wisdom, recited at every meeting (147); "friendly guidance rather than direction" (42) |
| openness of membership, Tradition 3 | no requirement to believe anything or to identify yourself in any way (43) |
| autonomy, Tradition 4 | the script is "meant to serve as a suggested template" and meetings may edit it (147) |
| self-support, Tradition 7 | the dāna basket in the announcements (151) |
| no governing hierarchy, Tradition 9 | peer-led, following no one leader or teacher; the facilitator disclaims any particular authority (147) |
| confidentiality, Tradition 12 | the closing (151) |
| singleness of purpose and no outside issues, Traditions 5 and 10 | **inverted.** "In the Dharma, there's no such thing as an 'outside issue' to my recovery when all things are interdependent" (103) |
| attraction rather than promotion, Tradition 11 | partial only: the program presents itself as not the only path and as compatible with other programs (xi, 147) |

What is genuinely absent is narrower than a charter and easy to state. A mechanical search of the
full text returns no occurrence of "group conscience", "consensus", "business meeting", "trusted
servant", "quorum", "rotation", "bylaw" or "governance". The fellowship names an authority and
supplies no written procedure by which that authority reaches a decision. That is the real
asymmetry, and it is a difference in the *specification* of governance rather than in its presence.

**The fellowship exists because of a governance failure of exactly the kind this book models.**
Recovery Dharma is a 2019 schism from Refuge Recovery, and the personal stories, written by people
who were officers of the predecessor, say so plainly. One contributor followed the predecessor's
founding teacher, whose meditation organization was the hub from which Refuge Recovery grew, and
became Refuge Recovery's Executive Director (84). Another managed its retreats and co-hosted
its conferences (98). Her account of what happened is the passage to read twice: the
community "was
heavily influenced by unhealthy masculinity and inequities among leaders", and "Great heartache
ensued as people were harmed and a sangha was fractured" (98). A third contributor describes
arriving at the 2019 Refuge Recovery conference and "walking into division", and calls it the
moment Recovery Dharma was born (119).

Two things follow, and both bear directly on Part Two.

The successor's constitutional commitment was chosen in response to that failure, deliberately and
by people who had lived it. The Executive Director's account of the founding is explicit about the
design: "We wanted to be intentional in our framework — it had to be peer-led and trauma-informed"
(84). The predecessor was organized around a named founding teacher. The successor's first stated
commitment, recited in every meeting, is that it follows no one leader or teacher. A fellowship with
no knowledge of this model, and no interest in Golub and Jackson, responded to concentrated
influence by abolishing the office that concentrated it. That is Traditions 2 and 9 arrived at
independently, in 2019, under pressure.

**An independent account corrects where that line falls, and the correction improves the fit.**
Everything above comes from the successor's own literature, written by people who left, which is
the weakest possible evidential position for a claim about why a schism happened. *Tricycle*
covered the split on 13 July 2019 and was read at source on 17 August 2026. It confirms the
structural fact from outside: two nonprofits came out of 2019, the continuing body retained
associated teacher-led retreats and professional treatment options, the successor was formed
without them, and individual sanghas chose between them. It also corrects the contrast. Both
organizations describe their *meetings* as peer-led and democratically run, and the predecessor's
own book did so before the split, so the difference was never that one had peer-led meetings and
the other did not. What separates them is the layer above the meeting.

That is a better fit to what this book models, not a worse one. The model has no representation of
a meeting's internal democracy, which both fellowships share and always did. What it has is a
governance layer that can be concentrated or diffuse, and the split is precisely about whether
such a layer exists above the group at all. The independent source therefore narrows the claim to
the one the model can actually speak to.

And there *is* a decision procedure, at least once, even though none is written down. The
transition was not decreed: "all of the meetings in our area voted to switch from Refuge to RD"
(119). A vote across meetings is a group-conscience act in everything but name, and its existence
in practice alongside its absence in the literature is the sharpest single observation in this
section.

The model-relevant consequence should be stated carefully, because the first pass overstated it.
A2.4 gives five Traditions empty governance rows and uses them as protective modifiers, and the
effective-adherence construction needs provisions whose adherence can vary independently while the
constitution stands still. Recovery Dharma does have a fixed constitution: the three jewels, the
Four Noble Truths, the Eightfold Path and the Five Precepts are not what a meeting edits. What it
lacks is *differentiation*. Its governance commitment is a single undivided act of refuge rather
than twelve separately adherable provisions, so there is no set of rows to vary one at a time and
no counterpart to the Tradition ranking of A5.2. That is a statement about the shape of the object,
not about its absence, and it is weaker and truer than what this section said before.

None of this compares the two fellowships for quality of governance. It observes that one of them
was founded, within living memory and at considerable cost to the people who did it, on the
proposition this book spends twenty-five chapters arguing for.

### A12.5 What the fourteen personal stories show

Section II was not read in the first pass and was described then as the one place the source might
carry anything resembling evidence about what members do. It was read in full afterwards, and it
does. What follows is testimony, written by participants in their own program literature, which is
the genre most likely to tidy a history in hindsight. It is reported here as testimony and supports
no rate, no proportion and no outcome.

**Arrival is almost entirely exogenous, which inverts the model's arrival term.** A2.7 makes
endogenous arrivals scale with members' Step 12 state and a single attraction multiplier, with a
separate constant `lam_exog` for everything else. Across the fourteen stories the reported routes in
are a flier on a coffee shop noticeboard (59), an existing meditation community (63), the Buddhist
Recovery Network website and a book available free online (70), an internet search during the 2020
pandemic (80), online meetings joined from a thousand miles away (88), a therapist's referral (92),
a Buddhist chaplain visiting a treatment unit (106), a stranger's message on a meditation app (114)
and, in three cases, founding a group rather than finding one. Only one route resembles a member
carrying the message to a stranger. For this fellowship the exogenous constant would carry nearly
all of the arrivals and the endogenous term would be close to idle, which is the reverse of the
weighting the model uses and the reason inference 6 of A12.7 cannot be carried over unchanged.

**Membership overlaps rather than substitutes.** Several contributors describe attending Recovery
Dharma and a Twelve Step fellowship at the same time, one naming a sponsor, wise friends and a
therapist in the same sentence (88), and one arriving after a suggestion to attend a second meeting
on a day they had already been to a first (70). The model has one room and no representation of a
member belonging to two fellowships, so it cannot express the most common pattern in this sample.

**Two contributors left Twelve Step fellowships over the Traditions themselves.** One found the
singleness-of-purpose rule "stifling" because the presenting problem was not the only problem (70);
another describes being asked to avoid discussing addictions deemed unrelated to the meeting, and
sets against it the claim that in the Dharma nothing is an outside issue because everything is
interdependent (103). The book's own reading of Traditions 5 and 10 is that they protect a group's
capacity to do one thing well. These two accounts are the cost side of that protection, reported by
people who paid it. A model in which Tradition adherence only ever helps has no place to put them.

**Service is described as load-bearing, and one contributor states the mechanism in the model's own
shape.** Reported service includes chairing and facilitating meetings, hosting, mentoring, finding
locations, organizing retreats, serving as an intersangha representative, and sitting on the global
board. One account moves from observation to practice in two sentences: the people who served most
seemed most at ease, so the writer began serving too, and later concluded that nothing helped more
than helping other people (106). That is the helper-therapy proposition the corpus already holds in
Pagano et al. (2004), arrived at here by noticing it in a room. It is an observed association
reported by one person and is not evidence of direction.

**The order gate is contradicted in the source's own words.** A12.7 argues that two of the model's
core inferences depend on practices being worked in sequence, and that Recovery Dharma's path is
not. A contributor puts it more sharply than this appendix did: the Eightfold Path is supportive
precisely "because it's not a consecutive sequence", and the Dharma is "kaleidoscopic", each part of
the path reflecting the others (65). That is a member describing the absence of the order gate as a
feature.

**Affinity meetings spawn cheaply, and a member reports the homogeneity benefit directly.** A12.7
names a trade the model cannot score, between within-room homogeneity and room size. One account
supplies both halves: noticing that no meeting existed for a particular process addiction, the
writer and others simply created a sangha and meetings for it, and reports that although every
addiction is welcome at every meeting, connection and healing deepened among people concentrating on
the same topic (103). The same contributor draws the structural contrast explicitly, that this
fellowship does not have to spawn a new fellowship for each new process addiction. Cheap
within-fellowship segmentation is an architecture the model has no way to represent, since it has one
room of capacity 60.

**Growth outran the founders, and one of them says so.** A founding contributor describes the
fellowship going from the same five people doing everything to a point where she knows neither half
the board nor most of the group's online administrators, alongside a main online group of more than
ten thousand people (84). That is the scaling problem of Part Two stated from the inside, by someone
watching it happen, and it is offered here only as a description and not as a measurement of
anything.

---

### A12.6 What an actual comparison would require

Registered so that the gap is explicit rather than implied.

1. A step-resource matrix for Recovery Dharma over the same eight resources, elicited from people
   in the fellowship rather than authored here.
2. A governance matrix, which cannot be built until it is decided what plays the Traditions' part:
   the meeting script, the commitments of The Practice, or neither.
3. A prespecified equivalence margin, because the interesting claims are absence-of-difference
   claims, and A5.2 already records that the founding-composition contrasts are unresolved for
   exactly this reason.
4. Membership data for both fellowships, which the project has for neither.

Absent all four, what is above is a reading of two sets of documents in a shared vocabulary. It
supports no comparative claim about outcomes, effectiveness, or persistence, and it must not be
cited as though it did.

### A12.7 The model's core inferences, and which of them travel

A12.3 and A12.4 read two sets of documents. This subsection does something weaker and more general:
it states what the model infers about groups of this kind, stripped of AA vocabulary, and then asks
which inferences depend on features Recovery Dharma shares. Everything here is theme-level. A theme
that travels is a hypothesis about a fellowship the model has never been fitted to, not a result.

**The six core inferences, stated without reference to any fellowship.**

1. *The causal chain runs one way and through the room.* Member practice states produce group
   resources; resources feed back into individual growth. There is no direct member-to-member
   coupling anywhere in the model. Whatever a group provides, it manufactures out of the aggregate
   practice of the people currently in it.
2. *Growth is gated multiplicatively, not added up.* Three gates multiply: an order gate making each
   practice depend on the one before it, a peer gate weighted by `beta`, and a capacity gate whose
   weight `w` rises linearly from 0.05 at the first practice to 1 at the last. Late practice is
   therefore both the most group-dependent and the most capacity-limited thing a member does.
3. *Retention and reproduction load on opposite ends of the sequence.* Exit hazard falls with early
   practice, the mean of Steps 1 to 3. Endogenous arrivals scale with late practice, the Step 12
   state alone. A group keeps people through its cheapest practice and reproduces through its most
   expensive one.
4. *Dispersion is a multiplier, not a detail.* The `unity` term, one minus twice the standard
   deviation of practice level among established members, multiplies three of the eight resources:
   identification, continuity and gentle pressure. Spread degrades a room independently of level.
5. *Openness compounds across its channels.* Losing Tradition 3's friction path costs
   2.962 [1.848, 4.077] in final membership and its governance path 6.027 [5.043, 7.012], but losing
   both costs 11.045 [10.030, 12.060], with interaction -2.055 [-3.414, -0.696]. The joint loss
   exceeds the sum of the parts.
6. *Referral loss is slow and it is disguised.* Under pure attraction loss, membership runs 21.55 at
   year 5, 11.68 at year 10, 2.50 at year 20 and 0.51 at year 30, while endpoint viability falls
   from 0.970 to 0.0275. In these runs a group losing its referral channel looks healthy for years
   before the decline is legible.

**Which of these depend on features Recovery Dharma shares.**

| Inference | Travels? | Why |
|---|---|---|
| one-way causal chain | yes | the source describes the sangha as where the teachings find expression and are put into action, which is the same one-way shape |
| multiplicative gating | **no** | the gating rests on the order gate, and the Eightfold Path is explicitly not worked in sequence |
| retention and reproduction on opposite ends | **no**, and this is the interesting failure | it is a corollary of the order gate; remove the sequence and the two ends are no longer far apart |
| dispersion as multiplier | yes, and it becomes sharper | see the affinity-meeting note below |
| openness compounds | untested either way | Recovery Dharma is open by construction, so the model's loss conditions have no counterpart to switch off |
| referral loss is slow and disguised | partially | the arrival channel differs in kind; see below |

**The sequence is where the two programs part company, and it is load-bearing.** Inferences 2 and 3
are not independent findings. Both descend from the order gate, which makes each Step's growth
depend on the state of the one before it. That gate is why the practice driving arrivals is also the
most expensive to reach, and it is why a group's reproduction lags its retention. Recovery Dharma's
Path is grouped under three headings and practiced simultaneously, and the source states that each
person practices each aspect in their own way. A program without a sequence has no structural reason
for its reproduction-driving practice to be its costliest one. That is the single largest difference
between the two, larger than any count, and the model can identify it precisely because the order
gate is an explicit term rather than an assumption buried in prose.

**Dispersion, and the one place the model has something uncomfortable to offer.** Affinity meetings
are encouraged by the source, including the instruction to start one where none exists. In the
model's vocabulary that is deliberate management of within-room dispersion: it raises homogeneity
inside each room while reducing the number of people in it. The `unity` term says the first effect
raises three resources, and the saturation terms say the second lowers several. The model cannot
score the trade, because it has one room of capacity 60 and no representation of a fellowship split
across rooms. What it can do is name the trade as a real one with effects in both directions, which
is more than the source does and less than a recommendation. Nothing here evaluates affinity
meetings, and nothing here should be read as advice about them.

**The arrival channel is a scope limit rather than a difference.** Endogenous arrivals in the model
scale with members' Step 12 state and a single attraction term, which presumes members belong to one
group. Recovery Dharma presents itself as not the only path, compatible with other programs, and
commits members to attending recovery meetings whether with Recovery Dharma, other Buddhist
communities, or other fellowships. The model has no representation of shared or overlapping
membership at all, so inference 6 cannot be carried over as stated. This belongs with A11 item 4,
the absence of a competing organization, and it is the same gap seen from the other side.

**The helper threshold is a hypothesis the model generates and cannot settle.** The recipient
capacity term is opportunity per high-practice potential helper, so widening the pool of eligible
helpers enlarges the denominator. Recovery Dharma widens it deliberately: the mentor role is not a
formal position, nobody is certified or authorized, and anyone with any period of renunciation and
practice may serve. The model therefore predicts a lower recipient resource per helper under that
rule, which sounds like a finding and is not one. The clean recipient ablation is unresolved: forcing
recipient capacity to one changes final membership by 1.028 [-0.259, 2.314], an interval crossing
zero, which is not the same as no effect. Disabling Step 12 does cost 5.325 [4.437, 6.213], but that
is the whole Step, not the recipient path, and A5.1 is explicit that the mechanism-specific version
of this question has no released answer. Anyone tempted to read the helper threshold as a finding
should stop at the ablation.

**What none of this licenses.** No comparison of effectiveness, persistence or outcome between the
two fellowships. No claim that either program's structure is better suited to the mechanisms above,
since the mechanisms are authored. No advice about how a meeting of either kind should be run, and
nothing whatever about an individual's recovery.

### A12.8 The Machinery

This section was written to be self-contained and is now depended on in one place. Chapter
Twenty-Four cites the 2019 schism described in A12.4 as the closest thing to a live case the book
has, and states there that it corroborates rather than confirms. Nothing else in Parts One through
Five, in A1 through A11, or in the paper depends on this section; the primer carries a short
follow-up of its own. Removing A12 would require removing four paragraphs of Chapter Twenty-Four
with it.

**1. What the comparison says.** Four findings, in descending order of how well they are supported.

The word simplification does not survive a count: the program carries thirty-five enumerated items
across seven lists against twenty-four across two, and the eight-against-twelve reading compares one
list with one list.

Two of the model's six core inferences, multiplicative gating and the loading of retention and
reproduction on opposite ends of the sequence, both descend from the order gate and therefore do not
travel to a program whose path is not worked in sequence. A member of the fellowship states the same
thing independently, calling the path kaleidoscopic rather than consecutive.

The fellowship has a group-conscience analogue, the sangha, which is constitutional rather than
procedural, and it has no written decision procedure. An earlier draft of this section claimed it
had no Traditions-equivalent object at all, which was wrong, and correcting it produced the finding
below. What the governance object lacks is not existence but differentiation: it is one undivided
act of refuge rather than twelve separately adherable provisions, so there is nothing for A5.2's
Tradition ranking to range over.

And the fellowship is a 2019 schism from a predecessor organized around a single named founding
teacher, which fractured over inequities among its leaders. Its successor's first stated commitment,
recited at every meeting, is that it follows no one leader or teacher. That is Traditions 2 and 9
reached independently and under cost, and it is the only contemporary case of the kind the project
has.

One threat to validity belongs to this section rather than to A11, because it is visible only from
here. The architecture encodes AA's document structure rather than recovery-group structure in
general: it requires one Step matrix and one differentiated Tradition matrix, and this comparison
exhibits a functioning fellowship that distributes the same functions across a practice taxonomy, a
commitments list, a community chapter and a meeting script, and whose governance commitment does not
decompose into rows at all. A12.5 adds a second: the model's arrival term is weighted for a
fellowship that recruits through its members, and this one recruits mostly through the internet,
professionals and its own free book.

**2. The technical version.** Every quantity attributed to the model here is deterministic algebra
on the two authored matrices at the canonical hash, and carries no interval. For Step `j`,
group dependence is

```text
beta[j] = row_sum(S[j,:]) / max_k row_sum(S[k,:])
```

which is 1.000 at Steps 1 and 12 and below 0.71 everywhere else. Column shares are
`S[j,k] / col_sum(S[:,k])`: Step 1 holds 0.800 of admission and 0.588 of identification, Step 2
holds 0.526 of proof, Step 5 holds 0.667 of confidentiality, Step 12 is the sole nonzero entry in
recipient opportunity, and counsel and gentle pressure spread over eleven Steps each with top shares
of 0.300 and 0.226. Governance mass is `col_sum(GOV[:,k])`, largest at 2.40 for recipient
opportunity and smallest at 1.00 for gentle pressure.

The interval-bearing figures quoted in A12.7 are not recomputed here. They are the released
confirmatory results reported in A5.1, A5.2 and A5.4, at 400 seeds paired by common random numbers,
and they are quoted rather than re-derived so that this section adds no cache and no seed. The one
figure a reader should not over-read is the clean recipient ablation, 1.028 [-0.259, 2.314], whose
interval crosses zero and which is therefore unresolved rather than null.

The counting exercise is arithmetic on the source's own lists: three jewels, four Noble Truths,
eight path factors, five precepts, four heart practices, four foundations of mindfulness and seven
commitments in The Practice, totalling thirty-five across seven lists.

**3. Notes on sources.** One source does all the work, and all of it has now been read. Sections I
and II were read in full on 16 August 2026, as were the glossary, the meeting format and the
dedication of merit. The selected meditations and the inquiry questions, which are practice material
rather than description, were read on 13 September 2026 and hold no governance text. Page references
are the printed pagination, which runs sixteen behind the PDF pagination in the arabic range.

**A first pass got the central question wrong, and the record should show how.** That pass read
Section I and the meeting format, did not read the personal stories, and concluded that the
fellowship had no Traditions-equivalent object. Two things were missed. The meeting script has every
member affirm trust in the wisdom of the Sangha, which is a group-conscience analogue sitting in
plain sight in a document that had been read. And the stories, which had not been read, contain the
fellowship's founding history, the schism that produced it, and the one recorded instance of
meetings voting. The error was corrected by reading the rest, and the correction is the reason this
section now has a finding worth citing in a chapter. The general lesson is the one the corpus rules
already state: file presence is not reading, and a partial read is a place where an absence claim
can go wrong.

The absence claim that survives is narrow and was tested mechanically over the full text rather than
by reading alone. No occurrence of "group conscience", "consensus", "business meeting", "trusted
servant", "quorum", "rotation", "bylaw" or "governance" appears anywhere in the document. The single
"committee" and the references to an elected board occur inside personal stories and describe the
global nonprofit rather than a rule binding a meeting.

The individual at the centre of the predecessor organization's collapse is named in the source and
is deliberately not named in this project. The structural claim does not require the name, and
nothing here can adjudicate an allegation about a living person. Chapter Twenty-Four carries the
same restriction.

Provenance took two steps. The copy first read was an ephemeral session attachment removed from
disk before it could be stored; the same document was then located locally and confirmed by page
count, byte size and verbatim spot-checks against passages already read. That copy is the one
hashed and indexed. The bibliographic record was taken from the file's own title and copyright
pages rather than from an independent catalogue entry, which is the one open item on this source.

**4. References.**

**Read in full:**

Recovery Dharma Global (2023). *Recovery Dharma: How to use Buddhist practices and principles to
heal the suffering of addiction.* Second edition. Recovery Dharma Inc. CC BY-NC-SA 4.0. Read in
full: the contents and front matter through The Practice (ix to xvi); Section I entire (1 to 54);
Section II entire, the fourteen personal recovery stories (57 to 121); and Section III entire, the
selected meditations (122 to 135), the inquiry questions (136 to 144), the glossary (145 to 146),
the meeting format (147 to 151) and the dedication of merit (152). The meditations and inquiry
questions were read on 13 September 2026 and the rest on 16 August 2026. Source of every page
reference in this section and of the four paragraphs in Chapter Twenty-Four. Stored as
`research/incorporated/RecoveryDharma_2023/`, git-ignored with a SHA-256 and a verification index.
It is the one source in the corpus whose licence would permit committing the document; the project
git-ignores it anyway, because the rule is uniform.

Jensen, K., and M. Abrahams (2019). "Buddha Buzz Weekly: Refuge Recovery Splits." *Tricycle: The
Buddhist Review*, 13 July 2019. Read at source on the publisher's site on 17 August 2026 and held
as record only. The one independent account A12.4 uses, for the structure of the split and for the
correction that both organizations describe their meetings as peer-led.

**Referenced but not reproduced:**

The Pali canon and the early Buddhist teachings from which the Four Noble Truths, the Eightfold
Path, the Five Precepts and the four foundations of mindfulness derive. This section takes all of
them at second hand, as Recovery Dharma presents them, and consulted no primary Buddhist text. Any
claim here about what the Dharma says is therefore a claim about what this fellowship's literature
says the Dharma says, and the distinction matters for the chronology argument in A12.1, which rests
on the source's own dating rather than on independent scholarship.

**Internal, and reproducible from this repository:**

`model/aa_group_model.py` at the canonical hash, for `S`, `GOV`, the group-dependence coefficients,
the column shares and the governance masses. The interval-bearing figures are quoted from A5.1,
A5.2 and A5.4 and their registered caches; this section computes none of them and adds no cache of
its own. The source record, read scope and rights position are in
`research/incorporated/RecoveryDharma_2023/` and in `research/SOURCES.md`.

**What was not read:**

Little that is independent about the 2019 schism. Beyond the successor organization's own
literature, written by people who left the predecessor, A12.4 rests on one contemporaneous press
account, *Tricycle*'s. No court record or statement from the predecessor was sought, and the
predecessor's own account of the same events has not been read. The record still leans to one side,
and Chapter Twenty-Four's use of it inherits the weakness.

The empirical literature on Buddhist and mindfulness-based recovery programs, which was not searched
at all. This section compares program documents and one fellowship's account of its own history. It
does not know what either fellowship's outcomes are, and no part of it should be cited as though it
had looked.

---

## A13. The personal stories read against the model's arrival term

A12 compared program documents. This section does something narrower and evidentially stronger: it
reads twenty-nine first-person accounts against one specific modelling choice, the arrival term in
A2.7, and asks whether the fellowship the model was built from actually recruits the way the model
says. It is a coding exercise on text. It adds no cache, no seed and no interval, and it changes no
number in the release.

### A13.1 What the source is, and a correction to the record

The document read here was supplied as the fourth edition of *Alcoholics Anonymous*. It is not.
Its title page reads "The 4th Edition of Alcoholics Anonymous" and immediately below, "This book
contains a complete reprint of the 1st edition 1939", published by the Alcoholics Anonymous Big
Book Study Group and marked "No Copyright 1999". The fourth edition is the numbering of the
reprinter's own printing, not of AA's editions. Its contents are the 1939 first edition: the
Foreword, the Doctor's Opinion, the eleven chapters of the basic text, and the twenty-nine personal
stories of that edition, from "The Doctor's Nightmare" through "Ace Full Seven-Eleven". AA's actual
fourth edition of 2001 carries an entirely different set of stories and roughly four hundred more
pages.

This matters twice. The stories analyzed below are the 1939 stories, contemporaneous with the
founding period Part One is about, and not a 2001 selection. And the work was already in the corpus
as `BigBook_1939`, whose record notes the same reprint and the same contested rights position. The
uploaded file differs from the stored one by a few bytes and 99.91 per cent of its extracted text is
identical, so this is a second copy of a source the project already held and had recorded as
"acquired; not yet used as claim support". That last clause is what this section changes.

### A13.2 The estimand and the coding rule

A2.7 makes arrivals Poisson with mean `lambda * dt`, where

```text
lambda = lam_exog + lam0 * sum_i X[i,12] * attraction_T11.
```

The first term is arrival that does not pass through a member. The second is arrival carried by
members, scaled by their Step 12 state. The model gives the endogenous term the dominant role, and
that is an authored choice. The question here is whether the fellowship's own accounts of how people
arrived support it.

The coding rule is: for each story, does the account describe a person who was themselves a recovered
alcoholic making contact with the subject before the subject stopped drinking? A family member
hearing of the fellowship and then arranging such a contact is coded as member-carried, because the
arrival still passes through a member; the family is the broker, not the channel.

### A13.3 The census

Twenty-seven segments were recovered automatically from the running heads. One of them, "A Vision
For You", is Chapter 11 of the basic text rather than a story, and is excluded, leaving twenty-six
story segments. Explicit personal-contact language appears in twenty of the twenty-six.

That count is a **lower bound and should be read as one**, because the matcher keys on a fixed
phrase list and misses accounts describing the same event in other words. The six segments without a
match are named so a reader can check them: "The Doctor's Nightmare", "The Unbeliever", "Our
Southern Friend", "Fired Again", "Smile With Me, At Me" and "Hindsight". At least two are certainly
false negatives. Dr Bob's account, the first story in the book, describes his wife being telephoned
by a woman who wanted him to meet a friend who might help, then six hours in that friend's company,
and finally the observation that the man "talked my language"; none of that matches a listed phrase.
"Fired Again" describes a neighbour who had heard of a recovered alcoholic doctor "busily engaged in
passing on the benefits he had received", which is the same channel reported at one remove. The true
figure is therefore above twenty and the method cannot say by how much.

The recurring shape is a visit, and often several. One writer records that while he was in hospital
"about twenty men called on me" and told him their experiences. Another was seen by a doctor who
"sent two of the members" to him. A third describes men who came to him "one by one and told me"
what had happened to them. A fourth met his first recovered alcoholic as a fellow patient. What the
accounts do not describe is somebody reading their way in.

### A13.4 The exception, and what the fellowship said about it

One story is the exception and the fellowship marked it as one. "Lone Endeavor" is the account of a
man in the far west reached only by correspondence and a pre-publication copy of the book, and the
narrative frame around it is the fellowship describing its own experiment. It calls the attempt
"our initial effort to help others through the book alone", says it was "the first time we have had
an opportunity of trying to help an alcoholic at long distance", and records that during the silence
that followed "we began to think this book was inadequate without personal contact".

That is the strongest single piece of evidence in this section, and it is strong because it runs
against the interest of the people writing it. A fellowship publishing a book had every reason to
believe the book would be sufficient. Its own literature says it doubted that, and that the doubt
was based on the absence of a personal visit.

### A13.5 What this supports, and what it bounds

**It supports the architecture of the arrival term for the fellowship the model was built from.**
The dominant endogenous channel is not an artifact of convenience. It is what the source describes,
in twenty-nine independent accounts, and the one case of arrival without a member is presented by
the fellowship as an untested experiment about which it recorded doubt.

**It bounds that architecture to that fellowship, and A12.5 is the other half of the bound.** The
fourteen Recovery Dharma accounts report arrival through a noticeboard flier, a website, a free
online book, internet searches, online meetings, a therapist and a prison chaplain, with almost no
member-carried arrival at all. Two fellowships, eighty-four years apart, sit at opposite ends of the
same parameter. A model that fixes the weighting between `lam_exog` and the endogenous term is
therefore making a claim about a period and an organization rather than about mutual-aid groups, and
the pair of censuses is the evidence for saying so.

**Two smaller observations, both weaker.** Dr Bob's account gives four reasons for passing on what he
learned, of which the fourth is that each time he does it he takes out "a little more insurance for
myself" against a slip. That is the helper-therapy proposition the corpus holds in Pagano et al.
(2004), stated by the fellowship's co-founder in 1939 and consistent with the model's treatment of
Step 12, though a single retrospective statement of motive is not evidence of direction. And Dr Bob
describes what moved him as a man who "talked my language", after reading widely and consulting
many non-alcoholic experts to no effect. That is the identification resource of A2.2, which the
matrix loads most heavily onto Step 1, described from the inside.

**What it does not do.** It does not validate any numerical value. `lam_exog`, `lam0` and the
attraction multiplier remain three of the hundred and eighteen registered values, fitted to nothing.
A census of how people say they arrived cannot set a rate. It also cannot speak to survivorship: the
twenty-nine accounts are of people who recovered and were chosen for a book intended to persuade, so
they are the least representative sample imaginable of everyone the fellowship met. Nothing here
touches retention, dropout or group survival.

### A13.7 The same census on the fourth edition, and what moves

The 1939 reading was carried on this list as unextendable, because the fourth edition of
2001 carries a different set of stories and the project did not hold it. The Human Author owns
several copies and supplied the text on 17 August 2026, and AAWS also posts the book in per-section
PDFs, so the obstacle was never as solid as this appendix said.

The fourth edition has forty-two personal stories in three parts: ten Pioneers, seventeen They
Stopped in Time, fifteen They Lost Nearly All.

**The coding rule had to be extended, and the reason is itself the finding.** A13.2 asks whether a
recovered alcoholic made contact with the subject before the subject stopped drinking. In 1939 that
question had two answers, because a person who wanted to find the fellowship had almost no way to
do so: it was small, unadvertised, and not yet in any telephone directory. By 2001 there are three
answers, and the middle one could not have existed in 1939.

| Initiating channel | Stories | Share of classifiable |
|---|---:|---:|
| A member sought the subject out | 13 | 43% |
| The subject contacted the fellowship | 6 | 20% |
| A professional or an institution referred | 11 | 37% |
| Channel not stated plainly enough to code | 12 | |

Thirty of the forty-two state the channel plainly. Twelve do not, and they are reported as
unresolved rather than assigned, on the same principle the release gate applies to an interval
crossing zero.

**What this supports.** The model's arrival term has two parts, an exogenous rate and a
member-carried rate scaled by Step 12 practice, and the fourth edition shows both operating. The
exogenous term is not a modelling convenience: its code comment names courts, treatment and
desperation, and the stories supply a judge sending a man to A.A. for a month, a college requiring
attendance as a condition of readmission, counsellors producing meeting lists, and repeated arrival
through treatment centres. In 1939 that term had almost nothing to point at. It now has more than a
third of the classifiable stories.

**What this bounds.** The member-initiated share falls from twenty of twenty-six in 1939, seventy-
seven per cent, to thirteen of thirty here, forty-three per cent. The model holds `lam_exog` fixed
at 0.12 per week for every run, so it cannot represent that shift at all. A fellowship large enough
to be found in a telephone book, and embedded in courts and treatment systems that refer to it, has
an exogenous arrival rate that grew with its own institutional presence. That is a mechanism the
model does not contain, and the two censuses together are the clearest evidence in this appendix
that it should be treated as a limitation rather than a detail.

**What it is not.** Neither census is a sample. The stories are selected by the fellowship for
publication, and selection on outcome is total: every subject recovered. Nothing here estimates
the arrival mix in the population, and the comparison between editions is a comparison between two
edited collections sixty-two years apart, not a time series.

### A13.6 The Machinery

**1. What the census says.** The model's arrival term gives the member-carried channel the dominant
role. Twenty-nine first-person accounts from 1939 describe arrival that way, with a lower bound of
twenty of twenty-six story segments carrying explicit personal-contact language, and the single
counter-case is one the fellowship itself flagged as an untested experiment about which it recorded
doubt. Read beside A12.5, where a modern fellowship arrives almost entirely without members, the
pair localizes the arrival weighting as a property of a fellowship and a period rather than of
mutual-aid groups in general.

**2. The technical version.** The estimand is the arrival intensity of A2.7. The coding rule is in
A13.2 and treats a family broker as member-carried. Segmentation was automatic from running heads
and recovered twenty-seven segments, of which one is a chapter and is excluded, leaving twenty-six
of the twenty-nine stories. The phrase matcher is a lower bound; A13.3 names all six segments it
failed to match and identifies two as certain false negatives, so a reader can see the size and
direction of the error rather than take the figure on trust.
No number in the release changes. No cache, seed, horizon or interval is involved, and nothing here
is a stochastic claim.

**3. Notes on sources.** The file supplied as the fourth edition is the 1939 first edition in the
1999 Big Book Study Group reprint, and A13.1 sets out how that was established. It duplicates
`research/incorporated/BigBook_1939/`, whose SOURCES.md entry previously read "acquired; not yet
used as claim support"; this section is the first use. The reprint asserts no copyright and the
1939 rights position is contested, which is why the project holds the document git-ignored rather
than as record only. Quotations here are short phrases with attribution, per the project rule that
nothing is quoted at length.

The stories are testimony selected for a persuasive purpose, and the survivorship problem in A13.5
is the governing limitation on everything in this section.

**4. References.**

**Read in full:**

*Alcoholics Anonymous*, first edition, 1939, in the Alcoholics Anonymous Big Book Study Group
reprint of 1999. The twenty-nine personal stories, printed pages 183 to 400, read for this section;
the Foreword, the Doctor's Opinion and the eleven chapters of the basic text were read for context.
Stored as `research/incorporated/BigBook_1939/`, git-ignored with a SHA-256 and a verification
index.

**Internal, and reproducible from this repository:**

`model/aa_group_model.py` at the canonical hash for the arrival term of A2.7 and the identification
column of A2.2. A12.5 for the Recovery Dharma census that forms the other half of the bound. No
cache is read or written by this section.

**What was not read:**

AA's actual fourth edition of 2001, which was the document requested and which the project does not
hold. Its stories are a different selection made sixty-two years later, and a census of them would
be a genuinely separate finding: it would show how the fellowship's recruitment channel had changed
across the period in which telephone, treatment referral and eventually the internet became
available. That comparison is the obvious next piece of work and this section does not attempt it.

Any systematic literature on referral pathways into mutual-aid groups, which was not searched. The
census here is of one book's self-selected accounts and is not a study.

# Appendix: What the Model Says About the Twelve Steps and the Twelve Traditions

Released to the public domain under The Unlicense. See the repository's license notice.

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

*What was assumed.* Unity is the only Tradition given a non-zero entry in all eight
columns: continuity 0.9, gentle pressure 0.6, identification 0.5, visible proof 0.3,
confidentiality 0.3, admission 0.2, counsel 0.2 and recipient opportunity 0.1. Because
the governance table is column-normalised, what those numbers do is set shares. Unity
ends up owning 60 per cent of gentle pressure and 50 per cent of continuity, and much
smaller shares of everything else.

The decision to let one Tradition touch every resource is the single most consequential
choice in the governance table, and it is what makes unity the largest load by a wide
margin. It was not forced. A reader who thinks unity is a property that emerges from the
other eleven rather than a supplier alongside them would give it an empty row, as the
five protective Traditions have, and unity's primacy would vanish by construction rather
than by argument. The project's answer is not that the choice is obviously right but
that it is testable in one specific place: unity's lead depends on holding continuity and
gentle pressure, and moving either to Tradition 5 hands over the lead.

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

*What was assumed.* Four non-zero entries: counsel 0.9, continuity 0.2, gentle pressure
0.2 and confidentiality 0.1. After column normalisation that makes the group conscience
the owner of 69 per cent of all counsel in the model, the most concentrated position any
Tradition holds over any resource except anonymity's hold on confidentiality.

That single assumption is doing nearly all the work in this row, and it encodes a
specific reading: that when somebody in a meeting has somebody to ask, what they are
drawing on is the group's collective judgement rather than an individual friendship.
It is a defensible reading and it is not the only one. Note also that the row and the
theorem are independent of each other. The Golub and Jackson result about a single member
holding influence does not come from this table at all, and would stand unchanged if
every entry in this row were different. That is why the deliberation findings are the
most robust things in the primer and the load figure is among the least.

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

*What was assumed.* Four non-zero governance entries: admission 1.0, recipient
opportunity 0.8, identification 0.4 and continuity 0.1, giving it 71 per cent of
admission and a third of recipient opportunity. Two further assumptions matter more than
the cells. The first is an absence: because the Tradition removes a group's power to
refuse anyone, Tradition 3 was deliberately left out of the arrival rate, so in the
default model an open door does not bring more people through it. The second is the
dropout friction path, where the effect is weighted by the exponential of minus six times
a member's mean practice.

That weighting is an assumption with a specific and easily misread consequence. It
concentrates the effect on members whose practice is near zero, and the model has no
concept of tenure, so those are not newcomers. They are members with little practice,
who may have been in the room for years. Every plain-language reading of this Tradition
has to be policed on that point, and the earlier version of this primer failed to.

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

*What was assumed.* The empty row is the assumption. Autonomy was coded as governing
none of the eight resources, which makes its load exactly zero, and that zero then
propagates into every Step's index-mate comparison as an unbeatable disadvantage. Its
only route into the simulation is a multiplier it shares with Tradition 7.

Both halves of that were chosen. Deciding that a Tradition protects rather than supplies
is a judgement about what kind of thing it is, and pairing it with self-support in a
single symmetric term is a modelling convenience with no evidential content whatever. The
entry already says the identical membership figures are an artefact; the deeper point is
that the whole protective category is an authored partition of the twelve, not a result.
Five Traditions were placed on one side of it and seven on the other before any
calculation was done.

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

*What was assumed.* Six non-zero entries: recipient opportunity 0.9, visible proof 0.5,
identification 0.4, continuity 0.3, gentle pressure 0.2 and admission 0.1. Its share of
recipient opportunity, 38 per cent, is the largest any Tradition holds of that column,
which is what makes it the principal supplier of Step Twelve.

The contest with unity described in the technical line is therefore a contest between two
authored rows, and the numbers deciding it are 0.9 and 0.6 in one row against 0.3 and 0.2
in the other on the same two resources. Nothing outside the author's reading placed them
that way. This is the most honest place in the primer to see what the whole apparatus
rests on. A real and unsettled question about AA, whether unity or single-purposedness is
the load-bearing idea, is here decided by four numbers one person wrote down. The
project's contribution is not the answer but the demonstration that those four numbers
are where the answer lives.

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

*What was assumed.* An empty governance row, and a multiplier shared with Tradition 10
acting on the effective adherence of singleness of purpose. The pairing is the
interesting assumption: it says that refusing endorsements and refusing outside issues
protect the same thing, and protect it in the same way, so the model gives them one
mechanism between them.

That is a claim, not an observation, and it has the same consequence as the Tradition 4
and 7 pairing: the two members of the pair are guaranteed identical numbers before any
simulation runs. When two Traditions in this primer report the same figure to the last
digit, that is always construction and never evidence.

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

*What was assumed.* An empty governance row, and the shared multiplier with Tradition 4.
The consequential assumption is where money went instead. The model does represent
solvency, through a term that drops the continuity resource from 1.0 to 0.45 when a
group's established members cannot cover the rent, but that term was attached to the
group's finances directly rather than to the Tradition that produces them.

So the zero in this row is not a claim that self-support does not matter. It is a
bookkeeping decision about where to attach an effect the model plainly contains. The
entry says a second person building the table would likely disagree here, and this is
what they would be disagreeing with: not a finding, but an attribution.

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

*What was assumed.* Four small non-zero entries: confidentiality 0.3, and
identification, visible proof and counsel at 0.1 each, the smallest set of non-zero
values given to any Tradition that has any. The reading is that keeping the fellowship
unpaid mainly protects candour, which is why confidentiality is the largest of the four.

Everything the primer says about this Tradition follows from those four small numbers,
which is why the entry says the model can say least about it. The unresolved membership
figure is not independent evidence of unimportance: a row built small will produce small
effects, and the design cannot separate a Tradition that does little from one the author
coded as doing little. Both readings fit the same output.

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

*What was assumed.* An empty governance row, so the entire membership column result for
this Tradition is a consequence of a coding decision rather than a measurement.

The rotation finding is the important thing here and it rests on different assumptions
altogether. It comes from the deliberation model, not from the matrices, and it assumes
that influence is concentrated in whoever currently holds a service position and is
shared evenly within the rotating pool. That is a stylised picture of how attention works
in a room. What makes the result durable is that its conclusion does not depend on the
details: any fixed pool in a growing group floors influence above the flat benchmark, so
the divergence follows from the arithmetic of a constant divided by a growing number. The
26 per cent is parameter-dependent and is offered as an order of magnitude. The
divergence is not, and that distinction is why this entry carries a headline result while
its membership figure carries nothing.

*In plain terms.* This is the sharpest warning against reading the membership column as
importance. On that column Tradition 9 does nothing measurable, and it carries one of
the three headline results in the book.

Rotation is where the model knows something AA does not say, and since 17 August 2026 that
can be put more precisely. The Twelve Concepts for World Service, adopted in 1962 and the
fellowship's fullest statement on service structure, do contain a proportionality principle:
Concept 4 asks for voting representation in reasonable proportion to the responsibility each
part of the structure discharges. But it proportions voting weight to responsibility, not the
rotating pool to the size of the group. A structure could satisfy Concept 4 exactly and still
rotate twelve people through a fellowship of eight hundred. AA has the instinct for proportion
and applies it to representation rather than to the pool.

The long form of this
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

*What was assumed.* An empty governance row and the multiplier shared with Tradition 6,
with the same consequence: its membership figure is identical to Tradition 6's by
construction.

There is a further assumption worth naming because the model cannot see past it. Outside
issues enter this model only as a dilution of singleness of purpose. Nothing represents a
group splitting over a disagreement, losing members to a controversy, or attracting
people because of a position it took. Those are the things the Tradition appears to be
about, and the model contains none of them, so silence here is not a small effect but an
absent mechanism.

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

*What was assumed.* Four non-zero entries: visible proof 0.7, recipient opportunity 0.6,
identification 0.2 and continuity 0.2, giving it 44 per cent of visible proof. Unlike
Tradition 3 it also has a direct route into arrivals: the model's inflow is an exogenous
term plus a term scaling with the attraction adherence multiplied by the twelfth Step
practice in the room.

That asymmetry between Traditions 3 and 11 is the most important assumption in Part Two
and it is a deliberate one. The model says a group cannot increase how many people arrive
by opening its door wider, because the door is already open by Tradition 3, and can
increase it by being visibly worth arriving at. Because attraction moves both the
governance path and the arrival path together, an ordinary change to this Tradition's
adherence is a mixed intervention, and the primer separates the two paths rather than
reporting their sum.

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

*What was assumed.* Five non-zero entries, one of them decisive: confidentiality 1.0,
identification 0.3, and admission, counsel and continuity at 0.1 each. The 1.0 gives
anonymity 59 per cent of all confidentiality in the model, the largest single share any
Tradition holds of any resource.

This is the assumption that produces the cleanest result in the book, and it was made
independently of the matching assumption in Step Five's row only in the weak sense that
the two were written at different times by the same person. Both encode the same belief,
that what anonymity does is make disclosure safe. The primer's Step Five entry gives the
numerical size of that belief: the match survives 99.5 per cent of magnitude jitter and
17.5 per cent of full magnitude replacement. Read the two entries together, because
neither is independent evidence for the other.

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
CC BY-NC-SA 4.0. The only source for the follow-up section above. Read in full, in two
passes: the front matter, the whole of Section I, the whole of Section II with its fourteen
personal recovery stories, and the glossary, meeting format and dedication of merit on 16
August 2026, and the meditations and inquiry questions on 13 September 2026. The stories
were read only after a first pass had skipped them, and skipping them was the reason that
pass got the governance question wrong. The 2019 split is reported in the stories by people
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

The literature on how fast practices and habits lapse. Two papers on adult skill
depreciation were read on 13 September 2026 and put six per cent a week one to two
orders of magnitude above anything they measure, but they measure skills rather than
practices, so the rate is still a choice; Chapter Twelve gives the detail.

Anything independent about the 2019 split. The account above rests entirely on the
successor fellowship's own literature, written by people who left the predecessor. No
press coverage and no statement from the other side was sought. That is a one-sided
record and the book's use of it inherits the weakness.

The research literature on Buddhist and mindfulness-based recovery programs, which was
not searched at all. The follow-up section compares program documents and one
fellowship's account of its own history, and knows nothing about either fellowship's
outcomes.

# Appendix: The Working Paper

*Anonymity as an Aggregation Condition: Governance, Resource Structure,
and Membership Dynamics in Twelve-Step Mutual-Aid Organizations.*

This is the academic paper the book grew out of, reproduced so that the
book is self-contained. Its LaTeX source at
`paper/anonymity-as-an-aggregation-condition.tex` remains the single
source of truth for this document, and `paper/anonymity-as-an-aggregation-condition.pdf`
is its authoritative rendering; the copy below is converted from that
source at build time and its typesetting is the book's rather than the
paper's.

> **Scope and ethics.** This paper does not reproduce the text of the Twelve Steps or
> Twelve Traditions, which is copyrighted by Alcoholics Anonymous World Services, Inc.;
> short paraphrases are used throughout. AA is not affiliated with this work and, by its
> Sixth Tradition, could not be. Nothing in this paper can assess any individual's
> recovery, and it must not be used to do so. No AA publication was acquired for this
> project; the historical material is drawn from independent scholarship and from primary
> temperance sources in the public domain.

## Introduction

Two literatures have circled Alcoholics Anonymous without meeting. The clinical literature
asks whether AA works and through what mechanism; a Cochrane review concludes that
twelve-step facilitation performs at least as well as comparison treatments for abstinence
and operates chiefly through changes in participants' social networks (Kelly, Humphreys,
and Ferri 2020). The formal-modeling literature has produced compartmental models of
drinking dynamics (Sánchez et al. 2007; Sharma and Samanta 2015), agent-based models of
alcohol availability (Gorman et al. 2006), and individual-level dynamical models of
behavior change fitted to clinical data (Banks et al. 2014, 2017). Neither literature has
modeled the content of the Twelve Steps as a structured process, and neither has modeled
the Twelve Traditions at all.

The omission is notable because the Traditions constitute an unusually clean object of
institutional study. They are a written constitution for a radically decentralized
organization: codified in 1946 from a decade of documented group failures, formally
adopted in 1950, and unamended in substance since. They govern through autonomous groups
with no enforcement mechanism, no hierarchy, and no budget above the group level.
Organizations that hold a governance rule fixed for three-quarters of a century while
scaling through six orders of magnitude are rare, and rarer still is one whose founding
documents record the failure modes the rules were written to prevent.

**The central claim is narrow, formal, and interpretive at one joint.** Three of the
Traditions (group conscience with servant leadership, Tradition 2; the refusal to organize
hierarchically, Tradition 9; and anonymity with principles placed before personalities,
Tradition 12) share an effect that is invisible when they are read as ethics and immediate
when they are read as a constraint on a stochastic matrix: they prevent any member from
acquiring a non-vanishing share of the group's aggregate attention. That is precisely the
condition under which DeGroot (1974) belief averaging is asymptotically wise (Golub and
Jackson 2010). To our knowledge, this correspondence has not previously been stated.

The joint is worth naming before anything is built on it. The theorem is proved and was
read at source. The mapping from three sentences of a fellowship's constitution onto the
theorem's hypothesis is a reading of those sentences, arrived at by the author, and *no
computation anywhere in this paper touches it*. Everything downstream inherits that
status. Section 8.1 states what would settle it and Section 9 states what evidence would
overturn it.

Three further contributions support the central one. We derive the coupling between Steps
and Traditions from first principles, testing and rejecting the natural conjecture that
the two lists pair by index, a reading the historical record already casts doubt on. We
reformulate the Steps as a multistage production technology in the form of Cunha, Heckman,
and Schennach (2010), under which the informal rule that steps cannot be skipped becomes
the Leontief limit of a CES family and its strictness a single estimable parameter. And we
build a stochastic membership model disciplined by an institutional constraint central to
AA's design: under Tradition 3, an AA group cannot refuse *membership*, so "closing the
door" in the sense of excluding a person from the fellowship is not an action available to
any group, and open-door adherence operates through newcomer retention rather than
newcomer arrival. The constraint proves informative, separating empirically
distinguishable channels of group decline.

### Roadmap

Section 2 reviews the relevant literatures. Section 3 states the aggregation framework and
the mapping from Traditions to its conditions, with the rotation-scaling and
obstruction-scaling corollaries and the touring-speaker structure. Section 4 derives the
Step--Tradition coupling and reports six robustness designs against it. Section 5 presents
the CES formulation of the Steps and its identification strategy. Section 6 describes the
simulation model, its results, and the sensitivity analysis that bounds them. Section 7
gives the comparative historical case. Section 8 collects limitations; Section 9 states
predictions, marking where the analysis above already bears on them; Section 10 concludes.
Appendix A restates the paper in plain language. Appendix B is a reproducibility note.

## Literature Review

### Effectiveness and mechanisms of AA

The Cochrane review of twelve-step facilitation (Kelly, Humphreys, and Ferri 2020) finds
manualized TSF at least as effective as comparison treatments for continuous abstinence
and, in several trials, superior. The mechanism literature converges on social network
change: Kaskutas, Bond, and Humphreys (2002) find that AA's effect on drinking outcomes is
mediated substantially by changes in the composition of a participant's social network;
Rynes and Tonigan (2012) examine whether sponsorship effects reduce to network effects.
Measurement instruments for affiliation and involvement are established (Humphreys,
Kaskutas, and Weisner 1998; Tonigan, Connors, and Miller 1996; Greenfield and Tonigan
2013). The helper-therapy principle (Riessman 1965) and its AA-specific test (Pagano et
al. 2004) address whether helping others benefits the helper. Galanter (1981) supplies an
earlier account of why large-group affiliation relieves distress, which is the closest
antecedent to this paper's treatment of the group as a producer of resources members
consume.

### Formal models of drinking and recovery

Compartmental epidemic-style models treat drinking as transmissible (Sánchez et al. 2007;
Sharma and Samanta 2015). Agent-based work has modeled drinking in relation to alcohol
availability and outlet density (Gorman et al. 2006). Individual-level dynamical models
fitted to clinical data are due to Banks and coauthors (2014, 2017). The relapse
literature supplies the nonlinear, multiple-equilibrium structure this paper's individual
model borrows (Hufford et al. 2003; Witkiewitz and Marlatt 2004, 2007).

### Skill formation

The Steps are treated here as a multistage technology in the sense of Cunha and Heckman
(2007) and Cunha, Heckman, and Schennach (2010), with self-productivity, dynamic
complementarity, and a CES aggregator whose substitution parameter carries the substantive
content. Ben-Porath (1967) is the antecedent. Identification of latent skill from noisy
proxies follows Schennach (2004) and Hu and Schennach (2008).

### Social learning and the wisdom of groups

DeGroot (1974) gives the averaging model. Golub and Jackson (2010) give the condition
under which such averaging is asymptotically wise, together with the three obstructions to
it: prominent agents receiving non-vanishing attention, imbalance between attention given
and received, and insufficient dispersion between subgroups. This paper's central section
is an application of that result and nothing more; the theorem is not extended.

### Economics of religion, clubs, and teams

Iannaccone (1992) explains costly requirements as screening devices against free-riding in
collectives; Lembke (n.d.) applies the frame to AA directly. Holmström (1982) gives the
team production problem that a group producing a non-excludable good faces. Ostrom (1990)
supplies the design principles for self-governing common-pool institutions, of which the
Traditions are an unusually pure instance. Angrist (2014) and Carrell, Sacerdote, and West
(2013) supply the warning this paper takes most seriously about interventions built on
measured peer effects; see Section 6.7.

### Nineteenth-century mutual-aid temperance

The comparative case in Section 7 rests on primary temperance sources read at source
rather than on the secondary literature that descends from AA's own account: Grosh (1842),
the Washingtonian movement's own pocket manual; the autobiographies and histories of
Hawkins (1862), Marsh (1866), Gough (1869), Eddy (1887), and Blair (1888); and the later
scholarly treatments of Fehlandt (1904), Crothers (1911), and Krout (1925). Maxwell (1950)
is the one sociological comparison of the two fellowships we have found. Kurtz (1991) is
the standard scholarly history of AA and is used for the Traditions' drafting history.

### The gap

No prior work, so far as we have found, treats the Traditions as a formal constraint on an
influence structure, derives the Step--Tradition coupling rather than asserting it, or
models group-level membership dynamics under the institutional constraint that a group
cannot refuse membership. The gap is the paper's occasion; whether the paper fills it well
is the subject of Section 8.

## Governance as an Aggregation Mechanism

### Framework

A group of $N$ members holds beliefs about a matter of collective business. Let $A$ be the
row-stochastic trust matrix, $A_{ij}$ the weight member $i$ places on member $j$, and let
beliefs update by $b(t+1) = A\,b(t)$. Under strong connectivity and aperiodicity, beliefs
converge to a consensus equal to $s^{\top}b(0)$, where $s$, the influence vector, is the
normalized left stationary vector of $A$. Rows describe whose beliefs a member uses;
columns describe direct attention received. Neither row equality nor column sums alone are
long-run influence. Under the regularity conditions in Golub and Jackson (2010),
aggregation requires the largest stationary weight to vanish: $\max_j s_j \to 0$.

The error is available in closed form, which is how
Table [3](#tab:error){reference-type="ref" reference="tab:error"} is computed rather than
simulated. Assume here that the initial errors are iid Gaussian with standard deviation
$\sigma$. Then the consensus is $\mu + \sum_j s_j e_j$, a normal variable with mean zero
and standard deviation $\sigma\lVert s\rVert$, and for a mean-zero normal the expected
absolute value is its standard deviation times $\sqrt{2/\pi}$. So $$\begin{equation}
\mathbb{E}\,\lvert \text{consensus} - \mu \rvert \;=\; \sigma\,\lVert s\rVert\,\sqrt{2/\pi}.
\label{eq:err}
\end{equation}$$ Under equal weighting $s_j = 1/N$, so $\lVert s\rVert = N^{-1/2}$ and the
error is exactly $\sigma\sqrt{2/\pi}\,/\sqrt{N}$. The single-member baseline is the same
expression at $N=1$: $\sigma\sqrt{2/\pi} = 0.798$ at $\sigma = 1$. Every figure in this
section is deterministic algebra under that Gaussian benchmark, not Monte Carlo, and
carries no sampling error. Independence and a common variance without the Gaussian premise
are not sufficient for the consensus-error equation above.

### The mapping

| **Tradition (paraphrase)** | **Formal content** | **Role** |
|:---|:---|:---|
| 2\. Group conscience; leaders serve, do not govern | Offices are hypothesized not to confer persistent attention received | Proposed mechanism reducing stationary concentra­tion |
| 9\. No hierarchy; service rotates | Office-linked attention is periodically reassigned across a broad pool | Proposed mechanism preventing persistent stationary concentra­tion |
| 12\. Anonymity; principles before personalities | Some status cues on which attention may condition are suppressed | Proposed mechanism reducing one source of concentra­tion |
| 1\. Common welfare first | $A$ strongly connected | Precondi­tion for convergence |
| 4\. Group autonomy | No cross-group influence aggrega­tion | No prominent group at higher levels |
| 3\. Desire to stop drinking is the only require­ment for membership | $N$ unbounded; no screening on membership | Makes the asymptotic regime the relevant one |

: The mapping. **This table is an interpretation of the Traditions' wording, not a
result.** It is the paper's central and least verified step. {#tab:mapping}

::: {#prop:one .proposition}
**Proposition 1** (Vanishing stationary influence). *For a sequence of row-stochastic
influence matrices satisfying the convergence and signal conditions in Golub and Jackson
(2010), beliefs aggregate if the largest normalized stationary influence vanishes,
$\max_j s_j\to0$. Persistent stationary concentration on a bounded set is sufficient for
failure. A doubly stochastic matrix is a special case: its stationary vector is uniform
and $s_j=1/N$.*
:::

The institutional claim is a separate hypothesis: Traditions 2, 9, and 12 may make
persistent stationary concentration less likely. Their wording does not by itself imply
exchangeability or double stochasticity. Conversely, violating a Tradition is not
sufficient for aggregation failure; names, offices, and hierarchy can exist while
$\max_j s_j$ still vanishes.

::: remark
**Remark 1** (The status of Proposition [1](#prop:one){reference-type="ref"
reference="prop:one"}). *The established mathematics and the proposed mapping must not be
merged. Reading "leaders are trusted servants; they do not govern" as a mechanism limiting
attention received is an interpretation of a sentence, and a reader may reasonably hold
that Tradition 2 is about humility rather than weighting, or that anonymity is chiefly
protective of individuals and only incidentally structural. Nothing computed anywhere in
this paper validates that reading. Exchangeability is an additional assumption, not a
consequence of the absence of a named office. The testable institutional hypothesis is
directional: the Traditions reduce persistent concentration in $s$, not that they make
every realized weight equal.*
:::

### Failure modes, quantified

Tables [2](#tab:influence){reference-type="ref" reference="tab:influence"} and
[3](#tab:error){reference-type="ref" reference="tab:error"} report the two quantities
separately. They are distinct and are easily conflated: at $N = 10$ the flat regime's
maximum influence weight is 0.100 and its consensus error is 0.252, and only the first is
bounded by construction.

| $N$ |  Flat | Dominant | Caucus of 3 | Closed core of 5 | Rotating, pool 12 |
|----:|------:|---------:|------------:|-----------------:|------------------:|
|  10 | 0.100 |    0.350 |       0.167 |            0.200 |               n/a |
|  50 | 0.020 |    0.350 |       0.167 |            0.200 |             0.041 |
| 250 | 0.004 |    0.350 |       0.167 |            0.200 |             0.032 |
| 500 | 0.002 |    0.350 |       0.167 |            0.200 |             0.030 |

: Maximum influence weight $\max_j s_j$. Constructions: *dominant*, one member receives
0.35 of every row, remainder split evenly; *caucus*, three members receive 0.50 of every
row between them; *closed core*, five members receive 0.45 of every row and distribute
their own attention only among themselves; *rotating*, one of $R=12$ members holds share
0.35 in each term, time-averaged over the cycle (undefined at $N=10$, where the pool
exceeds the group). Exact to the digits shown; no sampling error. {#tab:influence}

| $N$ |  Flat | Dominant | Caucus of 3 | Closed core of 5 | Rotating, pool 12 |
|----:|------:|---------:|------------:|-----------------:|------------------:|
|  10 | 0.252 |    0.328 |       0.275 |            0.357 |               n/a |
|  50 | 0.113 |    0.289 |       0.238 |            0.357 |             0.132 |
| 250 | 0.050 |    0.281 |       0.232 |            0.357 |             0.093 |
| 500 | 0.036 |    0.280 |       0.231 |            0.357 |             0.087 |

: Mean $\lvert$consensus $-$ truth$\rvert$ at $\sigma = 1$, from
the consensus-error equation above, against a
single-member baseline of 0.798. Same constructions as
Table [2](#tab:influence){reference-type="ref" reference="tab:influence"}. {#tab:error}

Under flat weighting, error declines as exactly $N^{-1/2}$; under a dominant member or an
entrenched caucus it plateaus. The analytic limits confirm the tables: dominant tends to
$0.35\sqrt{2/\pi} = 0.279$; the caucus tends to 0.230; the closed core sits at exactly
$\sqrt{2/\pi}/\sqrt{5} = 0.357$, the error of a five-member group, because the influence
of every member outside the core is identically zero at every $N$, which is why that
column does not vary with $N$ at all.

The closed core is qualitatively worse than the other two and we did not expect that
before computing it. The first two put a floor under the group's error. The third deletes
the rest of the group from the calculation: in the limit all influence accrues to the
closed subgroup and the group's accuracy is exactly that of the subgroup alone, however
many other people are present. This is a direct consequence of Golub and Jackson's
imbalance condition and standard for absorbing sets in Markov chains; what is worth
reporting is the magnitude.

Consensus is reached in every regime. Concentration does not produce visible dysfunction,
only degraded accuracy delivered with undiminished confidence. Both of the first two
pathologies have vernacular names in AA: the old-timer whose view settles every group
conscience, and the caucus that has decided before the business meeting convenes.

### Obstruction is a property of scaling, not of severity

Golub and Jackson's three obstructions (prominent agents, imbalance, insufficient
dispersion) map naturally onto the dominant old-timer, the member whose sponsorship
lineage listens to him but who listens to nobody, and the clique. **That mapping was
asserted before it was computed, and computing it changed it.** The three obstructions are
properties of *sequences* of societies as they grow, not properties of a room.

Hold the magnitudes fixed and neither the clique nor the imbalanced member obstructs
anything. A clique of three giving a tenth of its attention outward holds, in aggregate,
0.750 of the influence at $N=10$, 0.375 at $N=50$, 0.107 at $N=250$ and 0.029 at $N=1000$.
A member receiving twenty times the attention he gives holds 0.690 at $N=10$, 0.290 at
$N=50$, 0.074 at $N=250$ and 0.020 at $N=1000$. Both shares vanish, both satisfy the
condition, and neither is an obstruction.

Now let the same two practices scale with the group. A clique whose inwardness approaches
one as the group expands holds 0.167 at every size tested from 10 to 1000. A member whose
attention advantage grows in proportion to the group runs from 0.182 at $N=10$ to 0.168 at
$N=1000$, converging to a positive share rather than settling on one exactly. Neither
falls toward zero, and that is the whole of what makes them obstructions.

::: corollary
**Corollary 2** (Obstruction scaling). *Whether a concentration of attention obstructs
group learning is determined by how it scales with $N$, not by how severe it is at any one
$N$. The diagnostic question about any concentration is therefore not how large it is but
whether it would still be there if the group doubled.*
:::

It is easy to read the three obstructions as three things a room can have at a given
moment, and on that reading a tight clique is an obstruction wherever it appears. It is
not. The general form of the point is the rotation result that follows.

### Rotation must scale

::: proposition
**Proposition 3** (Rotation breadth). *If service rotates over a pool of $R$ members, each
officeholder attracting attention share $\alpha$, time-averaged maximum influence is
approximately $\alpha/R$ plus residual flat weight. With $R$ fixed as $N$ grows,
$\max_j s_j$ is bounded below and the wisdom condition fails despite rotation.*
:::

At $N=400$ and $\alpha = 0.35$, the sweep over $R$ gives maximum influence 0.118, 0.060,
0.031, 0.016, 0.009, 0.005 and 0.003 at $R = 3, 6, 12, 25, 50, 100$ and 400, against a
flat benchmark of 0.0025. The $\alpha/R$ approximation tracks the computed value closely
at every point, which is the check that the mechanism is the one claimed. Holding the pool
at twelve while the group grows, maximum influence converges to a floor (0.041, 0.035,
0.032, 0.031, 0.030 at $N = 50, 100,
200, 400, 800$) while the flat benchmark does not (0.020, 0.010, 0.005, 0.0025, 0.0013).
The ratio between them runs 2.1, 3.5, 6.4, 12.3, 23.9. That divergence is the entire
result.

The pool required to come within a factor of two of flat is 13 at $N=50$, 26 at 100, 52 at
200, 104 at 400 and 208 at 800: **twenty-six per cent of the membership throughout**,
which is the operational form of the corollary.

### Rotation may be aimed at the wrong positions {#sec:elders}

The rotation result prices a pool that is too narrow. A separate objection, raised by the
fellowship's own commentary, is that the pool may be irrelevant. *Twelve Steps and Twelve
Traditions* (AAWS 1953) describes a group's rotating committee as sharply limited in
authority, states that in no sense whatever can its members govern or direct the group,
and then locates leadership elsewhere: in "elder statesmen," former officeholders who are
called the real and permanent leadership, who are said to become the voice of the group
conscience, and to whom a perplexed group inevitably turns. Those members hold no office
and therefore rotate out of nothing.

We model this directly. Let $e$ members hold share $\alpha_e$ of every row collectively,
with no rotation, and let the remaining attention be flat. This is not the dominant-agent
family reparameterised: the share is collective and there is no cycle to time-average.

::: proposition
**Proposition 4** (Advisory concentration). *Under the structure above,
$\max_j s_j \to \alpha_e / e$ as $N \to \infty$, which is bounded away from zero for any
$\alpha_e > 0$. The wisdom condition fails independently of the rotation pool $R$, since
the concentration lies outside it.*
:::

With $e = 3$ and $\alpha_e = 0.10$, maximum influence is 0.1233, 0.0513, 0.0369 and 0.0342
at $N = 10, 50, 250$ and 1000, against the predicted floor of 0.0333 and a flat benchmark
falling to 0.0010. Expected consensus error is 0.2552, 0.1214, 0.0681 and 0.0525 against
flat values of 0.2523, 0.1128, 0.0505 and 0.0252: a penalty of one per cent at $N = 10$
rising to a factor of 2.08 at $N = 1000$.

The decision-relevant contrast is whether the twenty-six per cent corollary rescues such a
group. It does not. Fixing $R = \lceil 0.26 N \rceil$ at every size and reporting
$\max_j s_j$ as a multiple of the flat benchmark: rotation alone holds at 2.0, 2.0, 2.0 at
$N = 50, 250, 1000$, which is a self-consistency check since twenty-six per cent was
defined as the within-a-factor-of-two pool. Adding three elders at $\alpha_e = 0.10$ gives
2.5, 9.2, 34.2. At $\alpha_e = 0.20$, 4.1, 17.4, 67.4. With five elders at
$\alpha_e = 0.20$, 2.7, 10.7, 40.7.

### Touring speakers: a closed form

A movement's attention structure can be modeled as bipartite: flat attention within local
societies, plus cross-society attention flowing through touring speakers. Let each member
give fraction *out* of their attention to the speakers and let the speakers return
fraction *back* of theirs to the general membership. Then $$\begin{equation}
\text{speakers' share of total influence} \;=\; \frac{\text{out}}{\text{out} + \text{back}},
\label{eq:speakers}
\end{equation}$$ exact to twelve decimal places, **independent of the number of members
and of the number of speakers**. Five speakers receiving three tenths of the movement's
attention and returning two tenths of their own hold six tenths of the influence in a
movement of ten and in a movement of a thousand alike.

This is stronger than the argument it replaces. It is not that the influence vector
converges on the speakers as the movement grows; the speakers' share is fixed by a ratio
and does not move with size at all, because growth adds members to the denominator of the
local channel and to the numerator of the speaker channel in equal measure. Section 7
applies it.

## Deriving the Step--Tradition Coupling

### A natural conjecture, tested {#sec:conjecture}

Two ordered lists of twelve, printed in a single volume, invite the conjecture that Step
$i$ draws on Tradition $i$. The conjecture merits testing rather than adoption. The
historical record gives grounds for doubt: the Traditions were codified from 1946 essays
written roughly a decade after the Steps, in response to specific organizational crises,
and no AA doctrine pairs the lists by index.

That last clause was previously an assertion about literature the project had not read. It
has since been checked. *Twelve Steps and Twelve Traditions* (AAWS 1953) is the only work
treating both lists at length, one chapter each, by the same author, and is therefore
where an intended pairing would surface. Across its twelve Tradition chapters, none cites
the Step of its own number; across its twelve Step chapters, the word *Tradition* does not
occur at all. The single indexed cross-reference in the volume runs off-index: the chapter
on Tradition 8 mentions the Twelfth Step, to distinguish paid service work from
twelfth-step work itself. The count is reproducible in minutes from the files AAWS
publishes free, and the procedure is stated here rather than only its result: in each
Tradition chapter, count references to the same-numbered Step; in each Step chapter, count
occurrences of *Tradition*. The stakes are concrete. Under index-pairing, Step 5 (telling
one's inventory to another person) would depend on Tradition 5 (primary purpose), though
what the step plainly requires is confidentiality, which is Tradition 12; and Step 12
(carrying the message) would couple to anonymity, though Tradition 5 states nearly the
same sentence. We therefore derive the coupling from first principles and test the
conjecture against the result.

### Method

To avoid re-deriving the same mistake, no direct step-to-tradition mapping is permitted.
An intermediate layer of eight group-produced resources is introduced (admission and
standing, identification, living proof, confidential audience, counsel, a recipient for
twelfth-step work, continuity, and normative pressure), and the coupling is computed as
$$\begin{equation}
B \;=\; S\,G^{\top},
\end{equation}$$ where $S[i,r]$ records how much Step $i$'s execution consumes resource
$r$ (written by asking what each step requires) and $G[j,r]$ records how much Tradition
$j$ governs the supply of $r$ (written independently of $S$). Both matrices are
hand-written judgments. That is the whole of their evidentiary status, and Section 4.5
does not soften it.

### Results

Table [4](#tab:coupling){reference-type="ref" reference="tab:coupling"} gives the
unperturbed coupling.

| Step           | Principal | Value | Runner-up | Value | Index-mate | Value | Its rank |
|:---------------|:----------|------:|:----------|------:|:-----------|------:|---------:|
| 1 admit        | T3        |  1.22 | T1        |  0.99 | T1         |  0.99 |        2 |
| 2 believe      | T11       |  0.82 | T5        |  0.72 | T2         |  0.13 |        7 |
| 3 decide       | T2        |  0.31 | T1        |  0.27 | T3         |  0.01 |        7 |
| 4 inventory    | T1/T2 tie |  0.35 | ---       |   --- | T4         |  0.00 |        8 |
| 5 tell someone | T12       |  1.08 | T1        |  0.65 | T5         |  0.12 |        5 |
| 6 willing      | T1        |  0.25 | T2        |  0.24 | T6         |  0.00 |        7 |
| 7 ask          | T1        |  0.17 | T2        |  0.13 | T7         |  0.00 |        7 |
| 8 list harms   | T2        |  0.43 | T1        |  0.29 | T8         |  0.07 |        4 |
| 9 amends       | T2        |  0.90 | T1        |  0.48 | T9         |  0.00 |        8 |
| 10 daily       | T1        |  0.94 | T2        |  0.43 | T10        |  0.00 |        8 |
| 11 connect     | T1        |  0.47 | T2        |  0.21 | T11        |  0.11 |        4 |
| 12 carry it    | T5        |  1.25 | T3        |  1.10 | T12        |  0.12 |        6 |

: The author-coded semantic overlap $B = SG^{\top}$, unperturbed. It is not the executable
state-update map. Competition ranks use $1+$ the count of strictly larger entries, so
exact ties share rank. Not one Step has its index-mate in the maximizing set. Load per
Tradition, exact: T1 6.52, T2 3.89, T5 3.88, T3 2.69, T11 2.69, T12 2.62, T8 1.11, and
exactly zero for T4, T6, T7, T9 and T10. {#tab:coupling}

1.  **The author coding contains a two-tier division.** Five Traditions (autonomy,
    non-endorsement, self-support, non-hierarchy, and no outside issues) have identically
    zero rows in $G$. Those zeros were assigned by the author; the matrix multiplication
    reveals their consequences but does not independently discover or validate the
    classification.

2.  **Unity has the largest raw semantic load under this coding.** Under index-pairing,
    unity fed one step; in the authored matrices it overlaps with resources consumed by
    nearly every Step. The multiplication summarizes those judgments; it does not supply
    independent evidence for them.

3.  **The index-pairing conjecture is rejected on all twelve counts.** Step 5's principal
    supplier is Tradition 12 and Step 12's is Tradition 5, the two correspondences a
    reader would guess, reversed.

4.  **Classification is not always intuitive.** Tradition 8 (non-professionalism), which a
    functional reading might class as protective, lands in the enabling tier with small
    load, because it governs the identity of the confidential hearer, a fellow member
    rather than a clinician.

### Six robustness designs, and what each can and cannot see

##### The trivial-count decomposition, stated first because it deflates the headline.

T4, T6, T7, T9 and T10 have identically zero rows in $G$, so Steps 4, 6, 7, 9 and 10 have
index-mate entries of exactly zero, and index-pairing cannot hold for them under *any*
perturbation that preserves sparsity. Both multiplicative designs below preserve sparsity.
The consequence is checkable and was checked: at every level, the proportion of draws in
which index-pairing fails on all twelve equals the proportion in which it fails on the
seven non-trivial Steps, to the last draw (98.75 and 98.75 at $\pm15$ per cent; 85.50 and
85.50 at $\pm30$; 72.45 and 72.45 at $\pm50$; 65.15 and 65.15 at $\pm75$; 40.60 and 40.60
structurally). **Five of the twelve counts are not evidence, and no multiplicative design
could have made them so.**

##### Design 1, multiplicative jitter.

Every entry of $S$ and $G$ is multiplied by an independent uniform draw on $[1-L, 1+L]$
for $L \in \{0.15, 0.30, 0.50, 0.75\}$; 2,000 draws per level, seed 3. This represents a
reader who disagrees with the magnitudes by up to $L$ and agrees about which cells are
empty.

##### Design 2, structural randomization.

Every non-zero entry of $S$ and $G$ is replaced by an independent uniform draw on
$[0.05, 1.00]$; zeros stay zero. 2,000 draws, seed 23. This represents a reader who
accepts only the pattern of which Tradition touches which resource and rejects every
magnitude we chose. A parallel 1,000-draw screen passes randomized nonzero matrices
through the full executable model: the referral-versus-pure-attraction comparison is
strict in all 1,000 draws on final membership and endpoint viability and in 999, with one
tie, on existence. Full-adherence viability in all three screening seeds holds in only 784
draws. The comparison and the absolute outcome therefore cannot borrow one another's
robustness.

| Design | T1 leads | Index-pairing wrong, all | Step 5 $\to$ T12 | Step 12 $\to$ T5 |
|:---|---:|---:|---:|---:|
| jitter $\pm$`<!-- -->`{=html}15% | 100.0 99.8 to 100.0 | 98.8 98.2 to 99.2 | 100.0 99.8 to 100.0 | 89.7 88.3 to 91.0 |
| jitter $\pm$`<!-- -->`{=html}30% | 100.0 99.8 to 100.0 | 85.5 83.9 to 87.0 | 99.5 99.1 to 99.7 | 67.3 65.3 to 69.4 |
| jitter $\pm$`<!-- -->`{=html}50% | 98.0 97.3 to 98.5 | 72.5 70.5 to 74.4 | 88.7 87.2 to 90.0 | 52.9 50.7 to 55.1 |
| jitter $\pm$`<!-- -->`{=html}75% | 86.8 85.3 to 88.3 | 65.2 63.0 to 67.2 | 71.5 69.5 to 73.4 | 43.8 41.6 to 45.9 |
| **structural** | **75.4 73.5 to 77.2** | **40.6 38.5 to 42.8** | **17.5 15.9 to 19.2** | **27.6 25.7 to 29.7** |

: Percentage of draws in which each claim holds. Wilson intervals at 95 per cent on
$n = 2{,}000$. The two 100.0 entries are 2,000 of 2,000 and should be read as "not
observed to fail", not as certainty. {#tab:coupling-robust}

Step 12 is the fragile row and the reason is the margin, not the level: its top two are T5
at 1.25 and T3 at 1.10, and both Traditions govern the recipient resource (T5 at 0.9, T3
at 0.8), so a perturbation moving them in opposite directions flips the winner.

##### Design 3, the threshold test, which is the only one that can see the five.

For Step $i$, let $w_i$ be the row sum of $S$ (total consumption across the eight
resources) and $b_i$ the largest entry in row $i$ of $B$ excluding the index-mate's own
entry. If Tradition $i$ governed every resource at a uniform strength $c$, its entry in
row $i$ would be $c\,w_i$, so index-pairing holds at Step $i$ exactly when
$$\begin{equation}
c \;>\; c^{*}_i \;=\; b_i / w_i .
\end{equation}$$ This is one division per Step, carries no sampling error, and is the only
design here that can turn a structural zero into a non-zero.

|   Step | Index-mate | Beats | Row sum of $S$ |   $c^{*}$ | $c^{*}$ / mean live entry |
|-------:|:-----------|------:|---------------:|----------:|--------------------------:|
|      1 | T1         |  1.22 |           2.40 |     0.508 |                      1.36 |
|      2 | T2         |  0.82 |           1.70 |     0.482 |                      1.29 |
|      3 | T3         |  0.31 |           0.70 |     0.443 |                      1.18 |
|  **4** | **T4**     |  0.35 |           0.80 | **0.438** |                      1.17 |
|      5 | T5         |  1.08 |           1.70 |     0.635 |                      1.70 |
|  **6** | **T6**     |  0.25 |           0.60 | **0.417** |                      1.11 |
|  **7** | **T7**     |  0.17 |           0.40 | **0.425** |                      1.14 |
|      8 | T8         |  0.43 |           0.80 |     0.538 |                      1.44 |
|  **9** | **T9**     |  0.90 |           1.50 | **0.600** |                      1.60 |
| **10** | **T10**    |  0.94 |           1.50 | **0.627** |                      1.67 |
|     11 | T11        |  0.47 |           0.80 |     0.588 |                      1.57 |
|     12 | T12        |  1.25 |           2.40 |     0.521 |                      1.39 |

: The threshold test. Bold rows are the five protective Traditions, whose index-mate
entries are structurally zero and therefore invisible to
Table [5](#tab:coupling-robust){reference-type="ref" reference="tab:coupling-robust"}.
Exact; no sampling error. {#tab:threshold}

The governance matrix has 35 non-zero entries of 96 cells, with mean 0.374, median 0.300,
minimum 0.10 and maximum 1.00. *Every* $c^{*}$ exceeds both the mean and the median. The
protective range, 0.417 to 0.627, is not contained in the enabling range, 0.443 to 0.635;
it extends below it at both ends. Mean $c^{*}$ is 0.501 for the five protective Steps,
0.531 for the seven enabling ones, and 0.518 across all twelve. The protective Steps are
therefore marginally *closer* to index-pairing holding, by 0.03 on the mean threshold,
which is the direction an objector would predict and an order of magnitude smaller than
the distance to the mean live entry. Setting $c$ to the mean live entry of 0.374 for every
Step simultaneously, all twelve index-mates still lose, by margins from 0.02 at Step 7 to
0.44 at Step 5.

What the test licenses is the statement that index-pairing would require the index-mate to
govern its own Step's needs more strongly than a typical entry in the matrix, uniformly
across all twelve. What it does not license is any statement about whether the zeros are
correctly *placed*: it holds the sparsity pattern's origin fixed and prices only its
consequences. It is a sensitivity analysis of a judgment, not a test of it.

##### Design 4, the resource-list test.

Delete each of the eight resources in turn, then merge each pair, then delete each pair:
sixty-four resource lists in all. Only Step 1 and Step 2 ever regain their index-mates, in
fifteen variants and one respectively, and every one of the fifteen Step 1 failures
involves removing or merging the admission resource, which is precisely what gives the
open door its lead there. This establishes that the list is no *finer* than it needs to
be. It cannot establish that the list is fine *enough*, because inventing a ninth resource
requires a judgment about what it contains and cannot be done by rearranging the eight.

##### Design 5, the reassignment test.

Kurtz (1991) records that in some later AA literature the concept conveyed by
*single-purposed* was obfuscated by substituting *unity*. If the governance matrix
absorbed that semantic drift, unity's primacy is an artifact of it. For each of the eight
resources in turn, set $G[\text{T5},r]$ to the maximum of its current value and
$G[\text{T1},r]$, set $G[\text{T1},r]$ to zero, and recompute: this transfers unity's
entire governance of one resource to singleness of purpose, which is the strongest form of
the objection, and it is exact. **Six of the eight transfers leave unity leading**, by
margins from 1.44 to 2.54. Transferring continuity gives T5 the lead 5.14 to 4.63;
transferring pressure gives it 5.12 to 4.66. So unity's primacy is conditional on two
assignments and on nothing else in the matrix. Notably, the single resource-list variant
that breaks it (Design 4) drops continuity and pressure together, which is exactly the
pair this test identifies: two independent designs agreeing on which two resources carry a
result is worth more than either alone. The passage Kurtz names as decisive is in an
AA-copyright work that has not been obtained, so the source identified as settling the
question is unread. The 1953 commentary, read in full on 10 August 2026, keeps unity and
singleness of purpose apart across its chapters on Traditions 1 and 5, which corroborates
the assignment without being the passage Kurtz cited.

##### Design 6, sparsity perturbation.

Every design above varies magnitudes and holds the sparsity pattern fixed; a second reader
would disagree about the pattern. Flipping cells at random within the seven enabling rows
(56 cells, so the two-tier split is held fixed), 2,000 draws per row:

| Cells flipped | Index-pairing wrong, all | T1 leads | Step 5 $\to$ T12 | Step 12 $\to$ T5 |
|--------------:|-------------------------:|---------:|-----------------:|-----------------:|
|             1 |                    96.3% |   100.0% |            98.7% |            94.8% |
|             2 |                    92.7% |    99.7% |            96.3% |            90.5% |
|             4 |                    86.2% |    96.5% |            93.3% |            80.3% |
|             8 |                    75.0% |    83.7% |            85.4% |            72.0% |
|            16 |                    53.0% |    50.8% |            70.8% |            53.0% |

: Sparsity perturbation. Section 4 tolerates a reader differing on about four of fifty-six
enabling cells and does not tolerate one differing on sixteen. {#tab:sparsity}

**This is a bound, not a measurement, and the distinction is the caveat.** A random flip
is not a plausible reader. Somebody who thinks self-support governs continuity changes
that cell for a reason, and their remaining cells correlate with the reason. Random flips
are harsher in respecting no reason and gentler in not concentrating on the cells that
carry the results. The sweep answers "how much disagreement, counted in cells" and says
nothing about which cells a reader would choose. It also holds the two-tier split fixed,
because the split is what defines which rows are available to flip, so the more serious
disagreement, a reader who fills a protective row, cannot be represented by any
perturbation design at all. Only completed elicitation forms can answer either question,
and none has been returned; see Section 8.

### What the coupling results rest on

Two classes of claim in this paper rest on different things and must not be defended the
same way.

The executable model's **referral-versus-pure-attraction comparison** survives replacing
every nonzero matrix magnitude with a random value while preserving sparsity: 1,000 of
1,000 strict draws on final membership and endpoint viability, and 999 strict plus one tie
on existence. The fully adherent group's endpoint viability is not invariant. This result
concerns the executable model, not the raw coupling statistics in this section.

The **coupling** claims of this section do not. Index-pairing fails on all twelve in only
40.6 per cent of structurally randomized draws, which is less often than it holds; the
Step 5 inversion survives in 17.5 per cent and the Step 12 inversion in 27.6. These claims
rest on the magnitudes in two matrices we wrote, and they must be argued for rather than
certified by a robustness percentage earned elsewhere. The one exception is unity's
primacy, which survives structural randomization in 75.4 per cent of draws, the highest
figure of any claim in this section: three-quarters of the time a random matrix with the
same sparsity pattern puts unity first anyway.

A reader who thinks the two matrices are arbitrary should not be persuaded by Section 4,
and we would rather say so than borrow an executable endpoint comparison's robustness for
a semantic-coupling result that has not earned it.

## The Steps as a Multistage Technology

> **This section is a reformulation, not the simulation's update rule, and the two must
> not be read as the same object.** The CES form below is a way of *stating* the ordering
> claim so that its strictness becomes one estimable parameter. The dynamic model of
> Section 6 uses the gated-growth equation given in §6.2, which is not a CES aggregator.
> Nothing in Section 6 depends on the value of $\rho$.

Let $x_{i,t}$ denote latent practice of step $i$. Following Cunha, Heckman, and Schennach
(2010): $$\begin{equation}
x_{i,t+1} \;=\; A_i \Big[\, \gamma_{i1} x_{i,t}^{\rho_i} + \gamma_{i2} x_{i-1,t}^{\rho_i}
 + \gamma_{i3} G_{i,t}^{\rho_i} + \gamma_{i4} M_t^{\rho_i} \,\Big]^{1/\rho_i},
\end{equation}$$ with weights summing to one, elasticity of substitution
$\sigma_i = 1/(1-\rho_i)$, $G_{i,t}$ the resource bundle from Section 4, and $M_t$
maintenance capacity built from Steps 10 to 12. (Cunha, Heckman, and Schennach write the
substitution parameter as $\phi$ and reserve $\rho$ for an outcome share; $\rho$ here is
our notation.) Self-productivity is $\gamma_{i1} > 0$; the cross-partial in prior-stage
stock and group input is positive throughout (from $+1.73$ at $\rho = -4$ to $+0.08$ at
$\rho = 0.5$), so group support is worth more to a member who has done the preceding work:
dynamic complementarity in Cunha and Heckman's sense.

::: proposition
**Proposition 5** (The ordering rule as a limit). *As $\rho_i \to -\infty$ the aggregator
converges to $\min(\cdot)$, so zero prior-stage stock forces zero output: the informal
rule that steps cannot be skipped. The rule holds for all $\rho_i \le 0$ and fails for
$\rho_i > 0$, where the group input substitutes for the missing stage (output 0.217 at
$\rho = 0.3$ with prior stage at zero).*
:::

The reduction converts a widely held but untested claim of practice into a sharp empirical
question: within this CES reformulation, the sign of $\rho$ decides whether the Steps are
a chain or a menu. Estimating that sign would require an empirical identification design;
the calculation here does not estimate it. In the one setting where an analogous parameter
has been estimated, children's skill formation, Cunha, Heckman, and Schennach (2010) find
it positive in early childhood and strongly negative later for cognitive skill, and
negative at both stages for noncognitive skill, so there is no reason to expect a single
sign across all twelve Steps.

### Identification, anchoring, and design

Latent practice would have to be measured with a design that addresses error in the
inputs, loadings, scale, and group-input endogeneity. Schennach (2004) and Hu and
Schennach (2008) describe identification strategies under explicit assumptions, but this
paper does not implement them. Its simulation gives the four regressors and proxy loadings
to the estimator without error and adds noise only to the outcome. Repeating that exercise
shows the modest point that averaging three rescaled output proxies improves resolution
relative to one. It does not recover a latent-variable estimator, justify three
instruments per latent per wave, or settle the sign of $\rho$.

The binding obstacle to estimation is endogeneity of the group input: groups direct
attention to struggling members and successful members attract sponsees, so $G$ is not
exogenous to member state. CHS address the analogous endogeneity of parental investment;
adapting their approach is necessary before any fit to panel data and is not attempted
here.

## Membership Dynamics Under the Open Door

### The institutional constraint, restated

Tradition 3 makes the desire to stop drinking the sole requirement for **membership**. It
is tempting to render this as "an AA group cannot refuse admission," and that overstates
it. AA groups hold closed meetings as a matter of routine, and a closed meeting restricts
who is present in a room; it does not remove anyone's membership in the fellowship. The
constraint is on membership, not on attendance, and the model is built to that constraint.
The distinction was supplied by a reader who knows the rooms, and it is the single
correction this work has received that changed the most for the fewest words.

The distinction has modeling consequences. Arrival at a meeting does not depend on the
group's welcome in the default model. Tradition 3 instead has two separately controllable
paths: its row governs four resource columns, and it adds dropout friction weighted by
inverse practice. The second is not an early-tenure variable: the model contains no tenure
or cohort state, so a long-tenured low-practice member receives the same weight as a
recent arrival at the same practice. Inflow contains an exogenous referral floor
independent of the group's attractiveness; exit also includes a practice-independent churn
term for relocation and mortality.

Two further design choices follow from the same logic. Carrying capacity is supplied by
the established core rather than the population mean, since a room of three veterans and
twenty newcomers still contains three people able to carry a newcomer. And the
maintenance-capacity gate, whose role is to model relapse in members with something to
maintain, phases in with step index rather than throttling entry-level growth, to which it
does not conceptually apply.

### Model summary

Members occupy a twelve-dimensional practice state. Per-step growth, in full, for member
$m$ and step $i$: $$\begin{equation}
\frac{dx_i}{dt} \;=\; h(m)\, a_i\, \mathrm{gate}_i\, \mathrm{peer}_i\, C^{m}_i\,\bigl(1 - x_i\bigr)
 \;-\; d_i\, x_i,
\label{eq:growth}
\end{equation}$$ with $$\begin{align}
\mathrm{gate}_i &= x_{i-1}^{\,p}, \qquad \mathrm{gate}_1 = 1, \\
\mathrm{peer}_i &= (1-\beta_i) + \beta_i G_i, \qquad G = S_{\text{norm}} R, \\
C^{m}_i &= 1 - w(i)\,(1 - C), \qquad w(i) = 0.05 + (i-1)\tfrac{0.95}{11}, \\
d_i &= \delta_0\bigl(1 + \psi(1 - x_{i+1})\bigr) \ \ (i < 12), \qquad d_{12} = \delta_0 .
\end{align}$$ Maintenance capacity $C$ is identical across steps for a given member and is
defined in two parts. Own capacity is a Hill gate on $M$, the mean of that member's Steps
10 to 12, and group support supplies a floor beneath it: $$\begin{equation}
C(M) = \frac{M^{n}}{k^{n} + M^{n}}, \quad n = 3.0,\ k = 0.12;
\qquad
C = C(M) + \bigl(1 - C(M)\bigr)\,\omega\,\overline{C}, \quad \omega = 0.75,
\label{eq:capacity}
\end{equation}$$ where $\overline{C}$ is the mean own-capacity across living members, so a
member whose own maintenance has collapsed retains a fraction of capacity as long as the
group around them has not. Because Steps 10 to 12 sit at the heavy end of the $w(i)$
weighting, maintenance gates its own accumulation. That architecture can be bistable, but
it is not generally so in the corrected model's own endpoint environments: a
capability-one high/low-start test separates in 7 of 400 environments and collapses to one
low state in the mean environment. Here $w(i)$ is per-step exposure to it, rising linearly
from 0.05 at Step 1 to 1.00 at Step 12, which is the formal content of the claim that an
arrival has nothing to maintain and a veteran has a great deal; and $h(m)$ is member
heterogeneity, a lognormal draw made once when a member arrives and fixed thereafter. It
is parameterized as $\exp(N(-\sigma_h^2/2,\sigma_h))$, so its arithmetic expectation is
one and changing $\sigma_h$ changes dispersion without mechanically changing mean
capability.

Group resources $R$ are produced from member states through the governance-weighted
averages of Section 4, so shortfalls do not compound multiplicatively, with protective
Traditions acting solely as multipliers on the enabling ones they guard. Membership is
endogenous: arrivals are exogenous referrals plus attraction proportional to members'
twelfth-step practice and the attraction path of Tradition 11; exits combine
practice-dependent dropout, the Tradition-3 friction path, and churn. Tradition 11 also
has a distinct resource-governance path. Integration is Euler at $dt = 0.5$ weeks over a
1,560-week (thirty-year) horizon. This horizon is a reporting choice, not a steady-state
assertion. In 200-seed checks, mean membership is 29.34, 21.14, 16.43 and 15.64 at 10, 20,
50 and 100 years. The 100-year condition includes one closure. Paired changes in final
membership from $dt=0.5$ to 1.0, 0.25 and 0.125 weeks are respectively 1.54 $\pm$ 1.78,
0.87 $\pm$ 1.84 and -0.41 $\pm$ 1.74. None resolves at this sample size, so the tested
step is adequate for the reported finite-horizon comparisons; the runs do not establish an
equilibrium or indefinite persistence.

Parameters: $\delta_0 = 0.06$ per week (unattended half-life 11.6 weeks), $\psi = 0.20$,
$p = 1.5$, step top speeds from 0.15 at Step 9 to 0.30 at Step 1. The inventory is 22
continuous scalars, 12 step speeds, 49 non-zero cells in $S$ and 35 in the governance
matrix: **118 registered sensitivity values out of 226 listed cells, none fitted.** The
model-choice inventory separately records fixed constants, structural zeros, equations,
thresholds and experiment-design choices, so 118 is not the count of every authored
choice.

::: remark
**Remark 2** (Calibration, and the exact sense in which it fails). *Inflow, dropout and
churn were originally set to target a group near forty-five members with an experienced
core near nine, roughly a healthy urban meeting. That was calibration to a stylized fact,
not a dataset. After the lognormal capability draw was corrected to have arithmetic mean
one, the target fails. Across 400 runs the model delivers 17.80 members, 95 per cent
half-width 0.88. Among the 394 viable endpoints, the *established* count above 0.1 is
14.13, half-width 0.79, and the *experienced* count above 0.5 is 1.25, half-width 0.20.
The two thresholds are not interchangeable. The authored rates are not retuned after
observing this failure, and the absolute levels are not estimates of real meetings.*
:::

::: remark
**Remark 3** (Thirty-five parameters that cannot matter at full adherence). *The
governance matrix is column-normalized, so governance quality is identically 1 when every
Tradition is at 1.0 and the matrix cancels exactly. This is algebra, not simulation. All
35 governance cells therefore produce exactly zero change in every outcome at full
adherence, and a sensitivity design that perturbs them and reports no effect has found
nothing. Thirty-five of the 118 registered values are in that position.*
:::

### Three channels of decline

Four configurations, 400 paired seeds each, thirty-year horizon, $dt = 0.5$ weeks.
"Viable" means more than five members; existence means at least one, and zero is permanent
closure. **Quality is established-member practice in viable groups and is conditional
throughout; the viable fraction is printed beside it in every row.** Viability carries a
95 per cent Wilson interval; membership and quality carry a 95 per cent half-width from
the cross-run standard error.

| Condition | Viable y10 | $N$ if viable, y10 | Quality y10 | Viable y30 | 95% int. | Quality y30 |
|:---|---:|---:|---:|---:|---:|---:|
| nothing wrong | 0.9975 0.9860 to 0.9996 | 29.40 ± 1.16 | 0.3016 ± 0.0052 | 0.985 | 0.968--0.993 | 0.2648 ± 0.0058 |
| invisible | 0.9925 0.9782 to 0.9974 | 12.98 ± 0.34 | 0.2949 ± 0.0079 | 0.985 | 0.968--0.993 | 0.2592 ± 0.0071 |
| unreferred | 0.660 0.612 to 0.705 | 16.47 ± 1.18 | 0.3475 ± 0.0084 | 0.0275 | 0.015--0.049 | 0.3642 ± 0.0443 |
| unwelcom­ing | 0.905 0.872 to 0.930 | 15.70 ± 0.82 | 0.3597 ± 0.0097 | 0.5475 | 0.499--0.596 | 0.3211 ± 0.0134 |

: Decline scenarios, **400 paired seeds**, 1,560-week horizon. *Invisible* sets only
Tradition 11's attraction path to zero; *unreferred* sets exogenous inflow to zero;
*unwelcoming* sets both Tradition 3 paths to zero. Only eleven unreferred runs are viable
at year thirty, so its conditional quality interval is wide. {#tab:decline}

Membership counted over all runs with closures as zero reaches, at year thirty,
17.80 ± 0.88, 12.38 ± 0.34, 0.51 ± 0.23 and 6.76 ± 0.59 respectively.

Three signatures separate. Attraction loss leaves a smaller remnant sustained by referrals
and produces no closure. Referral loss closes 89.5 per cent of groups by year thirty,
while the eleven viable endpoints have high conditional practice. Combined Tradition 3
loss closes 25.0 per cent and leaves 54.8 per cent viable.

The mortality profiles follow from structure rather than from hand-tuning. A group on one
engine has no floor underneath it: its inflow becomes a function of its own state, which
makes the population dynamics multiplicative rather than additive, and a multiplicative
process with no floor has an absorbing state at zero. Invisible and unwelcoming groups
retain a referral floor, but the latter can still close through its resource and dropout
paths. Unreferred groups are the only ones whose inflow itself can go to zero and stay
there.

### The gap between decline and death

The unreferred condition separates two questions that a single membership series
conflates.

| Series | y5 | y10 | y20 | y30 |
|:---|---:|---:|---:|---:|
| unreferred, all runs | 21.55 ± 1.01 | 11.68 ± 1.02 | 2.50 ± 0.48 | 0.51 ± 0.23 |
| unreferred, viable only | 22.07 ± 1.00 | 16.47 ± 1.18 | 11.39 ± 1.37 | 12.27 ± 3.81 |
| viable fraction | 0.970 | 0.660 | 0.1725 | 0.0275 0.015 to 0.049 |

: Unconditional versus viability-conditioned membership under referral loss. Both decline
sharply; conditioning still hides the mass of closures but no longer makes membership look
stable. {#tab:conditional}

This is why conditioning is load-bearing throughout the paper. In the referral-loss
condition both the all-run and viable-only membership series decline, but the all-run
series also carries the growing mass of closures. Neither series can stand in for the
other.

### Comparative statics under variance control

Discipline preceded comparison: baseline survival is stable across independent seed
blocks, and common random numbers reduce the paired standard error of membership
comparisons. The reference cross-seed standard deviation is 5.67, while paired standard
errors range from 0.22 to 0.33. Each Tradition is degraded singly from 0.85 to 0.5 against
a reference group of 13.10 members.

| Tradition              | Tier       | Members cost | 95% half-width |  $t$ |
|:-----------------------|:-----------|-------------:|---------------:|-----:|
| T3 mixed adherence     | enabling   |         2.99 |           0.65 |  9.1 |
| T11 mixed adherence    | enabling   |         1.88 |           0.60 |  6.1 |
| T1 unity               | enabling   |         1.65 |           0.65 |  4.9 |
| T12 anonymity          | enabling   |         0.99 |           0.58 |  3.3 |
| T5 one purpose         | enabling   |         0.96 |           0.61 |  3.1 |
| T4 autonomy            | protective |         0.88 |           0.62 |  2.8 |
| T7 self-support        | protective |         0.88 |           0.62 |  2.8 |
| T2 group conscience    | enabling   |         0.48 |           0.62 |  1.5 |
| T6 no endorse­ment      | protective |         0.23 |           0.46 |  1.0 |
| T10 no outside opinion | protective |         0.23 |           0.46 |  1.0 |
| T9 no organiza­tion     | protective |         0.02 |           0.43 |  0.1 |
| T8 non-professional    | enabling   |        -0.20 |           0.51 | -0.8 |

: Single-Tradition degradation, **400 paired replications** under common random numbers.
Seven of twelve have intervals excluding zero. T3 and T11 are mixed adherence
interventions; their paths are split in the release factorials. {#tab:tradition}

> **The replication budget determines the ranking, and 30 is not enough.** Computed at 30
> paired replications, this comparison returns autonomy and self-support at 5.5 members
> each with $t = 2.6$ as the only pair clearing $\lvert t \rvert > 2.5$, which invites the
> inference that the protective Traditions lead the ranking, consistent with their derived
> role as guards on everything else. Under the corrected model, at 400 replications mixed
> Tradition 3 leads at 2.99 members, mixed Tradition 11 follows at 1.88, and seven
> comparisons resolve rather than two. **A common-random-numbers design at 30 replications
> is more efficient than 30 independent runs and is still 30 replications.** Variance
> reduction buys precision per replication; it does not substitute for replications, and
> any ranking reported at that budget is an artifact of it.

### Sensitivity, outcome definitions, and scope

The simulation's parameters were subjected to: global multiplicative jitter at three
amplitudes over 1,002 draws; a tiered design and a randomized-matrix design at 1,000 draws
each; 944 multi-level one-at-a-time perturbations covering all 118 registered values at
four distances in each direction; a twenty-trajectory Morris elementary-effects screen
over all 118; a Sobol decomposition on a 1,024-row base design over the eight Morris
membership leaders; four structural variants that change the model's architecture rather
than its numbers; and a resource-list test. Full specifications are in the book's
technical appendix, sections A3 to A9.

##### Which parameters matter.

The ordering exponent $p$ has the largest single influence of any parameter on every
outcome the multi-level sweep scores. Against a full-adherence baseline of 0.0431
maintenance, moving $p$ alone by 25 per cent in each direction swings maintenance from
0.0027 to 0.2373, a range of 5.45 times baseline; the decay rate $\delta_0$ is second at
3.27 and the step-10 speed third at 2.22. Across the full four-distance ladder the $p$
range is 14.64 times baseline, $\delta_0$ 12.98 and member heterogeneity 4.69. The
twenty-trajectory Morris screen ranks the same two first on membership $\mu^*$, at 52.44
and 51.21, followed by churn at 33.48, dropout sharpness at 24.30, exogenous referral at
23.46, heterogeneity at 18.90 and the step-6 and step-12 speeds at 18.54 and 15.87. Sobol
total-order indices on membership, over those eight leaders at plus or minus 25 per cent,
agree: $p$ at 0.576 \[0.510, 0.643\], $\delta_0$ at 0.373 \[0.320, 0.428\], dropout
sharpness at 0.171, churn at 0.132, heterogeneity at 0.079 and exogenous referral at
0.058, against a noise floor of 0.043 for membership and 0.073 for practice. The two step
speeds, at 0.029 and 0.038, sit at or below that floor and are not separated from Monte
Carlo error.

At the retired 128-row base sample the first-order column failed three internal
diagnostics and was withheld. The 1,024-row release design repairs the membership column
and not the practice column. On membership no factor now has $S_1 > S_T$, and the
first-order indices sum to 0.693, so the column is admissible: $p$ resolves at 0.404
\[0.288, 0.525\] and $\delta_0$ at 0.238 \[0.156, 0.327\], while the remaining six have
intervals covering zero and are unresolved rather than zero. On practice the column is
still not usable: $\delta_0$ returns $S_1 = 0.421$ against $S_T = 0.417$, violating the
identity $S_T \ge S_1$ that holds for any true decomposition, and the practice first-order
indices sum to 1.074, whereas a sum of first-order indices cannot exceed one. No practice
first-order number is quoted elsewhere. The sums of $S_T$ are 1.456 for membership and
1.464 for practice, and the excess over one is the signature of interaction counted once
per factor involved, so interactions are present and are not dominant. The decomposition
is conditional on these eight factors and these ranges; it is not a decomposition of the
model's total variance.

##### Structural variants.

Four changes to the architecture, not the numbers, are compared with the base model: a
flat per-step gate, admission moved to Tradition 3, capacity supplied by all members
rather than the established core, and a piecewise-linear rather than hyperbolic
member-side capacity response. The last variant still clips at one; its historical
filename is shorthand, not a literal absence of saturation. Each of the five architectures
is run at 400 paired seeds for five scenarios. Under pure attraction loss, endpoint
existence is 1.000, 0.870, 1.000, 1.000 and 1.000; endpoint viability is 0.985, 0.658,
0.985, 1.000 and 0.995; and mean membership is 12.38, 6.61, 12.38, 14.73 and 13.04. Under
referral loss the corresponding values are 0.105, 0.120, 0.105, 0.258 and 0.145 for
existence; 0.028, 0.055, 0.028, 0.123 and 0.058 for viability; and 0.51, 0.75, 0.51, 2.00
and 1.02 for membership. Thus the referral-loss ordering holds on all three outcomes in
all five tested architectures. This is a finite structural audit, not a proof over
untested architectures.

> **What the structural audit says, and no more.** In the corrected model, referral loss
> is worse than pure attraction loss on existence, endpoint viability and mean final
> membership in the base architecture and all four variants. The earlier result in which
> the size ordering reversed under three variants came from the retired, uncentred
> capability model and does not reproduce. The parameter screens remain a separate
> question and report strict orderings, ties and reversals at each design level. Specific
> probabilities and memberships remain conditional statements about a constructed model.

##### What the designs could in principle have found.

Two failures are worth naming because both were made in this project. A multiplicative
perturbation cannot move a structural zero, so no multiplicative design is evidence about
the two-tier split (Section 4.4). And a $\pm30$ per cent jitter cannot tell you whether a
result depends on the magnitudes at all, only whether it tolerates small disagreement
about them; the structural randomization is the design that answers the first question,
and it is the one the coupling claims fail.

### Founding composition: an unresolved comparison

Twenty-five founders with a fixed total practice of 13.75 distributed three ways (even:
all at 0.55; concentrated: five at 1.00 and twenty at 0.4375; split: twelve at 0.90 and
thirteen at 0.2269), 400 paired seeds each. Membership ends at 17.80, 18.09 and 17.45 with
half-widths 0.88, 0.99 and 0.93; endpoint viability is 0.985, 0.9875 and 0.985;
established practice is 0.2645, 0.2628 and 0.2660. Relative to even founders, the paired
membership differences are 0.29 \[-0.90, 1.48\] and -0.35 \[-1.47, 0.78\]. No equivalence
margin was prespecified, so the result is unresolved rather than evidence of equality.

The unresolved comparison should be discounted heavily before it is read. Founding
practice changes ordering gates, maintenance, resource capacities, dropout and attraction
jointly. Resources are computed from aggregates and no member's state appears in another
member's growth equation except through those aggregates, so the model has no
representation of mentoring, pairing, cliques or sponsorship. **It also has no
representation of the mechanism that produced the Carrell--Sacerdote--West result**, which
is people choosing whom to associate with inside a group whose composition has been
arranged. That experiment engineered Air Force Academy squadrons from measured peer
effects, predicted a gain of 0.053 grade points for the bottom third, and measured a
treatment effect of $-0.061$ on exactly the students it set out to help, because the
low-ability cadets re-sorted toward each other. A non-significant contrast from a design
without that mechanism is not evidence of practical equality.

The design also cannot separate two things: the conditions differ in the variance of
founding practice *and* in the number above the stricter 0.5 experienced threshold (25, 5
and 12). All 25 exceed the 0.1 established threshold in every condition. A resolved
difference could still have arisen through any of several state-dependent channels.

## The Comparative Case

A formal correspondence gains little from a single historical case and can lose a great
deal by leaning on one. This section is included because the case bears directly on the
paper's central claim, and because the standard account of it, which is what a reader is
most likely to bring, turns out to be false.

### The received account, and what the primary source says

The Washingtonian Total Abstinence Society was founded in Baltimore in April 1840 by six
working men, in a scene whose earliest surviving account is Harrison (1860) and which
reaches most modern readers through Maxwell (1950), spread nationally within four years on
claims reaching into the hundreds of thousands, and was effectively finished within a
decade. In the literature descending from AA it is standardly described as a movement that
died of having no rules, and it is used to illustrate why the Traditions matter. That
literature arrives with its moral pre-attached.

The movement's own manual falsifies the account. Grosh (1842), the *Washingtonian Pocket
Companion*, printed at Utica and by then in a second edition, carries in its first fifteen
pages a definition of principles, directions for organizing and conducting meetings, and a
model constitution. Among its provisions: each society independent and subordinate to
none; funds controlled by its own members; and nothing sectarian or political admitted to
lectures, speeches, singing, or the doings of the society. A footnote records that a
Washingtonian mass convention at Utica passed a declaration of principles and a model
constitution on 22 February 1842, that it was printed in the *Utica Washingtonian* of 25
February and reprinted in October because of demand, and that a copy should be procured
wherever a society is organized. **They had written rules, they had them within two years
of founding, and they had a mechanism for transmitting them.**

What they had, in writing, were analogues of four of the Traditions this analysis
classifies as protective. What they had none of were the seven classified as enabling. And
on anonymity they took the opposite position deliberately and with an argument: Grosh's
directions for a first meeting have joiners rise and call out their names for the
secretary, because "publicity and freedom are preferable to private solicitations,
whisperings, and secresy in giving the names."

The comparison the case actually supports is therefore not rules against no rules. It is
one written code against another, and the provisions missing from the first are the ones
the aggregation condition points at.

### Prominence without anonymity

The touring-speaker structure of §3.6 was built for this case. Washingtonian expansion
from 1841 to 1843 proceeded through touring speakers addressing local societies, which is
exactly a rise in the proportion of total attention carried by a one-directional
cross-society channel. By the consensus-error equation above the speakers' share of influence is fixed by the ratio of
outward to returned attention and does not fall as the movement grows, so the movement
could not have outgrown the exposure.

The exposure was realized. John B. Gough, the movement's most prominent speaker, relapsed
publicly in September 1845; opponents seized on it, and public confidence in the movement
was impaired. His own account, read at source, contains the words "I have fallen," an
acceptance of blame, and a submission to his church's judgment. It is worth reading rather
than inferring from its chapter headings, which suggest a man rebutting a charge rather
than owning a relapse. He had relapsed once before, twenty-nine months earlier, when his
influence weight was small, and that episode was handled internally and quickly. Same man,
same illness, same candor: what differed was the weight.

### Maxwell, and a priority problem stated plainly

Milton Maxwell's 1950 comparison of the two fellowships reaches, without any formal
apparatus, a substantial part of this paper's conclusion. His final section lists AA's
advantages as exclusively alcoholic membership, singleness of purpose, a definite program
of recovery, anonymity, and what he calls hazard-avoiding traditions; he writes that a
comparison with the Washingtonian experience underscores *the sheer survival value* of the
principle of anonymity; and he reaches that conclusion by way of Gough's relapse and what
it cost a movement whose credibility sat in named men. He also identifies the tradition of
keeping authority in principles rather than in offices and personalities, and connects it
to rotating leadership.

**What this paper adds to Maxwell is the theorem, and nothing else.** He had the
observation, the mechanism, and the case. He had no formal condition to which the
observation could be referred, and therefore no way to say why anonymity should have
survival value rather than merely that it did. Whether the vanishing-influence condition
is what Maxwell was pointing at is a separate question, and this paper does not settle it.

### What the case cannot do

It is one case, selected because it is the obvious comparison, and the direction of
selection is unfavorable: the Washingtonians are famous among people interested in AA
precisely because the contrast is instructive. Nothing here establishes that the missing
enabling provisions caused the decline; the movement was also absorbed by a temperance
politics it had defined itself against, and the manual's anti-politics article had nothing
to bite on once the movement's identity was itself a political position. How widely the
Utica model constitution was actually adopted is not recorded in the manual and we have
found no source that settles it. The historical material is offered as an existence proof
that the distinction between the two tiers of rule is visible in a real code, not as
evidence about the consequences of omitting one tier.

## Limitations

### The largest one, stated first

**The mapping in Table [1](#tab:mapping){reference-type="ref" reference="tab:mapping"} is
an interpretation of the Traditions' wording, arrived at by the author, and no computation
in this paper touches it.** Everything the paper claims about AA specifically, as opposed
to about stochastic matrices, passes through it. A reader who holds that Tradition 2
concerns humility rather than weighting, or that anonymity is chiefly protective of
individuals, can accept every number here and reject the paper's thesis. This is not a
caveat on a result; it is the status of the result.

What would settle it is elicitation: give the Traditions' published short text to readers
who do not know the hypothesis, ask them to say what each rule constrains, and measure
agreement with the mapping. That has not been done. A single reader who knows the rooms
did read a draft and identified a substantive error, the membership-versus-attendance
conflation of §6.1, and no other intervention in the project changed as much for as few
words. The implication for the parts nobody has checked is uncomfortable and is the reason
this limitation is listed first.

### The remaining limitations

1.  **No parameter is estimated.** Section 3's computations demonstrate a theorem on
    constructed matrices; Section 6's are simulations from 118 assumed values, none
    fitted, because the longitudinal data such a model would need has never been
    collected. The paper's empirical content is its predictions, not its numbers. A model
    of this kind can show that a set of ideas is consistent and that a mechanism is
    available. It cannot show that anything is true.

2.  **The $S$ and $G$ matrices are hand-written judgments**, and all of Section 4 plus the
    resource structure of Section 6 inherits from them. Their tolerance of $\pm30$ per
    cent perturbation is necessary and not sufficient support, and the structural
    randomization they fail (§4.5) is the design that speaks to the question. The correct
    remedy is a second governance matrix elicited independently from another reader,
    scored by Cohen's kappa against the first. A blank elicitation form exists; no second
    reader has completed it. Until one does, Section 4 rests on one person's judgment.

3.  **Member heterogeneity was tuned to produce a desired behavior.** Its standard
    deviation was selected in an attempt to convert individual cliffs into a graded group
    response. After mean-centring and re-estimating the state-dependent environment, the
    corrected audit finds typical-member bistability in only 1.75 per cent of 400 endpoint
    environments. The intended mechanism is therefore not established by the released
    baseline, and Section 6's quantities inherit from the authored spread.

4.  **Specification search.** Several architectural choices (the retention channel for
    Tradition 3, core-based carrying capacity, the placement of the capacity gate) were
    refined against simulation behavior as well as substantive reasoning. This risks
    tailoring an architecture to expected behavior and no assurance can be given that it
    has not happened. The four structural variants of §6.6 are a partial and inadequate
    answer.

5.  **Thirty-five parameters cannot affect a fully adherent group at all**, because the
    governance matrix cancels exactly at full adherence. Any sensitivity result quoted
    over the full 118 must be read with that in mind, and a design that perturbs those 35
    and reports no effect has found nothing.

6.  **Conditional figures read as unconditional.** Quality in
    Table [8](#tab:decline){reference-type="ref" reference="tab:decline"} is computed
    among members of surviving groups. Read without the surviving fraction beside it,
    "quality is maintained" would describe a population that has partly ceased to exist.
    Table [9](#tab:conditional){reference-type="ref" reference="tab:conditional"} exists
    to make the difference visible.

7.  **DeGroot averaging is a strong simplification of a group conscience.** Real members
    argue, defer selectively, abstain, update out of order, and sometimes harden rather
    than converge. Golub and Jackson's result is about naive averaging specifically.
    Whether real deliberating groups behave like DeGroot updaters has not been tested here
    or, so far as we have found, anywhere.

8.  **Endogeneity of the group input** blocks estimation of Section 5's technology and is
    unsolved here.

9.  **The sign of $\rho$ has never been measured.** The contribution is to make the
    question answerable, not to answer it.

10. **No representation of who attends to whom.** In Section 6's model no member's state
    enters another member's growth equation except through group aggregates, so there is
    no sponsorship, no pairing, no clique, and no re-sorting. The mechanism that produced
    the Carrell--Sacerdote--West result is absent by construction (§6.7). Building it is a
    different model, not a different run, and it is the largest single piece of technical
    work outstanding.

11. **Durations were never calibrated.** The horizon, the arrival rate and the churn floor
    are three of the 118 registered numeric values. Endpoint orderings have
    outcome-specific sensitivity records, and the 10-, 20-, 30-, 50- and 100-year checks
    continue to move. The trajectories are shapes inside the model, not forecasts of how
    long a real group lasts or evidence of steady state.

12. **Combinations were not tested.** Each decline condition switches one thing off at
    full adherence elsewhere. Real decline is unlikely to be so tidy and there is no
    reason to expect the costs to add.

13. **A correspondence is not a cause.** That the Traditions implement a known aggregation
    criterion does not establish that this is why they were written, or why AA has
    endured.

14. **The decay rate is uncalibrated and consequential.** $\delta_0$ is second only to $p$
    in every sensitivity design. The two estimates read for anything comparable measure
    skills, not practices: Dinerstein, Megalokonomou, and Yannelis (2022) put the
    depreciation of teaching skill at 4.3 per cent a year for early-career teachers, and
    Cohen, Johnston, and Lindner (2023) find no measurable decline in cognitive skills
    over up to three years of unemployment. Read as skill, $\delta_0 = 0.06$ per week is
    one to two orders of magnitude too fast; read as practice it is untested. In the
    one-at-a-time screen, downward moves of $\delta_0$ of 25 per cent or more reverse the
    ordering of referral loss against pure attraction loss on final membership, so that
    ordering is conditional on practice lapsing at roughly the assumed rate.

15. **Sources not read.** Alexander (1988) on the class and domestic dimensions of the
    Washingtonian movement; Blumberg (1980, 1991) on its political entanglement; the full
    text of Pagano et al. (2004), which is cited at a remove; White's *Slaying the
    Dragon*. Maxwell (1950) was read in full, but the copy available to us is a retyped
    web reproduction with visible transcription errors, not a scan of the journal, so
    every Maxwell citation here has been checked against a transcription rather than
    against the journal. *Twelve Steps and Twelve Traditions* (1953) was read in full on
    10 August 2026 and is held as a record with no document; the rest of AA's own
    literature has not been obtained.

## Falsifiable Predictions

Where the analysis reported above bears on a prediction, or narrows what it should say,
this is marked.

1.  **Decision quality improves with group size under flat influence and plateaus under
    concentrated influence.** Testable with forecast or vignette tasks administered to
    group consciences of varying structure. Unchanged, and untested.

2.  **Rotation breadth, not rotation per se, predicts group durability.** Testable from
    service rosters. *Narrowed by the analysis above:* the operational threshold is
    roughly a quarter of the membership in the rotation pool, computed as twenty-six per
    cent across sizes from 50 to 800 (§3.5). The effect of falling short is a real but
    moderate permanent cost, not a near-clique regime, and a test should be powered
    accordingly.

3.  **Groups losing exogenous newcomer inflow decline demographically while established
    practice among selected viable remnants can remain high.** Unlisted meetings,
    schedule-disadvantaged meetings, and meetings distant from referral sources provide
    natural variation. *Narrowed by the corrected trajectories:* viable-room membership
    also falls sharply, so the interior is not warning-free. The testable divergence is
    between losses in groups and members and the smaller change in practice among those
    who remain; it must be measured on all three series.

4.  **The two supply channels dissociate**: attraction loss produces stable remnants,
    referral loss produces delayed dissolution, so proximity to treatment facilities
    should predict survival through low-attraction periods. *Partly answered, and
    qualified.* Earlier drafts described this as one of exactly two universal simulation
    results. The corrected analysis reports strict support, ties, reversals, and
    unresolved screens separately; it does not promote a finite sensitivity suite into a
    universal claim. Mortality and membership remain distinct estimands.

5.  **Tradition 3 has distinct resource-governance and inverse-practice friction paths.**
    *Bearing of the analysis above:* at 400 paired seeds, combined loss ends at 6.76
    members against 17.80, closes 25.0 per cent of groups, and leaves 54.8 per cent
    endpoint-viable against 98.5 per cent at baseline. Friction loss alone costs 2.96
    members \[1.85, 4.08\]; governance loss alone costs 6.03 \[5.04, 7.01\]. The earlier
    predominantly-size interpretation does not survive the corrected model.

6.  **If step order does not predict step completion** ($\rho > 0$ throughout), the chain
    interpretation of the CES reformulation fails. The proxy-averaging exercise in §5.1
    neither identifies latent practice nor establishes a required number of instruments.

7.  **the two-tier division should be visible to readers who do not know the hypothesis.**
    Give the published short text of the Traditions to independent readers and ask which
    of them supply anything a member uses directly and which only protect other rules. The
    present split is author-coded, not a tier discovered by the model. If independent
    readers do not reproduce it, the resource layer is encoding the author's prior rather
    than the text's content.

8.  **the mapping itself is testable by elicitation.** See §8.1. This is the prediction
    whose failure would cost the paper the most.

## Conclusion

This paper's durable contribution is a correspondence: three of AA's Twelve Traditions, on
a reading of their wording that the paper states plainly and does not verify, jointly
implement the vanishing-influence condition under which naive collective deliberation
aggregates information, a criterion formalized by Golub and Jackson in 2010 and reached by
a fellowship of laypeople, from eleven years of watching groups fail, in 1946. The
correspondence yields two corollaries with immediate empirical content, that rotation must
scale with the group and that obstruction is a matter of scaling rather than severity, and
it reframes anonymity from an ethic of humility to a structural precondition of
trustworthy group decision-making.

Around that center, the paper contributes a method: deriving institutional couplings
through an explicit resource layer rather than asserting them, which rejects the natural
index-pairing conjecture on all twelve of its instances while recovering, unbidden, the
functional division of the Traditions and the primacy of unity. It also contributes an
accounting of what that method cannot support. Five of the twelve rejections are
structurally forced and invisible to the perturbation design that was originally quoted
for them; a threshold test that can see them finds them failing by comparable margins; and
the central coupling claim survives structural randomization less often than it fails.
Those facts are reported here because a derivation whose robustness is asserted rather
than measured is worth less than one whose limits are known.

The membership model's principal prediction, that referral-starved groups decline
demographically while looking healthy from inside, is specific, mechanistically grounded,
distinguishable from rival accounts, and testable with records AA's service structure
already keeps. In the corrected five-architecture comparison, referral loss is worse than
pure attraction loss on existence, endpoint viability and mean final membership. The
expanded parameter screens bound that result over their stated ranges; they are not a
proof outside them.

Where this line of work should go next is not further modeling. It is measurement: of the
mapping, by elicitation from readers who do not know the hypothesis; of the governance
matrix, by a second independent elicitation; of rotation breadth against group longevity;
of step ordering against step completion; and of the quiet demographic signature of groups
that seekers have stopped finding.

## References {#references .unnumbered}

*Status note.* An entry explicitly marked read at source, read in full, abstract only,
cited at a remove, or not read has that current-project status. For entries without an
explicit status, the repository does not document whether the full work was read; they are
background citations and do not upgrade a load-bearing claim. The complete current status
register is `research/SOURCES.md`. The separately supplied corpus was worked through on 9
August 2026; what remains under `research/staged/` is two journal articles that are
recorded as verified online, are unread because retrieval returned an access challenge,
and are not evidence for this paper. No source document is committed to the repository:
each source is published as a citation, a rights position, a provenance URL, a SHA-256 and
a vocabulary-only verification index.

::: list
Alexander, R. M. (1988). "'We Are Engaged as a Band of Sisters': Class and Domesticity in
the Washingtonian Temperance Movement, 1840-1850." *Journal of American History* 75(3):
763-785. **Not read**; cited for the women's dimension of the movement, which this paper
does not develop.

Angrist, J. D. (2014). "The perils of peer effects." *Labour Economics* 30: 98-108. **Read
in full** in its working-paper version.

Banks, H. T., K. L. Rehm, K. L. Sutton, C. Davis, L. Hail, A. Kuerbis, and J. Morgenstern
(2014). "Dynamic modeling of behavior change." *Quarterly of Applied Mathematics* 72:
209-251.

Banks, H. T., K. Bekele-Maxwell, R. A. Everett, L. Stephenson, S. Shao, and J. Morgenstern
(2017). "Dynamic modeling of problem drinkers undergoing behavioral treatment." *Bulletin
of Mathematical Biology* 79: 1254-1273.

Ben-Porath, Y. (1967). "The production of human capital and the life cycle of earnings."
*Journal of Political Economy* 75(4): 352-365.

Blair, H. W. (1888). *The Temperance Movement: or, The Conflict Between Man and Alcohol.*
Boston: William E. Smythe. **Read at source**; public domain.

Blumberg, L. U. (1980). "The Significance of the Alcohol Prohibitionists for the
Washingtonian Temperance Societies." *Journal of Studies on Alcohol* 41(1): 37-77. **Not
read.**

Blumberg, L. U., and W. L. Pittman (1991). *Beware the First Drink! The Washingtonian
Temperance Movement and Alcoholics Anonymous.* Seattle: Glenn Abbey Books. **Not read**;
cited as an outstanding book-length comparison, not as evidence for a specific result.

Carrell, S. E., B. I. Sacerdote, and J. E. West (2013). "From Natural Variation to Optimal
Policy? The Importance of Endogenous Peer Group Formation." *Econometrica* 81(3): 855-882.
doi:10.3982/ECTA10168. **Read at source** from the lead author's university copy. Earlier
circulated as NBER Working Paper 16865 and, before that, as *Beware of Economists Bearing
Reduced Forms?*. In copyright; full text not redistributed.

Cohen, J. P., A. C. Johnston, and A. S. Lindner (2023). "Skill depreciation during
unemployment: Evidence from panel data." NBER Working Paper 31120. **Read in full** apart
from its appendices.

Crothers, T. D. (1911). *Inebriety: A Clinical Treatise.* Cincinnati: Harvey Publishing.
**Read at source**; public domain.

Cunha, F., and J. J. Heckman (2007). "The technology of skill formation." *American
Economic Review* 97(2): 31-47. **Read in full** in its working-paper version.

Cunha, F., J. J. Heckman, and S. M. Schennach (2010). "Estimating the technology of
cognitive and noncognitive skill formation." *Econometrica* 78(3): 883-931. **Read in
full** in its working-paper version.

DeGroot, M. H. (1974). "Reaching a consensus." *Journal of the American Statistical
Association* 69(345): 118-121. **Read at source**; the updating model.

Dinerstein, M., R. Megalokonomou, and C. Yannelis (2022). "Human capital depreciation and
returns to experience." NBER Working Paper 27925. **Read in full** apart from its online
appendix.

Eddy, R. (1887). *Alcohol in History.* New York: National Temperance Society. **Read at
source**; public domain.

Fehlandt, A. F. (1904). *A Century of Drink Reform in the United States.* Cincinnati:
Jennings and Graham. **Read at source**; public domain.

Fatimah, H., M. D. Hunter, and M. A. Bornovalova (2025). "Modeling the Dynamics of
Addiction Relapse Via the Double-Well Potential System." *Journal of Psychopathology and
Clinical Science* 134(1): 69-80. doi:10.1037/abn0000960. **Read in full** from the author
manuscript; the strongest empirical warrant used here for a two-well relapse landscape,
with the limitations stated in Section 5.

Galanter, M. (1981). "The 'relief effect': A sociobiological model for neurotic distress
and large-group therapy." *American Journal of Psychiatry* 138(5): 588-591.

Golub, B., and M. O. Jackson (2010). "Naïve Learning in Social Networks and the Wisdom of
Crowds." *American Economic Journal: Microeconomics* 2(1): 112-149. **Read at source.**
The wisdom criterion, the three obstructions, and the convergence conditions. Every formal
claim in Section 3 originates here.

Gorman, D. M., J. Mezic, I. Mezic, and P. J. Gruenewald (2006). "Agent-based modeling of
drinking behavior." *American Journal of Public Health* 96(11): 2055-2060.

Gough, J. B. (1869). *Autobiography and Personal Recollections of John B. Gough.*
Springfield, Mass.: Bill, Nichols & Co. **Read at source**; public domain. The September
1845 episode in his own words.

Grosh, A. B., comp. (1842). *Washingtonian Pocket Companion.* Second edition. Utica, N.Y.:
B. S. Merrell. **Read at source**; Harvard copy digitized by Google, via HathiTrust,
<https://hdl.handle.net/2027/hvd.32044004487591>. Public domain. The definition of
principles, the model constitution's articles, the Utica mass convention of 22 February
1842, and the directions for taking names publicly.

Harrison, D., Jr. (1860). *A Voice from the Washingtonian Home.* Boston. **Read at
source**; public domain. The earliest account of the founding scene.

Hawkins, W. G., ed. (1862). *Life of John H. W. Hawkins.* Boston: Briggs and Richards,
sixth thousand. **Read at source**; public domain. Note the edition: this is not the
Jewett printing usually cited.

Holmström, B. (1982). "Moral hazard in teams." *Bell Journal of Economics* 13(2): 324-340.

Hu, Y., and S. M. Schennach (2008). "Instrumental variable treatment of nonclassical
measurement error models." *Econometrica* 76(1): 195-216. **Read in part**; used here at a
remove, through Cunha, Heckman, and Schennach.

Hufford, M. R., K. Witkiewitz, A. L. Shields, S. Kodya, and J. C. Caruso (2003). "Relapse
as a nonlinear dynamic system." *Journal of Abnormal Psychology* 112(2): 219-227.

Humphreys, K., L. A. Kaskutas, and C. Weisner (1998). "The Alcoholics Anonymous
Affiliation Scale." *Alcoholism: Clinical and Experimental Research* 22(5): 974-978.

Iannaccone, L. R. (1992). "Sacrifice and stigma: Reducing free-riding in cults, communes,
and other collectives." *Journal of Political Economy* 100(2): 271-291.

Kaskutas, L. A., J. Bond, and K. Humphreys (2002). "Social networks as mediators of the
effect of Alcoholics Anonymous." *Addiction* 97(7): 891-900.

Kelly, J. F., K. Humphreys, and M. Ferri (2020). "Alcoholics Anonymous and other 12-step
programs for alcohol use disorder." *Cochrane Database of Systematic Reviews*, CD012880.

Krout, J. A. (1925). *The Origins of Prohibition.* New York: Alfred A. Knopf. **Read at
source**; public domain. Independent corroboration of the founding, the officers, the fee
and the dues.

Kurtz, E. (1991). *Not-God: A History of Alcoholics Anonymous.* Expanded edition. Center
City, Minn.: Hazelden. **Consulted at source**; in copyright, full text not stored. The
Traditions' drafting history. A vocabulary-only verification index is retained at
`research/incorporated/Kurtz_1991/` in place of the text.

Lembke, A. (n.d.). "Sacrifice, stigma, and free-riding in Alcoholics Anonymous."
Association for the Study of Religion, Economics and Culture. **Read in full.**

Marsh, J. (1866). *Temperance Recollections.* New York: Charles Scribner. **Read at
source**; public domain.

Alcoholics Anonymous World Services (1953). *Twelve Steps and Twelve Traditions.* New
York: AAWS. **Read in full** 10 August 2026, from the per-chapter files AAWS publishes
free at aa.org. Source for the elder-statesman structure of
Section [3.6](#sec:elders){reference-type="ref" reference="sec:elders"} (Tradition 2,
printed pp. 132-138), the statement that rotating leadership is best and the warning
against entrenched power (Tradition 9, pp. 174-178), the two functions of anonymity
(Tradition 12, pp. 187-191), and the unity/singleness-of-purpose distinction (Traditions 1
and 5, pp. 129-131 and 151-155). Also the cross-reference count reported in
Section [4.1](#sec:conjecture){reference-type="ref" reference="sec:conjecture"}. **In
copyright; no copy is held in the project repository.**

Kurtz, E. (c. 1984). "A Talk About the History of Alcoholics Anonymous From the Letters of
Bill Wilson." Undated recorded talk; transcript restored by historyofrecovery.com. **Read
in full** 10 August 2026. The year is inferred from internal evidence and is given as
approximate throughout. Distinct from Kurtz (1979/1991). Wilson's letters are quoted
within it from memory and without page citations, so anything attributed to Wilson through
this source is at a remove. **No copy is held.**

Maxwell, M. A. (1950). "The Washingtonian Movement." *Quarterly Journal of Studies on
Alcohol* 11: 410-452. **Read in full**, with a caution: the available copy is a retyped
web reproduction carrying visible transcription errors, not a scan of the journal. Every
citation to Maxwell in this paper has been checked against that transcription rather than
against the journal.

Ostrom, E. (1990). *Governing the Commons: The Evolution of Institutions for Collective
Action.* Cambridge: Cambridge University Press.

Pagano, M. E., K. B. Friend, J. S. Tonigan, and R. L. Stout (2004). "Helping other
alcoholics in Alcoholics Anonymous and drinking outcomes." *Journal of Studies on Alcohol*
65(6): 766-773. **Read in full**; NIH author manuscript, PMCID PMC3008319, obtained 10
August 2026. Source for the 40 against 22 per cent abstinence contrast, its independence
from meeting attendance, and the authors' 8 per cent helping-rate limitation.

Rohr, R. (2011). *Breathing Under Water: Spirituality and the Twelve Steps.* Cincinnati:
Franciscan Media. **Read in full** 10 August 2026. Cited only for its reading of anonymity
as confidentiality and for containing no discussion of the Traditions. The copy consulted
was an unauthorised posting; the bibliographic record was confirmed independently of it,
no copy is held, and nothing is quoted at length. See `research/incorporated/Rohr_2011/`
for the rights position in full.

Riessman, F. (1965). "The 'helper' therapy principle." *Social Work* 10(2): 27-32.

Rynes, K. N., and J. S. Tonigan (2012). "Do social networks explain 12-step sponsorship
effects?" *Psychology of Addictive Behaviors* 26(3): 432-439.

Sánchez, F., X. Wang, C. Castillo-Chávez, D. M. Gorman, and P. J. Gruenewald (2007).
"Drinking as an epidemic." In K. Witkiewitz and G. A. Marlatt (eds.), *Therapist's Guide
to Evidence-Based Relapse Prevention*, 353-368.

Schennach, S. M. (2004). "Estimation of nonlinear models with measurement error."
*Econometrica* 72(1): 33-75.

Sharma, S., and G. P. Samanta (2015). "Analysis of a drinking epidemic model."
*International Journal of Dynamics and Control* 3: 288-305.

Tonigan, J. S., G. J. Connors, and W. R. Miller (1996). "The Alcoholics Anonymous
Involvement (AAI) scale." *Psychology of Addictive Behaviors* 10: 75-80.

Greenfield, B. L., and J. S. Tonigan (2013). "The General Alcoholics Anonymous Tools of
Recovery: The Adoption of 12-Step Practices and Beliefs." *Psychology of Addictive
Behaviors* 27(3): 553-561. **Read in full**; NIH author manuscript, PMCID PMC3707937,
obtained 10 August 2026. Source for the two-factor structure of step-work and the
disagreement between instruments on nine of twelve steps.

Witkiewitz, K., and G. A. Marlatt (2004). "Relapse prevention for alcohol and drug
problems." *American Psychologist* 59(4): 224-235.

Witkiewitz, K., and G. A. Marlatt (2007). "Modeling the complexity of post-treatment
drinking." *Clinical Psychology Review* 27(6): 724-738.
:::

**Referenced but not reproduced.** The Twelve Steps and Twelve Traditions of Alcoholics
Anonymous, paraphrased throughout. The text is copyright Alcoholics Anonymous World
Services, Inc. and is not reproduced here. *Twelve Steps and Twelve Traditions* (1953) was
read in full on 10 August 2026 from the files AAWS publishes free at aa.org; no copy is
held, and it is paraphrased rather than quoted at length. AA's other publications
(*Alcoholics Anonymous Comes of Age*, *Pass It On*, the *Grapevine* essays of 1946, and
service pamphlets) have not been obtained.

**What was not read.** Any work testing whether real deliberating groups behave like
DeGroot updaters. Any literature on peer-group composition in voluntary mutual-aid
settings specifically. Alexander (1988), Blumberg (1980, 1991), Pagano et al. (2004) in
full, and White's *Slaying the Dragon*. Jellinek's per-capita consumption estimates, which
are quoted through Maxwell and whose original has not been traced. The literature on how
fast practices and habits lapse, as distinct from skills.

## The Whole Paper in Plain Language

*This appendix says everything the paper says, without the math. It is written for a
reader with no background in economics or statistics. Where a natural way of putting
something would be wrong, this appendix says so.*

### What this paper is about

AA runs on two sets of twelve ideas. The Twelve Steps are for the person. The Twelve
Traditions are for the group. This paper turns both into math and checks whether the
pieces fit together, and along the way it finds that some things everybody assumes about
them are wrong, and some things nobody says about them are true.

### The big finding: why "nobody's in charge" actually works

Think about how an AA group makes a decision. There is no boss. People talk it over until
the room agrees. That is called the group conscience.

Now here is a question: when can you trust a decision made that way? In 2010, two
economists proved the answer. A group that decides by talking it out can be trusted only
if no single person's opinion carries a big fixed chunk of the final answer. Here is why.
Everyone's opinion is partly right and partly mistaken. When lots of opinions get blended
evenly, the mistakes point in different directions and cancel out, and the more people the
better. But if one person's opinion always makes up a third of the result, their mistakes
never cancel. Adding more people does not help. The group just gets more and more sure of
an answer that is no more likely to be right.

Now look at three of the Traditions. Leaders serve the group; they do not run it. There is
no ladder to climb, because service jobs rotate. And everyone is anonymous: no last names,
no job titles, no status. Each of those rules does the same thing from a different angle:
it stops any one person's voice from getting too heavy. This paper proposes that those
mechanisms can reduce stationary influence concentration, which is the condition in the
2010 proof. The wording alone does not establish that they do.

> *The rules written in 1946 are consistent with a condition mathematicians would
> formalize 64 years later. That is a present-day mapping, not evidence that AA's drafters
> discovered, intended, or implemented the theorem.*

**One honest warning about that paragraph, and it is the most important sentence in this
appendix.** The proof is real and we have read it. But the step from "Tradition 2 says
leaders do not govern" to "therefore nobody's opinion carries extra weight in the math" is
our reading of a sentence. Nobody has checked it. None of the computer work in this paper
tests it. Somebody could reasonably say those Traditions are about humility, not about
arithmetic, and this paper has no answer for them yet. Everything else here is downstream
of that one unverified step.

### What it looks like when the rule breaks

Two familiar characters break it. The first is the old-timer whose opinion ends every
discussion, not because there is a vote, but because everyone waits to hear what they
think. The second is the little circle of long-timers who have already talked it over
before the meeting starts.

Here is the alarming part from the math: when this happens, nothing looks wrong. The group
still reaches agreement. The meetings feel fine. There is no argument and no drama. The
group is simply wrong more often, it is wrong confidently, and getting bigger does not fix
it. A broken group conscience feels exactly like a working one from the inside.

There is a third case, worse than both, that we did not expect. If a small group of people
not only receives most of the attention but gives all of *their* attention only to each
other, then in the long run the rest of the room counts for literally nothing. The group's
judgment becomes exactly the judgment of that handful, no matter how many other people are
in the chairs.

And it does not take a monster to cause the problem. One person holding five per cent of
the room's attention, which is not very much, already nearly doubles how wrong a large
group ends up.

### Something the Traditions forgot to mention

The Traditions say to rotate service jobs so nobody becomes a boss. The math agrees, and
adds a catch nobody wrote down. Rotating only works if lots of different people take
turns. Picture a group of 400 where the same twelve people trade the jobs among themselves
forever. Rotation like that leaves a permanent floor under how much attention the rotating
dozen hold, and the floor does not go down as the group grows. To really work, roughly a
quarter of the group needs to be in the rotation. Any group could check this against its
own service list.

**One thing not to overstate.** It would be easy to say that a group of 400 rotating
twelve people behaves almost the same as a group run by a clique. That is too strong. It
sits in between, and it is closer to the healthy case than to the clique. The honest
description is a real but moderate permanent cost.

**And a bigger lesson underneath it.** The obvious question to ask about a prominent
member is "how prominent?" That is the wrong question. It is "does the prominence grow
when the group grows?" A clique that keeps to itself in a room of ten but gets diluted as
the room fills is not a problem at all in the long run. A single person who stays equally
prominent no matter how big the room gets is a problem forever. Severity is not the test.
Scaling is the test.

### The steps don't match the traditions by number

It is tempting to think Step 1 goes with Tradition 1, Step 2 with Tradition 2, and so on
down the line. It sounds neat. But it does not hold up, and it was never AA teaching. The
Traditions were written about ten years after the Steps, to fix real problems groups were
having.

Instead of matching them by number, we asked a different question for each step: what does
a person actually need from the group to do this step? Then the matching takes care of
itself. Step 5 is telling another human being the worst things you have ever done. What do
you need for that? You need to know it will not leave the room. That is anonymity,
Tradition 12, not Tradition 5. Step 12 is carrying the message to the alcoholic who still
suffers. Tradition 5 says the group's one job is to carry its message to the alcoholic who
still suffers. Same sentence, basically. Those two go together.

And when we code this for all twelve steps, two things follow from those authored choices.
First, five of the Traditions (autonomy, no endorsements, paying your own way, no
hierarchy, no outside opinions) turn out to give members nothing directly. Their whole job
is to protect the other seven from being eroded. Those five empty rows were put into the
table by the author; multiplication did not discover them independently. Second, unity has
the largest semantic overlap under the same coding. That is a concise description of the
table, not a fact about AA groups established by data.

**Now the part that argues against the finding.** We tested how much of this survives if
you disagree with the numbers we made up.

Unity's importance holds up well. Even if you throw away every number we chose and keep
only the pattern of which rule touches which need, unity still comes out on top about
three times in four.

The rest does not hold up nearly as well. Do the same thing to the
"steps-don't-match-traditions" finding and it only survives about four times in ten, which
is less often than it fails. Worse, five of our twelve pieces of evidence for it were not
really evidence at all: those five Traditions had zeros in our table by construction, so
of course they never matched. We built a different test that could actually see those
five, and they still fail, by about the same margins as the other seven. So we think the
finding is right. But it rests on our judgment about the numbers, not on a proof, and
anyone who thinks we chose the numbers badly is entitled to reject it. That is worth
saying plainly rather than dressing it up.

### Can you skip a step? Nobody has ever checked

Everyone in AA says you cannot skip a step, that you cannot make honest amends (Step 9)
for harms you never wrote down (Step 4). It sounds obviously true. But as far as we could
find, no researcher has ever actually tested whether people work the steps in order, or
whether doing an early step really is what makes a later one possible.

This paper turns that belief into one measurable number. If the number comes out one way,
the steps are truly a chain: skip a link and everything after it fails. If it comes out
the other way, they are more like a menu, and a strong group can carry someone past a step
they missed. The number might be measured with a purpose-built longitudinal design. Our
limited exercise adds noise only to an output while supplying the inputs and loadings
without error; it shows that averaging more output proxies can improve resolution. It does
not establish how many instruments a valid latent-variable design needs.

### What can actually go wrong for a group

Start with a fact about AA that shapes everything here: the only requirement for
*membership* is a desire to stop drinking, and no group can take that away from anybody.

**One thing that is easy to get wrong here.** It is tempting to put this as "a group
cannot close its doors," and that is not right. Closed meetings are ordinary and
long-standing, and a closed meeting is about who is in the room, not about who is a
member. Nobody can be thrown out of AA. Somebody can absolutely be in a room where they
are not welcome. In the executable model Tradition 3 affects both resource governance and
inverse-practice-weighted dropout friction; it does not record tenure and therefore cannot
identify literal newcomer retention. The two paths are now tested separately.

So if a group cannot revoke anyone's membership, what can actually go wrong? Three
different things, and they leave three different marks:

1.  **The group becomes invisible.** Nobody finds it anymore: it is not listed, it meets
    at a bad time, word of mouth dried up. The model says this group shrinks to a small
    huddle kept alive by court cards and treatment-center referrals. It does not die. It
    just gets small, and the people in it are somewhat worse off than they would be in a
    healthy group.

2.  **The referrals dry up.** The treatment center closed; the court program ended. The
    group coasts on word of mouth for about ten years, and then, in roughly two runs out
    of three, it quietly dissolves.

3.  **The group gets unwelcoming.** Nobody loses their membership, but there is an
    in-crowd, and newcomers can feel it. They come once and do not come back. This group
    shrinks by about a third and mostly survives. It is smaller than it should be.

**How much you can trust that number depends entirely on how many times the simulation was
run.** From ten runs, that middle case looks like four groups in five dissolving. From
four hundred, it is closer to two in three, and a healthy group settles at about 42
members rather than 45. Ten runs is far too few. A number produced by a random simulation
and quoted to three digits from ten runs is not a result at all, and it is very easy to
print one without noticing.

And here is the strangest thing the model says. In the case that actually kills groups,
the people still in it are doing fine. Their recovery holds up right to the end, and if
anything looks slightly *better* than average, because the ones who were struggling have
already gone. From the inside, that dying group looks like a healthy group. Nobody in the
room feels anything going wrong. If that is true in the real world, and it is checkable,
it means a group cannot rely on how the meetings feel to know whether it is in trouble. It
has to look at the numbers: how many newcomers came this year, and how many came back.

**One qualification, because the loose version of this is wrong.** Quality does not hold
up in all three cases. In the invisible case it drops noticeably. The sharp version of the
claim is narrower and more useful: *the failure that kills groups is the one with no
warning signal inside the room*.

### Does it matter who starts a group?

We tested three founding-state distributions with the same mean initial practice. Their
paired final-membership differences are imprecise and no equivalence margin was specified.
The correct result is unresolved, not that all three are the same.

You should not believe that result very much, and the reason is a famous experiment.
Researchers at the Air Force Academy measured how much cadets help each other study, then
used those measurements to build squadrons designed to help the weakest students. Their
own model predicted a gain. What actually happened was a loss of about the same size, on
exactly the students they had tried to help. The reason was that once you put fifteen
strong students and fifteen weak ones in a room with nobody in between, the weak ones
stopped mixing with the strong ones and found each other instead. The measurement was
real; building a room out of it destroyed the thing that had been measured.

Our model has no way for people to choose who they spend time with, so it could not
reproduce the Air Force mechanism. That study is a warning about transport and endogenous
mixing, not a measurement of the upside or downside of arranging an AA group. No causal
claim about AA composition follows from this comparison.

### The movement that came before, and what it actually did

AA was not the first fellowship of drunks helping each other stay sober. In 1840, six men
in a Baltimore tavern founded the Washingtonians. It spread across the country in four
years and was essentially finished in ten.

The story usually told, especially in AA circles, is that they died of having no rules.
**We checked, and that story is false.** Their own handbook from 1842 turned up, and it
contains written rules: each society independent and answering to nobody above it, funds
controlled by its own members, and nothing political or religious allowed into the
meetings. They passed a model constitution at a convention in February 1842, printed it in
a newspaper, reprinted it because of demand, and told every new society to get a copy.

What they did not have was any of the rules on the other side of the ledger, the ones that
give a member something. And on anonymity they took the opposite view on purpose, with a
reason: their handbook tells new joiners to stand up and call out their names, because
publicity is better than "whisperings and secresy."

So the real comparison is not rules against no rules. It is one written code against
another, and the ones missing from the first are exactly the ones the math points at. That
is a better comparison than the one we started with, and it is better because it is true.

Their most famous speaker relapsed in public in 1845, opponents made the most of it, and
the movement's credibility suffered. He had relapsed once before, quietly, two and a half
years earlier, and the institutional response was much smaller. The same-person contrast
is suggestive, but it does not identify influence weight as the sole cause and the first
episode was not literally costless.

### How much of this should you believe?

Here is the honest answer, and it is less flattering than the summary above may have
sounded.

The mathematical theorem in A.2 is real and settled. The claim that AA's three rules are
the same thing as the theorem's condition is *our reading of three sentences*, and nobody
has checked it. That is the whole hinge of the paper and it is the part with the least
support.

The finding about rotation follows from the theorem and is solid math.

The step-and-tradition results come from two tables of numbers we made up, and they do not
survive if you throw those numbers away. We say so in the paper rather than quoting a
robustness figure that belongs to a different claim.

Everything from the computer model has never been checked against real people or real
groups. Every number in it was chosen by us, not measured. The sensitivity exercises are
screens over specified ranges, not proofs that claims rest on no number. Their strict,
tied, and reversed outcomes must be reported separately, and the earlier referral
comparison used a mixed Tradition 11 intervention. The corrected headline compares
referral loss with the pure attraction path, while structural size and endpoint-viability
orderings are reported separately.

A model like that can show that ideas fit together. It cannot show they are true.

Treat the group-decision math as settled mathematics, treat its application to AA as an
unverified reading, and treat everything else as sharp questions waiting for someone to
check them. Be suspicious of any idea, ours included, that feels certain before it has
been tested. The claims here that felt most obvious at the outset are, without exception,
the ones that needed the most narrowing.

> One thing this paper must never be used for: judging any individual person's recovery.
> It has nothing to say about whether you, or anyone, is "doing it right." It has never
> been tested on a single human being. For anything personal, talk to a sponsor, a doctor,
> or a counselor.

### The one-sentence version

> *The rule that nobody in AA is in charge and nobody uses their last name may not be just
> humility: read a certain way, it is the exact mathematical condition that makes a
> group's decisions trustworthy, written down by people who learned it from failure
> sixty-four years before anyone proved it. Whether that reading is right is the thing
> still to be checked.*

## Reproducibility Note

Every quantitative claim in this paper is reproducible from the companion repository
without reference to any external dataset, because there is no external dataset.

##### Deterministic results.

Sections 3 and 4 are algebra on constructed matrices. Influence vectors are normalized
left dominant eigenvectors; consensus errors come from the closed form in
the consensus-error equation above; the coupling is
a matrix product; the threshold test is one division per Step. These carry no sampling
error and are exact to the digits printed.

##### Stochastic results.

Section 6 reports Monte Carlo output. The design is: Euler integration at $dt = 0.5$ weeks
over 1,560 weeks; **400 seeds minimum for any published figure**; survival reported with
Wilson intervals; membership and quality with 95 per cent half-widths from the cross-run
standard error; Tradition comparisons under common random numbers at 400 paired
replications. **Common random numbers reduce variance and do not reduce the replication
count required**: the comparison in Table [10](#tab:tradition){reference-type="ref"
reference="tab:tradition"} was originally run at 30 paired replications, produced a
different ranking, and reversed when rerun at 400. Numerical checks use 200 paired seeds
at $dt=1.0$, 0.5, 0.25 and 0.125 weeks and 200 seeds at 10, 20, 50 and 100 years. These
support the finite-horizon numerical resolution and show continued long-run movement; they
do not prove a steady state.

##### Perturbation designs.

Multiplicative jitter at $L \in \{0.15, 0.30, 0.50, 0.75\}$, 2,000 draws per level, seed
3. Structural randomization replacing every non-zero entry with a uniform draw on
$[0.05, 1.00]$, 2,000 draws, seed 23. Wilson intervals throughout on $n = 2{,}000$. A
multiplicative design cannot move a structural zero and is not evidence about sparsity;
the structural design is not evidence about where the zeros belong.

##### Named threats.

Selection effects in the historical case (§7.4); conditioning on survival, addressed by
printing the surviving fraction beside every conditional quality figure; specification
search on architecture (§8.2); the exact cancellation of 35 governance parameters at full
adherence; and, largest of all, the unverified mapping of §3.2.

##### Verification.

All figures are asserted against recomputed values in a notebook executed end to end in a
single process, which exits non-zero on any exception, any failed assertion, or any cell
producing no output. A separate checker verifies consistency *between* documents: that
every decimal is reachable from the notebook, that simulation output states its seeds and
an interval, and that no citation attributes to a source something that source does not
contain. Each of those checks exists because an error of exactly that kind got as far as a
written page before it was caught.
