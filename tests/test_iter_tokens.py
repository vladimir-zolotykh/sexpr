import re
import pytest
from textwrap import dedent
from iter_tokens import Token, Symbol, iter_tokens


def test_masterpat():
    assert (
        Symbol.masterpat()
        == "(?P<NUM>\\d+)|(?P<WS>\\s+)|(?P<PLUS>\\+)|(?P<LPAREN>\\()|(?P<RPAREN>\\))|(?P<MINUS>-)|(?P<MUL>\\*)|(?P<DIV>/)"
    )


def test_num():
    num = Token(Symbol("NUM"), val=6)
    assert str(num) == "Token(Symbol('NUM'), 6)"
    num = Token(Symbol("NUM"), val=10)
    assert str(num) == "Token(Symbol('NUM'), 10)"


def test_symbol_argument_not_used():
    with pytest.raises(UserWarning, match="foo not used"):
        Symbol("WS", "foo")
    pat = r"(?P<WS>\s+)"
    with pytest.raises(UserWarning, match=re.escape(pat + " not used")):
        Symbol("WS", pat)


def test_new_symbol2(capsys):
    ws1 = Symbol("WS")
    ws2 = Symbol("WS")
    assert ws1 is ws2


def test_iter_tokens(capsys):
    for tok in iter_tokens("2 + (3 * 4) + 5"):
        print(tok)
    assert capsys.readouterr().out == dedent(
        """\
Token(Symbol('NUM'), '2')
Token(Symbol('PLUS'), '+')
Token(Symbol('LPAREN'), '(')
Token(Symbol('NUM'), '3')
Token(Symbol('MUL'), '*')
Token(Symbol('NUM'), '4')
Token(Symbol('RPAREN'), ')')
Token(Symbol('PLUS'), '+')
Token(Symbol('NUM'), '5')
"""
    )
