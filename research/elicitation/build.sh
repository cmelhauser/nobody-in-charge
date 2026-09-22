#!/bin/sh
# Build the elicitation packet. Run from this directory:  sh build.sh
# Requires xelatex (the .sty uses fontspec and TeX Gyre Pagella, matching the book).
# Tectonic is used if xelatex is absent: same engine, and it is what the book builds with.
# 5-invitation-email.md is Markdown on purpose and is not built here.
set -e
cd "$(dirname "$0")"
for f in 0-start-here 1-respondent-form 2-recruiting-note 3-response-template 4-collator-notes; do
  if command -v xelatex >/dev/null 2>&1; then
    xelatex -interaction=nonstopmode -halt-on-error "$f.tex" >/dev/null
    xelatex -interaction=nonstopmode -halt-on-error "$f.tex" >/dev/null
  else
    tectonic -X compile "$f.tex" >/dev/null
  fi
  echo "built $f.pdf"
done
rm -f ./*.aux ./*.log ./*.out ./*.toc
