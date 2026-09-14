"""Names this project has undertaken not to print, and the test for them.

The names are stored as SHA-256 digests of the lowercased form, so that enforcing the rule
does not require writing the name in the repository: a checker that stored the string it
forbids would publish it.

There is one person. The founder of the organization Recovery Dharma split from in 2019 is
named in `RecoveryDharma_2023` in connection with its collapse, and the project's rule, in
CLAUDE.md and in that source's own metadata, is that he is named nowhere here. The
structural claim, that the predecessor was organized around a founding teacher and the
successor abolished the office, does not need the name, and this project cannot adjudicate
an allegation about a living person. The appendix named him anyway between 16 and 17 August
2026, and it shipped in a rendered PDF before `tools/check_book.py` checked for it.

That check read a fixed list of prose files, and until 14 September 2026 the surname sat in
two verification indexes it never opened. Three tools now use this module:
`tools/build_corpus.py` leaves a withheld word out of every vocabulary it writes,
`tools/check_book.py` looks for one in every tracked text file, and `tools/check_pdfs.py`
looks in the text of each rendered PDF.
"""
from __future__ import annotations

import hashlib
import re

WITHHELD = {
    '56d447a05a7c48cdd011b0485110052b6cf0ecdad090fe4e70d98aae3a8d71be',  # full name
    '4d8d163722179946e84391aa25ab3a73b3a02b3202d0eebd0d0d882e51a1431c',  # surname alone
}

# Both tools' tokenizers keep a possessive or a hyphenated compound as one token, and its
# digest is not the name's, so each piece is tested as well as the whole.
JOINERS = re.compile(r"['’-]")
WORD = re.compile(r"[A-Za-z][A-Za-z'’-]+")


def is_withheld(term: str) -> bool:
    """True if `term`, a word or a two-word phrase, is or contains a withheld name."""
    term = term.lower()
    return any(hashlib.sha256(piece.strip().encode()).hexdigest() in WITHHELD
               for piece in [term, *JOINERS.split(term)])


def prints_withheld(text: str) -> bool:
    """True if any word, or any pair of adjacent words, in `text` is a withheld name.

    Pairs are what catch the full name across a line break, which is how the regression
    test of 17 August 2026 reinserted it.
    """
    words = WORD.findall(text)
    grams = {w.lower() for w in words}
    # Deliberately ragged: the second iterable is one shorter, which is the point of a
    # bigram. strict would raise on every call.
    grams |= {f'{a.lower()} {b.lower()}' for a, b in zip(words, words[1:], strict=False)}
    return any(is_withheld(g) for g in grams)
