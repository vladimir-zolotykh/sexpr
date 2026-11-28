#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import operator


class Node:
    pass


class Num:
    def __init__(self, val: float):
        self.val = val

    def __repr__(self):
        return str(self.val)

    def __eq__(self, other) -> bool:
        if isinstance(other, Num):
            return self.val == other.val
        else:
            return NotImplemented

    def __float__(self):
        return self.val


class BinaryOp(Node):
    def __init__(self, left: Node, right: Node):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{type(self).__name__}({repr(self.left)}, {repr(self.right)})"

    def __eq__(self, other) -> bool:
        if isinstance(other, type(self)):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented

    def __float__(self):
        return self.op(float(self.left), float(self.right))


class Plus(BinaryOp):
    op = operator.add


class Minus(BinaryOp):
    op = operator.sub


class Mul(BinaryOp):
    op = operator.mul


class Div(BinaryOp):
    op = operator.truediv
