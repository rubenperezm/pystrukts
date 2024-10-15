'''
Binary Search Tree.

This module contains the implementation of a binary search tree.
'''

from typing import Any
from .binary_tree import BinaryTree

class BinarySearchTree(BinaryTree):
    '''
    Binary search tree class.

    This class represents a binary search tree. There are no duplicate nodes in the tree.
    '''

    def insert(self, data: Any) -> None:
        '''
        Inserts a new node in the tree.

        Args:
            data (Any): The data of the new node.
        '''
        if data < self.data:
            if self.left is None:
                self.left = BinarySearchTree(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = BinarySearchTree(data)
            else:
                self.right.insert(data)

    def search(self, data: Any) -> bool:
        '''
        Searches for a node in the tree.

        Args:
            data (Any): The data to be searched.

        Returns:
            bool: True if the data is found, False otherwise.
        '''
        if self.data == data:
            return True

        child = self.left if data < self.data else self.right

        if child is None:
            return False

        return child.search(data)

    def _find_successor(self) -> 'BinarySearchTree':
        '''
        Finds the in-order successor of the node.

        Returns:
            BinarySearchTree: The in-order successor of the node.
        '''
        temp = self.right

        while temp.left is not None:
            temp = temp.left

        return temp

    def delete(self, data: Any) -> 'BinarySearchTree':
        '''
        Returns the root of the tree after deleting a node.

        Args:
            data (Any): The data of the node to be deleted.

        Returns:
            BinarySearchTree: The root of the tree after the deletion.
        '''
        if data < self.data:
            if self.left is not None:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right is not None:
                self.right = self.right.delete(data)
        else:
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            temp = self._find_successor()
            self.data = temp.data
            self.right = self.right.delete(temp.data)

        return self
