#!/usr/bin/env python3
"""Normalize the research corpus and build verification indexes.

Every source now lives in one directory under `research/incorporated/` or
`research/staged/`, named `<ShortAuthor>_<Year>`, holding:

    <Dir>.<ext>                     the document itself, git-ignored
    citation.md                     the bibliographic entry
    metadata.json                   rights, provenance, checksums, sizes
    source_summary.md               what it is and what it may support
    <Dir>_verification-index.json   vocabulary only, tracked

The documents are deliberately not committed. Several are in copyright, the rest are large
public-domain scans that bloat a repository that is public, and none of them is a project
output. What is committed is the record needed to re-acquire the document and prove it is the
same one: a citation, a URL, and a SHA-256.

The verification index is what makes that safe rather than lossy. `tools/check_book.py`
confirms that a chapter citing a source for a subject is citing a work that actually contains
that subject. It does not need the text to do that, only the vocabulary, so each index stores
the sorted set of word tokens and no running prose. That pattern already existed for Kurtz
(1991), which is in copyright and was never stored as full text; this script generalizes it.

An index is only as good as the document it was built from, so each one records the SHA-256 of
its source file. If the file is re-acquired and the hash differs, the index is stale and must be
rebuilt rather than trusted.

Idempotent. Run from anywhere:  python3 tools/build_corpus.py [--check]
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"
INCORP = RESEARCH / "incorporated"

# stem as it appears today -> canonical directory name. The stem is also how
# `tools/check_book.py` used to find the file, so it is kept in metadata for continuity.
REGISTRY = {
    "blair-1888-the-temperance-movement": "Blair_1888",
    "crothers-1911-inebriety": "Crothers_1911",
    "eddy-1887-alcohol-in-history": "Eddy_1887",
    "fatimah-2025-double-well-relapse": "Fatimah_2025",
    "fehlandt-1904-century-of-drink-reform": "Fehlandt_1904",
    "gough-1869-autobiography": "Gough_1869",
    "grosh-1842-washingtonian-pocket-companion": "Grosh_1842",
    "harrison-1860-voice-from-the-washingtonian-home": "Harrison_1860",
    "hawkins-1862-life-of-john-hw-hawkins": "Hawkins_1862",
    "krout-1925-origins-of-prohibition": "Krout_1925",
    "marsh-1866-temperance-recollections": "Marsh_1866",
}

# Directories that already exist but do not follow the convention.
RENAMES = {
    "American_Temperance_Union_Report_1840": "ATU_1840",
    "American_Temperance_Union_Annual_Report_1841": "ATU_1841",
    "American_Temperance_Union_Almanac_1849": "ATU_1849",
    "AA_Tradition_P17": "AAWS_2024_P17",
}

# Rights, recorded per source rather than assumed. Pre-1929 United States publications are
# public domain; the rest are named explicitly.
RIGHTS = {
    "Fatimah_2025": "NIH author manuscript, PMC. Not redistributed here.",
    "Krout_1925": "Published 1925 in the United States; public domain.",
    "AAWS_2024_P17": "Copyrighted AAWS literature. Not redistributed here; cite from aa.org.",
    "Maxwell_1950": "Journal article, 1950. Retyped reproduction, not a scan. Not redistributed here.",
    "Golub_Jackson_2010": "Author-hosted PDF. Not redistributed here.",
    "Kurtz_1991": "In copyright, all rights reserved. Never stored as full text.",
    # Catalogued 16 August 2026. Named here rather than left to DEFAULT_RIGHTS for the same
    # reason as the three below: the default asserts a pre-1929 public-domain position, which
    # is false for a 2023 book. This is the one source whose licence would permit committing
    # the document; it is git-ignored anyway, because the rule is uniform.
    "RecoveryDharma_2023": "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 "
                           "International. Sharing and adaptation permitted with attribution; "
                           "no commercial use. Not committed, per the uniform rule.",
    # Catalogued 10 August 2026. All three are record only: no document is held at any time,
    # which is a stronger condition than the git-ignored majority of the corpus. Naming them
    # here rather than letting DEFAULT_RIGHTS apply matters, because the default asserts a
    # pre-1929 public-domain position that is false for each of them.
    "TwelveAndTwelve_1953": ("Copyrighted AAWS literature, published free per chapter on "
                             "aa.org. Never stored here; cite from aa.org."),
    "Rohr_2011": ("In copyright and in print, all rights reserved. Never stored here. The copy "
                  "consulted was an unauthorized posting; see metadata.json."),
    "KurtzTalk_c1984": ("Transcript of a recorded talk; rights position not established. Never "
                        "stored here."),
}
DEFAULT_RIGHTS = "Pre-1929 United States publication; public domain. Internet Archive scan."

DOC_SUFFIXES = {".pdf", ".txt", ".djvu", ".epub"}
TOKEN = re.compile(r"[a-z0-9''-]+")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def citation_from_ledger(stem: str) -> str | None:
    """Lift the bibliographic paragraph for a source out of research/SOURCES.md.

    SOURCES.md is the authoritative ledger, so the citation is copied from it rather than
    retyped here, which would create a second place for it to drift.
    """
    text = (RESEARCH / "SOURCES.md").read_text(errors="ignore")
    lines = text.splitlines()
    anchor = next((i for i, l in enumerate(lines) if f"`{stem}" in l), None)
    if anchor is None:
        return None
    start = None
    for i in range(anchor, max(-1, anchor - 40), -1):
        if lines[i].lstrip().startswith("**") and "Saved" not in lines[i]:
            start = i
            break
    if start is None:
        return None
    end = start
    while end < len(lines) and lines[end].strip():
        end += 1
    return "\n".join(lines[start:end]).strip()


def registered_subjects() -> list[str]:
    """The multi-word subjects tools/check_book.py checks citations against.

    Read from the checker rather than duplicated, so the two cannot drift apart.
    """
    src = (ROOT / "tools" / "check_book.py").read_text()
    block = re.search(r"^SUBJECTS = \[(.*?)\]", src, re.S | re.M)
    if not block:
        return []
    # Strip comments first. They contain apostrophes ("the book's most-cited source"), which
    # unbalance the quote pairing and otherwise yield separator fragments as if they were
    # subjects.
    body = re.sub(r"#[^\n]*", "", block.group(1))
    found = re.findall(r"'([^']+)'", body)
    return [s for s in found if s.strip(" ,")]


def build_index(doc: Path, work: str, digest: str) -> dict:
    raw = doc.read_text(errors="ignore").lower()
    flat = re.sub(r"\s+", " ", raw)
    vocab = sorted({t for t in TOKEN.findall(raw) if len(t) > 1})
    # A vocabulary set has no word order, so a phrase like "sheer survival value" cannot be
    # confirmed from it. Phrase presence is therefore decided here, against the real text,
    # and recorded. It is a statement about this exact file, which is why the hash is stored
    # beside it: if the document is re-acquired and the hash differs, rebuild rather than trust.
    present = sorted(s for s in registered_subjects() if fuzzy_in(s, flat))
    return {
        "work": work,
        "note": ("Full text NOT stored in this repository. This is a verification index only, "
                 "so tools/check_book.py can confirm that a cited subject appears in the source "
                 "without redistributing it."),
        "source_file": doc.name,
        "source_sha256": digest,
        "words": len(raw.split()),
        "subjects_present": present,
        "subjects_checked": sorted(registered_subjects()),
        "vocab": vocab,
    }


def fuzzy_in(term: str, blob: str, thresh: float = 0.72) -> bool:
    """Presence allowing OCR noise. Mirrors tools/check_book.py's matcher."""
    if term in blob:
        return True
    n = len(term)
    if n == 0 or n > len(blob):
        return False
    step = max(1, n // 4)
    for i in range(0, len(blob) - n, step):
        window = blob[i:i + n]
        hits = sum(1 for a, b in zip(term, window) if a == b)
        if hits / n >= thresh:
            return True
    return False


def ensure_dir(name: str) -> Path:
    d = INCORP / name
    d.mkdir(parents=True, exist_ok=True)
    return d


def move(src: Path, dst: Path) -> None:
    if src.resolve() == dst.resolve():
        return
    try:
        subprocess.run(["git", "mv", str(src), str(dst)], cwd=ROOT,
                       capture_output=True, check=True)
    except Exception:
        shutil.move(str(src), str(dst))


def main() -> int:
    check_only = "--check" in sys.argv
    problems: list[str] = []

    for old, new in RENAMES.items():
        src, dst = INCORP / old, INCORP / new
        if src.is_dir() and not dst.exists():
            if check_only:
                problems.append(f"directory not normalized: {old} -> {new}")
            else:
                move(src, dst)

    # Pull loose documents into their own directories.
    for stem, dirname in REGISTRY.items():
        target = ensure_dir(dirname)
        for doc in sorted(RESEARCH.glob(stem + ".*")):
            if doc.suffix.lower() not in DOC_SUFFIXES:
                continue
            dest = target / (dirname + doc.suffix.lower())
            if check_only:
                problems.append(f"loose document: {doc.name}")
            else:
                move(doc, dest)

    # Normalize document filenames inside every source directory, then write records.
    written = []
    for d in sorted(INCORP.iterdir()):
        if not d.is_dir():
            continue
        docs = [p for p in sorted(d.iterdir()) if p.suffix.lower() in DOC_SUFFIXES]
        for doc in docs:
            want = d / (d.name + doc.suffix.lower())
            if doc != want and not want.exists() and not check_only:
                move(doc, want)
        docs = [p for p in sorted(d.iterdir()) if p.suffix.lower() in DOC_SUFFIXES]

        stem = next((s for s, n in REGISTRY.items() if n == d.name), None)
        citation_file = d / "citation.md"
        if stem and not citation_file.exists() and not check_only:
            cite = citation_from_ledger(stem)
            if cite:
                citation_file.write_text(
                    f"# Citation\n\n{cite}\n\n"
                    f"Copied from `research/SOURCES.md`, which remains authoritative for read\n"
                    f"status and claim support.\n")

        meta_file = d / "metadata.json"
        meta = json.loads(meta_file.read_text()) if meta_file.exists() else {}
        meta.setdefault("id", d.name)
        meta["rights_note"] = RIGHTS.get(d.name, meta.get("rights_note") or DEFAULT_RIGHTS)
        meta["legacy_stem"] = stem or meta.get("legacy_stem")
        meta["documents"] = {}
        for doc in docs:
            meta["documents"][doc.name] = {
                "sha256": sha256(doc), "bytes": doc.stat().st_size,
                "tracked_in_git": False,
            }
        meta["documents_note"] = ("Documents are git-ignored. Re-acquire from the recorded URL "
                                  "and check the SHA-256 above.")
        if not check_only:
            meta_file.write_text(json.dumps(meta, indent=1) + "\n")

        # Verification index, built from the text document when there is one.
        text_doc = next((p for p in docs if p.suffix.lower() == ".txt"), None)
        if text_doc:
            idx_file = d / f"{d.name}_verification-index.json"
            work = (citation_file.read_text(errors="ignore").split("\n\n")[1].strip()
                    if citation_file.exists() and len(citation_file.read_text().split("\n\n")) > 1
                    else d.name)
            work = re.sub(r"[*`]", "", work).replace("\n", " ")[:300]
            digest = meta["documents"][text_doc.name]["sha256"]
            stale = True
            if idx_file.exists():
                try:
                    stale = json.loads(idx_file.read_text()).get("source_sha256") != digest
                except Exception:
                    stale = True
            if stale:
                if check_only:
                    problems.append(f"verification index missing or stale: {d.name}")
                else:
                    idx_file.write_text(json.dumps(build_index(text_doc, work, digest)) + "\n")
                    written.append(d.name)

    if check_only:
        for p in problems:
            print("FAIL: " + p)
        print(f"\n{len(problems)} corpus problems")
        return 1 if problems else 0

    print(f"indexes written or refreshed: {len(written)}")
    for name in written:
        print("  " + name)
    print("corpus normalized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
