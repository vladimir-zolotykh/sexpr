#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from typing import Iterator
import re
from textwrap import dedent


class Token:
    _tokens = {}

    def __new__(cls, name, val=None, pat=None):
        tok = None
        if name not in cls._tokens:
            tok = super().__new__(cls)
            tok.name = name
            tok.val = val
            tok.pat = pat
            cls._tokens[name] = tok
        else:
            tok = cls._tokens[name]
        if tok.val is None and val is not None:
            tok.val = val
        if name == "NUM" and name in cls._tokens:
            del cls._tokens[name]
        return tok

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
    for k, v in tokens.items():
        Token(k, pat=v)
    return "|".join(tokens.values())


def test_masterpat():
    assert (
        masterpat()
        == "(?P<NUM>\\d+)|(?P<WS>\\s+)|(?P<PLUS>\\+)|(?P<LPAREN>\\()|(?P<RPAREN>\\))|(?P<MINUS>-)|(?P<MUL>\\*)|(?P<DIV>/)"
    )


def test_num():
    num = Token("NUM", pat=r"(?P<NUM>\d+)", val=6)
    assert str(num) == "NUM(6)"
    num = Token("NUM", pat=r"(?P<NUM>\d+)", val=10)
    assert str(num) == "NUM(10)"


def test_new_token(capsys):
    ws1 = Token("WS", pat=r"(?P<WS>\s+)")
    ws2 = Token("WS", pat=r"(?P<WS>\s+)")
    assert ws1 is ws2


def iter_tokens(sexpr: str) -> Iterator[Token]:
    for match in re.finditer(masterpat(), sexpr):
        if (grp := match.lastgroup) != "WS":
            yield Token(match.lastgroup, val=match.group(grp))


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
