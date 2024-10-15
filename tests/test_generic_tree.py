import pytest
from pystrukts.tree import GenericTree

def test_initialization():
    tree = GenericTree(1)
    assert tree.data == 1
    assert tree.max_children is None
    assert tree.n_children() == 0

    tree2 = GenericTree(2, 3)
    assert tree2.data == 2
    assert tree2.max_children == 3
    assert tree2.n_children() == 0

    with pytest.warns(UserWarning):
        tree3 = GenericTree(3, 2)
        assert tree3.data == 3
        assert tree3.max_children == 2
        assert tree3.n_children() == 0

def test_initialization_error():
    with pytest.raises(TypeError):
        GenericTree()

def test_add_child():
    tree = GenericTree(1, 3)
    tree.add_child(2)
    assert tree.n_children() == 1
    assert tree.get_child(0).data == 2

    tree.add_child(3)
    assert tree.n_children() == 2
    assert tree.get_child(1).data == 3

    tree.add_child(4)
    assert tree.n_children() == 3
    assert tree.get_child(2).data == 4

    with pytest.warns(UserWarning):
        tree.add_child(4)
        assert tree.n_children() == 3

    tree.get_child(0).add_child(5)
    assert tree.get_child(0).n_children() == 1
    assert tree.get_child(0).get_children()[0].data == 5

def test_remove_child():
    tree = GenericTree(1, 3)
    tree.add_child(2)
    tree.add_child(3)
    tree.add_child(4)

    tree.remove_child(1)
    assert tree.n_children() == 2
    assert tree.get_child(1).data == 4

    tree.remove_child(0)
    assert tree.n_children() == 1
    assert tree.get_child(0).data == 4

    tree.remove_child(0)
    assert tree.n_children() == 0

def test_get_child():
    tree = GenericTree(1, 3)
    tree.add_child(2)
    tree.add_child(3)
    tree.add_child(4)

    assert tree.get_child(0).data == 2
    assert tree.get_child(1).data == 3
    assert tree.get_child(2).data == 4

def test_negative_index():
    tree = GenericTree(1, 3)
    tree.add_child(2)
    tree.add_child(3)
    tree.add_child(4)

    tree.remove_child(-1)
    assert tree.n_children() == 2
    assert tree.get_child(-1).data == 3

def test_remove_out_of_bounds():
    tree = GenericTree(1, 3)
    tree.add_child(2)
    tree.add_child(3)
    tree.add_child(4)

    with pytest.raises(IndexError):
        tree.remove_child(3)

    with pytest.raises(IndexError):
        tree.remove_child(-4)

def test_get_child_out_of_bounds():
    tree = GenericTree(1, 3)
    tree.add_child(2)
    tree.add_child(3)
    tree.add_child(4)

    with pytest.raises(IndexError):
        tree.get_child(3)

    with pytest.raises(IndexError):
        tree.get_child(-4)

def test_get_children():
    tree = GenericTree(1, 3)
    tree.add_child(2)
    tree.add_child(3)
    tree.add_child(4)

    children = tree.get_children()
    assert children[0].data == 2
    assert children[1].data == 3
    assert children[2].data == 4

def test_is_leaf():
    tree = GenericTree(1, 3)
    assert tree.is_leaf() == True

    tree.add_child(2)
    assert tree.is_leaf() == False

    tree.get_child(0).add_child(3)
    assert tree.get_child(0).is_leaf() == False
    assert tree.is_leaf() == False

    tree.get_child(0).remove_child(0)
    assert tree.get_child(0).is_leaf() == True
    assert tree.is_leaf() == False

    tree.remove_child(0)
    assert tree.is_leaf() == True