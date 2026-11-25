#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from typing import Iterator
import re
from textwrap import dedent


class Token:
    def __init__(self, name, val):
        self.name = name
        self.val = val

    def __eq__(self, other) -> bool:
        if isinstance(other, __class__):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented

    def __repr__(self):
        if self.name == "NUM":
            return f"NUM({self.val})"
        else:
            return self.name


def masterpat():
    return "|".join(tokens.values())


def iter_tokens(sexpr: str) -> Iterator[Token]:
    for match in re.finditer(masterpat(), sexpr):
        if (grp := match.lastgroup) != "WS":
            yield Token(match.lastgroup, match.group(grp))


tokens = {
    k: f"(?P<{k}>{v})"
    for k, v in {
        "NUM": r"\d+",
        "WS": r"\s+",
        "PLUS": r"\+",
        "LPAREN": r"\(",
        "RPAREN": r"\)",
        "MINUS": r"-",
        "MUL": r"\*",
        "DIV": r"/",
    }.items()
}


def test_iter_tokens(capsys):
    for tok in iter_tokens("2 + (3 * 4) + 5"):
        print(tok)
    assert capsys.readouterr().out == dedent(
        """\
NUM(2)
PLUS
LPAREN
NUM(3)
MUL
NUM(4)
RPAREN
PLUS
NUM(5)
"""
    )


if __name__ == "__main__":
    for k in iter_tokens("2 + (3 * 4) + 5"):
        print(k)
