import pytest
from calculator import add, sub, mul, div, exp

def test_add():
    assert add(2, 3) == 5

def test_add_neg():
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 3) == 2

def test_sub_big_from_small():
    assert sub(0, 5) == -5

def test_div():
    assert div(10, 2) == 5

def test_div_by_zero():
    assert div(5, 0) == "undefined"

def test_div_by_one():
    assert div(30, 1) == 30

def test_mul():
    assert mul(3, 4) == 12

def test_mul_neg():
    assert mul(-2, 3) == -6

def test_exp():
    assert exp(2, 3) == 8

def test_exp2():
    assert exp(5, 0) == 1