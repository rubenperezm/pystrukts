import pytest
from pystrukts.tree import FenwickTree, RUPQ, RURQ


def test_initialization_ftree():
    f = [0, 1, 0, 1, 2, 3, 2, 1, 1, 0]
    ft = FenwickTree(f)
    assert ft.n == 10
    assert ft.ftree == [0, 0, 1, 0, 2, 2, 5, 2, 10, 1, 1]
    assert ft.query(1, 6) == 7
    assert ft.query(1, 3) == 1
    assert ft.select(7) == 6
    ft.update(5, 1)
    assert ft.query(1, 10) == 12

def test_rupq():
    r = RUPQ(10)
    r.update(2, 9, 7)
    r.update(6, 7, 3)
    assert r.query(1) == 0
    assert r.query(2) == 7
    assert r.query(3) == 7
    assert r.query(4) == 7
    assert r.query(5) == 7
    assert r.query(6) == 10
    assert r.query(7) == 10
    assert r.query(8) == 7
    assert r.query(9) == 7
    assert r.query(10) == 0

def test_rurq():
    r = RURQ(10)
    r.update(2, 9, 7)
    r.update(6, 7, 3)
    assert r.query(3, 5) == 21
    assert r.query(7, 8) == 17