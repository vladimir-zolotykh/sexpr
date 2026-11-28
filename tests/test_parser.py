from parser import Parser
from node import Node
import pytest


def test_parser_node():
    n: Node = Parser().parse("2 + (3 * 4) + 5")
    assert str(n) == "Plus(Plus(NUM(2), Mul(NUM(3), NUM(4))), NUM(5))"


@pytest.mark.parametrize(
    "sexpr",
    [
        "2 + (3 * 4) + 5",
        "2 + ((12 * 3) / 3) + 5",
    ],
)
def test_parser_float(sexpr):
    n: Node = Parser().parse(sexpr)
    assert float(n) == eval(sexpr)
