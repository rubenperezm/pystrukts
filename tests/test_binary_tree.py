import pytest
from pystrukts.tree import BinaryTree

def test_initialization():
    tree = BinaryTree(1)
    assert tree.data == 1
    assert tree.left is None
    assert tree.right is None

    tree2 = BinaryTree(2)
    assert tree2.data == 2
    assert tree2.left is None
    assert tree2.right is None

def test_initialization_error():
    with pytest.raises(TypeError):
        BinaryTree()

def test_add_child():
    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(3)

    assert tree.left.data == 2
    assert tree.right.data == 3
    

def test_remove_child():
    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(3)

    del tree.left
    assert tree.left is None

    del tree.right
    assert tree.right is None

def test_is_leaf():
    tree = BinaryTree(1)
    assert tree.is_leaf() == True

    tree.left = BinaryTree(2)
    assert tree.is_leaf() == False

    tree.left.left = BinaryTree(3)
    assert tree.left.is_leaf() == False
    assert tree.is_leaf() == False

    del tree.left.left
    assert tree.left.is_leaf() == True
    assert tree.is_leaf() == False

    tree.left = None
    assert tree.is_leaf() == True