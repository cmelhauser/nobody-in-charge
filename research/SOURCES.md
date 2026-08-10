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
| ATU, *Report of the Executive Committee* (1840) | public domain, pre-1929 | PDF and OCR | consulted, not read in full |
| ATU, *Annual Report* (1841) | public domain, pre-1929 | PDF and OCR | read for the Washingtonian passages; p. 39 verified against the page image |
| ATU, *Almanac for 1849* (1848) | public domain, pre-1929 | PDF and OCR | consulted, not read in full |
| AAWS, *A.A. Tradition: How It Developed*, P-17 (2024) | **copyrighted; not mirrored** | citation and metadata only | read; two passages verified against page images; supplies the 1946 Twelve Points text for Chapter 5 |
| Pagano et al., "Helping Other Alcoholics" (2004) | NIH author manuscript, open access | PDF and extracted text | read in full; figures checked against the results section |
| Greenfield and Tonigan, "General AA Tools of Recovery" (2013) | NIH author manuscript, open access | PDF and extracted text | read in full; cited in Chapter 12 as an objection to one dial per step |
| Wilson, "Twelve Suggested Points for A. A. Tradition", *A.A. Grapevine* (April 1946) | **A.A. Grapevine copyright; not archived** | record only | read at source; Chapter 5's opening quotation verified, and the two-title problem explained |
| DeGroot, "Reaching a Consensus" (1974) | **ASA / Taylor & Francis; not archived** | record only | read at source; the updating rule behind Part Two |
| *Alcoholics Anonymous*, first edition 1939, in the 1999 BBSG reprint | reprint asserts no copyright; 1939 status contested | PDF and extracted text | acquired; not yet used as claim support |
| AAWS, *Twelve Steps and Twelve Traditions* (1953) | **copyrighted; not archived** | record only | **read in full 10 August 2026**; supplies the elder-statesman objection to Chapters 8 and 10, the rotating-leadership text for Chapter 10, the cross-reference count for Chapter 16, and the unity/purpose distinction for Chapter 17 |
| Rohr, *Breathing Under Water* (2011) | **in copyright and in print; not archived** | record only | read in full 10 August 2026; cited only for its reading of anonymity and for containing no discussion of the Traditions; see the provenance note below |
| Kurtz, "A Talk About the History of Alcoholics Anonymous" (about 1984) | **rights position not established; not archived** | record only | read in full 10 August 2026; the closing survival answer in Chapter 25; distinct from Kurtz (1991) |

### The three copyrighted works read on 10 August 2026

These three changed the project's own rule, and the change should be stated rather than absorbed
quietly. The rule was previously written, in several chapters, as *this project does not acquire
AA copyright material*. That conflated two different things. A rule against **holding** a
copyrighted work is a copyright rule and the project keeps it strictly: nothing is stored, nothing
is committed, nothing is quoted at length. A rule against **reading** one was never a copyright
rule at all, and it had been costing the argument evidence.

What it cost is now measurable. *Twelve Steps and Twelve Traditions* contained the book's own
thesis in Wilson's words, the single strongest objection to that thesis, the disproof of the
index-pairing conjecture, and corroboration for the unity assignment Kurtz had challenged. Three
of those four are things the book had recorded as unavailable.

`TwelveAndTwelve_1953` is held on exactly the P-17 footing: AAWS publishes the book free, one
chapter per PDF, and a reading copy was assembled locally, read, and left outside the repository.
The record keeps the citation, the assembly's SHA-256, the pages verified, and the reproducible
cross-reference count.

`Rohr_2011` carries a provenance problem recorded in full at
`research/incorporated/Rohr_2011/metadata.json`. The file consulted bore an OceanofPDF.com
imprint, which is an unauthorized distribution site, and the work is a current in-print commercial
title, so the posting was plainly not authorized. This is a stronger objection than the
unverified-authorization cases below. The file was not retained; the bibliographic record was
confirmed against publisher and library listings independently of it; and both claims the
manuscript draws from it are **absence** claims, checkable by anyone holding a lawful copy. Before
release, any Rohr citation should be confirmed against a lawfully obtained edition.

`KurtzTalk_c1984` is dated only by inference and must always be cited as "about 1984". Wilson's
letters are quoted within it from memory and without page citations, so anything attributed to
Wilson through it is at a remove.

The P-17 document itself is deliberately absent. It is copyrighted AAWS literature distributed
as a free official PDF, and this repository is public, so mirroring the full PDF and a full OCR
transcript here would be redistribution beyond the authorized source context. The record retains
the citation, the official URL, the SHA-256 of the July 2024 file, and the verified quotations. A
verifier should download it from aa.org. Removing the mirror changes nothing about what the book
may claim from it.

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
Membership."* Located and not acquired. It is the group-and-member series by year that Chapter
21 proposes as the starting point for an out-of-sample test. It is AAWS material distributed
under a content-use policy permitting a single printed copy, and this project does not acquire
AAWS publications on the book's behalf. Recorded here so the identifier does not have to be
found again.

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
There are thirteen active text files outside the staged corpus: eleven source transcriptions
or OCR files plus the incorporated Maxwell text and Golub-Jackson OCR. Their individual
rights and reliability differ and are stated in their entries.

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

## Obtained, partly read

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

Not read in full. The remainder is national temperance-movement business: state society reports,
crime and consumption statistics, and correspondence. An institutional self-presentation
throughout, so its numbers carry the movement's own interest in them.

**American Temperance Union (1840). *Report of the Executive Committee.*** and
**American Temperance Union (1848). *Almanac for the Year 1849.***

Stored alongside the 1841 report, same rights and provenance. Consulted rather than read: the
1840 report predates the Washingtonian founding and is held for institutional context, and the
1849 almanac is popular-facing material held for messaging and dissemination. **Neither currently
supports any claim in the manuscript.** They are recorded so that a later reader knows they were
looked at and set aside, not overlooked.

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

Read: Chapters I to V, X, XIII, and the trial examination in XXVIII. Not yet read: the
middle chapters, XXVII in full, and XXIX.

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
| Angrist (2014) | Read status not documented | General warning about peer-effect interventions; do not treat as read-at-source evidence. |
| Banks et al. (2014, 2017) | Read status not documented | Background on dynamic behavior-change models only. |
| Ben-Porath (1967) | Read status not documented | Background analogy for stock accumulation only. |
| Cunha and Heckman (2007) | Read status not documented | Background on dynamic complementarity. |
| Cunha, Heckman and Schennach (2010) | Paper bibliography says read at source; no local copy | Methodological analogy; current project has not recorded pages used. |
| Galanter (1981) | Read status not documented | Background on large-group therapy. |
| Gorman et al. (2006) | Read status not documented | Agent-based drinking-model background. |
| Hu and Schennach (2008) | Read status not documented | Identification literature; the project does not implement its estimator. |
| Humphreys, Kaskutas and Weisner (1998) | Read status not documented | Measurement background. |
| Kaskutas, Bond and Humphreys (2002) | Read status not documented | Social-network mediation background. |
| Kelly, Humphreys and Ferri (2020) | Read status not documented | Review background; no numerical claim in this project is upgraded from it. |
| Lembke (undated) | Cited at a remove | Economics-of-religion application to AA. |
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
