import re
import pytest
from textwrap import dedent
from iter_tokens import Token, masterpat, iter_tokens


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
