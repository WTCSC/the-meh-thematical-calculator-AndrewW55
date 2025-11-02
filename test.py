import pytest
from main import add, sub, mul, div, exp

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 5) == -5

def test_div():
    assert div(10, 2) == 5
    assert div(5, 2) == 2.5

def test_mul():
    assert mul(3, 4) == 12
    assert mul(-2, 3) == -6

def test_exp():
    assert exp(2, 3) == 8
    assert exp(5, 0) == 1