# Chapter Nineteen
## You Cannot Close the Door

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
