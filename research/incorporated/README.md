# Incorporated sources

Every source the project has obtained lives here in its own directory, named
`<ShortAuthor>_<Year>`. Placement here means the source is part of the project's evidence
record. It does not mean every claim made from it is correct, or that it has been read in full;
`../SOURCES.md` is authoritative for read status and claim support.

## What a source directory holds

```text
<Dir>/<Dir>.pdf                     the document, git-ignored
<Dir>/<Dir>.txt                     its text, git-ignored
<Dir>/citation.md                   the bibliographic entry
<Dir>/metadata.json                 rights, provenance, SHA-256 of each document
<Dir>/source_summary.md             what it is and what it may support
<Dir>/<Dir>_verification-index.json vocabulary and subject presence, committed
```

## Why the documents are not committed

Several sources are in copyright, and this repository is public. The public-domain ones are
large scans that are not project outputs and that dominated the repository's size. And a
checksum with a URL is a stronger provenance record than a copy, because it can be verified
against the original rather than trusted.

So the documents are local working files. Re-acquire any of them from the URL in its
`metadata.json` and check the recorded SHA-256.

## Why that does not weaken citation checking

`tools/check_book.py` confirms that a chapter citing a source for a subject is citing a work
that actually contains that subject. Each verification index carries the source's vocabulary
and, because a vocabulary set has no word order, an explicit list of which registered subjects
the document contains, decided against the real text at build time and stamped with that file's
SHA-256. With no documents present at all, every citation-subject pair still verifies.

If a re-acquired document's hash differs from the recorded one, the index is stale. Rebuild it
rather than trust it:

```bash
python3 tools/build_corpus.py          # normalize layout, refresh stale indexes
python3 tools/build_corpus.py --check   # report drift without changing anything
```

## Notes on individual sources

**Maxwell (1950)** is a retyped reproduction circulated on the web, not a scan of the journal,
and it carries transcription errors. Citations were checked against that transcription, which is
one remove from the journal. It paginates as sheets, not as pp. 410-452, so page references from
it are not reliable.

**AAWS (2024), pamphlet P-17** has no document at all, by decision rather than by accident. It is
copyrighted AA literature distributed as a free official PDF; the record keeps the citation, the
aa.org URL, the file hash and the two passages verified against page images.

**Kurtz (1991)** is in copyright and was never stored as full text. It has always been held as a
verification index, and is the source of the pattern now used for everything.

**Golub and Jackson (2010)** is the mathematical anchor of Part Two. Nothing in the historical
corpus bears on the theorem, and nothing in the theorem bears on the historical mapping.
