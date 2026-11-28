#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK

from typing import Iterator
from node import Node, Plus, Minus, Div, Mul, Num
from iter_tokens import Token, iter_tokens, NUM, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN


class Parser:
    def __init__(self):
        self.tok: Token | None = None
        self.tokens: Iterator[Token] = None

    def parse(self, sexpr: str) -> Node:
        self.tokens = iter_tokens(sexpr)
        self._advance()
        return self.expr()

    def expr(self) -> Node:
        res: Node = self.term()
        while (tok := self.tok) and tok in (PLUS, MINUS):
            self._consume()
            res = (Plus if tok == PLUS else Minus)(res, self.term())
        return res

    def term(self) -> Node:
        res: Node = self.factor()
        while (tok := self.tok) and tok in (MUL, DIV):
            self._consume()
            res = (Mul if tok == MUL else Div)(res, self.factor())
        return res

    def factor(self) -> Node:
        if self.tok == LPAREN:
            self._consume()
            res = self.expr()
            self._expect(RPAREN)
        else:
            res = Num(float(self.tok.val))
            self._consume()
        return res

    def _advance(self) -> Token:
        self.tok = next(self.tokens, None)
        return self.tok

    def _consume(self) -> None:
        self.tok = next(self.tokens, None)

    def _expect(self, expected: Token) -> None:
        if self.tok != expected:
            raise SyntaxError(f"{self.tok!r} expected {expected}")
        self._consume()


if __name__ == "__main__":
    n: Node = Parser().parse("2 + (3 * 4) + 5")
    print(n)
    print(float(n))
