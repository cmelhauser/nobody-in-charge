# Sources

Current provenance for sources cited in the manuscript, paper, appendix, and primer. Each
entry states its actual status: read in full, partly read, abstract/secondary only,
referenced but not reproduced, or not obtained. Historical status notes are retained only
when they are explicitly marked superseded.

---

## Staged corpus, now fully incorporated

`research/staged/` held a separately acquired working corpus dated 2026-08-04: source files and
OCR, per-item metadata and citations, pending-source records, an acquisition report, and
incorporation instructions. Every source in it has now been reviewed and entered in the categories
below. The rule it existed to enforce still stands for anything acquired in future: material is
**not part of this source register and is not evidence used by the manuscript** until it is
reviewed and entered here.

The staged corpus preserves its own provenance in
`research/staged/reports/ACQUISITION_REPORT.md` and
`research/staged/metadata/`. Its status vocabulary describes acquisition state inside the
staged package, not incorporation into the book. The package was relocated from the former
`corpus_build 2` delivery container directly into `research/staged/` on 2026-08-05; relative
paths within the package were preserved.

On 6 August 2026, Golub and Jackson (2010) and Maxwell (1950) were removed from staged
status. Their active source files are now under `research/incorporated/`; the duplicate
staged Maxwell package was discarded while the project's original Maxwell PDF and text were
kept.

On 9 August 2026 the staged corpus was worked through at the user's direction. Four of its six
items moved to `research/incorporated/` that day: the three American Temperance Union documents
and the source record for AA pamphlet P-17. The two journal articles followed on 10 August 2026,
once each had been obtained by hand. All six are now incorporated, so the staged boundary that
governed the release round is closed rather than merely narrowed.

**The staged corpus is now empty of unread material.** Both journal articles were obtained by
hand on 10 August 2026, after automated retrieval returned a reCAPTCHA challenge that this project
would not work around. Pagano et al. (2004) and Greenfield and Tonigan (2013) are read in full and
are under `research/incorporated/`. Their entries below record what each supports and what it does
not.

What remains under `research/staged/` is the acquisition record itself: the report, the metadata,
and the incorporation instructions. Those are provenance, not evidence, and they stay because they
document how the corpus arrived.

---

## Incorporated source storage

`research/incorporated/` contains Maxwell (1950) and Golub and Jackson (2010), which overlapped
the staged acquisition package, and the six items promoted out of it, four on 9 August 2026 and
the two journal articles on 10 August:

| Item | Rights | Local files | Read status |
|---|---|---|---|
| ATU, *Report of the Executive Committee* (1840) | public domain, pre-1929 | PDF and OCR | **read in full 13 September 2026**; supports no claim in the manuscript; the 1839 treasurer's account (printed p. 6) verified against the page image |
| ATU, *Annual Report* (1841) | public domain, pre-1929 | PDF and OCR | read for the Washingtonian passages in August, **read in full 13 September 2026**; p. 39 and the treasurer's account (printed p. 33) verified against the page images |
| ATU, *Almanac for 1849* (1848) | public domain, pre-1929 | PDF and OCR | **read in full 13 September 2026**; supports no claim in the manuscript; the Sons of Temperance statistics for 1848 (printed p. 17) verified against the page image |
| AAWS, *A.A. Tradition: How It Developed*, P-17 (2024) | **copyrighted; published free by AAWS** | PDF and extracted text since 13 September 2026, byte-identical to the file read in August | read; two passages verified against page images; supplies the 1946 Twelve Points text for Chapter 5 |
| Pagano et al., "Helping Other Alcoholics" (2004) | NIH author manuscript, open access | PDF and extracted text | read in full; figures checked against the results section |
| Greenfield and Tonigan, "General AA Tools of Recovery" (2013) | NIH author manuscript, open access | PDF and extracted text | read in full; cited in Chapter 12 as an objection to one dial per step |
| Wilson, "Twelve Suggested Points for A. A. Tradition", *A.A. Grapevine* (April 1946) | **A.A. Grapevine copyright; not archived** | record only | read at source; Chapter 5's opening quotation verified, and the two-title problem explained |
| DeGroot, "Reaching a Consensus" (1974) | **ASA / Taylor & Francis; not archived** | record only | read at source; the updating rule behind Part Two |
| *Alcoholics Anonymous*, first edition 1939, in the 1999 BBSG reprint | reprint asserts no copyright; 1939 status contested | PDF and extracted text | **thirty personal stories read in full 17 August 2026** (counted as twenty-nine until 13 September 2026); supports appendix A13, the census of arrival channels against the model's arrival term; the printed wording quoted in Chapter 4 (printed pp. 71 and 95) checked 13 September 2026 |
| AAWS, *Twelve Steps and Twelve Traditions* (1953) | **copyrighted; published free per chapter by AAWS** | assembled PDF and extracted text since 13 September 2026 | **read in full 10 August 2026**; supplies the elder-statesman objection to Chapters 8 and 10, the rotating-leadership text for Chapter 10, the cross-reference count for Chapter 16, and the unity/purpose distinction for Chapter 17 |
| Rohr, *Breathing Under Water* (2011) | **in copyright and in print; not archived** | record only | read in full 10 August 2026; cited only for its reading of anonymity and for containing no discussion of the Traditions; see the provenance note below |
| Kurtz, "A Talk About the History of Alcoholics Anonymous" (about 1984) | **sold as an audiobook; the Human Author's own transcription** | PDF and extracted text since 13 September 2026 | read in full 10 August 2026; the closing survival answer in Chapter 25; distinct from Kurtz (1991) |
| Recovery Dharma Global, *Recovery Dharma*, second edition (2023) | CC BY-NC-SA 4.0; the one licence here that would permit committing the document | PDF and extracted text | **read in full**, in two passes: Sections I and II 16 August 2026, the meditations and inquiry questions 13 September 2026; source for appendix A12 and four paragraphs of Chapter 24 |

### Seven open-access papers, held and read on 13 September 2026

At the Human Author's direction the corpus also holds seven papers posted free by their publisher
or author, each git-ignored with a SHA-256 and a verification index. All seven were read the day
they were obtained, six in full and one in part, and quotations were checked against the page
images. What they bear on was applied to the manuscript, the paper, the primer and the appendix
the same day, at the Human Author's direction; the model is unchanged. Page numbers below are those printed on
the copies held; five are working papers paginated differently from the published articles, so a
page reference taken from one must be checked against the article before it is cited.

| Directory | Work | Copy from | Read status |
|---|---|---|---|
| `Angrist_2014` | Angrist (2014), "The Perils of Peer Effects", as NBER Working Paper 19774 (December 2013, revised January 2014) | nber.org | **read in full**; cited in the paper only |
| `CunhaHeckman_2007` | Cunha and Heckman (2007), "The Technology of Skill Formation", as NBER Working Paper 12840 (January 2007) | nber.org | **read in full**, with notes and tables |
| `CunhaHeckmanSchennach_2010` | Cunha, Heckman and Schennach (2010), as NBER Working Paper 15664 (February 2010) | nber.org | **read in full**, with tables; the web appendix is not held |
| `HuSchennach_2008` | Hu and Schennach (2008), *Econometrica* 76(1): 195-216, a JSTOR download | the first author's university site | read in part: abstract, introduction and the assumptions of section 2 (195 to 200); cited at a remove in Chapter 13 |
| `Lembke_nd` | Lembke (n.d.), "Sacrifice, stigma, and free-riding in Alcoholics Anonymous" | asrec.org | **read in full**; cited in Chapters 2 and 15 since 13 September 2026 |
| `Dinerstein_2022` | Dinerstein, Megalokonomou and Yannelis, "Human Capital Depreciation and Returns to Experience", NBER Working Paper 27925 (2020, revised 2022) | nber.org | **read in full**, apart from the online appendix; cited in Chapter 12 and the paper since 13 September 2026 |
| `CohenJohnstonLindner_2023` | Cohen, Johnston and Lindner, "Skill Depreciation during Unemployment: Evidence from Panel Data", NBER Working Paper 31120 (2023) | nber.org | **read in full**, apart from the appendices; cited in Chapter 12 and the paper since 13 September 2026 |

**What the reading found, and where it now stands.** Each finding was applied on 13 September 2026
at the Human Author's direction; the last sentence of each item says where.

1. **Every attribution Chapters 12 and 13 and the paper make to the two Cunha papers holds, with
   three qualifications.** Self-productivity and dynamic complementarity are defined in Cunha and
   Heckman (2007, 7 to 10), who sum up their joint effect as "skills beget skills and abilities
   beget abilities" (8), which Chapter 13 paraphrases fairly; the CES technology, its elasticity
   1/(1 - φ) and its Leontief limit as φ goes to minus infinity are at 11 to 12. The five-input
   stage technology the paper adapts is Cunha, Heckman and Schennach's equation (2.3) (6). Their
   measurement system in logs of the factors (23) matches Chapter 13's proxy equation, their
   anchoring of latent skill in adult outcomes is section 3.5 (16 to 18), and they draw on
   Schennach (2004a) and Hu and Schennach (2008) for identification (3, 11). The qualifications:
   - *Notation.* They write the substitution parameter as φ and use ρ for the share of cognitive
     skill in an adult outcome (6). The book's ρ is its own, and a reader moving between the two
     should be told.
   - *"Multiplicative."* Chapter 12 says the multiplicative production of a stage from several
     inputs comes from these papers. Their technology is a CES, multiplicative only in its
     Cobb-Douglas case (Cunha and Heckman 2007, 14). The book's multiplicative growth equation,
     which the paper itself says is not a CES aggregator, is the book's own.
   - *"And solve it."* Chapter 13 says Cunha, Heckman and Schennach face the endogeneity of
     investment and solve it. They address it (18 to 21, 29 to 30): first with time-invariant
     heterogeneity identified from adult outcomes, then with time-varying heterogeneity, using
     family income as the excluded variable under parametric assumptions they state.

   All three are now corrected in Chapters 12 and 13 and in the paper, and Chapter 14 no longer
   credits Cunha, Heckman and Schennach with a depreciation structure their technology does not
   have.
2. **The sign of the substitution parameter is exactly what Cunha, Heckman and Schennach find
   varying.** In their estimates allowing for heterogeneity (Tables 4 and 5), φ for cognitive skill
   is positive in early childhood (0.31 and 0.59, elasticities 1.46 and 2.41) and strongly
   negative later (-1.24 and -1.22, elasticity about 0.45); for noncognitive skill it is negative at
   both stages (elasticities 0.62 to 0.68). Chapter 13 frames the sign of ρ as deciding whether the
   Steps are a chain or a menu. The one literature where the analogous parameter has been estimated
   finds the answer depends on the stage and the skill. That is an analogy, not evidence about the
   Steps, and Chapter 13 and the paper now present it as one.
3. **Angrist supports the paper's use of him.** Correlations between individuals and their
   groups are largely mechanical and predict nothing about what manipulating the groups would do
   (abstract; 1 to 12; summary, 21); designs that move peers independently of individual traits
   are the strong evidence, and have found little (17 to 21). His account of Carrell, Sacerdote
   and West's reassignment of Air Force Academy peer groups, which had no overall effect and
   marginally significant negative effects for the students it was meant to help (17), is the
   warning the paper cites. The paper's bibliography now marks it read in full.
4. **Lembke supports the paper's citation, and offers two things the book could use.** It applies
   Iannaccone's sacrifice-and-stigma account to AA directly (4 to 5, 19 to 21). It reads AA's entry
   cost as stigma rather than sacrifice, since the only requirement is a desire to stop drinking,
   which keeps the fellowship open to the most severe cases (6 to 7), while sponsors screen after
   entry as gatekeepers against free-riders (10, 13 to 17). That sits beside Chapter 2's contrast
   between AA and the Sons of Temperance, who screened at the door. And its sober member who does
   not work the Steps is costly because such members do not sponsor, which shrinks the pool of
   possible sponsors (11): the model's recipient resource in another vocabulary. The paper calls
   itself theoretical and in need of empirical support (21), and its two cases are clinical
   vignettes, so it supplies a frame and not evidence. Chapter 2 now carries the stigma reading and
   Chapter 15 the pool of sponsors, and the paper's bibliography marks it read in full.
5. **The two depreciation papers do not support six per cent a week for anything they measure.**
   The model's dials lose about six per cent of their value a week when nothing holds them up
   (Chapter 12; `delta0 = 0.06` in the canonical model), a half-life of about eleven and a half
   weeks, which compounds to a loss of about 96 per cent a year. Dinerstein and colleagues, using
   the quasi-random order in which Greek graduates wait for teaching posts, estimate the
   depreciation of teaching skill at 4.3 per cent a year for early-career teachers (standard error
   1.9) and 17.2 per cent for more experienced ones (standard error 22.5), rates they call large
   and describe as lower bounds if age effects are positive (4, 37 to 38): half-lives of about
   sixteen and about four years. Cohen and colleagues find "no decline in a wide range of cognitive
   and noncognitive skills" over up to three years of unemployment (abstract; 27), though the same
   measures fall after retirement (4). The comparison is imperfect in one direction: both papers
   measure skill, and the model's dial is practice, which may lapse faster than the capability
   behind it. So the literature does not calibrate the rate. It shows that read as skill, six per
   cent a week is one to two orders of magnitude too fast, and that the evidence Chapter 12 wanted
   is more likely in the literature on habit and relapse than in labour economics. Two further
   points came from reading the main texts in full. Dinerstein and colleagues' district-level
   estimates rest on a weak first stage (an F statistic of 4.6, reported with weak-instrument-robust
   sets, 31), and they chose a setting they expected to produce high depreciation, since waiting
   teachers had few ways to practise (9). Cohen and colleagues' null covers cognitive skills and the
   noncognitive skills that predict earnings, while self-assessed conscientiousness, risk
   tolerance, trust, patience and reciprocity fell by 0.2 to 0.6 standard deviations (15), the one
   result in either paper that looks more like a practice than a skill. The model is unchanged,
   because no source measures how fast a practice lapses. Chapter 12, the primer, the paper,
   appendix A11 and `research/PARAMETERS.md` now say all of this, and Chapters 1 and 24 note that
   large downward moves of the decay rate are among the few that reverse the ordering of referral
   loss against attraction loss. A 400-seed paired run the same day confirmed the reversal on final
   membership at 25 per cent lower, with the ordering still holding on endpoint viability and
   existence (`research/decay_ordering.json`; Chapter 12 and appendix A7.5).
6. **Hu and Schennach is correctly described at a remove.** It identifies nonlinear
   errors-in-variables models with nonclassical error from an instrument, assuming some measure of
   location of the error is zero (195 to 197), and Cunha, Heckman and Schennach use it that way (3).
   Chapter 13's statement that it is known through their application remains accurate.

### The three copyrighted works read on 10 August 2026

These three changed the project's own rule, and the change should be stated rather than absorbed
quietly. The rule was previously written, in several chapters, as *this project does not acquire
AA copyright material*. That conflated two different things. A rule against **holding** a
copyrighted work is a copyright rule and the project keeps it strictly: nothing is committed and
nothing is quoted at length. (Until 13 September 2026 nothing was stored either; since then the
corpus holds lawful copies git-ignored, at the Human Author's direction.) A rule against **reading** one was never a copyright
rule at all, and it had been costing the argument evidence.

What it cost is now measurable. *Twelve Steps and Twelve Traditions* contained the book's own
thesis in Wilson's words, the single strongest objection to that thesis, the disproof of the
index-pairing conjecture, and corroboration for the unity assignment Kurtz had challenged. Three
of those four are things the book had recorded as unavailable.

`TwelveAndTwelve_1953` is held on exactly the P-17 footing: AAWS publishes the book free, one
chapter per PDF, and a reading copy was assembled locally, read, and left outside the repository.
The record keeps the citation, the assembly's SHA-256, the pages verified, and the reproducible
cross-reference count. That August assembly was not retained. Since 13 September 2026 a fresh
assembly of the same twenty-nine chapter PDFs is held git-ignored in the directory, with each
chapter's SHA-256 recorded so it can be re-checked against aa.org.

`Rohr_2011` carries a provenance problem recorded in full at
`research/incorporated/Rohr_2011/metadata.json`. The file consulted bore an OceanofPDF.com
imprint, which is an unauthorized distribution site, and the work is a current in-print commercial
title, so the posting was plainly not authorized. The file was not retained, and the
bibliographic record was confirmed against publisher and library listings independently of it.

**Resolved 17 August 2026.** The Human Author holds a lawfully obtained copy of the work. The
objection was about the project's access resting on an unauthorized posting, and a copy on the
author's shelf settles that. It is worth being exact about what this does and does not cover: the
two claims were read from the posted file, and what has changed is that the work is now lawfully
to hand and re-checkable at will, not that anyone has re-read it. Neither claim carries a page
citation anywhere in the manuscript, the appendix or the paper, so the difference between the 2011
Franciscan Media first edition and the 2016 SPCK printing consulted is immaterial to every use
made of it.

`KurtzTalk_c1984` is dated only by inference and must always be cited as "about 1984". Wilson's
letters are quoted within it from memory and without page citations, so anything attributed to
Wilson through it is at a remove. Since 13 September 2026 the copy read in August, the Human
Author's own transcription of the audiobook, is held git-ignored in its directory.

The P-17 document is never committed. It is copyrighted AAWS literature distributed as a free
official PDF, and this repository is public, so committing the full PDF and a full OCR transcript
would be redistribution beyond the authorized source context. Until 13 September 2026 it was not
held at all; since then the official file is held git-ignored, byte-identical to the July 2024
file read in August, which is what the recorded SHA-256 is for. The record retains
the citation, the official URL, the SHA-256 of the July 2024 file, and the verified quotations. A
verifier should download it from aa.org. Removing the mirror changes nothing about what the book
may claim from it.

### Recovery Dharma (2023), the one source whose licence would permit committing it

Worth a note because it is the single exception to the reason everything else is git-ignored. The
book is published under CC BY-NC-SA 4.0, which expressly permits copying, redistribution and
adaptation with attribution. Nothing in its rights position would prevent committing the document.
It is git-ignored anyway, because the rule is uniform and because the repository does not carry
source documents of any kind. Stating this keeps a later reader from inferring a copyright
constraint that does not exist here.

**Provenance is a two-step record and is written that way deliberately.** The copy first read on
16 August 2026 was an ephemeral session attachment that was removed from disk before it could be
stored. The user's own copy was then located and confirmed to be the same document by page count
(172), byte size (871,059) and verbatim spot-checks against passages read from the attachment. That
copy is the one hashed and indexed. The bibliographic record was taken from the file's own title and
copyright pages rather than from an independent catalogue entry, which remains weaker than this
project prefers and is the one open item on this source.

**Read in full, in two passes.** Section I, the meeting format, the glossary, the dedication of merit
and the fourteen personal recovery stories were read on 16 August 2026, and the selected meditations
and inquiry questions on 13 September 2026. The second pass found practice material only and no
governance text, so appendix A12's one absence claim, scoped to what had been read when it was made,
now holds over the whole book. The appendix still states the narrower scope, which remains true.

**On its `subjects_present`.** The index reports `chase`, `utica` and `washingtonian`. All three are
artifacts of the shared OCR-tolerant matcher over-including short tokens, the same limitation the
`TwelveAndTwelve_1953` note records. No chapter cites this source, so no pair is ever adjudicated
against it and the artifact is inert.

### Layout and what is committed

Every source now lives in one directory, `research/incorporated/<ShortAuthor>_<Year>/`, holding
the document, `citation.md`, `metadata.json`, `source_summary.md`, and a verification index. Loose
source files no longer sit directly under `research/`. Run `python3 tools/build_corpus.py` to
normalize the layout and rebuild indexes; it is idempotent, and `--check` reports drift without
changing anything.

**No source document is committed.** `.gitignore` excludes every `.pdf`, `.txt`, `.djvu` and
`.epub` under `research/incorporated/` and `research/staged/`. What is committed is the record: a
citation, the rights position, the provenance URL, the SHA-256 of each file, and a vocabulary-only
verification index. Three reasons. Several sources are in copyright and this repository is public.
The public-domain ones are large scans that are not project outputs and that dominated the
repository's size. And a checksum with a URL is a better provenance record than a copy, because it
can be checked against the original rather than trusted.

This resolves, for the whole corpus, the inconsistency the Maxwell entry below used to note: that
Kurtz was held as an index while everything else was held as text. Everything is now held as an
index, and the documents are local working files.

**How citation checking survives.** `tools/check_book.py` confirms that a chapter citing a source
for a subject is citing a work that actually contains that subject. Each index carries the source's
vocabulary and, because a vocabulary set has no word order, an explicit list of which registered
subjects the document contains, decided against the real text when the index was built and stamped
with that file's SHA-256. With no documents present at all, all 55 citation-subject pairs still
verify. If a document is re-acquired and its hash differs from the recorded one, the index is stale
and must be rebuilt rather than trusted.

Two limitations, stated rather than buried. The subject matcher is deliberately tolerant of OCR
noise, so short subjects can match spuriously; that was true when the check ran against full text
and is unchanged. And an index records that a word appears somewhere in a work, which is weaker
than a page reference. Quotations are still verified against page images, as the ATU and P-17
entries record.

The entries below remain authoritative for how each source was read and used.

---

## Obtained and read in full

**Maxwell, M. A. (1950). "The Washingtonian Movement." *Quarterly Journal of Studies on
Alcohol* 11: 410-452.**
**Saved as `incorporated/Maxwell_1950/Maxwell_1950.pdf`**
(349 KB, 29 sheets) with the original project text beside it as `.txt` (~17,600 words). Read in full. The scholarly anchor for Chapters 1,
2, 5 and 6, and by a wide margin the most-cited source in the book. Note the irony recorded
in Chapter 2: the paper circulates through AA-affiliated archives and repeatedly contradicts
AA's own published history.

**What is saved is a transcription, not a scan, and this matters.** The file is a retyped
reproduction with running footers reading "CHIPS on the WEB", not a facsimile of the
*Quarterly Journal of Studies on Alcohol*. It carries transcription errors, and four are
demonstrable from internal evidence:

| In this copy | Almost certainly | How it is known |
|---|---|---|
| "the early 1940's" | 1840's | the sentence is about the movement's rise |
| "conformed inebriates", "conformed drunkard" | confirmed | Maxwell uses "confirmed" elsewhere in the same passages |
| "(form 4.9 gallons)" | from | grammar |
| "Battleboro, Vt." | Brattleboro | there is no Battleboro, Vermont |

So every Maxwell citation in this book has now been machine-checked, but against a
transcription rather than against the journal. That is one remove, it is a shorter remove
than not checking at all, and it is stated in Chapter 1's notes on sources as well as here.
A page reference taken from this copy should not be trusted; it paginates as 29 sheets, not
as pp. 410-452.

**On copyright.** The article is from 1950 and is not public domain. An earlier version of this
entry said the file was stored here because "this folder is private." **That was wrong.** The
repository is public and has been throughout. The reasoning was sound and the premise was false,
which is the more dangerous of the two failures.

The file is therefore no longer committed. As of 9 August 2026 the treatment given to Kurtz has
been extended to the whole corpus: the document is a local working file, `.gitignore` keeps it out
of the repository, and what is published is the citation, the rights position, the SHA-256 and a
vocabulary-only verification index. The departure this entry used to describe no longer exists.

**What checking it changed.** Three things in Chapter 1, all small and all in the direction of
less precision than had been claimed:

- The chapter said Maxwell was precise about all three founding dates. He gives 2 April and
  5 April and then says the pledge was to be signed "the next day". Monday 6 April is
  arithmetic, not his statement.
- The chapter said the period's vocabulary distinguished "at least eight grades of drinker".
  Maxwell lists ten terms. The floor was true and the count is better.
- The chapter rounded Jellinek's consumption figure to "about fourteen per cent across the
  whole decade". It is 14.3 per cent, for ages fifteen and over, from a base of 4.9 gallons,
  between 1840 and 1850.

Everything else checked out. The pledge text, the six founders and their trades, the
membership fee of twenty-five cents and monthly dues of 12.5 cents, the two-thirds of 300 at
eight months, the anniversary parade of about 1,000 reformed drunkards and 5,000 others before
40,000 spectators, Mitchell's motto, the 23,340 signatures, Pittsburgh's 10,000, Cincinnati's
900 of 8,000, the Vermont 518 of 42,273, Hawkins joining on 14 June 1840 and speaking at
Annapolis in February 1841, the 600,000 figure's descent from the 1843 ATU Report, Marsh's
revisions to 4,000,000 and then 150,000, Jellinek's nine words about the missing ideology, the
"sheer survival value" passage and Maxwell's five-point comparison are all present and say
what the book says they say.

**A disclosure that should travel with every Maxwell citation.** Kurtz, writing in 1979,
describes Maxwell as *currently an A.A. trustee*. The book's principal scholarly source on
the Washingtonians was, at least by the late 1970s, a serving officer of the organisation
whose founding comparison he had assessed. That does not impeach the 1950 paper, which
predates the trusteeship and which repeatedly contradicts AA's own published account. It
does mean the book cannot describe him as a disinterested outsider, and Chapter 6's coda
already says he was not disinterested for a different reason.

*Superseded storage description.* An earlier note in this file described the source as a scan of
the original journal article. It is not; it is a retyping, as set out above. The description
was wrong for as long as it stood and is corrected here rather than deleted.

**Kurtz, E. (1979, expanded 1991). *Not-God: A History of Alcoholics Anonymous.* Center City,
Minn.: Hazelden. Chapter Five, further reading 2 August 2026.**

The first reading covered Chapters Two and Five for the Washingtonian material and the
founding. The second covered the composition of the Traditions and the 1937 professionalism
crisis, for the rewrite of Chapter 5. Nothing about the storage decision changes: the work is
in copyright, the full text is not kept here, and `incorporated/Kurtz_1991/Kurtz_1991_verification-index.json` holds
the vocabulary only.

What the second reading supplied, all of it new to the book:

| Subject | Where it lands |
|---|---|
| Membership about 2,000 in 1941, over 15,000 by 1945 | ch5 opening |
| The 1941 to 1945 problem stated as sharing experience without creating a central authority that would stifle it | ch5, and it is this book's Tradition 9 argument in AA's historian's words |
| The house style of Wilson's replies to group letters | ch5, quoted |
| Wilson's hesitation, and writer's cramp, scant staff and repetition overcoming it | ch5 |
| The seven matters he listed as settled by painful experience | ch5 |
| His disclaimer that a code of traditions could never become rule or law | ch5, and it corrected the chapter's central vocabulary |
| Long form April 1946; short form November 1949; adoption June 1950 | ch5, replacing a wrong adoption claim |
| "Nobody invented Alcoholics Anonymous. It grew. Trial and error has produced a rich experience." | ch5, quoted; it is the chapter's thesis in Wilson's own words |
| "Honest" dropped from Tradition Three in 1949 | ch5 |
| The 1937 Towns offer, the Clinton Street meeting and the group's reply | ch5, quoted at length |
| That meeting as Wilson's first encounter with the group conscience | ch5 |
| The December 1937 board room: attendance, the silence, Scott's two questions, Wilson going for broke | ch4, which had the sequence wrong |
| Two incompatible memories of why the fifty thousand dollars was refused | ch4, which now carries both |

**An internal inconsistency in Kurtz, recorded because it cannot be resolved here.** He cites
the April 1946 *Grapevine* publication twice with different details: as "Alcoholics Anonymous
Tradition: Twelve Points to Assure Our Future," *AAGV* 2:10 (April 1946), 7-9, and as the long
form in *AAGV* 2:11 (April 1946), 2-3. Same month, different issue, different pages. One is a
slip. The *Grapevine* itself is AA copyright and the 1946 issues have not been obtained, so the
conflict stands recorded in Chapter 5 rather than settled.

**A conflict with Maxwell, resolved in Kurtz's favour.** Maxwell dates the emergence of the
Traditions to 1947 and 1948, in *Grapevine* editorials and then a booklet. Kurtz dates first
publication to April 1946. Maxwell was contemporary; Kurtz had the files, and Maxwell's dates
fit the elaborating editorials and the 1947 booklet he was reading rather than the first
publication. Chapter 5 follows Kurtz and says why.

---

**Carrell, S. E., B. I. Sacerdote and J. E. West (2013). "From Natural Variation to Optimal
Policy? The Importance of Endogenous Peer Group Formation." *Econometrica* 81(3): 855-882.**

doi:10.3982/ECTA10168. **Read at source, 2 August 2026**, from the lead author's copy hosted at
the University of California, Davis. Earlier circulated as NBER Working Paper 16865 (March 2011)
under the title *From Natural Variation to Optimal Policy? The Lucas Critique Meets Peer
Effects*, and before that, per the NBER record, as *Beware of Economists Bearing Reduced Forms?
An Experiment in How Not To Improve Student Outcomes.*

**In copyright; the full text is not stored here.** Same treatment as Kurtz. What is recorded is
the four figures Chapter 22 uses, each taken from the paper's own text:

| Figure | Where it appears in Chapter 22 |
|---|---|
| Predicted gain of 0.053 grade points for the bottom third of the academic distribution | the prediction their own model made |
| Observed treatment effect of minus 0.061 on the lowest-ability students | the result |
| p = 0.055 on that effect | the significance |
| Design pairing roughly fifteen lowest-ability with roughly fifteen highest-ability cadets | the intervention |
| Homophily: low-predicted-grade students in treatment squadrons actively sought out other low-predicted-grade students | the mechanism |

**This unblocked Chapter 22**, which had been drafted at 762 words under an explicit instruction
in `plans/PART-5-PLAN.md` not to write it at full length without this paper. It is now 1,297
words and the paper carries it.

**One acquisition attempted on 2 August 2026 and not obtained. The other has since been read.**

*Pagano, M. E., K. B. Friend, J. S. Tonigan and R. L. Stout (2004).* **Obtained and read in full
on 10 August 2026**, as the NIH author manuscript, PMCID PMC3008319, supplied by the project's
author after automated retrieval was blocked by a challenge page. Stored in
`research/incorporated/Pagano_2004/`. Reading it settled the sourcing question Chapter 15 had
flagged against itself: the 40 against 22 per cent figures, previously taken from a 2011 news
release, appear in the paper's own results section, and the independence from meeting attendance
is established there by proportional-hazards regression controlling for meetings attended. It
also supplied a limitation the news release did not carry, and which now appears in Chapter 15:
the authors' first stated limitation is that only 8 per cent of the sample were coded as helping,
on a measure they call crude. **Chapter 15's sourcing is no longer the weakest in the book.** The
copy held is the author manuscript, so its pagination is not the journal's.

*Greenfield, B. L. and J. S. Tonigan (2013).* **Obtained and read in full on 10 August 2026**, as
the NIH author manuscript, PMCID PMC3707937, supplied by the project's author after automated
retrieval was blocked by a challenge page. Stored in
`research/incorporated/Greenfield_Tonigan_2013/`. The staged record's citation was wrong in two
places, giving 27(2): 553-560 where the article reads 27(3): 553-561, and is corrected here and in
the manuscript.

Reading it confirmed rather than corrected what Chapters 13 and 24 had taken from the abstract:
the two-factor structure of step-work, the differing predictors and time paths of the two factors,
spiritual step-work predicting percent days abstinent where behavioural step-work did not, and the
instrument disagreement on nine of twelve steps. What it added is scale and design, 130 affiliates
over nine months, observational, which is now stated beside the findings.

It also supports a caveat the project had been making on its own authority, that the practice scale
corresponds to no validated instrument, and it raises an objection the project cannot answer: the
model gives each step one practice level, while this study finds step-work is at least
two-dimensional with only one dimension predicting outcome. Chapter 12 states the objection. No
sensitivity design here can reach it, because every design varies the values of the dials rather
than the decision to have one dial per step. The copy held is the author manuscript, so its
pagination is not the journal's.

*Alcoholics Anonymous World Services, SMF-132, "Estimated Worldwide A.A. Individual and Group
Membership,"* Rev. 12/20. **Read in full at source on 17 August 2026** from the fellowship's own
free posting, and held under `research/incorporated/SMF132_2020/`, record only until 13 September 2026 and a
git-ignored copy since. It is the
group-and-member series by year that Chapter 21 proposes as the starting point for an
out-of-sample test, and it now supplies one. Dividing reported members by reported groups gives
18.4 members per group on average across 2001 to 2020, ranging from 16.5 to 22.1 and falling
steadily; the model's endpoint membership at full adherence is 17.80 [16.92, 18.68]. **Read that
as a consistency check and not a validation.** AA keeps no membership lists, the figures are
reports from groups registered with general service offices, and a ratio of two estimated
aggregates is not a sample of group sizes: it carries no interval and describes no distribution.
The series is also worldwide rather than regional, so the natural experiment Chapter 21 wants
still needs finer data. **Superseded wording:** this entry previously said the source was located
and not acquired, and before that that the project does not acquire AAWS publications on the
book's behalf. Neither is now the case.

*W., Bill, The Twelve Concepts for World Service (Short Form), SMF-114, adopted 1962.* **Read in
full at source on 17 August 2026**, held under
`research/incorporated/TwelveConcepts_1962/`, record only until 13 September 2026. This was listed for months as the place where the
fellowship's own thinking about rotation is set out at greatest length, and unread. It is now
read, and the finding is a narrowing rather than a confirmation. Concept 4, the Right of
Participation, asks for voting representation in reasonable proportion to the responsibility each
element of the structure discharges, so AA does hold a proportionality principle about service.
It proportions voting weight to responsibility, not the rotating pool to the size of the group,
and a structure could satisfy it exactly while rotating twelve people through a fellowship of
eight hundred. Supports Chapter 10 and the primer's Tradition 9 entry. The long-form Concepts and
their essays were read on 13 September 2026 in `ServiceManual_2024`, below.

*Alcoholics Anonymous World Services, The A.A. Service Manual Combined with Twelve Concepts for
World Service by Bill W., 2024-2026 edition (BM-31).* **Read in part on 13 September 2026**: Concepts
IV and V in full, Concept XI on rotation, and every passage in the manual mentioning rotation.
Posted free by A.A.W.S. on its own file host and held git-ignored under
`research/incorporated/ServiceManual_2024/`. It closes the Concept 4 item that `HANDOFF.md`
section 10 carried as needing a purchase. **The Concept IV essay holds no rule about the size of a
rotating pool**: it is about voting participation in proportion to responsibility among trustees,
service directors and staff. Rotation doctrine sits in Concept XI, which ties term length to
responsibility and warns against attempting more rotation than that, and Concept V defends the
well-heard minority against a hasty majority. A 1962 prescription for the world service
structure, not evidence about how home groups rotate. Supports Chapter 10.

*Alcoholics Anonymous World Services, Alcoholics Anonymous, Fourth Edition (2001).* **Read in part
at source on 17 August 2026**, held under `research/incorporated/BigBook_2001/`, record only until 13 September 2026 and since
then a git-ignored copy assembled from the per-section PDFs aa.org posts.
Supplied by the Human Author, who owns several copies; AAWS also posts the book in per-section
PDFs. Title page, copyright page, contents and all three parts of the personal stories were read;
the programme chapters were not, being unchanged from 1939 and covered by `BigBook_1939`. Supports
Appendix A13.7, which repeats the 1939 arrival census on the forty-two stories of this edition:
thirteen member-initiated, six subject-initiated, eleven professional or institutional, twelve
unresolved and reported as unresolved. Member-initiated arrival is 43 per cent of the classifiable
stories against 77 per cent in 1939. **Neither census is a sample**: the stories are selected by
the fellowship for publication and selection on outcome is total.

*The Book That Started It All: The Original Working Manuscript of Alcoholics Anonymous.* Center
City, Minn.: Hazelden, 2010. **Read in full on 12 September 2026**, every facsimile page, from
photographs the Human Author took of their own copy, and held under
`research/incorporated/WorkingManuscript_1939/` as a git-ignored reading copy with its OCR text, at
the Human Author's direction. It was the first in-print copyrighted work in the corpus held rather than
record only. The facsimile is of the multilith copy onto which the comments on the February 1939
draft were collated, so read against `BigBook_1939` it shows both what was circulated and what
changed before print. Step 3's "as we understood Him" is already typed; Step 11's is written in by
hand; the "choose your own conception of God" episode in Bill's Story is a handwritten insert that
the circulated draft did not contain. Second-person instruction is recast as first-person report,
usually keeping the modal, so **Chapter 4's "you must" to "we ought" is not what the pages show**;
Chapter 4 was corrected on 13 September 2026, with each quotation checked against the page images.
Collective "group" language is taken out; the Foreword's anonymity, no-fees and single-requirement
statements are already typed, beside a proposed trust with a permanent non-alcoholic majority; and
ten of the printed stories are absent from the draft. The only numbers it supplies are early-1939
meeting sizes as members reported them, a consistency check on the model's room capacity and not a
validation. **Hazelden's essays are secondary and anonymous**, and what they report from AA's own
histories is cited at a remove. The full account and suggested uses are in
`edits_and_suggested_uses.md` in the source directory.

*Jensen, Karen, and Matthew Abrahams, "Buddha Buzz Weekly: Refuge Recovery Splits," Tricycle: The
Buddhist Review, 13 July 2019.* **Read in full at source on 17 August 2026**, held as record only
under `research/incorporated/Tricycle_2019/`. The independent account of the 2019 schism that
Appendix A12.4 previously lacked, everything there having come from the successor fellowship's own
literature. It confirms the structure from outside and corrects the contrast: both organizations
describe their meetings as peer-led and democratically run, and what separates them is the layer
above the meeting, teacher-led retreats and professional treatment on one side and nothing above
the sangha on the other. The article names the predecessor's founder; this project does not, and
`tools/check_book.py` fails the build if the name appears.

---

**Golub, B., and M. O. Jackson (2010). "Naive Learning in Social Networks and the Wisdom
of Crowds." *American Economic Journal: Microeconomics* 2(1): 112-149.**
The theorem underlying all of Part Two. Read at source. The author-hosted PDF, OCR and
provenance record are saved at `research/incorporated/Golub_Jackson_2010/`.

**DeGroot, M. H. (1974). "Reaching a Consensus." *Journal of the American Statistical
Association* 69(345): 118-121.**
The updating model in Chapter 7. Read at source.

**Holmström, B. (1982). "Moral Hazard in Teams." *Bell Journal of Economics* 13(2):
324-340.**
The budget-breaker impossibility applied to Tradition 7 in Chapter 5.

**Iannaccone, L. R. (1992). "Sacrifice and Stigma." *Journal of Political Economy* 100(2):
271-291.**
The club-good theory of costly screening, used in Chapter 2 to explain why the Sons of
Temperance should have beaten the Washingtonians, and did.

**Marsh, J. (1866). *Temperance Recollections: Labors, Defeats, Triumphs. An Autobiography.*
New York: Charles Scribner & Co.**

**Saved here as `incorporated/Marsh_1866/Marsh_1866.txt`** (862 KB, ~128,800 words). Public
domain. Retrieved from the Internet Archive scan of the New York Public Library copy,
identifier `temperancerecoll00mars`, plain text.

Acquired 2 August 2026 and it changed two chapters. Marsh was Corresponding Secretary of
the American Temperance Union for thirty years and editor of the Annual Reports on which
the entire decline chronology rests, so this is a participant document, not a historian's.
Everything below had previously reached the book through Maxwell.

Offsets are into the whitespace-normalised text, which is how the passages are located:

| Offset | Passage |
|---|---|
| 188,562 | The Connecticut convention resolving for prohibition, with the parenthesis *for a great change had come over the Washingtonians in this matter* |
| 246,648 | Lyman Beecher to Marsh, Cincinnati, 21 January 1845, in full: the Washingtonians' *thunder is worn out*, the *novelty of the common-place narrative is used up* |
| 341,795 | The churches *in a measure set aside* by the movement and its successor orders |
| 342,456 | American Temperance Union Ninth Report, 1845, on the reform languishing without church support |
| 420,699 | The movement *finished its course, and its fruits were gathered into new organizations*; the rise of the Sons of Temperance |
| 421,139 | Marsh not a member of the Sons, *not being a reformed man*, and preferring open organisations |
| 624,387 | The founding scene from the eleventh annual report of the Maryland State Temperance Society, naming Elder Knapp, and the note that the account was later denied |

**A conflict this source creates rather than settles.** Marsh's founding account names the
preacher as Elder Knapp and has four of the six attend; Maxwell has Matthew Hale Smith and a
single delegate. Both are retrospective and descend from different Baltimore informants.
Recorded in Chapter 1's notes on sources; not resolved.

**Grosh, A. B., comp. (1842). *Washingtonian Pocket Companion: containing a choice
collection of temperance hymns, songs, &c. With brief directions for commencing, organizing,
and conducting the meetings of Washingtonian Temperance Societies; and for the private action
of Washingtonians.* Second edition. Utica, N.Y.: B. S. Merrell.**

**Saved here as `incorporated/Grosh_1842/Grosh_1842.txt`** (193 KB, ~33,400 words)
with the scanned page images as `incorporated/Grosh_1842/Grosh_1842.pdf` (22.8 MB).
Public domain. Harvard copy, digitised by Google, from HathiTrust,
https://hdl.handle.net/2027/hvd.32044004487591. Supplied by the author of this book after an
earlier search failed; the note in this file predicting that it would most sharpen or most
damage the thesis has been left in the history rather than deleted, because it turned out to
be right in both directions.

**This is the single most important acquisition in Part One.** It is the movement's own
statement of how a Washingtonian society should be started, organised and run, written by a
Washingtonian compiler in the movement's own lifetime, with no knowledge of and no interest
in anything AA would later say about it. It is the direct counterpart to the Twelve
Traditions and it is uncontaminated by the curation problem that affects every other
accessible account.

Structure: about fifteen pages of prose at the front, then something over two hundred pages
of hymns and songs. The prose is what matters and it is short enough to read at a sitting.

Printed page numbers, which are marked in the plain text and match the page images in the
PDF. Offsets are into the whitespace-normalised text, as in the Krout entry.

| Page | Offset | Passage |
|---|---|---|
| 4 | 6,921 | Definition of principles, paragraph I: Washingtonianism embraces all classes, sexes, ages and conditions, aims to cure as well as prevent, and works through the sisters to enlist the inebriate's family |
| 5 | 7,879 | Paragraph II: the old societies were auxiliary to county, state and national bodies, whose agents imposed political and religious views; Washingtonianism makes each society independent, funds and actions under members' control, subordinate to none, and bars anything inimical to any party or denomination from periodicals, lectures, meetings or proceedings |
| 6 | 10,701 | Paragraph III: the old societies denounced; Washingtonianism adopts the law of kindness and disavows compulsion, threats and denunciation |
| 7 | 11,330 | "Moral suasion, not force-love, not hate, are the moving springs in the Washingtonian Creed" |
| 7 | 11,539 | Directions I, the commencement: chairman and secretary, preferably reformed inebriates; experience first, then the pledge |
| 8 | 13,250 | "Publicity and freedom are preferable to private solicitations, whisperings, and secresy in giving the names"; the roll called back so nobody is missed; THE CHARGE |
| 8 | 14,252 | Directions II, the organisation: the model constitution's nine articles, including Article 2 on moral suasion, Article 3 forbidding sectarian sentiments and party politics in any lecture, speech, singing or doing of the society, Article 4 on officers and committees, Article 9 on labours with pledge-breakers and withdrawal of members |
| 9 | 15,931 | Footnote: the Washingtonian mass convention at Utica, 22 February 1842, passed a declaration of principles and a constitution for the adoption of all Washingtonian societies; printed in the *Utica Washingtonian* of 25 February and reprinted 28 October and in extras because of demand |
| 10 | 16,561 | Officers elected, always preferring reformed inebriates as far as possible and consistent |
| 10 | 16,793 | Directions III, conducting the meetings: as many experiences as possible, kept brief |
| 10 | 18,017 | The president must call a transgressing member to order and he should sit down |
| 11 | 18,261 | Advice to Washingtonians: contribute to the society's funds and to relief of poor members and of the families of unreformed inebriates |
| 11 | 19,598 | Visit the man who breaks his pledge, and afterwards forget the violation |
| 12 | 19,872 | Differences between societies: some require prior drinking within a year, some exclude children, some require renouncing membership of other temperance societies |
| 13 | 22,599 | The female members act as a benevolent society within the society, or form separate societies |
| 14 | 23,276 | The two pledges, Baltimore and Utica |

**What it establishes, first-hand.** That the Washingtonians had written analogues of
Traditions 4, 7 in part, 9 between societies, and 10, in print within two years of founding
and circulated by a convention and a newspaper. That they had no analogue of Tradition 2:
elected officers, a president with the power to end a member's speech, and no rotation. That
they took the opposite position to Tradition 12 deliberately and with an argument. And that
the porous boundary Maxwell identifies as the cause of absorption was doctrine rather than
drift.

**What it does not establish.** How widely the model constitution was adopted, or what any
society actually did. It is prescriptive. Its own section on differences is the evidence that
practice varied, and that section is the reason to trust the rest of it: a manual willing to
record how much its societies disagree is not concealing much.

**A caution on edition and provenance.** This is the second edition, from Utica, compiled by
a man who was not one of the Baltimore six. It is the movement's manual, not Baltimore's
minute book, and the Baltimore practices in Chapter 1 continue to rest on Harrison, Marsh and
Krout.

---

**Krout, J. A. (1925). *The Origins of Prohibition.* New York: Alfred A. Knopf.**

**Saved here as `incorporated/Krout_1925/Krout_1925.txt`** (796 KB, ~110,800 words). Public
domain. Internet Archive identifier `originsofprohibi0000krou`, plain text.

The first scholarly history of the American temperance movement, written twenty-five years
before Maxwell and wholly independent of him, which matters because until now almost all of
Part One rested on a single 1950 paper. Chapter IX, "The Washingtonian Revival", pp.
182-222, read in full.

Offsets into the whitespace-normalised text:

| Offset | Passage |
|---|---|
| 367,771 | Chapter IX opens; the movement as reformed drunkards addressing a class reformers had written off |
| 370,670 | The founding from the Maryland State Temperance Society's 1842 annual report: pledge text, officers, twenty-five cent fee, twelve-and-a-half cent dues, bring-a-friend, the rejected Jefferson name |
| 372,109 | Mitchell's rule: the Baltimore society admitted no outside speakers unless they came to relate their experience as reformed men, and the standard for other societies was thereby set |
| 420,894 | The first fundamental weakness: no connection between societies, centralised control considered too great an infringement, so systematic organisation was impossible and **chance largely determined the formulation of principles** |
| 422,359 | The founding motive of the Sons of Temperance: the movement not properly organised to retain the fruits of its victories, desertions numerous, the need for a body that would hold members after the first enthusiasm had spent itself |
| 422,889 | Sons of Temperance founded at Teetotalers' Hall, 71 Division Street, 29 September 1842 |

**What it changed.** Chapter 1 gains Mitchell's speaking rule, which is a Tradition in
function and which the chapter had missed; the corroboration of the founding details from a
second independent reading of the 1842 report; and a sharper account of why the practice did
not survive, namely that it spread by imitation and nothing obliged anyone to keep it.
Chapter 2 gains the two contemporary structural weaknesses, the first of which is this
book's thesis stated in 1925 by a historian who had never heard of Alcoholics Anonymous.

**Eddy, R. (1887). *Alcohol in History: An Account of Intemperance in All Ages, together
with a History of the Various Methods Employed for Its Removal.* New York: The National
Temperance Society and Publication House.**

**Saved as `incorporated/Eddy_1887/Eddy_1887.txt`** (~173,200 words). Public domain, Internet
Archive `alcoholinhistor00eddygoog`, Google scan. **The optical character recognition is
poor**: Mitchell appears variously as Mitrhell, Mituhell and MitrLell on a single page, and
`tools/check_book.py` matches source terms with tolerance for this.

Supplied by the author 2 August 2026. What it gives at first hand:

- **The founding of the Sons of Temperance**, including the motive (a more perfect
  organisation, one that *should shield the members from temptation, and more effectually
  elevate and guide them*), the call of Thursday 29 September 1842 sent to some forty
  prominent Washingtonians, the sixteen who attended, and the terms: initiation one dollar,
  dues six and a quarter cents a week, four dollars a week in sickness, thirty dollars for
  a funeral. Chapter 2 previously attributed this to Crothers, wrongly.
- **Mitchell on the liquor traffic**, quoted from Dr Jewett, who spoke from personal
  knowledge: Mitchell held that as Washingtonians they should have nothing to say against
  the traffic or the men in it, would have no pledge against manufacture or sale, would
  admit sellers to membership, and admitted having bought liquor at the bar for others
  after signing the pledge.
- **The judgement that Washingtonianism was not irreligious**, with the detail that
  chaplains opened meetings and reformed men joined churches, some becoming eminent in the
  ministry.
- **Eddy's own decline account**, which is close to Beecher's: it stopped because it had
  reached the limit of the exclusive means it employed. And his verdict that it was not a
  failure, having rescued thousands and opened the way for more advanced work.

**Crothers, T. D. (1911). *Inebriety: A Clinical Treatise on the Etiology, Symptomology,
Neurosis, Psychosis and Treatment.* Cincinnati: Harvey Publishing.**

**Saved as `incorporated/Crothers_1911/Crothers_1911.txt`** (~105,700 words). Public domain, Internet Archive
`inebrietyclinica00crot`. Supplied by the author 2 August 2026.

**Acquiring it corrected a citation rather than supporting one.** Chapter 2 had cited
Crothers for the founding rationale of the Sons of Temperance. **He does not mention the
Sons anywhere in the book.** The misattribution was caught within minutes by the new
`sources` check in `tools/check_book.py`, which was written the same day and found it on its
first run. Corrected to Eddy.

What Crothers does supply, and Chapter 2 now uses:

- **Five million pledges between 1840 and 1845**, followed immediately by the concession
  that of those, *a certain unknown number* remained abstainers for life. A sympathetic
  physician, writing seventy years later with every reason to want a figure, says he has
  not got one.
- **The medical line of descent.** Lodging houses for men who had broken their pledges
  became the beginning of the hospital system of cure; one opened in Boston in 1857 grew
  into the Washingtonian Home, by 1911 among the oldest institutions in the world for the
  physical care of inebriates. The movement's residue went into medicine as well as into
  the fraternal orders.
- **His summary judgement**, that the movement was a clearing house which broke up old
  theories and concentrated public attention on what inebriety was, and then receded.

**Harrison, D., Jr. (1860). *A Voice from the Washingtonian Home: Being a History of the
Foundation, Rise, and Progress of the Washingtonian Home, an Institution Established at
No. 36 Charles Street, Boston, for the Reformation of the Inebriate; Also, a Review of Some
of the Evils of Intemperance in England, Together with a Sketch of the Temperance Reform in
America.* Boston: Redding & Co.**

**Saved as `incorporated/Harrison_1860/Harrison_1860.txt`** (~99,100 words). Public
domain, Internet Archive `voicefromwashing00harr`. Supplied by the author 2 August 2026.

**This is the origin of the founding scene**, the text Maxwell quotes and every later
retelling descends from. Reading it directly corrected three things in Chapter 1:

- **The preacher is unnamed.** Harrison says only that a clergyman preaching in the city had
  given public notice of a discourse on temperance. Maxwell's Matthew Hale Smith and Marsh's
  Elder Knapp are both later attributions to a silence.
- **Four of the six went**, not one. This agrees with Marsh's source and against Maxwell.
- **The pledge was written Monday morning**, not on the Sunday walk. What happened on the
  walk was the agreement to draft one.

It also supplies *between walking and treating*, the six men's trades, and the Anderson
signing in full. **A calibration on its reliability:** Harrison dates the tavern evening to
"Friday evening, the second of April, 1840". The second of April 1840 was a Thursday.

**Hawkins, W. G. (1862). *Life of John H. W. Hawkins.* Compiled by his son. Boston: Briggs
and Richards. Sixth thousand.**

**Saved as `incorporated/Hawkins_1862/Hawkins_1862.txt`** (~143,000 words). Public domain,
Internet Archive `LifeOfJohnHHawkins`. Supplied by the author 2 August 2026.

**Edition warning, and it matters.** This is the 1862 Briggs and Richards printing. The
edition usually cited, and the one Maxwell used, is the earlier Jewett printing. **The two
have not been collated.** Chapter 1 cites what was actually read and says which it is; a
page reference checked against Jewett should be expected to differ.

Gives Hawkins's platform account of 12 June 1840 verbatim: the quart and a pint a day
through the first two weeks of June, the daughter's *I hope you won't send me for any whisky
to-day*, *I suffered all the horrors of the pit that day*, and his wife saying *hold on,
hold on*. The wife's part is absent from the versions that circulate, which credit the
daughter alone.

**A date conflict it creates.** Maxwell has Hawkins signing on 14 June 1840. Hawkins says
the crisis was the 12th, that he felt better the next day, and that he signed on the Monday.
The 12th was a Friday, so his Monday is the 15th; the 14th was a Sunday. Unresolved, and
Chapter 1 now says the middle of June.

**Blair, H. W. (1888). *The Temperance Movement; or, The Conflict Between Man and Alcohol.*
Boston: William E. Smythe.**

**Saved as `incorporated/Blair_1888/Blair_1888.txt`** (~240,400 words). Public domain,
Internet Archive `temperancemoveme00blai`. Supplied by the author 2 August 2026.

Blair was a United States senator and the author of a proposed prohibition amendment, so he
is a hostile witness with a legislative motive, which is what makes the passage worth having
whole rather than as the one clause usually quoted. He allows a hundred and fifty thousand
reformed men saved, asks what that is among so many, and then charges the Washingtonians'
opposition to legal restraint with demoralising public sentiment and so with the four hundred
and fifty thousand *who fell and perished*. The maudlin insanity line is the end of that
sentence, not a stray insult. He also recites the six hundred thousand figure Chapter 1
shows cannot be supported.

**Fehlandt, A. F. (1904). *A Century of Drink Reform in the United States.* Cincinnati:
Jennings and Graham.**

**Saved as `incorporated/Fehlandt_1904/Fehlandt_1904.txt`** (~78,300 words). Public domain,
Internet Archive `centuryofdrinkre00fehl`. Supplied by the author 2 August 2026.

Useful as the received view Maxwell was correcting rather than as evidence in its own right:
*By 1843, however, interest began to wane, and soon Washingtonianism had spent its force.*
Maxwell's regional evidence shows that is both too early and too uniform. Fehlandt also has
the Martha Washington Societies and Lincoln's Springfield address, and notes Hawkins
labouring until his death in 1858 having visited every state but California.

**Fatimah, H., M. D. Hunter, and M. A. Bornovalova (2025). "Modeling the Dynamics of
Addiction Relapse Via the Double-Well Potential System." *Journal of Psychopathology and
Clinical Science* 134(1): 69-80.** doi:10.1037/abn0000960.

**Saved as `incorporated/Fatimah_2025/Fatimah_2025.txt`** (~10,400 words). NIH author manuscript,
public access. Supplied by the author 2 August 2026. Model code deposited at osf.io/tkg9s;
study protocol at osf.io/kysdt.

**This is now the strongest external evidence in the book, and it was not on the acquisition
list.** It supersedes Hufford (2003) as the empirical warrant for Chapter 14.

The double-well potential model treats post-treatment substance use as a dynamical system
with two stable equilibria, use and non-use, and a continuous latent state that occupies one
well and can be pushed into the other. Fitted to timeline followback data from N = 139 adults
with a substance use disorder returning to the community after residential treatment, using
the `dynr` package.

What it gives Chapter 14:

- **Two fitted attractors, not two assumed ones.** The parameters carry information beyond
  the standard metrics: steepness and relapse risk predicted life satisfaction and criminal
  behaviour at long follow-up **over and above proportion of days used and time to first
  use**.
- **Separation energy, asymmetric by direction.** The disturbance needed to move from
  abstinence to relapse differs from the disturbance needed to move back. That is Chapter
  14's separatrix and its hysteresis, arrived at from data.
- **Significant between-subject variance in steepness and relapse risk**, predictable from
  demographics, baseline psychopathology and treatment history. This is the empirical
  counterpart of `het_sd`, the least defensible parameter in the model, and it is the single
  most useful thing in the paper for this project.
- They note the double well's advantage over the cusp catastrophe and regime-switching
  models: the separation energy yields an individualised relapse risk, which those do not.

**What it does not give, stated because the temptation to over-read it is real:**

- **Their object is not this model's object.** They model substance use behaviour. This model
  places bistability in maintenance capacity, the mean of Steps 10 to 12. Nobody has fitted a
  double well to step practice.
- **Their model is descriptive; this one is generative.** They fit a landscape to observed
  behaviour and read its parameters. This model derives a landscape from a claimed mechanism,
  that maintenance gates its own recovery. A different mechanism producing the same landscape
  would fit their data equally well. The paper supports the shape and is silent on the
  mechanism.
- **Their sample is not an AA meeting.** Criminal-justice-involved, largely polydrug, leaving
  residential treatment, about a quarter from minoritised groups. Their own limitations
  section notes the retrospective timeline followback gives weekly rather than daily
  resolution over long windows.
- **Non-use was the predominant stable state.** Most people's landscape tilts toward staying
  well. The two wells exist and are not of equal depth, and Chapter 14 now says so.

**Kurtz, E. (1979; expanded edition 1991). *Not-God: A History of Alcoholics Anonymous.*
Center City, Minn.: Hazelden.**

**IN COPYRIGHT. The full text is deliberately NOT stored in this repository.** The copyright
page carries an all-rights-reserved notice. Supplied by the author as an epub on 2 August
2026, converted to PDF and kept outside the repository; read in full, ~185,500 words.

What is stored is `incorporated/Kurtz_1991/Kurtz_1991_verification-index.json`, a vocabulary index with no running
text. It exists so `tools/check_book.py` can confirm that a cited subject appears in the
work without the repository holding a redistributable copy. **This follows the precedent
used for other in-copyright sources. Maxwell 1950 is also read in full, but unlike Kurtz its
retyped reproduction and text are saved privately under research/incorporated/Maxwell_1950/.
Each source that is not record-only keeps one text file beside its document, so the twenty-eight
sources holding a document carry one transcription or OCR file apiece and the five record-only
entries carry none. All of them are git-ignored, so a fresh clone has none of them and that is
not drift. Their individual rights and reliability differ and are stated in their entries.

**The single most valuable thing it contains, for this book:** the folk account of the
Washingtonians' death has an author, a date and a motive. Kurtz tracks it to Bill Wilson's
article "Modesty One Plank for Good Public Relations", *A.A. Grapevine* 2:3, August 1945,
pp. 1 and 4, prompted by a member's piece the previous month (C.H.K., "History Offers Good
Lessons for A.A.", *AAGV* 2:2, July 1945, p. 3). Wilson credits the movement with about a
hundred thousand alcoholics helping each other stay sober, laments that its influence had so
completely disappeared that few of us had ever heard of it, and lists four flaws. Kurtz says
Wilson was *explicitly conscious of seeking support for the Traditions he was formulating*.
The article ran eight months before the Traditions were published. Between 1945 and 1976 the
*Grapevine* carried twelve separate articles on the Washingtonians. Now the opening of
Chapter 2.

**A terminological finding that bears on Part Four.** Kurtz's note 16 to Chapter Five records
that in some later AA literature the concept properly conveyed by *single-purposed* was
obfuscated by substituting *unity* as its supposed exact equivalent, and that after Wilson's
death AA itself at times fell into this. Chapter 17 is planned around Tradition 1 (unity)
coming out as the most load-bearing in the derived coupling, with Tradition 5 (single
purpose) close behind. If the two terms were historically conflated, that finding needs
re-examining before the chapter is written. Flagged in `plans/PART-4-PLAN.md`.

**Chapters 4 and 5 material now first-hand**, though not yet fully worked in: the failed
Akron proxy fight of early May 1935; Wilson pacing the Mayflower Hotel lobby on Saturday 11
May, the day before Mother's Day, with the bar at one end and the church directory at the
other; *God, I am going to get drunk*, and the panic that followed it; Dr Bob Smith's last
drink and rounds of restitution on 10 June 1935, recorded in AA's own "Landmarks" as the
founding. Kurtz names four founding moments rather than one.

**Also relevant:** Kurtz describes Maxwell as *currently an A.A. trustee*, which is recorded
above under Maxwell.

---

## Obtained, read in two passes

The four sources in this section were entered as partly read and finished on 13 September 2026.
They stay here rather than moving, so that what each first pass covered, and what it supported,
remains visible beside what the second pass found.

**Recovery Dharma Global (2023). *Recovery Dharma: How to use Buddhist practices and principles to
heal the suffering of addiction.* Second edition. Recovery Dharma Inc. 172 PDF pages.**

Stored in `research/incorporated/RecoveryDharma_2023/` with PDF, extracted text (57,419 words),
citation, metadata and verification index. CC BY-NC-SA 4.0. Read 16 August 2026 at the user's
direction, to test whether the group model can speak to a fellowship organised on Buddhist rather
than Twelve Step lines.

Read on 16 August 2026: the contents and front matter through The Practice (ix to xvi); the whole of
Section I (1 to 54); the whole of Section II, the fourteen personal recovery stories (57 to 121); and
from Section III the glossary (145 to 146), the meeting format (147 to 151) and the dedication of
merit (152). **Read on 13 September 2026:** the selected meditations (122 to 135) and the inquiry
questions (136 to 144), the only pages left. They are practice material rather than description:
guided meditations, and inquiry prompts on the Four Noble Truths, the path factors, the precepts and
amends. They contain no governance, decision-procedure or group-conscience text and do not mention
Twelve Step programs. The whole book is now read.

**A first pass got the central question wrong and the record keeps how.** That pass read Section I
and the meeting format, skipped the stories, and concluded the fellowship had no Traditions
equivalent. It was wrong twice: the meeting script already contained a group-conscience analogue in
the affirmation of trust in the Sangha, and the unread stories contained the fellowship's founding
history. Reading Section II corrected both and produced the finding the manuscript now cites.

Supports appendix A12 and four paragraphs of Chapter 24. Specifically: the program's seven
enumerated lists and their thirty-five items; the sangha as a group-conscience analogue; the absence
of any written decision procedure, established by mechanical search of the full text; the 2019
schism from Refuge Recovery and the peer-led commitment adopted in response to it; the
overwhelmingly exogenous arrival channels reported across the fourteen stories; and members' own
statements that the Eightfold Path is not worked in sequence.

**One handling rule.** The founder of the predecessor organization is named in this source in
connection with its collapse. The project does not name him anywhere. The structural claim does not
need the name and nothing here can adjudicate an allegation about a living person.

**What it cannot support.** Nothing about what Recovery Dharma groups do, no outcome, and no
effectiveness comparison with AA. It also cannot support a derivation claim in either direction: the
Eightfold Path predates the Twelve Steps by roughly two and a half thousand years, and the book
presents its program as an application of early Buddhist teaching. The absence claim that the
fellowship has no Traditions-equivalent charter was scoped, when made, to the table of contents,
Section I and the Section III appendix, where a charter would be a listed item. Since the pages then
unread were read on 13 September 2026, it holds over the whole book. Appendix A12 and the primer
still state the narrower scope, which remains true; widening it waits for the next rebuild of the
book and primer.

**American Temperance Union (1841). *Annual Report of the American Temperance Union.***

Stored in `research/incorporated/ATU_1841/` with PDF, OCR,
citation and metadata. Public domain, pre-1929. Internet Archive scan `annualreportamer00amer_5`.
84 PDF pages.

Read for its Washingtonian material, principally the Appendix at printed page 39, which is the
earliest contemporary institutional account the project holds and is independent of Harrison
(1860), of Maxwell (1950), and of the 1842 Maryland state report that Krout used. The quoted
sentence was verified against the rendered page image; the OCR matched it exactly, but the OCR is
a search aid and the page image is the authority.

Supports, in Chapter 1: the founding date of 5 April 1840; six men; a public tavern; a simple
total-abstinence pledge; the society's name; growth past one thousand members within the year;
the rule that at successive meetings *each man to bring a man*; and meetings working through *a
public relation by each individual of his own experience and history*. The last two are
contemporary descriptions of practice, corroborating Krout's bring-a-friend agreement a year
earlier and from a different organisation. They are not evidence that those practices caused the
growth, and nothing in this source bears on Part Two.

**Read in full on 13 September 2026.** The remainder is national temperance-movement business: state
society reports, crime and consumption statistics, and correspondence. It is an institutional
self-presentation throughout, so its numbers carry the movement's own interest in them. None of what
follows is used in the manuscript. Each item is candidate material, and a quotation should be checked
against the page image before use, except the treasurer's account, which has been.

- *The mechanism, as the movement stated it in 1841.* Of the 12,000 drunkards the American
  Temperance Society reported reformed by 1835, the report says "there was no associated action
  among themselves for countenance and support", and they "went back by scores to destruction".
  Baltimore's thousand reformed men came "without any special agency excepting their action one
  upon another" (printed pp. 14 to 16). Dr Reese's "Plea for the Intemperate" in Appendix C has
  them "each helping the other to do what neither is able to do for himself", with their vigilance
  over one another "a barrier against a relapse". Bears on Chapters 1 and 4.
- *Meeting rules, first-hand.* John Hawkins at Faneuil Hall in May 1841 (Appendix C): meetings every
  night; "We would have no sectarianism, no politics or arguments. Whoever ventured upon either was
  made to take his seat; he must tell his own experience, and not another's"; rum-sellers may take
  the pledge and join; the reformed "are all missionaries". The earliest statement the corpus holds
  of a no-outside-issues rule enforced at the meeting itself. Bears on Chapters 1 and 11.
- *One patron.* The treasurer's account for 1840 (printed p. 33, verified against the page image):
  receipts of $10,666.52, of which $5,000.00 is the "Residue of Mr. Delavan's donation", 47 per
  cent. The next largest gifts were $100. The report says the $10,000 gift "has now all been
  expended" and that the Union "must now look to other friends for support". Bears on Tradition
  Seven.
- *An autonomy clause from 1833.* Appendix E reprints the American Temperance Society's plan: each
  society "is independent of all others, except so far as each may choose for mutual benefit ... no
  one society having power to dictate to another, or to control its operations" (printed p. 56). A
  Tradition Four antecedent in the predecessor movement's own constitution, worth setting against
  Chapter 11.
- *Membership by payment.* The British and Foreign Temperance Society made "the pecuniary
  subscription the only test" of membership and the pledge optional (Appendix O). The Bedloe's
  Island army society sent each departing squadron out as a branch reporting to the parent society,
  and recorded 22 expulsions (Appendix H).

**American Temperance Union (1840). *Report of the Executive Committee.*** and
**American Temperance Union (1848). *Almanac for the Year 1849.***

Stored alongside the 1841 report, same rights and provenance. Consulted in August and **read in full
on 13 September 2026.** The 1840 report covers the year before the Washingtonian founding and is
institutional context; the 1849 almanac is popular-facing material. **Neither supports any claim in
the manuscript.** The 1840 volume's scan also binds a second copy of the 1841 report, read through
`ATU_1841`. What the full reading found, as candidate material only:

- *The benefit design is older than the Sons of Temperance.* The 1840 report (printed pp. 25 to 26)
  describes Temperance Beneficial Societies arising in Philadelphia "in the commencement of 1836":
  an entrance fee and monthly contributions forming a fund for sick members, monthly meetings with a
  fine for absence, fourteen societies in the city and county. Its rationale is the one Chapter 2
  gives the Sons: many "will join a temperance beneficial society, who never could be induced to
  join a temperance society", and the recruits are less likely "to desert" because "a new and strong
  motive of self interest is added", as "the small number of expulsions" shows. Chapter 2 is right
  that the Sons built on benefits and should not be read as saying they invented them. OCR reading;
  check the page image before quoting.
- *One patron, a year earlier.* The treasurer's account for 1839 (printed p. 6, verified against the
  page image): receipts of $6,710.96, of which $2,500.00 was a donation from E. C. Delavan, 37 per
  cent; every other donor together gave $280.00. With the 1841 account, the national body ran on
  one man's money for at least two years.
- *The political drift, argued inside the movement.* Conventions divided over voting only for
  prohibition candidates (in Massachusetts the business committee stood six to five); Pennsylvania's
  convention wanted the cause "never ... brought into conflict with the politics of the State";
  Connecticut's report blamed "a reliance upon" legislation "to the neglect of moral influence";
  and the Union denied that urging temperance votes meant "forming a political party". Bears on
  Chapter 2's political-entanglement question.
- *The Sons of Temperance in their own figures.* The almanac's page 17, verified against the page
  image, gives the Order's statistics for 1848: 28 Grand Divisions, 2,654 Subordinate Divisions and
  149,372 members; 5,041 suspended, 8,043 expelled and 772 deaths in the year; 8,001 who "Violated
  the pledge", 2,452 reinstated and 742 who "Violated the second time"; $475,987.57 received and
  $140,058.39 paid in benefits. It is the only count of pledge-breaking in the corpus's temperance
  sources, and it was kept because benefits made membership an account. The almanac dates the
  Order's founding to 29 September 1841, which conflicts with the 1842 call Chapter 2 takes from
  Eddy (1887); the almanac is the weaker witness and the date should not be taken from it. Bears on
  Chapter 2, which gives Maxwell's 1850 figures and lists "the Sons of Temperance material beyond
  what Maxwell reports" as unread.
- The almanac also lists the United Brothers of Temperance, whose constitution forbids "oaths,
  signs, catechisms, or other secret ways of recognition", the Rechabites' weekly dues, and two
  state societies still under the Washingtonian name in 1848.

**Gough, J. B. (1869). *Autobiography and Personal Recollections of John B. Gough.*
Springfield, Mass.: Bill, Nichols & Co. 552 pp.**

**Saved here as `incorporated/Gough_1869/Gough_1869.txt`** (~176,000 words).
Public domain. Retrieved from the Internet Archive full text at
`archive.org/stream/AutobAndPersRecollOfJohnBGough/`, HTML stripped to plain text.

Chapter offsets in the saved file, for going straight to a passage:

| Chapter | Char offset | Content |
|---|---|---|
| I to V | 0 to 261,000 | Early life, emigration, his mother's death |
| X | 261,020 | The April 1843 relapse, in full |
| XIII | 348,780 | The September 1845 episode, his statement, the church committee |
| XXVII | 694,056 | The Dead Letter controversy of 1857 |
| XXVIII | 717,336 | The libel trial, *Gough vs Lees*, 21 June 1858 |

Read first, for Chapter 3: Chapters I to V, X, XIII, and the trial examination in XXVIII. **Read in
full on 13 September 2026:** the remaining chapters, VI to IX, XI, XII and XIV to XXXV. Nothing in
them changes what Chapter 3 says. The text is the Internet Archive's stripped full text, so any
quotation below should be checked against a page image before use. What the rest adds, as candidate
material only:

- *Gough on the Washingtonians, in his own words.* "I know I did not agree with the 'Washingtonians'
  in all their declarations and proceedings" (XVI), set against "the steady, persistent opposition of
  some of the temperance papers"; and his table of average receipts per lecture, from $2.77 in 1843
  to $173.39 in 1867. Bears on Chapter 3.
- *Signatures, never retention.* Three pledge books "containing nearly one hundred and fifty
  thousand signatures", and of three hundred young men who signed at Cincinnati, "How many were
  faithful to the promise they made, God knows" (XVIII); 215,179 names by 1853 (XXXV). Bears on
  Chapter 11.
- *A fee between signing and belonging.* A British society charged sixpence for the certificate
  that made a pledge-signer a member. A destitute couple balked at it; a gentleman paid and told the
  man "you are one of us" (XXVI). One anecdote from an interested narrator.
- *The schism.* The "dead letter" of 1857 and its sequel (XXVII to XXIX): the moral-suasion League
  that employed Gough against the prohibitionist United Kingdom Alliance, with rival newspapers, a
  pamphlet campaign and the libel suit *Gough v. Lees*. Gough put the American decline "partly, as I
  believe, owing to the neglect of the purely moral means", with "the pledge ... very much
  discarded". On oath (XXVIII) he described the money: ten guineas a lecture, the surplus going to
  the local society that hired him from the League, and literature bought "from head-quarters".
- *A society that ruled itself.* Julia Wightman's Shrewsbury society (XXXIII) grew from 20 men to 230
  in a year; after the first six, "They have come to me as perfect strangers, asking me to receive
  them"; a full meeting adopted a rule on medical prescriptions of drink with "unanimous content",
  enforced by expulsion. Gough thought British societies more permanent for "the very formality of
  their proceedings" (XXIII).
- Joel Stratton, who brought Gough to sign, was a Son of Temperance "rarely absent from the weekly
  meeting of his division" (XXXIV).

---

## Limited-status journal sources

Each entry carries its own current read status. This mixed section replaces the earlier
blanket “abstract only” heading, which was false for Hunter-Reel and colleagues.

**Hufford, M. R., K. Witkiewitz, A. L. Shields, S. Kodya, and J. C. Caruso (2003).
"Relapse as a Nonlinear Dynamic System: Application to Patients with Alcohol Use
Disorders." *Journal of Abnormal Psychology* 112(2): 219-227.**
The empirical warrant for the threshold shape in Chapter 14. What the abstract states:
two preliminary studies, 51 inpatients and 43 outpatients, six-month follow-up, and a
cusp catastrophe model with "more predictive utility than traditional linear models".
**The comparison statistics have not been seen.** The Part Three plan described this as
outperforming "linear and logistic" specifications; the abstract says linear only, and the
stronger word has been removed from the chapter. PubMed is behind a challenge page and the
full text was not reachable. Worth obtaining: the sample sizes are small and the chapter
would be improved by knowing how much better the cusp model actually fitted.

**Witkiewitz, K., and G. A. Marlatt (2007). "Modeling the Complexity of Post-Treatment
Drinking: It's a Rocky Road to Relapse." *Clinical Psychology Review* 27(6): 724-738.**
Cited in Chapter 14 for the general argument that post-treatment drinking is nonlinear,
not for any specific result. Abstract only.

**Hunter-Reel, D., B. McCrady, and E. Hildebrandt (2009). "Emphasizing Interpersonal
Factors: An Extension of the Witkiewitz and Marlatt Relapse Model." *Addiction* 104(8):
1281-1290.**
**Read in full via PubMed Central.** Used only as the source of a Witkiewitz and Marlatt
quotation describing relapse as a feedback loop running "until a steady state of drinking
or not drinking is achieved". That is bistability in their own words, but it reaches the
book at two removes and is therefore confined to Chapter 14's notes on sources rather than
used in the main text.

**Greenfield, B. L., and J. S. Tonigan (2013).** *Psychology of Addictive Behaviors* 27(3):
553-561. **Status upgraded: read in full on 10 August 2026** and moved out of this section's
limited status. The full entry is under "Obtained and read in full" below. Kept here as a pointer
because Chapters 13 and 24 cited it while it was abstract-only, and a reader tracing those
citations should land on the current status rather than the old one.

---

## Identified but not obtained

These are the binding constraints on finishing Part One. None is reachable without a
library, a purchase, or an Internet Archive borrowing account.

| Source | Needed for | Status |
|---|---|---|
| Blumberg, L. U., with Pittman, W. L. (1991). *Beware the First Drink!* Glenn Abbey Books. | Chapters 1, 2, 6 | Not on the Internet Archive at all. Purchase or interlibrary loan. |
| Alexander, R. M. (1988). *Journal of American History* 75(3): 763-785. | Chapter 1, the women's dimension | JSTOR. |
| Blumberg, L. U. (1980). *Journal of Studies on Alcohol* 41: 37-77. | Chapter 2, the political-entanglement question | Journal access. **Largely relieved:** Marsh 1866 supplies a participant's evidence that the Washingtonians came round to prohibition rather than resisting it, and Grosh 1842 supplies the rule they had against it. Blumberg would still add the local detail. |
| White, W. L. *Slaying the Dragon*, 2nd ed. | Chapters 1, 4 | Cited second-hand throughout; should stop. |
| Gough scrapbook, American Antiquarian Society, Worcester | Chapter 3 | Gough's own clippings on the 1845 affair. Research enquiry to AAS. |
| Rockefeller Archive Center, Sleepy Hollow | Chapters 4, 5 | The 1937-40 correspondence and the Frank Amos report. Independent of AA. |

---

## Paper-only bibliography: current read status

The paper cites additional methodological and empirical works that the manuscript does
not otherwise use. Earlier versions of this register omitted them, and the paper's
bibliography often omitted read status. The current-project record supports the following:

| Source | Current status | Use and limitation |
|---|---|---|
| Angrist (2014) | **Read in full 13 September 2026** in its working-paper version (`Angrist_2014`) | General warning about peer-effect interventions; do not treat as read-at-source evidence. |
| Banks et al. (2014, 2017) | Read status not documented | Background on dynamic behavior-change models only. |
| Ben-Porath (1967) | **Read at source**, confirmed by the Human Author 14 September 2026; no copy is held, and the paper's bibliography now says so | Background analogy for stock accumulation only. |
| Cunha and Heckman (2007) | **Read in full 13 September 2026** in its working-paper version (`CunhaHeckman_2007`) | Background on dynamic complementarity. |
| Cunha, Heckman and Schennach (2010) | **Read in full 13 September 2026** in its working-paper version (`CunhaHeckmanSchennach_2010`), which documents the paper's read-at-source claim | Methodological analogy; current project has not recorded pages used. |
| Galanter (1981) | Read status not documented | Background on large-group therapy. |
| Gorman et al. (2006) | Read status not documented | Agent-based drinking-model background. |
| Hu and Schennach (2008) | Read in part 13 September 2026, abstract, introduction and assumptions (195 to 200) (`HuSchennach_2008`) | Identification literature; the project does not implement its estimator. |
| Humphreys, Kaskutas and Weisner (1998) | Read status not documented | Measurement background. |
| Kaskutas, Bond and Humphreys (2002) | Read status not documented | Social-network mediation background. |
| Kelly, Humphreys and Ferri (2020) | Read status not documented | Review background; no numerical claim in this project is upgraded from it. |
| Lembke (undated) | **Read in full 13 September 2026** (`Lembke_nd`); the paper's bibliography now says so | Economics-of-religion application to AA. |
| Ostrom (1990) | Read status not documented | Institutional-design analogy only. |
| Riessman (1965) | Not obtained | Helper-therapy principle; cited at a remove. |
| Rynes and Tonigan (2012) | Read status not documented | Sponsorship/network background. |
| Sánchez et al. (2007) | Read status not documented | Epidemic-model background. |
| Schennach (2004) | Read status not documented | Nonlinear measurement-error identification; not implemented here. |
| Sharma and Samanta (2015) | Read status not documented | Drinking-epidemic background. |
| Tonigan, Connors and Miller (1996) | Read status not documented | Measurement background. |
| Witkiewitz and Marlatt (2004) | Read status not documented | Relapse-prevention background. |

“Read status not documented” is not shorthand for unread or read. It means the repository
does not contain evidence sufficient to claim either. Until a source is logged with pages
or a saved/authorized location, the paper may cite it for orientation but may not use it to
upgrade a load-bearing claim.

## AA publications: what is used, and how

**This section previously said that AA's own publications were deliberately not used as primary
sources. That is no longer true of one of them, and the correction matters more than the heading
did.**

*Twelve Steps and Twelve Traditions* (1953) was read in full on 10 August 2026 and **is** used as
a primary source, in Chapters 8, 10, 16 and 17 and in the paper. It is AAWS copyright and no copy
is held: the book is paraphrased, quoted only in fragments short enough to identify a claim, and
the reader is pointed at aa.org, which gives it away. See the entry in "Incorporated source
storage" above for why the distinction between reading and holding was worth drawing.

*Alcoholics Anonymous Comes of Age* (1957), *Pass It On* (1984), *Dr. Bob and the Good Oldtimers*
(1980), and the *Grapevine* essays remain AAWS copyright and **have not been obtained**. Where the
book reports their content it does so at one or more removes and says so. *Comes of Age* is the
most conspicuous gap: Kurtz names pages 97 to 98 as the passage that settles a question Chapter 17
depends on, and it is the one source the project most needs and has not read.

The 1939 first edition of *Alcoholics Anonymous* appears to be public domain in the US:
the copyright was not renewed and facsimile reprints are commercially available. It
contains the Steps but not the Traditions, which were written in 1946. **This should be
verified against US Copyright Office renewal records before any text is quoted.**

The Twelve Steps and Twelve Traditions themselves are paraphrased throughout and never
reproduced.
