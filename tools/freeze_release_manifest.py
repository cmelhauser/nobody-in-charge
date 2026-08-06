#!/usr/bin/env python3
"""Freeze hashes and structural facts before or after a release-gate correction.

This is deliberately independent of the notebook.  It inventories source files,
cached data, and rendered artifacts, records JSON top-level shapes without copying
the data, and hashes every item so a later audit can distinguish reproduction from
agreement with a stale cache.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import platform
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SUFFIXES = {".py", ".md", ".tex", ".ipynb"}
GENERATED_SUFFIXES = {".json", ".pdf"}
SKIP_PARTS = {"__pycache__", "staged"}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def json_shape(path: Path) -> dict:
    try:
        value = json.loads(path.read_text())
    except Exception as exc:
        return {"valid": False, "error": f"{type(exc).__name__}: {exc}"}
    out = {"valid": True, "type": type(value).__name__}
    if isinstance(value, dict):
        keys = list(value)
        out.update(
            top_level_keys=len(keys),
            sample_keys=keys[:20],
            numeric_job_keys=sum(k.replace("|", "").replace("_", "").isdigit() for k in keys),
            has_meta="meta" in value,
            has_result="result" in value,
        )
    elif isinstance(value, list):
        out["length"] = len(value)
    return out


def included(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if any(part in SKIP_PARTS for part in rel.parts):
        return False
    if rel.parts[0] in {"model", "tools", "manuscript", "appendix", "paper", "reference", "plans"}:
        return path.suffix in SOURCE_SUFFIXES | GENERATED_SUFFIXES
    if rel.parts[0] == "research":
        return path.suffix in {".json", ".md"}
    return rel.name in {"README.md", "CLAUDE.md", "BOOK-PLAN.md", "AGENT_VERIFY.md"}


def build(label: str) -> dict:
    files = {}
    for path in sorted(p for p in ROOT.rglob("*") if p.is_file() and included(p)):
        stat = path.stat()
        rel = str(path.relative_to(ROOT))
        item = {
            "sha256": digest(path),
            "bytes": stat.st_size,
            "mtime_utc": dt.datetime.fromtimestamp(stat.st_mtime, dt.timezone.utc).isoformat(),
        }
        if path.suffix == ".json":
            item["json"] = json_shape(path)
        files[rel] = item
    return {
        "schema_version": 1,
        "label": label,
        "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "project_root": str(ROOT),
        "python": sys.version,
        "platform": platform.platform(),
        "file_count": len(files),
        "files": files,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("label", choices=("pre-correction", "post-correction"))
    ap.add_argument("--output")
    args = ap.parse_args()
    default = ROOT / "research" / f"audit-{args.label}-manifest.json"
    out = Path(args.output).resolve() if args.output else default
    payload = build(args.label)
    tmp = out.with_suffix(out.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, out)
    print(f"wrote {out} ({payload['file_count']} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
