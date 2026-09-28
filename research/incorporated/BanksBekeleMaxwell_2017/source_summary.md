# Summary

A dynamical-systems model of behaviour change fitted to one problem drinker's clinical data from a
behavioural-treatment trial. The authors build a preliminary ordinary-differential-equation model
of four intra-personal variables, alcohol consumption, norm violation, confidence and a treatment
input, estimate its parameters by iterative weighted least squares with a fitted statistical error
model, and show the iterative process of revising a model against one individual's series.

**Read in full at PubMed Central on 14 September 2026.** What the reading established is recorded
in `research/SOURCES.md`: it is background on dynamic behaviour-change models only, it fits one
patient's daily data, so it demonstrates a method rather than a population result, and it is the
route by which Banks et al. (2014) is cited at a remove, since it describes that paper's method.

The display equations are MathML in the deposit and do not survive rendering to plain text. That
matches how the paper was read: through the authors' term-by-term description of the model rather
than from rendered mathematics. A claim that needs an equation from this paper must be checked
against the published article.

## Note on the directory token

`BanksBekeleMaxwell` rather than `Banks`, for the reason `CohenJohnstonLindner_2023` records: the
paper's bibliography also cites Banks et al. (2014), a different work that this corpus does not
hold, and a bare surname token would let `tools/check_book.py` check a citation of one against the
text of the other.
