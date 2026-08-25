# The governance matrix: an elicitation form for a second reader

> **Do not send this file to a respondent.** It is the working source, and it carries the
> collator's section further down, which names what the exercise exists to elicit. The packet to
> send is `research/elicitation/1-respondent-form.pdf`, built by `sh research/elicitation/build.sh`;
> **never send `4-collator-notes.pdf`.** Section 9 of `HANDOFF.md` covers the round.

**What this is for.** The book's Part Four rests on a twelve-by-eight table saying which of AA's
Traditions governs the supply of which of eight things a group produces for its members. One
person built that table. No amount of further computation can test whether it is right, because
every perturbation design in the project takes the table's pattern of empty cells as given and
prices its consequences. The only test is whether somebody else, working from the same
definitions and without seeing the original, fills it in the same way.

**Please do not read `model/aa_group_model.py` before filling this in.** The whole value of the
exercise is that your answers are independent of mine. Everything you need is below.

**Time required:** twenty to forty minutes. There are no right answers and the exercise is not
a test of you.

---

## What you are marking

Below are eight things a group produces that its members need, and the twelve Traditions.

For each pair, mark whether that Tradition **governs the supply** of that thing: whether how well
a group adheres to that Tradition changes how much of that thing the group has available to give.

Mark it **1** if yes and **0** if no. That is the whole task. **The presence or absence of a mark
matters far more than any number**, so if you want to hedge, hedge toward the mark you would
defend rather than toward a middle value. If you want to record strength as well, use a scale of
0.1 to 1.0 in the same cell, but fill in the zeros and ones first and treat the strengths as a
second pass.

"Governs the supply" is meant in a direct sense. A Tradition that makes the group better in
general, and therefore better at everything, is not thereby governing every resource. Ask instead:
if this Tradition were abandoned tomorrow and nothing else changed, would this particular thing
become scarcer?

---

## The eight resources

1. **Admission.** A way in. Whether a person who turns up can become a member at all.
2. **Identification.** Somebody in the room whose story is close enough to yours that you
   recognise yourself in it.
3. **Proof.** The visible demonstration that recovery happens, supplied by people who are
   evidently recovered.
4. **Confidentiality.** The reasonable expectation that what you say here is not repeated
   outside.
5. **Counsel.** Guidance about what to do, from the group or from individuals in it.
6. **Recipient.** Somebody to help. A newcomer who is actually an alcoholic and can therefore
   receive twelfth-step work.
7. **Continuity.** The group still existing, in the same form, next week and next year.
8. **Pressure.** The expectations other members place on you, and the mild social cost of not
   meeting them.

## The twelve Traditions, in short form

1. Common welfare first; personal recovery depends on AA unity.
2. One ultimate authority, a loving God as expressed in the group conscience; leaders are
   trusted servants who do not govern.
3. The only requirement for membership is a desire to stop drinking.
4. Each group autonomous except in matters affecting other groups or AA as a whole.
5. Each group has one primary purpose, to carry its message to the alcoholic who still suffers.
6. A group ought never endorse, finance or lend the AA name to any related facility or outside
   enterprise.
7. Every group fully self-supporting, declining outside contributions.
8. AA should remain forever non-professional, though service centres may employ special workers.
9. AA ought never be organised, though service boards or committees responsible to those they
   serve may be created.
10. AA has no opinion on outside issues; the AA name ought never be drawn into public
    controversy.
11. Public relations policy based on attraction rather than promotion; personal anonymity at the
    level of press, radio and films.
12. Anonymity is the spiritual foundation of the Traditions, ever reminding us to place
    principles before personalities.

---

## The grid

|  | Admission | Identification | Proof | Confidentiality | Counsel | Recipient | Continuity | Pressure |
|---|---|---|---|---|---|---|---|---|
| T1 common welfare | | | | | | | | |
| T2 group conscience | | | | | | | | |
| T3 open membership | | | | | | | | |
| T4 autonomy | | | | | | | | |
| T5 one purpose | | | | | | | | |
| T6 no endorsement | | | | | | | | |
| T7 self-support | | | | | | | | |
| T8 non-professional | | | | | | | | |
| T9 no organisation | | | | | | | | |
| T10 no outside opinion | | | | | | | | |
| T11 attraction | | | | | | | | |
| T12 anonymity | | | | | | | | |

---

## Three questions afterwards, which matter as much as the grid

1. **Did any row come out entirely empty?** If so, which, and did that feel like a finding or
   like a failure of the resource list?
2. **Is the resource list wrong?** If there is something a group supplies that a member's
   recovery needs and it is not among the eight, say what. That is a more serious objection to
   the book than any individual cell.
3. **Which cell did you find hardest?** The book's results turn out to hinge on two cells in
   particular, and it would be worth knowing whether an independent reader finds those two hard
   or easy. The two are not named here so as not to lead you.

---

## What will be done with your answers

Compared with the original on three things, in this order:

1. **Which rows are empty.** The book's Chapters 16, 17 and 18 all rest on a claim about which
   Traditions govern nothing any Step consumes. If your empty rows match the book's, that claim
   has independent support for the first time. If they do not, Chapter 18 is wrong and will say
   so. How many rows the book leaves empty, and which, is deliberately not stated here, for the
   same reason the two decisive cells are not named above.
2. **The whole sparsity pattern**, cell by cell, as a simple agreement count out of 96.
3. **The consequences**, by rebuilding the book's coupling from your matrix and rerunning
   Chapters 16 and 17. If the results hold on your matrix as well as mine, Part Four stops
   resting on one person's judgement.

**A disagreement is the useful outcome.** The book already records that Part Four's coupling
claims do not survive structural randomisation, so a matrix that differs from mine substantially
is expected to change the results and that is information. Nothing here is looking for
confirmation.

---

## For the person collating

**This section is for the collator, not the respondent.** It names things the grid above
deliberately withholds, so do not hand a respondent a copy that includes it.

Three respondents is the useful minimum. With three you can report, per cell, whether zero, one,
two or three marked it, and the empty-rows claim becomes a statement about agreement rather
than about one person.

Store completed forms as `research/governance-elicitation-<initials>.md` and add a section to
`research/SOURCES.md` recording who filled each one in, what they were told, and whether they had
seen the book. **Whether the respondent has read Part Four is the single most important thing to
record**, because a reader who has will not be independent.

**The comparison script exists and is fixed in advance.** `model/elicitation_compare.py` was
written before any form came back, so the analysis cannot be chosen after seeing the answers. It
reports per-cell agreement out of 96 with the two kinds of disagreement separated, Cohen's kappa
alongside the raw rate because the book's matrix is sparse enough that chance agreement is high,
which rows each respondent left empty and whether they match the book's, and Chapters 16 and 17
recomputed on the respondent's matrix.

Check it before sending any forms out:

```bash
python3 model/elicitation_compare.py --self-test   # exercises a matching and a contradicting respondent
python3 model/elicitation_compare.py               # reads every completed form
```

The self-test includes a respondent who differs by one row and confirms the script says so rather
than smoothing it over. A respondent may give bare marks or strengths; with bare marks the rerun
substitutes the book's own magnitude where both agree a cell is non-zero, and 0.5 where the
respondent filled a cell the book left empty. The script states that substitution in its output
every time, because a bare-marks respondent is testing the sparsity pattern rather than the
magnitudes, which is the more important half.
