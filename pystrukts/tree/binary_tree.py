'''
Binary Tree module.

This module contains the implementation of a binary tree.
'''

from typing import Any

class BinaryTree():
    '''
    Binary tree class.

    This class represents a binary tree.
    '''
    def __init__(self, data: Any):
        '''
        Initializes the tree.

        Args:
            data (Any): The data of the root node.
        '''
        self.data = data
        self.__left = None
        self.__right = None

    @property
    def left(self) -> 'BinaryTree':
        '''
        Returns the left child of the node.

        Returns:
            BinaryTree: The left child of the node.
        '''
        return self.__left

    @left.setter
    def left(self, left: 'BinaryTree') -> None:
        '''
        Sets the left child of the node.

        Args:
            left (BinaryTree): The left child of the node.
        '''
        self.__left = left

    @left.deleter
    def left(self) -> None:
        '''
        Deletes the left child of the node.
        '''
        self.__left = None

    @property
    def right(self) -> 'BinaryTree':
        '''
        Returns the right child of the node.

        Returns:
            BinaryTree: The right child of the node.
        '''
        return self.__right

    @right.setter
    def right(self, right: 'BinaryTree') -> None:
        '''
        Sets the right child of the node.

        Args:
            right (BinaryTree): The right child of the node.
        '''
        self.__right = right

    @right.deleter
    def right(self) -> None:
        '''
        Deletes the right child of the node.
        '''
        self.__right = None

    def is_leaf(self) -> bool:
        '''
        Checks whether the node is a leaf.

        Returns:
            bool: True if the node is a leaf, False otherwise.
        '''
        return self.__left is None and self.__right is None
