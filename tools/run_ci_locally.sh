#!/usr/bin/env bash
# Run what continuous integration runs, in the same order, on this machine.
#
# The workflow in .github/workflows/ci.yml has two jobs, split by whether a step needs a
# network. This mirrors both so the split can be checked before pushing rather than after:
#
#   checks      every push and pull request, needs pip and nothing else
#   documents   main and on demand, needs pandoc, tectonic and TeX Gyre Pagella
#
# Usage:
#   tools/run_ci_locally.sh            both jobs
#   tools/run_ci_locally.sh checks     the fast job only
#   tools/run_ci_locally.sh documents  the rendering job only
#
# This is a convenience, not an authority. The workflow file is the authority, and if the
# two drift apart the workflow is right. Keep them in step by hand; nothing enforces it.
#
# One deliberate difference. CI installs its own toolchain and this does not, because a
# local machine already has one and reinstalling it would be slower and less faithful than
# using what the author actually builds with. That is also the one thing this cannot check:
# whether a fresh runner can obtain pandoc, tectonic and the font.
set -uo pipefail
cd "$(dirname "$0")/.."

PY=python3
[ -x .venv/bin/python ] && PY=.venv/bin/python

pass=0; fail=0
step() {
  local name="$1"; shift
  printf '\n\033[1m== %s\033[0m\n' "$name"
  if "$@"; then
    pass=$((pass+1))
  else
    fail=$((fail+1)); printf '\033[31mFAILED: %s\033[0m\n' "$name"
  fi
}

model_hash() {
  "$PY" - <<'PYEOF'
import hashlib, pathlib, sys
expected = "c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952"
digest = hashlib.sha256(pathlib.Path("model/aa_group_model.py").read_bytes()).hexdigest()
print("model sha256:", digest)
sys.exit(0 if digest == expected else "model hash changed; see CLAUDE.md")
PYEOF
}

overfull_gate() {
  "$PY" - <<'PYEOF'
import pathlib, re, sys
bad = False
for name, log in (("book", "build/pandoc.log"), ("primer", "build/primer-pandoc.log")):
    path = pathlib.Path(log)
    if not path.exists():
        continue
    hits = sorted({ln.strip() for ln in path.read_text(errors="ignore").splitlines()
                   if re.search(r"Overfull .hbox \(\d+\.?\d*pt", ln)})
    print(f"{name}: {len(hits)} overfull boxes")
    for hit in hits:
        print("    " + hit)
    bad |= bool(hits)
sys.exit(1 if bad else 0)
PYEOF
}

reports() {
  "$PY" tools/inventory_model_choices.py >/dev/null \
    && "$PY" tools/summarize_release_gate.py >/dev/null \
    && "$PY" tools/summarize_robustness.py >/dev/null \
    && echo "derived reports regenerated"
}

build_docs() {
  { "$PY" tools/build_primer.py || "$PY" tools/build_primer.py; } \
    && { "$PY" tools/build_book.py || "$PY" tools/build_book.py; } \
    && ( cd paper && { tectonic anonymity-as-an-aggregation-condition.tex \
                        || tectonic anonymity-as-an-aggregation-condition.tex; } )
}

job="${1:-all}"

if [ "$job" = all ] || [ "$job" = lint ]; then
  printf '\033[1m--- job: lint ---\033[0m\n'
  RUFF=""
  [ -x .venv/bin/ruff ] && RUFF=.venv/bin/ruff
  [ -z "$RUFF" ] && command -v ruff >/dev/null && RUFF=ruff
  if [ -n "$RUFF" ]; then
    step "python lint" "$RUFF" check .
    step "canonical model takes no lint waiver" \
         "$RUFF" check model/aa_group_model.py --isolated --select E9,F,B
  else
    echo "ruff not installed; skipping lint"
  fi
  if command -v shellcheck >/dev/null; then
    step "shell lint" shellcheck tools/run_ci_locally.sh
  else
    echo "shellcheck not installed; skipping"
  fi
fi


if [ "$job" = all ] || [ "$job" = checks ]; then
  printf '\033[1m--- job: checks ---\033[0m\n'
  step "tests and the 100 per cent coverage gate" \
       "$PY" -m pytest --cov --cov-report=term-missing -q
  step "canonical model hash"        model_hash
  step "corpus drift"                "$PY" tools/build_corpus.py --check
  step "portability"                 "$PY" tools/check_portability.py
  step "book-level checks"           "$PY" tools/check_book.py
  step "derived reports"             reports
  step "release gate, less artifacts" "$PY" tools/check_release.py --skip-artifacts
fi

if [ "$job" = all ] || [ "$job" = documents ]; then
  printf '\n\033[1m--- job: documents ---\033[0m\n'
  if ! command -v pandoc >/dev/null || ! command -v tectonic >/dev/null; then
    echo "pandoc or tectonic missing; skipping the rendering job"
  else
    step "derived reports"     reports
    step "build all three PDFs" build_docs
    step "no text outside the type block" overfull_gate
    step "PDFs are sound documents" "$PY" tools/check_pdfs.py
    step "full release gate"   "$PY" tools/check_release.py
    step "slow integration tests" env NIC_SLOW_TESTS=1 "$PY" -m pytest tests/test_tools_integration.py -q
  fi
fi

printf '\n\033[1m%d passed, %d failed\033[0m\n' "$pass" "$fail"
[ "$fail" -eq 0 ] || exit 1
echo "local CI clear"
