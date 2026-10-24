# Research Corpus: Washingtonian Temperance, Mutual Aid, and AA

This package is a verified working corpus for research on the nineteenth-century Washingtonian temperance movement, Alcoholics Anonymous, and mutual-help mechanisms. It intentionally excludes manuscript drafts and any unlawfully obtained material.

## Repository status

**Everything in this directory is the acquisition-time record. `../SOURCES.md` and
`../../CLAUDE.md` are the current authority.** A rights review dated 7 August 2026 governed the
package when it arrived. `metadata/acquisition_status_rights_reviewed.yaml` and
`reports/ACQUISITION_REPORT_updated.md` superseded the original status files beside them, and
all of these are kept as the record of that moment, not as a description of the corpus today.
The review's opening instruction was: *do not add a full-text PDF to the corpus unless the listed
authorization route is met.* Two sources consulted on 10 August 2026, DeGroot (1974) and the
April 1946 *A.A. Grapevine* article, were therefore held as record-only entries under
`../incorporated/`, with a citation, a rights position, the hash of the scan consulted and the
passages verified from it, and no archived document. They still are, with Kurtz (1991),
Iannaccone (1992), Rohr (2011) and *Tricycle* (2019) making six. AAWS pamphlet P-17 had the same
treatment until 13 September 2026, when the Human Author directed that the corpus hold a lawful
copy of every source it can, git-ignored and never committed.

The review also corrects one identification: `Heelas_1999` was the wrong citation and the intended
work is Valverde and White-Mair (1999). Neither is cited by the manuscript.

**This corpus is now fully incorporated.** On 9 August 2026 the four acquired items were
reviewed and moved to `../incorporated/`: the three American Temperance Union documents and the
source record for AA pamphlet P-17. `../SOURCES.md` records what each now supports.

Both pending journal articles were obtained by hand on 10 August 2026 and read in full, so
nothing here is unread. (`sources/pending/` was emptied; an empty directory is not tracked by
Git, so a fresh clone does not have it.) What is left is this package's own
provenance: the acquisition reports, the metadata, and the incorporation instructions.

The AA pamphlet's PDF and OCR were deleted rather than moved on 9 August 2026. It is copyrighted
AAWS literature and this repository is public, so only the citation record travelled to
`../incorporated/`; since 13 September 2026 the official file is held there, git-ignored.

Everything still under `research/staged/` remains **staged research, not incorporated manuscript
evidence**. Presence here does not mean a source has been read, cited, or relied on. Before
incorporating an item, review it, record its status in `../SOURCES.md`, and update the relevant
manuscript notes and project log explicitly.

The corpus was acquired on 2026-08-04 and relocated into `research/staged/` on 2026-08-05.
The former delivery-container name (`corpus_build 2`, also described as
`corpus_build_2`) was removed from the repository layout. Its contents were copied directly
to this directory without changing their relative paths; the acquisition metadata and
report remain authoritative for source-level provenance.

On 2026-08-06, Golub and Jackson (2010) and the project's original Maxwell (1950)
files were placed under `../incorporated/` because both works were already read and used.
The duplicate staged Maxwell package was removed rather than merged. Neither source is part
of the staged corpus now.

## What the package included when it arrived

- Three public-domain American Temperance Union documents downloaded from Internet Archive, with searchable text.
- The 2024 AA pamphlet *A.A. Tradition: How It Developed*, retained as staged and subject to the project's source-policy and licensing review.
- Per-item citation, metadata, and use notes.
- Verified records for two open-access PMC research articles whose web delivery could not be downloaded as a stable PDF in this run; their authoritative full-text URLs are preserved rather than falsely recording an HTML interstitial as a PDF.
- A research ledger for high-priority sources that require library, controlled-digital-lending, or further location work.

## Status vocabulary

- `acquired`: original document is physically included.
- `verified_online`: citation and lawful full-text location confirmed; no local PDF is claimed.
- `restricted`: needs library, purchase, ILL, or controlled lending.
- `pending`: source is known but needs lawful acquisition or further bibliographic work.

## Use and provenance

The three American Temperance Union items are pre-1929 publications supplied by Internet
Archive as public-domain scans. OCR is machine-generated or text-layer extraction and must
be checked against page images before quoting. The AA pamphlet has a separate source-policy
and licensing boundary. See `reports/ACQUISITION_REPORT.md` and
`agent/SOURCE_INCORPORATION_AGENT.md`.
