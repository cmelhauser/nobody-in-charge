#!/bin/sh
# Build the elicitation packet. Run from this directory:  sh build.sh
# Requires xelatex (the .sty uses fontspec and TeX Gyre Pagella, matching the book).
set -e
cd "$(dirname "$0")"
for f in 0-start-here 1-respondent-form 2-recruiting-note 3-response-template 4-collator-notes; do
  xelatex -interaction=nonstopmode -halt-on-error "$f.tex" >/dev/null
  xelatex -interaction=nonstopmode -halt-on-error "$f.tex" >/dev/null
  echo "built $f.pdf"
done
rm -f ./*.aux ./*.log ./*.out ./*.toc
