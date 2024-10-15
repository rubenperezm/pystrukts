import pytest
from pystrukts.tree import BinarySearchTree

def _inorder(tree: 'BinarySearchTree'):
    if tree is None:
        return []

    return _inorder(tree.left) + [tree.data] + _inorder(tree.right)


def test_initialization():
    tree = BinarySearchTree(1)
    assert tree.data == 1
    assert tree.left is None
    assert tree.right is None

    tree2 = BinarySearchTree(2)
    assert tree2.data == 2
    assert tree2.left is None
    assert tree2.right is None

def test_initialization_error():
    with pytest.raises(TypeError):
        BinarySearchTree()

def test_add_child():
    tree = BinarySearchTree(1)
    tree.left = BinarySearchTree(2)
    tree.right = BinarySearchTree(3)

    assert tree.left.data == 2
    assert tree.right.data == 3
    

def test_remove_child():
    tree = BinarySearchTree(1)
    tree.left = BinarySearchTree(2)
    tree.right = BinarySearchTree(3)

    del tree.left
    assert tree.left is None

    tree.right = None
    assert tree.right is None

def test_is_leaf():
    tree = BinarySearchTree(1)
    assert tree.is_leaf() == True

    tree.left = BinarySearchTree(2)
    assert tree.is_leaf() == False

    tree.left.left = BinarySearchTree(3)
    assert tree.left.is_leaf() == False
    assert tree.is_leaf() == False

    del tree.left.left
    assert tree.left.is_leaf() == True
    assert tree.is_leaf() == False

    tree.left = None
    assert tree.is_leaf() == True

def test_insert():
    tree = BinarySearchTree(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(0)
    tree.insert(-1)
    tree.insert(5)

    assert _inorder(tree) == [-1, 0, 1, 2, 3, 5]

def test_search():
    tree = BinarySearchTree(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(0)
    tree.insert(-1)
    tree.insert(5)

    assert tree.search(1) == True
    assert tree.search(2) == True
    assert tree.search(3) == True
    assert tree.search(0) == True
    assert tree.search(-1) == True
    assert tree.search(5) == True
    assert tree.search(4) == False
    assert tree.search(-2) == False

    tree.delete(1)
    assert tree.search(1) == False
    assert tree.search(2) == True
    assert tree.search(3) == True
    assert tree.search(0) == True
    assert tree.search(-1) == True
    assert tree.search(5) == True

def test_delete():
    tree = BinarySearchTree(1)
    tree.insert(5)
    tree.insert(0)
    tree.insert(-1)
    tree.insert(4)
    tree.insert(3)

    tree = tree.delete(1)
    assert _inorder(tree) == [-1, 0, 3, 4, 5]
    assert tree.data == 3

    tree = tree.delete(0)
    assert _inorder(tree) == [-1, 3, 4, 5]

    tree = tree.delete(5)
    assert _inorder(tree) == [-1, 3, 4]

    tree = tree.delete(3)
    assert _inorder(tree) == [-1, 4]

    tree = tree.delete(4)
    assert _inorder(tree) == [-1]

    tree = tree.delete(-1)
    assert _inorder(tree) == []

