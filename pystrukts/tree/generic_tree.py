'''
Generic tree module.

This module contains the implementation of a generic tree with an optional number of children.
'''

from dataclasses import dataclass
from warnings import warn
from typing import Any

@dataclass
class GenericTree:
    '''
    Generic tree class.

    This class represents a generic tree with an optional number of children.
    '''
    def __init__(self, data: Any, max_children: int = 0):
        '''
        Initializes the tree. If max_children is less than 2,
        there are no restrictions on the number of children.

        Args:
            data (Any): The data of the root node.
            max_children (int): The maximum number of children the node can have.
        '''
        self.data = data
        self.children = []

        if max_children == 2:
            warn("Binary trees are better represented using the BinaryTree class.")

        self.max_children = int(max_children) if max_children > 1 else None

    def n_children(self) -> int:
        '''
        Returns the number of children of the node.

        Returns:
            int: The number of children of the node.
        '''
        return len(self.children)

    def add_child(self, data: Any) -> None:
        '''
        Adds a child to the node.

        Args:
            child (GenericTree): The child to be added.
        '''

        if self.max_children is not None and self.n_children() >= self.max_children:
            warn(f"Child not appended as node already has {self.max_children} children.")
        else:
            new_node = GenericTree(data, self.max_children)
            self.children.append(new_node)

    def remove_child(self, index: int) -> None:
        '''
        Removes a child from the node.

        Args:
            index (int): The index of the child to be removed.
        '''
        self.children.pop(index)

    def get_children(self) -> list:
        '''
        Returns the children of the node.

        Returns:
            list: The children of the node.
        '''
        return self.children.copy()

    def get_child(self, index: int) -> 'GenericTree':
        '''
        Returns a child of the node.

        Args:
            index (int): The index of the child to be returned.

        Returns:
            GenericTree: The child of the node.
        '''
        return self.children[index]

    def is_leaf(self) -> bool:
        '''
        Returns whether the node is a leaf or not.

        Returns:
            bool: True if the node is a leaf, False otherwise.
        '''
        return self.n_children() == 0
