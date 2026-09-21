# Project handoff

**Written for a cold start.** You may be Claude, ChatGPT, Cursor, or a person. Assume you have
no memory of this project and no access to any prior session. Everything you need is in this
repository. Read this file, then `CLAUDE.md`, then `AGENT_VERIFY.md` if you are verifying rather
than writing.

Last updated 15 September 2026. If the date at the bottom of `research/progress-log.md` is later
than that, this file is stale and the log wins.

`v0.9.0` is tagged and published as a GitHub pre-release; see `RELEASING.md` and `CHANGELOG.md`.
The branch, tag and CI structure that made that possible is built and exercised end to end. It
does not close any item in section 10 below.

---

## 0. What this project is, in one page

*Nobody in Charge* is an unpublished book by Human Author Christopher Melhauser
(christopher.melhauser@gmail.com), with AI writing collaboration by theonlymuffinbot
(theonlymuffinbot@outlook.com), using a mix of Anthropic Claude Opus 5 and OpenAI GPT-5.6 Sol and
Terra models. It argues that three of Alcoholics Anonymous's Twelve Traditions
implement a formal condition, proved by Golub and Jackson in 2010, for when a group that decides
by discussion can be trusted to converge on the truth. See `ATTRIBUTION.md` and `LICENSE` for
authorship, acknowledgment and public-domain dedication.

The condition: a group deciding by repeated averaging converges on the truth as it grows **if and
only if** the largest share of influence held by any single member shrinks toward zero. Nobody may
keep a fixed piece of the answer.

The claim: Tradition 2 denies weight to office, Tradition 9 stops weight accumulating by rotating
service, and Tradition 12 removes the surnames and status that unequal weight attaches to. Three
mechanisms, one condition.

The book adds three things to that. Rotation only works if the rotating pool scales with the
group, roughly a quarter of it. The natural conjecture that Step *i* pairs with Tradition *i* is
wrong on all twelve counts. And AA's own 1953 commentary describes a permanent non-rotating
advisory class that violates the condition it otherwise satisfies.

Milton Maxwell argued in 1950 that AA would outlive the Washingtonian movement because of its
Traditions, and that anonymity in particular had "sheer survival value". He was right and could
not prove it. This book supplies the proof.

**It is written for its own sake.** There is no publication deadline and no audience to please.
The correct instinct at every decision point is to make the claim smaller and better supported,
never larger.

---

## 1. Decisions that must not change

Do not change any of these without the user saying so explicitly, in the current session:

1. **The modeled room capacity is 60.**
2. **Confirmatory stochastic claims use 400 seeds**, paired by common random numbers where the
   comparison permits pairing.
3. **`model/aa_group_model.py` is frozen.** Its SHA-256 is
   `c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952`. Do not modify it unless you
   identify and document a genuine defect and the user decides.
4. **Do not retune the failed calibration targets.** 45 members and 9 experienced members return
   17.80 and 1.25. That failure is reported, not fixed.
5. **Do not delete source material or completed caches.**
6. **Run `python3 tools/check_portability.py` before any commit.** No host-specific absolute path
   may enter tracked files.
7. **Do not push, merge, or delete branches** unless the user authorizes those actions.

---

## 2. Authority order

When two things disagree, the higher one wins:

1. `model/aa_group_model.py` for executable semantics
2. hash-linked analysis scripts and complete caches for numerical results
3. manuscript, paper, appendix, primer, plans, ledgers for interpretation
4. generated Markdown and PDFs

Never make prose agree with a stale cache by hand, and never make a cache agree with prose by
hand. Regenerate.

**Every cache stores the model's SHA-256 and its generating script's SHA-256.** Editing a script
invalidates its cache. If you edit one, re-run it in the same session. This has been got wrong
before: `model/part5_runs.py` was edited without re-running and left the cache stale.

---

## 3. What the project contains

- 25 chapters plus preface and introduction, `manuscript/`
- an academic paper, `paper/anonymity-as-an-aggregation-condition.tex`, 35 pages
- a technical appendix, `appendix/APPENDIX.md`
- a Steps-and-Traditions primer, `reference/PRIMER-steps-and-traditions.md`
- the frozen model and 21 analysis scripts, `model/`
- hash-linked caches, ledgers and the source corpus, `research/`
- the elicitation packet, `research/elicitation/`
- checkers and builders, `tools/`
- three built PDFs: book 313 pages, paper 35, primer 23

---

## 4. Verification state

As of 21 September 2026, everything passes:

| Check | Result |
|---|---|
| `python3 -m pytest` | all passed, three skipped (poppler-dependent) |
| `tools/check_release.py --skip-artifacts` | 142 checks, 0 failed, 6 skipped (the full gate runs all 148 and passes with the artifacts built; it had 136 at the `v0.9.0` tag, see `RELEASING.md`) |
| `tools/check_book.py` | 0 failures, 39 warnings |
| `tools/check_chapter.py` on the primer | clear |
| `tools/check_portability.py` | clear |
| `tools/check_docs.py` | 19 checks, 0 failed |
| `tools/build_corpus.py --check` | 0 corpus problems |
| `tools/check_pdfs.py` | 21 checks, 0 failed |
| `model/book-calculations.ipynb` | 8 cells, 84 assertions, clean |
| `paper/anonymity-as-an-aggregation-condition.ipynb` | 10 cells, 108 assertions, clean |
| `model/elicitation_compare.py --self-test` | passed |

The 39 `check_book` warnings are repetition and sentence-length notes. They are not failures and
have been reviewed. Do not chase them to zero; some repetition between a chapter and its Machinery
is deliberate.

### The two notebooks verify different things

`model/book-calculations.ipynb` checks the model's identity and semantics, every cache's
completeness and provenance, and the derivation of every figure the chapters print.

`paper/anonymity-as-an-aggregation-condition.ipynb` does all of that and adds two paper-specific
cells: it re-derives the paper's headline tables from the caches, and it requires every decimal the
paper prints to be reachable from the model, a cache, or a shown derivation. Until 9 August 2026
the paper had no equivalent of the chapters' guarantee.

Run both. `tools/run_notebook.py` runs the book notebook; `tools/run_notebook.py --paper` runs the
paper's.

---

## 5. Reproduction

From the repository root, in this order. The PDFs must be built before the final check, because
that check requires each rendered artifact to be newer than every source feeding it.

```bash
python3 tools/inventory_model_choices.py
python3 tools/summarize_release_gate.py
python3 tools/summarize_robustness.py
python3 tools/build_corpus.py
python3 tools/regenerate_notebooks.py
python3 tools/run_notebook.py
python3 tools/run_notebook.py --paper
python3 tools/check_book.py
python3 tools/check_chapter.py reference/PRIMER-steps-and-traditions.md
python3 tools/check_portability.py
python3 tools/check_docs.py
python3 tools/build_book.py
cd paper && tectonic anonymity-as-an-aggregation-condition.tex && cd ..
python3 tools/build_primer.py
sh research/elicitation/build.sh
python3 tools/check_pdfs.py
python3 tools/check_release.py
```

Then open all three PDFs and look at them. The release rule requires visual inspection: no
clipping, no broken tables, no blank pages, no retired language.

---

## 6. The synchronisation rule

Any change to the model or to a public number must be propagated **in the same work session** to
every affected layer:

analysis scripts and caches; both notebooks; manuscript chapters and preface;
`appendix/APPENDIX.md`; `paper/anonymity-as-an-aggregation-condition.tex`;
`reference/PRIMER-steps-and-traditions.md` including its plain-language paragraph;
`research/PARAMETERS.md`, `research/SOURCES.md`, and the claim registers; `README.md`, the
applicable plans, `research/progress-log.md`, `AGENTS.md`, this file, and `AGENT_VERIFY.md`; then
the book, paper and primer PDFs.

Search the whole repository for retired values and phrases. The release checker supplements that
search; it does not replace reading the surrounding claim.

---

## 7. The source corpus

40 sources under `research/incorporated/`, one directory each, named `<ShortAuthor>_<Year>`,
holding `citation.md`, `metadata.json`, `source_summary.md`, and usually a verification index.
The newest are `ServiceManual_2024` and the seven open-access papers held on 13 September 2026.
`WorkingManuscript_1939` (12 September 2026) is the 1939 multilith with its pencilled revisions,
held git-ignored at the Human Author's direction. Its `edits_and_suggested_uses.md` sets out what it
implies for the manuscript: its two corrections, to Chapter 4 and to Appendix A13, were made on 13
September 2026, and its other suggested uses are section 10, item 8.

**No source document is committed and this repository is public.** `.gitignore` excludes every
`.pdf`, `.txt`, `.djvu` and `.epub` under `research/incorporated/` and `research/staged/`. What is
committed is the record: citation, rights position, provenance URL, SHA-256, and a vocabulary-only
verification index.

Citation checking does not need the documents. Each index records the source's vocabulary and,
because a vocabulary set has no word order, which registered subjects the document contains,
decided against the real text at build time. With no documents present, every citation-subject
pair still verifies.

Do not add a source by hand. Run `python3 tools/build_corpus.py`; `--check` reports drift.

A directory's leading token must be at least three characters and distinctive, because
`tools/check_book.py` identifies a source in prose by that token. "AA" is not usable. Two
directories may not share a leading token, which is why the corpus has `TwelveAndTwelve` and
`KurtzTalk` rather than a second `AAWS` and a second `Kurtz`.

### Five sources are record only

These have **no document at any time**, which is a stronger condition than the git-ignored
majority. A verifier should not report either category as a missing source. Each carries
`"record_only": true` in its metadata so this is machine-checkable.

| Source | Why | What would end it |
|---|---|---|
| `Kurtz_1991` | in copyright | the Human Author's own copy, photographed, or a bought ebook |
| `DeGroot_1974` | scan with unverified posting authorization | a JSTOR or publisher PDF |
| `Grapevine_1946` | scan with unverified posting authorization | a copy from the Grapevine archive |
| `Rohr_2011` | the copy consulted was an unauthorized posting | photographs of the Human Author's copy |
| `Tricycle_2019` | paywalled past its opening | a PDF saved from a subscribed browser |

Three of the five carry no verification index, because no text was retained to build one from:
`DeGroot_1974`, `Grapevine_1946`, `Tricycle_2019`. Their metadata says so. This is expected, not
drift. Six more were record only until 13 September 2026, when the Human Author directed that
the corpus hold a lawful copy of every source it can; each now says so under
`formerly_record_only`.

### The rule about copyright, stated precisely

**Reading a copyrighted work and holding one are different acts, and this project's rule is about
holding.** Read what is lawfully readable, hold only lawful copies and never commit them, quote
nothing at length, record the provenance.

Several chapters formerly said "this project does not acquire AA copyright material" and treated
that as a reason not to read it. That was a category error, corrected on 10 August 2026, and it
had been expensive. **Do not restore the old wording anywhere.**

### The Rohr provenance problem

`Rohr_2011` carries the corpus's strongest objection and it is recorded in full in its
`metadata.json`. The copy consulted bore an OceanofPDF.com imprint, an unauthorized distribution
site, and the work is a current in-print commercial title, so the posting was plainly not
authorized. The file was not retained; the bibliographic record was confirmed against publisher and
library listings independently of it; and both claims the manuscript draws from it are **absence**
claims, checkable by anyone holding a lawful copy.

**Action for a future session: confirm the Rohr citations against a lawfully obtained edition
before release.** It is part of section 10, item 4.

---

## 8. What changed on 10 August 2026

Three copyrighted works were read in full and catalogued as record only; the first and the last
have held copies since 13 September 2026. It remains the change to the evidence a cold reader most
needs to know about. Later changes are in section 10's closed lists and in
`research/progress-log.md`.

**From `TwelveAndTwelve_1953`, four things the book had recorded as unavailable:**

1. **The book's own thesis in Wilson's words.** Tradition 2's chapter concludes that the group
   conscience, well advised by its elders, will in the long run be wiser than any single leader.
2. **The strongest objection to that thesis, from AA itself.** The same chapter calls elder
   statesmen "the real and permanent leadership of A.A." and "the voice of the group conscience",
   people a perplexed group "inevitably turns" to. They hold no office and so rotate out of
   nothing. It also says the committee that *does* rotate cannot "in any sense whatever" govern or
   direct. So the fellowship rotates the positions its own commentary says carry no weight. This
   is now Chapter 8's central objection and it is answered rather than buried: the condition is a
   claim about what a rule does, not a claim that the fellowship obeys it.
3. **The disproof of index-pairing.** No Tradition chapter cites the Step of its own number; the
   twelve Step chapters contain no occurrence of the word "Tradition". The only indexed
   cross-reference is Tradition 8 citing the Twelfth Step, which is off-index. Chapter 16's old
   claim that AA literature "gestures at the parallel" is withdrawn rather than edited.
4. **Corroboration for Chapter 17.** The chapters on Traditions 1 and 5 keep unity and singleness
   of purpose distinct, which is the assignment Kurtz's conflation charge threatened.

**From `Rohr_2011`:** a named holder of the protective reading of anonymity, and a 105-page book
on the Steps that never mentions the Traditions.

**From `KurtzTalk_c1984`:** Chapter 25's closing counterweight, in which the historian with the
fullest archive access answers the survival question by pointing at the individual encounter
rather than at structure.

**Model.** `model/part2_influence.py` gained an `elders` family, sections 5b and 5c, with a cache
rebuild. The frozen model was not touched. Three elders holding a tenth of every row between them
floor maximum influence at alpha over *e*: computed 0.0342 at N = 1000 against a predicted 0.0333
and a flat benchmark of 0.0010. The error ratio against flat runs 1.012, 1.075, 1.350, 2.079 at
N = 10, 50, 250, 1000. Chapter 10's twenty-six per cent rotation prescription does not rescue such
a group: 2.5, 9.2, 34.2 times flat at N = 50, 250, 1000.

---

## 9. The elicitation round: the only thing left that could change a conclusion

Part Four rests on a twelve-by-eight governance matrix that one person wrote down. Every
robustness check varies the *values* in that matrix and holds its pattern of empty cells fixed, so
no further computation can test the pattern. A second reader filling the same grid independently is
the only available test.

The packet is `research/elicitation/`: five LaTeX documents plus a style file and `build.sh`.

| Document | Who sees it |
|---|---|
| `0-start-here.pdf` | you |
| `1-respondent-form.pdf` | **the respondent** |
| `2-recruiting-note.pdf` | you, to copy into an email |
| `3-response-template.pdf` | the respondent, optional return sheet |
| `4-collator-notes.pdf` | **you only** |

**Never send `4-collator-notes.pdf` to a respondent.** It states that the book leaves five rows
empty and names them. That is the answer the exercise exists to elicit independently, and sending
it destroys the round.

The analysis is preregistered: `model/elicitation_compare.py` was written before any form came
back and **must not be edited once forms start arriving**. If it turns out to need a change, make
it, record it in `research/progress-log.md`, and report both the original and revised analysis.

The result is two-sided and the script says so in plain words. If respondents leave different rows
empty, it reports that Chapter 18 is contradicted. Hold the project to that.

---

## 10. What actually remains

Nothing is blocked on engineering, and nothing here blocks release. Every checker passes, both
notebooks execute, all three PDFs render with zero overfull boxes, and continuous integration is
green. This is the complete list and the only place these are recorded; anything claiming a
shorter one is out of date.

**One item could change a conclusion.**

1. **The elicitation round.** Part Four rests on a twelve-by-eight matrix one person wrote down,
   and no computation can test its pattern of empty cells because every check holds that pattern
   fixed. It needs two or three human respondents. The packet is `research/elicitation/`; send
   `1-respondent-form.pdf` and **never** `4-collator-notes.pdf`, which names the answer the
   exercise exists to elicit.

**One item needs a copyrighted book bought or borrowed.** It cannot be closed by computation or by
inference from what is already here.

2. **Obtain *Alcoholics Anonymous Comes of Age*, pages 97 to 98.** Kurtz names it as the passage
   that settles the unity versus singleness-of-purpose question Chapter 17 depends on. It is the
   single most valuable unread source, and the last time an AA text was left unread on copyright
   grounds it turned out to contain the strongest objection to this book's own argument. It is
   sold rather than posted; AA's own site offers it for purchase only.

**One is an ordinary scholarly loose end.**

3. **Outstanding citations**, none load-bearing: Riessman (1965), Valverde/White/Mair (1999),
   Blumberg and Pittman (1991), Alexander (1988), Blumberg (1980), the Gough scrapbook at AAS, the
   Rockefeller Archive holdings, and the adult skill-depreciation literature, of which two working
   papers were read in full on 13 September 2026. The literature on how fast habits and practices
   lapse, which is where the decay rate's evidence would have to come from, was searched on 21
   September 2026 and the result is `research/DECAY-RATE-LITERATURE-SCAN.md`. Nothing measures the
   quantity `delta0` represents. What exists is deliberate habit degradation, stabilising in days;
   a computational habit-decay parameter in units of behavioural opportunities; and the lapse of
   voluntary practice regimes, whose median dropout times run to a few months, which is the order
   of the model's 11.6-week half-life. No copy is held, nothing is read in full, nothing is cited,
   and the model is unchanged. What is left is the Human Author's decision whether to hold and read
   the two open-access papers so that Chapter 12 can say the rate is bracketed rather than merely
   untested.

**One is a set of lawful copies only the Human Author can obtain.** None changes a conclusion;
each moves a record-only source onto the ordinary footing.

4. **Copies for the five record-only sources**: Kurtz (1991), DeGroot (1974), the April 1946
   *Grapevine* article, Rohr (2011) and *Tricycle* (2019). What each needs is in section 7.

**Two more need the Human Author.** Neither changes a conclusion.

5. **Photographs of book pages 22 and 23 of *The Book That Started It All*.** The reading copy of
   the 1939 working manuscript lacks them. They go through the same cleanup into the reading copy,
   and `python3 tools/build_corpus.py` then rebuilds its index. The same session could retake MS
   p. 56, PDF page 88, where Dr. Howard's name is not legible at the resolution checked.
6. **Copies, and a read status, for nine background citations.** The paper-only bibliography in
   `research/SOURCES.md` records "read status not documented" for:
   - Galanter (1981);
   - Humphreys, Kaskutas and Weisner (1998);
   - Kaskutas, Bond and Humphreys (2002);
   - Ostrom (1990);
   - Sánchez et al. (2007);
   - Schennach (2004);
   - Sharma and Samanta (2015);
   - Tonigan, Connors and Miller (1996);
   - Witkiewitz and Marlatt (2004).

   Each is cited as background, and the corpus holds none of them. More works are cited and have a
   read status but no copy:
   - **Read at PubMed Central on 14 September 2026:** Banks et al. (2017), Gorman et al. (2006),
     Kelly, Humphreys and Ferri (2020), Rynes and Tonigan (2012) and Witkiewitz and Marlatt (2007).
     A PDF saved from each article page in a browser would give the corpus a copy, since every
     scripted route refuses.
   - **Cited at a remove:** Banks et al. (2014), through the 2017 paper. AMS refuses its PDF to
     scripts, so it needs the same browser save.
   - **Other statuses:** Ben-Porath (1967), read at source, and Hufford et al. (2003), read in
     abstract only.

### Closed on 21 September 2026

- **Where the referral-versus-attraction ordering first reverses on final membership**, which was
  item 7 and was optional. `model/decay_reversal.py` ran the `decay_ordering.py` design at 10, 15
  and 20 per cent lower decay, 3,600 runs on seeds 0 to 399, cached in
  `research/decay_reversal.json`. The membership ordering holds at 10 and 15 per cent lower, at
  10.92 members [10.18, 11.66] and 6.35 [5.03, 7.68], and is reversed at 20 per cent lower, at
  -2.79 [-4.77, -0.81]; endpoint viability and existence are reversed in no paired run at any of
  the three. The two caches read as one seven-level series, which a test enforces by comparing the
  scripts with the docstring and the level list removed. Chapters 1, 4, 12 and 24, the primer, the
  paper, appendix A7.5 and A11 and `research/PARAMETERS.md` say where the turn is; the gate now
  runs 148 checks, 142 under `--skip-artifacts`. No released number changes.

### Closed on 15 September 2026

- **The working manuscript's other suggested uses.** All seven were drafted at the Human Author's
  request, each as its own commit so that any one can be dropped on its own:
  - Chapter 5, the 1939 Foreword and the Foundation page;
  - Chapters 7 and 9, how the fellowship's first book was settled;
  - Chapter 18, the protective tier's precursors;
  - Chapter 15, the editors on helping and its cost;
  - Chapter 19, the membership rule;
  - Chapter 22, the founders' answer to the composition question;
  - Chapters 24 and 21, the 1939 meeting sizes.

  Every quotation and page reference was checked against the facsimile's page images, and each
  addition says what it is not: a historical illustration or precursor, never a test of the model.
  Three parts were left out:
  - the title vote and the four people at the galleys, which reach the book only at a remove;
  - household autonomy on serving liquor, too weak a match for group autonomy;
  - the Bill's Story insert, whose point Step Eleven's handwritten qualifier already makes.

  Chapters 21 and 24 also now record that SMF-132 was read on 17 August 2026 and is held. Whether
  each addition stays is still the Human Author's decision.

### Closed on 14 September 2026

- **The published history, rewritten at the Human Author's direction.**
  - **What was removed** from every commit of `main` and from the `v0.9.0` tag:
    - **The withheld name**, from four places:
      - the appendix passage the 17 August fix reworded, which now carries that fix's wording
        throughout;
      - the generated book Markdown;
      - ten rendered book PDFs of 16 and 17 August;
      - two verification indexes.
    - **Host paths:** home-directory paths from the initial import.
    - **Source documents:** four of them, with their OCR text.
    - **The second email address:** removed from commit and tag metadata and replaced with the
      GitHub no-reply address. The address published on purpose in `README.md` and `CITATION.cff`
      is unchanged.
  - **What did not change:**
    - every current file is byte-identical;
    - every commit message is unchanged;
    - the release assets are the same files.

    Every commit hash changed, so a clone made before 14 September 2026 must be re-cloned rather
    than pulled.
  - **How:**
    - `git filter-branch` ran on a fresh copy, and the result was verified before anything was
      pushed.
    - `main` and the tag were force-pushed with leases.
    - The four merged branches were deleted.
  - **To keep it out:** this repository's commit email is set to the no-reply address.
  - **Left as it is:** GitHub still serves the old commits by hash and through the pull-request
    references of #1 to #22. On 15 September 2026 the Human Author decided not to ask GitHub
    Support to purge them. New commits use the no-reply address.
- **Four statements out of step with their sources**, corrected at the Human Author's direction.
  None changes a number the book computes.
  - **The Cochrane review:** the paper's literature review now reports its high-certainty
    advantage in continuous abstinence at twelve months. It had said "at least as effective" and
    superior "in several trials".
  - **Rynes and Tonigan (2012):** the review now presents them as the clearest dissent from the
    network-mediation account. It had counted them as part of that account.
  - **Gorman et al. (2006):** the review now describes the contagion model with a single bar that it
    is. It had said the model covered outlet density.
  - **Chapter 14:** it now adds the Project MATCH refit of Witkiewitz and Marlatt (2007) to the
    older strand's warrant, with its limits.

- **The six background papers supplied on 14 September 2026.** What arrived were six short
  summaries written by another tool, not the articles, so none was filed. Every scripted route to
  the articles refused, so five were read in full in the in-app browser at PubMed Central:
  - Banks et al. (2017);
  - Gorman et al. (2006);
  - Kelly, Humphreys and Ferri (2020);
  - Rynes and Tonigan (2012);
  - Witkiewitz and Marlatt (2007).

  `research/SOURCES.md`, Chapter 14's references and the paper's bibliography now record them as
  read, and Banks et al. (2014) as cited at a remove. The four statements the reading found out of
  step with their sources are corrected above.

- **A withheld name in two verification indexes.** A pass for personal information found the
  surname of the founder this project never names in the committed vocabularies of
  `RecoveryDharma_2023` and `Rohr_2011`. `check_book.py` enforced the rule over a fixed list of
  prose files, and no index was on it.
  - **The fix:**
    - The digests moved to `tools/withheld.py`.
    - `build_corpus.py` leaves a withheld word out of every index, and its `--check` reports one.
    - `check_book.py` scans every tracked text file.
    - `check_pdfs.py` scans the text of each rendered PDF.
  - **What changed in the indexes:** each lost that one word and nothing else.
  - **The published history:** rewritten on 14 September 2026, as recorded above.
- **Ben-Porath (1967)'s read status.** Chapter 12 said it was read at source, `research/SOURCES.md`
  recorded no read status, and Chapter 14 listed it as cited at a remove. The Human Author
  confirmed Chapter 12, so the ledger now records it as read at source, Chapter 14 lists it under
  read in full, and the paper's bibliography marks it. The corpus still holds no copy.

### Closed on 13 September 2026

- **The release gate's skip count, and tests for the generated files.** `check_release.py
  --skip-artifacts` counted its own notice as a passed check, and the gate's comment, `CLAUDE.md`,
  `AGENT_VERIFY.md` and both workflows said the flag omits seven checks; it omits six and now
  reports them as skipped. New tests execute both notebooks, compare them and
  `research/ROBUSTNESS-RESULTS.md` with their generators, and recompute three cached cells of
  `research/decay_ordering.json` from its script. Items 5 to 8 above were recorded elsewhere and
  are now here.
- **The referral-versus-attraction ordering at slower decay.** `model/decay_ordering.py` re-ran
  the one-at-a-time screen's three `delta0` reversals at 400 paired seeds, 4,800 runs cached in
  `research/decay_ordering.json`. The screen was right about direction, and only on final
  membership: at 25 per cent lower the referral-starved group ends larger, while referral loss is
  still worse on endpoint viability and existence; at 50 and 75 per cent lower every referral-loss
  run is viable. Chapters 1, 4, 12 and 24, appendix A7 and A11, the paper, the primer and
  `research/PARAMETERS.md` now say so, and the cache is registered in the release gate and both
  notebooks. No released number changes, and the model stays as it is until something measures
  how fast a practice lapses.
- **Appendix A13's count of the 1939 stories.** A13 said twenty-nine; the 1939 contents page lists
  thirty, and the working manuscript accounts for all of them. A13, the primer and the source
  records now say thirty, and A13 states that its census covers the twenty-six stories the automatic
  split recovered. No census figure changes.
- **Chapter 4's "you must" to "we ought".** The paragraph on the 1939 comment round now says what
  the working manuscript shows: instruction to "you" rewritten as a report of what "we" did, the
  modal usually kept, one command plainly softened, and force restored at galley stage. Each
  quotation was checked against the page images, and the claim register, `research/SOURCES.md` and
  the working-manuscript note record the correction.
- **The seven papers held on 13 September 2026 are read**, six in full and one in part, and what
  they bear on is applied. Chapter 12 sets the decay rate against the two skill-depreciation papers
  and says how much rides on it; Chapters 12 and 13 correct the three precision points, and Chapter
  14 stops crediting Cunha, Heckman and Schennach with the depreciation structure, which is
  Ben-Porath's; Chapter 13 adds their sign-changing estimate as an analogy; Chapters 2 and 15 use
  Lembke; Chapters 1 and 24 note that the decay rate is among the few values that reverse the
  referral-versus-attraction ordering; the paper, primer, appendix A11 and `research/PARAMETERS.md`
  follow. The model is unchanged, because nothing measures how fast a practice lapses.
- **The author block in rebuilt books.** `tools/build_book.py`, the preface and the appendix still
  named the Human Author, so every rebuild put the name back into the book that had been
  anonymized by hand. All three now say the book is by an anonymous author, and the book and
  primer were rebuilt from source.
- **The read-scope statements in the book and primer.** Appendix A12, the primer's Recovery Dharma
  entry and Chapters 1 and 2 now say what `research/SOURCES.md` says. Chapter 2's list of unread
  sources was stale on four more names than this list had recorded: Krout, Harrison, Marsh and
  Eddy had all been read at source long before.
- **The partly read sources on disk.** The three American Temperance Union documents, Gough's
  autobiography and Recovery Dharma's practice pages are read in full. None changes a conclusion.
  The candidates for use are the Sons of Temperance's own 1848 count of members who broke the
  pledge, and treasurer's accounts showing one donor giving 37 and then 47 per cent of the Union's
  receipts.
- **The Concept 4 essay.** AAWS posts the whole 2024-26 *A.A. Service Manual* with Bill W.'s
  Twelve Concepts free on its own file host; it is now `ServiceManual_2024`. The Concept IV essay
  is about voting participation in proportion to responsibility and holds no rule on the size of
  a rotating pool, which confirms Chapter 10's narrower reading. Rotation doctrine sits in
  Concept XI, which ties term length to responsibility and warns against attempting more rotation
  than that. A fourth item carried as unobtainable turned out to be published free.

### Closed on 17 August 2026

Three items that stood on this list were closed by reading sources that turned out to be
published free and officially, which had been assumed unobtainable without checking.

- **SMF-132**, the worldwide group-and-member series, read at source. It supplies the
  out-of-sample number Chapter 21 asked for: 18.4 members per group on average across 2001 to
  2020 against a modelled endpoint of 17.80. Recorded as a consistency check, not a validation.
- **The Twelve Concepts for World Service**, read in short form. Concept 4 holds a proportionality
  principle, but between voting weight and responsibility rather than between pool and group, so
  Chapter 10's claim survives in a narrower and better form.
- **An independent account of the 2019 Recovery Dharma schism**, from *Tricycle*. It confirms the
  structure from outside the successor's own literature and corrects where the contrast falls.
- **AA's fourth edition of the Big Book.** The Human Author owns several copies and supplied the
  text; AAWS also posts the book in per-section PDFs. Appendix A13.7 now repeats the 1939 arrival
  census on all forty-two stories of the 2001 edition: member-initiated arrival falls from 77 per
  cent to 43 per cent of the classifiable stories, with twelve unresolved and reported as such.
- **The Rohr provenance objection.** The Human Author holds a lawfully obtained copy of
  *Breathing Under Water*, confirmed 17 August 2026. The objection was always about access
  resting on an unauthorized posting, not about the accuracy of the reading, and a copy on the
  author's shelf settles it. No claim drawn from the book carries a page citation, so the edition
  difference between the 2011 Franciscan Media first edition and the 2016 SPCK printing is
  immaterial to anything the manuscript says.

The lesson is worth keeping: three items sat here as impossible because nobody checked whether the
publisher gives them away.

---

## 11. House style, because it is easy to violate

- **No em dashes in the author's prose.** Preserve punctuation inside quotations.
- Plain-language equations in manuscript Markdown; the paper stays LaTeX.
- **No subheadings or tables inside a chapter's narrative.** Use horizontal rules between narrative
  sections. Tables belong in The Machinery.
- Every chapter ends with The Machinery and its reference-status headings, in this fixed order,
  using only those that apply: Read in full; Cited at a remove; Referenced but not reproduced;
  Internal, and reproducible from this repository; What was not read. Omit a heading with nothing
  under it rather than filling it with a placeholder. Most chapters carry four of the five.
- A number from a stochastic run carries its uncertainty and design. Deterministic algebra is
  labeled deterministic.
- **Nothing in the project may be written as advice about an individual's recovery.**

---

## 12. Claims that must not be made

Do not claim steady state, indefinite persistence, universal sensitivity, causal composition
effects, or path-specific T3/T11 effects from mixed interventions. Do not describe an interval
crossing zero as "no effect"; it is unresolved.

Language that must stay exact:

- `B = S @ GOV.T` is semantic overlap, not executable coupling.
- `C = Snorm @ GOVW.T` is the normalized no-capacity linear map, not a trajectory effect.
- Tradition 3 has resource-governance and inverse-practice dropout-friction paths; Tradition 11 has
  resource-governance and attraction paths. Ordinary adherence changes move both paths and are
  **mixed interventions**.
- The recipient resource is low-practice opportunity per high-practice potential helper. Low and
  high practice are **not** tenure cohorts.
- Zero membership is absorbing closure. Existence is `N > 0`; endpoint viability is `N > 5`. First
  crossing, recovery, final membership and closure are different estimands.
- The practice scale is cardinal only inside this model and has no validated clinical unit.
- Chapter 14's frozen-environment high state, separatrix and hysteresis are **retired**
  diagnostics. In corrected endpoint environments, high and low starts separate in 7 of 400 cases.

---

## 13. If you change anything

1. Say what layer you are changing and why, before you change it.
2. Re-run the affected scripts so no cache goes stale.
3. Propagate through every layer in section 6.
4. Re-run the whole sequence in section 5.
5. Append to `research/progress-log.md`. That file is the project's memory across sessions, and it
   is where the next agent will look to find out what you did and what it cost.
6. Run `tools/check_portability.py` before committing.

Do not approve release until every required cache is complete and hash-current, both notebooks
execute cleanly, all checkers pass, and an independent verifier can return the documented verdict
using `AGENT_VERIFY.md`.
