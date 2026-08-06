# Part Two: The Group

The central claim of the book. Chapters 7 to 11, roughly 16,000 words.

Master plan: `../BOOK-PLAN.md`. Companion: `PART-1-PLAN.md`.

---

## 1. Why Part Two is different

**It needs no acquisitions.** Every result is derived, verified, and in hand. The
two sources it depends on, Golub and Jackson (2010) and DeGroot (1974), are read.
The model has been audited. Nothing in Part Two is waiting on a library.

**It is the register test.** If a plain-language account of the Golub and Jackson
condition works at book length, the book works. If it does not, the book has no
centre and Parts Three to Five are commentary. This is why Part Two should be
drafted before any more history.

**It is where the book earns its title.** Part One ends with Maxwell naming
anonymity, rotation and servant leadership as hazard-avoiding traditions and
having no way to show why those particular mechanisms mattered. Part Two shows
why.

---

## 2. Chapter plan

### Chapter 7. How a Room Decides
*Target 3,000 words. Status: partly drafted in the paper.*

The setup, with no notation. A group conscience is a room full of people who talk
until they agree. Model that: everyone starts with a view, everyone listens to
everyone, everyone adjusts, repeat. That is DeGroot averaging, and it is a
reasonable description of how a meeting actually reaches a decision.

Introduce the influence weight as the share of the final answer traceable to one
person's starting view. Establish that the weights sum to one and that they are
not the same as who talks most: influence is about whose view moves others.

**The chapter's job** is to make the reader feel that a group conscience is a
computation, without saying so in those words, and to plant the question: when can
you trust the answer?

**The Machinery.** DeGroot's updating rule; the influence vector as the left
dominant eigenvector; conditions for convergence (strong connectivity,
aperiodicity).

---

### Chapter 8. The Condition
*Target 3,500 words. Status: exists in the paper, needs translating.*

**The most important chapter in the book.**

Golub and Jackson's result: a group that decides this way converges on the truth
as it grows if and only if the largest influence weight vanishes. State it in
plain words: nobody may keep a fixed share of the answer.

Give the intuition properly, because everything depends on the reader believing
it. Everyone's view is partly right and partly wrong. Blend many views evenly and
the errors point in different directions and cancel. But if one person always
supplies a third of the result, their errors never cancel, no matter how many
people join. The group becomes more confident without becoming more correct.

Then the arithmetic, which is exact and pretty: under equal weighting the error
falls as exactly one over the square root of the number of members. Under a
dominant member it does not fall at all.

Then the mapping. Traditions 2, 9 and 12 are three independent mechanisms
enforcing the condition. Leaders serve rather than govern, so office buys no
weight. No hierarchy and rotating service, so weight does not accumulate.
Anonymity, so the things weight would attach to are not visible in the first
place.

**The Machinery.** Statement of the theorem; the closed form for consensus error;
why the flat case gives N to the minus one half exactly.

---

### Chapter 9. Confident and Wrong
*Target 3,000 words. Status: exists.*

The failure modes, each with numbers and a face.

- **The dominant member.** The old-timer whose view settles every group
  conscience. Max influence 0.350 at ten members and 0.350 at five hundred.
- **The clique.** The long-timers who have decided before the business meeting
  opens. 0.167, flat across all sizes.
- The comparison table across N.

Then the disturbing part, which deserves the chapter's second half: **a broken
group conscience feels exactly like a working one.** Consensus is reached either
way. There is no argument, no visible dysfunction, no symptom. The group is simply
wrong more often, and growing it does not help.

This is where Gough returns from Part One as the case study, and where the model's
asymmetry result belongs: damage travels from member to group at full strength and
from group to member attenuated.

**The Machinery.** The influence and error tables; the asymmetry derivation.

---

### Chapter 10. Rotation Has to Be Wide
*Target 2,500 words. Status: exists; this is the book's novel corollary.*

The Traditions require rotation. They say nothing about breadth. In a group of
four hundred rotating twelve people, maximum influence settles at 0.031, which is
twelve times the flat benchmark of 0.0025, and the group's error is about twice
what it could be. That is a real permanent cost, though well short of a caucus.
The sharper result is the scaling failure: a fixed pool floors at roughly the
officeholder's share divided by the pool size and stays there, so the gap against
an evenly weighted room widens without limit as the group grows. Clearing the bar
takes a pool of about twenty-six per cent of the group, at every size tested.

This is the one prediction in the book that a single AA group could test against
its own service records this year, and the chapter should say so plainly and tell
the reader how.

**The Machinery.** Time-averaged influence under rotation; the alpha over R
approximation; the pool-size sweep at N = 400.

---

### Chapter 11. What the Washingtonians Lacked
*Target 3,000 words. Status: new synthesis, no research needed.*

Part One meets Part Two. The Washingtonians concentrated their credibility in a
handful of named men, and the theorem says what that costs. Hawkins on the
platform, paid by the Massachusetts Temperance Society from 1841. Gough, and 1845.

Then the honest limits, which belong here rather than in a final chapter:

- The theorem concerns members averaging beliefs about a shared question. Public
  reputation is not that. The extension is a structural analogy, not an
  application.
- DeGroot averaging is a strong simplification. Real members argue, defer
  selectively, abstain, and update out of order.
- Exchangeability is exact only in the limit of perfect adherence.
- And the referral-stream objection from Part One resurfaces: the model treats
  losing newcomer inflow as more dangerous than losing the guard Traditions.

Close on Maxwell: he got here in 1950 without the mathematics, and the
mathematics says he was right.

---

## 3. What Part Two must not do

**It must not overclaim the correspondence.** The claim is that three Traditions
satisfy a provable condition, not that Bill Wilson anticipated a theorem, and not
that this is why AA survived. Chapter 11 states the limits explicitly.

**It must not bury the reader in notation.** The main text carries no equations.
Everything formal lives in the Machinery sections, which are skippable by
construction.

**It must not lose the people.** Part One works because it is about six drunks in
a tavern and a man in a house on Walker Street. Part Two is about a matrix. The
counterweight is that every failure mode has a recognisable human face, and the
chapters should be built around those faces rather than around the mathematics.

---

## 4. Sequence

1. **Chapter 8 first**, not Chapter 7. It is the hardest translation problem and
   the whole book depends on it. If plain-language Golub and Jackson works, write
   the rest; if it does not, stop and rethink before writing 60,000 more words.
2. Then Chapter 9, which is the same material at lower difficulty.
3. Then Chapter 7 as the ramp into them, written last of the three because it is
   easier to write an introduction once you know what it introduces.
4. Then Chapter 10, which is self-contained.
5. Then Chapter 11, which needs all of Part One and Part Two in place.

---

## 5. Definition of done, per chapter

A Part Two chapter is finished when all of the following hold:

1. Drafted with the four-part Machinery.
2. **Every number in it added to `../model/book-calculations.ipynb` with an assertion**, in the
   section for that chapter, and the notebook re-run clean. Not carried over from an
   earlier session. The Monte Carlo drift found in the audit came from exactly that.
3. `python3 check_chapter.py <file>` returns no FAIL.
4. Warnings either cleared or consciously accepted and noted.
5. Cross-checked against the chapters around it for repeated material. The
   influence tables already appear in ch03's Machinery; each further appearance
   needs a different job.

---

## 6. Dependencies and risks

**No dependency on Part One's outstanding acquisitions.** Part Two can be
completed while Kurtz and Blumberg are being obtained.

**One dependency in the other direction.** Chapter 11 uses Gough and the
Washingtonians, both now solidly sourced, so it is unblocked.

**The main risk is register.** These chapters have to be readable by someone with
no mathematics and satisfying to someone with plenty. The Machinery structure is
the mechanism for that, and Chapter 8 is where it either works or fails.

**A secondary risk is repetition.** The influence tables appear in the paper, in
Chapter 3's Machinery, and will appear again in Chapters 8, 9 and 10. Each
appearance needs a different job or the reader will feel the book circling.

**And there is now a fifth appearance, added 5 August 2026.**
`reference/PRIMER-steps-and-traditions.md` restates the dominant-member floor, the
five-per-cent dose, the rotation-pool scaling and the three obstructions, once under
Tradition 2, once under Tradition 9 and once under Tradition 12. It is a derived
document that asserts nothing and no checker reads it, so a corrected figure in
Chapters 8, 9 or 10 has to be carried there in the same session. `CLAUDE.md` has the
rule. The primer's job is different enough from the chapters' that it does not add to
the circling risk above: it is a lookup table, not another telling.

---

## 7. Release-gate corrections, opened 6 August 2026

The mathematical exposition will be corrected and standardized around four points:

1. Rows of the influence matrix are outgoing choices; columns receive direct attention; the stationary distribution is a left eigenvector under the project’s row-stochastic convention.
2. The empirical mapping from governance text to network operators is a proposed operationalization, not itself a theorem. Violating one mapped principle is not sufficient for capture unless the resulting perturbation actually concentrates stationary influence.
3. The mean-absolute-error identity used in the appendix is exact only under its stated Gaussian premise; outside that premise it is an approximation or diagnostic.
4. No prose may describe the model as applying literal reciprocal \(1/\beta\) weights where the implemented operator uses a different normalized transformation.

The incorporated Golub–Jackson PDF is the active local source for the convergence and influence claims. All equations, captions, notation tables, and plain-language summaries must follow these conventions.
