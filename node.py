#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


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
            NotImplemented


class Operator(Node):
    def __init__(self, left: Node, right: Node):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{type(self).__name__}({repr(self.left)}, {repr(self.right)})"

    def __eq__(self, other) -> bool:
        if isinstance(other, type(self)):
            return self.__dict__ == other.__dict__
        else:
            NotImplemented


class Plus(Operator):
    pass


class Minus(Operator):
    pass


class Mul(Operator):
    pass


class Div(Operator):
    pass
