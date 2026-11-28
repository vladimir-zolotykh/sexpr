#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from typing import Iterator
import re
import warnings


class Symbol:
    _symbols: dict[str, "Symbol"] = {}

    def __new__(cls, name: str, pat: str = None):
        if name not in cls._symbols:
            sym = super().__new__(cls)
            sym.name = name
            sym.pat = f"(?P<{name}>{pat})"
            cls._symbols[name] = sym
        else:
            if pat is not None:
                warnings.warn(f"{pat!r} not used")
            # pat is None
            sym = cls._symbols[name]
        return sym

    def __eq__(self, other) -> bool:
        if isinstance(other, type(self)):
            return self.name == other.name
        else:
            return NotImplemented

    def __repr__(self):
        return f"Symbol({self.name!r})"

    @classmethod
    def masterpat(cls) -> str:
        return "|".join(val.pat for val in cls._symbols.values())


class Token:
    def __init__(self, sym: Symbol, val=None):
        self.sym = sym
        self.val = val

    def __eq__(self, other) -> bool:
        if isinstance(other, __class__):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented

    def __repr__(self):
        return f"{type(self).__name__}({repr(self.sym)}, {self.val!r})"


NUM = Symbol("NUM", r"\d+")
WS = Symbol("WS", r"\s+")
PLUS = Symbol("PLUS", r"\+")
LPAREN = Symbol("LPAREN", r"\(")
RPAREN = Symbol("RPAREN", r"\)")
MINUS = Symbol("MINUS", r"-")
MUL = Symbol("MUL", r"\*")
DIV = Symbol("DIV", r"/")


def iter_tokens(sexpr: str) -> Iterator[Token]:
    for match in re.finditer(Symbol.masterpat(), sexpr):
        if (grp := match.lastgroup) != "WS":
            yield Token(Symbol(grp), val=match.group(grp))


if __name__ == "__main__":
    for k in iter_tokens("2 + (3 * 4) + 5"):
        print(k)
