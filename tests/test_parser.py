from parser import Parser
from node import Node
import pytest


def test_parser():
    n: Node = Parser().parse("2 + (3 * 4) + 5")
    assert str(n) == "Plus(Plus(NUM(2), Mul(NUM(3), NUM(4))), NUM(5))"
