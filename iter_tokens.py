#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from typing import Iterator
import re


class Token:
    _tokens = {}

    def __new__(cls, name, val=None, pat=None):
        tok = None
        if name not in cls._tokens:
            tok = super().__new__(cls)
            tok.name, tok.val, tok.pat = name, val, pat
            if name != "NUM":
                cls._tokens[name] = tok
        else:
            tok = cls._tokens[name]
        if val is not None:
            tok.val = val
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

NUM = Token("NUM", r"\d+")
WS = Token("WS", r"\s+")
PLUS = Token("PLUS", r"\+")
LPAREN = Token("LPAREN", r"\(")
RPAREN = Token("RPAREN", r"\)")
MINUS = Token("MINUS", r"-")
MUL = Token("MUL", r"\*")
DIV = Token("DIV", r"/")


def iter_tokens(sexpr: str) -> Iterator[Token]:
    for match in re.finditer(masterpat(), sexpr):
        if (grp := match.lastgroup) != "WS":
            yield Token(match.lastgroup, val=match.group(grp))


if __name__ == "__main__":
    for k in iter_tokens("2 + (3 * 4) + 5"):
        print(k)
