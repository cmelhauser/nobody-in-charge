#!/usr/bin/env bash
# Run what continuous integration runs, in the same order, on this machine.
#
# The workflow in .github/workflows/ci.yml has four jobs, split by whether a step needs a
# network and by whether it depends on the Python version. `checks` below is not a fourth
# workflow job but a local shorthand for unit-tests and checkers run together:
#
#   lint         every push and pull request, needs ruff and shellcheck
#   unit-tests   every push and pull request, needs pip and nothing else
#   checkers     every push and pull request, needs pip and nothing else
#   checks       unit-tests and checkers together
#   documents    main and on demand, needs pandoc, tectonic and TeX Gyre Pagella
#
# Run it from anywhere: it changes to the repository root itself. It writes only what the
# steps it runs write (build outputs, regenerated reports, the coverage data file).
#
# Exit status: 0 when every step that ran passed and at least one ran, even if a job was
# skipped for a missing toolchain (that is reported as NOT RUN); 1 when a step failed or when
# nothing ran at all; 2 for an unrecognised job name.
#
# Usage:
#   tools/run_ci_locally.sh                 all four jobs
#   tools/run_ci_locally.sh lint            the lint job only
#   tools/run_ci_locally.sh unit-tests      pytest and the model hash only
#   tools/run_ci_locally.sh checkers        the checker scripts only
#   tools/run_ci_locally.sh checks          unit-tests and checkers together
#   tools/run_ci_locally.sh documents       the rendering job only
#
# A job that could not run is reported as NOT RUN, and a run in which nothing ran at all
# prints "nothing ran" and exits 1, since no check passed.
#
# This is a convenience, not an authority. The workflow file is the authority, and if the
# two drift apart the workflow is right. Keep them in step by hand; nothing enforces it.
#
# CI's lint job also runs actionlint over the workflows, through a GitHub Action this script
# cannot call; locally, workflow syntax is checked only when the pull request runs.
#
# One deliberate difference. CI installs its own toolchain and this does not, because a
# local machine already has one and reinstalling it would be slower and less faithful than
# using what the author actually builds with. That is also the one thing this cannot check:
# whether a fresh runner can obtain pandoc, tectonic and the font.
set -uo pipefail

# The header above is the usage. An unrecognised job used to run nothing at all and still
# print "local CI clear", so a typo such as "chekers" reported success; it is refused now.
# usage() prints the header comment: from line 2 down to the line that starts the shell
# options, with that line dropped and each leading "# " removed. So the header must not
# contain the text that begins that line, and tools/check_docs.py reads the same header to
# confirm that every job implemented below is documented above.
usage() { sed -n '2,/^set -uo pipefail/p' "$0" | sed '$d' | sed 's/^# \{0,1\}//'; }
case "${1:-all}" in
  -h|--help) usage; exit 0 ;;
  all|lint|unit-tests|checkers|checks|documents) ;;
  *) printf 'unknown job: %s\n\n' "$1" >&2; usage >&2; exit 2 ;;
esac

# Everything below assumes the repository root. If this fails, running the checks
# against whatever directory we happen to be in would be worse than not running them.
cd "$(dirname "$0")/.." || { echo "cannot reach the repository root" >&2; exit 1; }

# Prefer the repository's own virtual environment so the pinned dev requirements are used;
# fall back to whatever python3 is on PATH.
PY=python3
[ -x .venv/bin/python ] && PY=.venv/bin/python

# Running tallies. `skipped` collects the reasons a job could not run, "; "-separated, so the
# final verdict can name them instead of reporting a clean pass.
pass=0; fail=0; skipped=""
not_run() { skipped="${skipped:+$skipped; }$1"; echo "$1; skipping"; }

# step NAME CMD...: run CMD under a heading and count it. A failing step does not stop the
# run (this script deliberately does not exit on error), so one invocation reports every
# failure rather than only the first.
step() {
  local name="$1"; shift
  printf '\n\033[1m== %s\033[0m\n' "$name"
  if "$@"; then
    pass=$((pass+1))
  else
    fail=$((fail+1)); printf '\033[31mFAILED: %s\033[0m\n' "$name"
  fi
}

# Fail if model/aa_group_model.py is not the canonical release file. The digest is also pinned
# in .github/workflows/ci.yml, tools/check_docs.py, CLAUDE.md and
# tests/test_release_invariants.py, and quoted in the README, the appendix and other documents;
# change every place together or not at all.
model_hash() {
  "$PY" - <<'PYEOF'
import hashlib, pathlib, sys
expected = "c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952"
digest = hashlib.sha256(pathlib.Path("model/aa_group_model.py").read_bytes()).hexdigest()
print("model sha256:", digest)
sys.exit(0 if digest == expected else "model hash changed; see CLAUDE.md")
PYEOF
}

# Fail if either PDF build log reports an overfull box, which means text sitting outside the
# type block. A missing log is skipped, not failed: the build step reports its own errors.
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

# Regenerate the three derived reports (model-choice inventory, release-gate results and
# robustness results) in place. The && chain stops at the first generator that fails.
reports() {
  "$PY" tools/inventory_model_choices.py >/dev/null \
    && "$PY" tools/summarize_release_gate.py >/dev/null \
    && "$PY" tools/summarize_robustness.py >/dev/null \
    && echo "derived reports regenerated"
}

# Build the primer, the book and the paper, retrying each once because a first run can fail
# on a cold cache or a transient fetch. SOURCE_DATE_EPOCH is set for the paper only (the book
# and primer builders set their own); it is exported inside a subshell so it cannot leak
# into later steps.
build_docs() {
  { "$PY" tools/build_primer.py || "$PY" tools/build_primer.py; } \
    && { "$PY" tools/build_book.py || "$PY" tools/build_book.py; } \
    && ( SOURCE_DATE_EPOCH="$("$PY" tools/source_date.py paper)" \
         && export SOURCE_DATE_EPOCH \
         && cd paper \
         && { tectonic anonymity-as-an-aggregation-condition.tex \
              || tectonic anonymity-as-an-aggregation-condition.tex; } )
}

# From here on, each block runs one job. "all" and the "checks" shorthand select several.
job="${1:-all}"

if [ "$job" = all ] || [ "$job" = lint ]; then
  printf '\033[1m--- job: lint ---\033[0m\n'
  # A tool is looked for in the virtual environment first, then on PATH. A missing tool is
  # reported as NOT RUN rather than silently passing.
  RUFF=""
  [ -x .venv/bin/ruff ] && RUFF=.venv/bin/ruff
  [ -z "$RUFF" ] && command -v ruff >/dev/null && RUFF=ruff
  if [ -n "$RUFF" ]; then
    step "python lint" "$RUFF" check .
    # --isolated ignores ruff.toml, so no per-file waiver can reach the canonical model.
    step "canonical model passes the original ruleset, no waiver" \
         "$RUFF" check model/aa_group_model.py --isolated --select E9,F,B
  else
    not_run "ruff not installed: lint not run"
  fi
  SHCK=""
  [ -x .venv/bin/shellcheck ] && SHCK=.venv/bin/shellcheck
  [ -z "$SHCK" ] && command -v shellcheck >/dev/null && SHCK=shellcheck
  if [ -n "$SHCK" ]; then
    step "shell lint" "$SHCK" tools/run_ci_locally.sh
  else
    not_run "shellcheck not installed: shell lint not run"
  fi
fi

if [ "$job" = all ] || [ "$job" = checks ] || [ "$job" = unit-tests ]; then
  printf '\033[1m--- job: unit-tests ---\033[0m\n'
  # --cov enforces the coverage floor set in .coveragerc, so a drop fails this step.
  step "tests and the 100 per cent coverage gate" \
       "$PY" -m pytest --cov --cov-report=term-missing -q
  # Types: tools/ must be fully annotated, tests/ only has to be free of type errors. mypy.ini
  # holds the settings; model/ is not checked because annotating it would change its hash.
  step "types: tools fully annotated" "$PY" -m mypy --disallow-untyped-defs tools
  step "types: tests" "$PY" -m mypy tests
  # pylint scores tools/ and tests/ at 10.00/10 under .pylintrc; any message fails the step.
  step "pylint 10/10" "$PY" -m pylint tools tests
  step "canonical model hash" model_hash
fi

if [ "$job" = all ] || [ "$job" = checks ] || [ "$job" = checkers ]; then
  printf '\033[1m--- job: checkers ---\033[0m\n'
  step "corpus drift"                "$PY" tools/build_corpus.py --check
  step "portability"                 "$PY" tools/check_portability.py
  step "book-level checks"           "$PY" tools/check_book.py
  step "documentation matches the tree" "$PY" tools/check_docs.py
  step "derived reports"             reports
  # Omits only the six checks that need a rendered PDF; the documents job runs the full gate.
  step "release gate, less artifacts" "$PY" tools/check_release.py --skip-artifacts
fi

if [ "$job" = all ] || [ "$job" = documents ]; then
  printf '\n\033[1m--- job: documents ---\033[0m\n'
  if ! command -v pandoc >/dev/null || ! command -v tectonic >/dev/null; then
    not_run "pandoc or tectonic missing: the documents job not run"
  else
    # Informational here: another font does not make a build wrong, only unable to match CI.
    step "font files match CI's (reports only)" "$PY" tools/check_fonts.py
    step "derived reports"     reports
    # Rendering comes before the gate: the gate requires each PDF to be at least as new as the
    # sources feeding it, so running it first would fail on the files about to be rebuilt.
    step "build all three PDFs" build_docs
    step "no text outside the type block" overfull_gate
    step "PDFs are sound documents" "$PY" tools/check_pdfs.py
    step "documentation, including page counts" "$PY" tools/check_docs.py
    step "full release gate"   "$PY" tools/check_release.py
    # Slow tests run here and in the release workflow only: they repeat the gate and the
    # builds, so the pull-request jobs and CI's documents job skip them. NIC_SLOW_TESTS=1 is
    # what un-skips them.
    step "slow integration tests" env NIC_SLOW_TESTS=1 "$PY" -m pytest tests/test_tools_integration.py -q
  fi
fi

# Verdict. A failure always wins; otherwise the wording depends on whether anything was skipped.
printf '\n\033[1m%d passed, %d failed\033[0m\n' "$pass" "$fail"
[ "$fail" -eq 0 ] || exit 1
# A job that could not run is not a job that passed, so say so where the verdict is read.
if [ $((pass + fail)) -eq 0 ]; then
  echo "nothing ran${skipped:+; NOT RUN: $skipped}"
  exit 1
elif [ -n "$skipped" ]; then
  echo "local CI clear for what ran; NOT RUN: $skipped"
else
  echo "local CI clear"
fi
