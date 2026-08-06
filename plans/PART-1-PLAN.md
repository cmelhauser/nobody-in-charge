# Part One: Status and Plan

Consolidated. Part-level detail for Part One. Master plan: `../BOOK-PLAN.md`. Companion: `PART-2-PLAN.md`.

---

## 1. Where Part One stands

Six chapters, roughly 29,000 words including Machinery sections, all drafted, all with
four-part Machinery sections, no em-dashes outside quoted sources.

Word counts are whole-file, as in earlier versions of this table, and include the Machinery.
`tools/check_chapter.py` reports a smaller main-text figure for each.

| Ch | Title | Words | Status |
|----|-------|-------|--------|
| 1 | Chase's Tavern | 7,978 | **Solid.** Maxwell, Harrison, Hawkins, Marsh, Krout and Grosh read at source. |
| 2 | The Fade | 7,993 | **Solid.** Same, plus Eddy, Blair and Kurtz. Revised 2 Aug 2026 after Grosh falsified a claim. |
| 3 | The Man Who Was the Movement | 4,625 | **Solid.** Gough read at source, both relapses and the trial. |
| 4 | Akron, 1935 | 3,336 | **Improved.** Kurtz read at source; the founding narrative and the December 1937 board room are first-hand, the Amos report is not. |
| 5 | Twelve Points to Assure Our Future | 4,158 | **Solid.** Rewritten on Kurtz 2 Aug 2026. Fifteen of sixteen claims read directly. |
| 6 | The Sociologist | 3,355 | **Solid on Maxwell.** The 1944 material is second-hand. |

Supporting documents: `../research/part1-claim-register.md` (every claim, sourced and graded)
and `../research/progress-log.md` (running record of corrections).

---

## 2. What Part One establishes

**The historical spine.** Six drunks in a Baltimore tavern in 1840 assembled a
recognisable draft of AA ninety-five years early, reached a great many people, and
were gone within a decade. They were not destroyed by scandal. They were
superseded by an organisation their own members founded, which added screening,
price, hierarchy, ritual, benefits and respectability, every one of which AA later
forbade. And they were absorbed by the temperance cause that had promoted them,
lacking, in Jellinek's phrase, an ideology distinctive enough to prevent their
dissolution.

**The mechanism, in one man.** Gough relapsed twice and documented both. In 1843
his influence weight was small: he told two friends, re-signed the pledge, and the
room received him with sympathy in about ten days. In 1845 he was famous: a church
committee was appointed, a congregation voted to investigate, investigators were
sent to New York, a press war ran for weeks, and thirteen years later, under oath
in the Court of Exchequer, the episode had been compressed into the words "a short
illness". Same man, same illness, twenty-nine months apart.

**The priority problem, handled.** Milton Maxwell made a substantial part of this
book's argument in 1950. The revised thesis is that a sociologist identified the
mechanism seventy-five years ago without the mathematics to prove it.

**The strongest objection, met.** The timing objection holds that AA survived
because temperance was discredited by 1935 and nothing tried to capture it. It
fails: something did try, in 1944, and AA initially said yes before withdrawing
and writing the rules eighteen months later.

---

## 3. House style, retro-applied

All six chapters have been normalised to the conventions in `../BOOK-PLAN.md` and
pass `../tools/check_chapter.py` with no failures. The normalisation removed em-dashes,
LaTeX, main-text subheadings and main-text tables, and corrected Chapter Three's
section structure. Two standing warnings are accepted rather than fixed:

- **Chapter Six reads at Flesch-Kincaid 11.0**, the hardest in the book. It is a
  chapter about a sociologist's argument and its limits, so some of that is
  inherent, but it is a candidate for a simplifying pass.
- **Several chapters carry sentences over forty-five words.** Mostly deliberate
  lists with a rhythm. Worth a look during any revision.

---

## 4. What I can still do without acquisitions

Nothing substantial. This is the point of the plan.

Everything reachable by reading public-domain sources, running the model, or
reasoning about what is already drafted has now been done: Gough read at source
including the trial chapters, the model numbers audited and one error corrected,
the paper's Monte Carlo figures replaced with closed form, the claim register
built, the timing objection researched and answered, the Martha Washington and
Black societies incorporated.

Two small items remain that need no acquisition and can be done any time:

- A light pass over Chapters 4 and 5 once Kurtz is in hand, to rewrite rather than
  patch.
- Final cross-chapter consistency check after any further revision.

---

## 5. What is needed from you

**These are the binding constraints. No amount of further work by me removes
them.**

### Tier 1: acquired, and what remains of it

~~**Kurtz, E. (1979). *Not-God.* Hazelden.**~~ **Obtained and read in full, 2 August 2026.**
Chapter 4's founding narrative is now first-hand and Chapter 2 gained the author, date and
motive of the story AA tells about the Washingtonians. In copyright, so the full text is not
stored here; a vocabulary-only verification index is, and `check_book.py` reads it. ~~**Chapter 5 has not yet been reworked with Kurtz.**~~ **Done 2 August 2026.**

~~**Grosh, A. B., comp. (1842). *Washingtonian Pocket Companion.*~~ **Obtained and read in
full, 2 August 2026**, and it was the most consequential acquisition in Part One. See section
6: it was on the falsification list, and what it falsified was a claim of this book's rather
than the thesis.

**Blumberg, L. U., with Pittman, W. L. (1991). *Beware the First Drink! The
Washingtonian Temperance Movement and Alcoholics Anonymous.* Seattle: Glenn Abbey
Books.** A book-length modern treatment of exactly the comparison Part One is
built on. Not held by the Internet Archive at all. **Requires purchase or
interlibrary loan.** This is the book most likely to have anticipated or corrected
the argument, and I would rather know now.

### Tier 2: closes specific gaps

- **Alexander, R. M. (1988).** "'We Are Engaged as a Band of Sisters': Class and
  Domesticity in the Washingtonian Temperance Movement, 1840-1850." *Journal of
  American History* 75(3): 763-785. JSTOR. Closes the women's dimension properly.
  **Partly relieved by Grosh**, who records first-hand that women acted as a benevolent
  society within a Washingtonian society or formed separate societies under numerous names,
  and that the movement urged it. The organisational fact is now sourced; Alexander's class
  and domestic argument is not.
- **Blumberg, L. U. (1980).** "The significance of the alcohol prohibitionists for
  the Washingtonian Temperance Societies." *Journal of Studies on Alcohol* 41:
  37-77. Bears directly on Chapter Two's claim that the political-entanglement
  story is unsupported.
- **An independent account of the 1944 NCEA episode.** Currently the whole
  sequence rests on AA's *Pass It On* at one remove, and it is load-bearing for
  the timing objection. Either Kurtz, or Brown and Brown's biography of Marty
  Mann.
- **White, W. L. *Slaying the Dragon*, 2nd ed.** Cited second-hand throughout.

### Tier 3: would make Chapter Three definitive, not required

- **The Gough scrapbook, American Antiquarian Society, Worcester.** Gough's own
  collection of clippings on the 1845 affair. Requires a research enquiry to AAS.
  It would also settle the one unresolved contradiction in Part One: the sceptical
  claim that there were no soda shops on Chatham Street, against Gough's statement
  that there were two or three and he could identify the one.
- **Rockefeller Archive Center, Sleepy Hollow.** The 1937 to 1940 correspondence
  and the Frank Amos report. The route to putting Tradition 7's origin on primary
  footing without AA's copyrighted books.

### Tier 4: reader passes, before anyone calls Part One done

- **A historian**, looking for citation chains running through partisan
  intermediaries, anachronistic reading of 1840s material, and whether the Maxwell
  dependency is acknowledged sufficiently.
- **Someone in AA**, looking for whether Chapter Three treats Gough humanely,
  whether the engineering reading of the Traditions reads as reductive, and
  whether anything about the Steps or Traditions is wrong in a way an outsider
  would not notice.

---

## 6. Falsification list

Part One makes historical claims. These would overturn them:

- Post-1950 scholarship showing the Washingtonians declined primarily from
  political entanglement would break Chapter Two and Chapter Six's framing of
  Maxwell. **Blumberg 1980 is the specific test.**
- Kurtz showing the Traditions were designed from principle rather than compiled
  from failure reports would break Chapter Five's central argument. **Tested 2 August 2026
  and not broken.** The test came back stronger than a null result: the first sentence of
  Wilson's April 1946 publication is "Nobody invented Alcoholics Anonymous. It grew. Trial
  and error has produced a rich experience." Chapter 5 has been rewritten on that basis.
- **A Washingtonian document prescribing rotation of officers, or advising societies against
  giving members' names to the press, would break the book's central comparison**, because
  the argument is that the movement lacked precisely Traditions 2 and 12. **Tested 2 August
  2026 against the *Washingtonian Pocket Companion*, the movement's own manual, and not
  broken.** The manual prescribes elected officers with no term limit and a president who may
  order a member to sit down, and it takes the opposite position on anonymity in terms:
  publicity and freedom are preferable to whisperings and secrecy in giving the names. What
  the same document did break was a claim of Chapter 2's, that the Washingtonians had no rule
  about outside issues. They had two. Both chapters now carry the correction in their main
  text, and the comparison the book makes is between two written codes rather than between
  rules and their absence.
- An account of the 1944 NCEA episode showing AA never meaningfully endorsed the
  NCEA would weaken the answer to the timing objection.
- Evidence that the Rockefeller refusal was financial caution rather than a
  judgment about money spoiling the fellowship would break Chapter Four's best
  story.

---

## 7. Verdict

Part One is **complete as a draft and substantially verified as history.** Chapters 1, 2, 3
and 6 rest on sources read at source, and Chapters 1 and 2 now rest on the movement's own
manual as well as on its historians. Chapter 4 is improved but its funding narrative still
reaches the reader through AA's copyrighted histories. Chapter 5 has been rewritten on Kurtz and is
now the second best sourced chapter in Part One. The weakest chapter is Chapter 4, whose
funding narrative after December 1937 still reaches the reader through AA's own histories.

The strongest thing Part One says is no longer that AA wrote rules and the Washingtonians did
not. It is that both wrote rules, within two years of founding in the Washingtonian case, and
that the ones the Washingtonians did not write are the three this book will argue carry the
weight. That is a claim a reader can check against a primary document, which the earlier
version was not.

The remaining work is not writing. It is four books and an archive enquiry.

---

## 8. Release-gate corrections, opened 6 August 2026

This plan is now subordinate to plans/RELEASE-GATE-PLAN.md. The documentary argument will be tightened as follows:

- treat the Gough material as a same-person contrast and historical observation, not as a causal identification of influence;
- qualify claims that governance mechanisms “cost nothing” so that they refer to low material or enforcement cost, not literally zero burden;
- acknowledge that Maxwell supplied several mechanisms; the project’s contribution is the stationary-influence formalization and test, not the discovery of “why” networks distribute influence;
- make clear that textual or chronological sequence does not prove that Alcoholics Anonymous intended or discovered the theorem; and
- keep the paper, source register, reference files, and plan at the same evidentiary status, explicitly labelling superseded notes.
