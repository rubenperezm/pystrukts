import pytest
from pystrukts import UnionFind

def test_ufds_initialization():
    ufds = UnionFind(5)
    assert ufds.parents == [0, 1, 2, 3, 4]
    assert ufds.ranks == [0, 0, 0, 0, 0]
    assert ufds.sizes == [1, 1, 1, 1, 1]
    assert ufds.numdisjoint == 5

def test_find():
    ufds = UnionFind(5)
    assert ufds.find(3) == 3
    ufds.union(1, 3)
    assert ufds.find(3) == 1

def test_union():
    ufds = UnionFind(5)
    ufds.union(1, 3)

    assert ufds.parents == [0, 1, 2, 1, 4]
    assert ufds.ranks == [0, 1, 0, 0, 0]
    assert ufds.sizes == [1, 2, 1, 1, 1]
    assert ufds.numdisjoint == 4

    ufds.union(2, 4)

    assert ufds.parents == [0, 1, 2, 1, 2]
    assert ufds.ranks == [0, 1, 1, 0, 0]
    assert ufds.sizes == [1, 2, 2, 1, 1]
    assert ufds.numdisjoint == 3

    ufds.union(1, 4)

    assert ufds.parents == [0, 1, 1, 1, 2]
    assert ufds.ranks == [0, 2, 1, 0, 0]
    assert ufds.sizes == [1, 4, 2, 1, 1]
    assert ufds.numdisjoint == 2

    ufds.union(0, 2)

    assert ufds.parents == [1, 1, 1, 1, 2]
    assert ufds.ranks == [0, 2, 1, 0, 0]
    assert ufds.sizes == [1, 5, 2, 1, 1]
    assert ufds.numdisjoint == 1

def test_union_sets():
    ufds = UnionFind(5)
    ufds.union(1, 3)
    ufds.union(1, 4)

    assert ufds.find(1) != ufds.find(0)
    assert ufds.find(1) != ufds.find(2)
    assert ufds.find(1) == ufds.find(3)
    assert ufds.find(1) == ufds.find(4)
    assert ufds.numdisjoint == 3

def test_union_same_set():
    ufds = UnionFind(5)
    ufds.union(1, 3)
    ufds.union(1, 4)

    numdisjoint = ufds.numdisjoint
    parents = ufds.parents.copy()
    ranks = ufds.ranks.copy()
    sizes = ufds.sizes.copy()

    ufds.union(1, 4)

    assert ufds.parents == parents
    assert ufds.ranks == ranks
    assert ufds.sizes == sizes
    assert ufds.numdisjoint == numdisjoint

def test_size():
    ufds = UnionFind(4)
    ufds.union(1, 3)

    assert ufds.size(0) == 1
    assert ufds.size(1) == 2
    assert ufds.size(2) == 1
    assert ufds.size(3) == 2

    ufds.union(1, 2)

    assert ufds.size(0) == 1
    assert ufds.size(1) == 3
    assert ufds.size(2) == 3
    assert ufds.size(3) == 3

    ufds.union(0, 2)
    
    assert ufds.size(0) == 4
    assert ufds.size(1) == 4
    assert ufds.size(2) == 4
    assert ufds.size(3) == 4