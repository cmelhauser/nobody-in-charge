# Preface
## What This Book Knows, and How

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
