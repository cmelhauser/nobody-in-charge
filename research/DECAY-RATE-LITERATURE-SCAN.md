# The decay rate against the literature on how fast practices lapse

Scan performed 21 September 2026. Nothing here is a source record, nothing here is held, and
nothing here is cited anywhere in the manuscript, the paper, the primer or the appendix. This file
exists because `HANDOFF.md` recorded that literature as unsearched, and a search is cheaper than
the uncertainty it left. `research/SOURCES.md` remains the authority on what has been read; a paper
named below has been read in abstract or in the open-access full text through a browser, no further,
and none has been catalogued with `tools/build_corpus.py`.

## What was being looked for

`delta0 = 0.06` per week is the rate at which a member's practice decays when it is not being
renewed. It is authored, it is second only to the ordering exponent in every sensitivity design,
and Chapter 12 states plainly that nothing measures it. Its unattended half-life is 11.6 weeks.

The question for the scan was narrow: does anything measure how fast a voluntary practice lapses
when the person is no longer doing it, in units that could be compared with a weekly decay rate.

## What exists, in three literatures, none of which measures that quantity

**1. Deliberate habit degradation, measured daily.** Edgren, Baretta and Inauen (2025), "The
temporal trajectories of habit decay in daily life: An intensive longitudinal study on four
health-risk behaviors", *Applied Psychology: Health and Well-Being* 17(1): e12612,
doi:10.1111/aphw.12612, open access at PMC11635905. 194 participants over 91 days, 11,805 daily
observations of the four-item Self-Report Behavioural Automaticity Index, across sedentary
behaviour, unhealthy snacking, alcohol and smoking. Six models were fitted per person; asymptotic
and logistic fitted best for 54 per cent. Time for decay to stabilise, defined as reaching 95 per
cent of the lower asymptote, had a median of 9 to 10 days and a range of 1 to 65 days, with 76 per
cent of variance between persons. A companion paper on the same cohort, "Determinants and
strategies of self-reported habit degradation", *Psychology & Health* (2026), PMID 41664447, finds
non-performance and reward driving degradation and habitual cues counteracting it; its full text
is behind a publisher bot check. A 2026 randomised trial on snacking strategies, PMID 41781506, is
the third paper of that group.

This is the closest measured object in form and the furthest in meaning. It measures how fast an
**unwanted** habit weakens while the person is **actively working to remove it**, with substitution,
inhibition or cue discontinuity. The model's dial is the opposite case: a **wanted** practice
fading because nothing renews it. The measured rate, stabilising in days, is an order of magnitude
faster than 0.06 per week, and the design gives no reason to expect the two to agree.

**2. Computational habit models.** "Theory-based Habit Modeling for Enhancing Behavior Prediction"
(arXiv 2101.01637) carries a habit-decay parameter of the same family as `delta0`, discounting past
behaviour exponentially, with best-fitting values around 0.15 to 0.2. The parameter is per
behavioural opportunity in an app dataset, not per week of elapsed time, so it cannot be converted
into this model's units without assuming an opportunity rate.

**3. Lapse of voluntary practice regimes, which is the nearest thing in substance.** No study found
measures practice strength decaying; several measure participation falling away, which is what a
lapsing practice looks like from outside.

- Kaskutas, Bond and Avalos (2009), "7-year trajectories of Alcoholics Anonymous attendance and
  associations with treatment", *Addictive Behaviors* 34(12): 1029-1035, doi:
  10.1016/j.addbeh.2009.06.015, author manuscript open at PMC2739250. 586 alcohol-dependent people,
  telephone follow-ups at 1, 3, 5 and 7 years, four latent attendance classes: low, 63 per cent,
  fewer than five meetings at most follow-ups; medium, 16 per cent, about 50 meetings a year
  throughout; descending, 11 per cent, about 150 meetings in year one falling steeply to about six
  by year five; high, 10 per cent, about 200 meetings at year one declining gradually through year
  seven. This is the book's own domain and it is attendance rather than practice, but a descending
  class that falls from 150 to about 6 over four years is the shape the model's decay produces when
  nothing renews it.
- Mindfulness home practice: a systematic review of adherence in chronic pain reports MBSR and
  MBCT participants completing about 39.6 per cent of recommended home practice, at roughly four
  days a week and four to eight minutes a day.
- Exercise adherence: a large mobile resistance-training cohort reports 18.1 per cent of beginners
  still adherent at six months with a median dropout time of 14 weeks; supervised programmes for
  chronic conditions report about 0.30 to 0.34 fully adherent at twelve months.

## What the scan changes, and what it does not

It does not change the model. Nothing measured here is the quantity `delta0` represents, and
replacing an authored number with one borrowed from a different construct would repeat the mistake
Chapter 12 already declines to make with the skill-depreciation papers.

What it does change is the shape of the ignorance. Chapter 12 currently sets the rate against one
literature only, adult skill depreciation, which is one to two orders of magnitude slower, and says
the rate is untested as practice. The scan finds the rate is bracketed rather than merely
unsupported: deliberate habit degradation, measured in days, is far faster; skill depreciation,
measured in years, is far slower; and the observed lapse of voluntary practice regimes, where
median dropout times run to a few months, is the same order as the model's 11.6-week half-life.
That is not evidence for the value. It is a statement that the value sits where a reader would
expect the lapse of a voluntary practice to sit, between two measured literatures rather than
outside them.

## What would have to happen before any of this reaches the book

1. The Human Author decides whether to hold copies. Edgren et al. (2025) and Kaskutas et al. (2009)
   are open access and could be held on the ordinary footing, git-ignored; the *Psychology & Health*
   paper needs a browser save past a bot check, which is the Human Author's to do and not this
   agent's.
2. Each is read in full, not in abstract, and `research/SOURCES.md` records the read status before
   anything is written.
3. Only then does Chapter 12's "How much rides on it" paragraph gain the bracket, and the paper's
   limitation item follow it.

Until then this file is a search record and nothing in the project may cite it as evidence.
