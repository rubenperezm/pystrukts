'''
Singly Linked List Module.

This module implements a Singly Linked List and Node data structures.
'''

from dataclasses import dataclass
from typing import Any
from .linked_list import LinkedList

@dataclass
class SinglyLinkedNode:
    '''
    SinglyLinkedNode Class.

    Attributes:
        data (Any): The data stored in the node.
        next (SinglyLinkedNode): The next node in the list.

    Methods:
        `__str__()`: Return the string representation of the node.
    '''

    data: Any = None
    next: 'SinglyLinkedNode' = None

    def __str__(self):
        return f"SinglyLinkedNode({self.data}){' -> ' + str(self.next) if self.next else ''}"

class SinglyLinkedList(LinkedList[SinglyLinkedNode]):
    '''
    SinglyLinkedList Class.

    Attributes:
        __head (SinglyLinkedNode): The head of the list.
        __tail (SinglyLinkedNode): The tail of the list.
        __length (int): The length of the list.
        __circular (bool): Whether the list is circular.

    Methods:
        `__str__()`: Return the string representation of the list.
        `__len__()`: Return the length of the list.
        `__iter__()`: Return an iterator for the list.
        `iscircular()`: Check if the list is circular.
        `_link(node1: Type[T], node2: Type[T])`: Link two nodes.
        `_preprocess_index(index: int)`: Preprocess the index.
        `insert(data: Any, index: int)`: Insert data at the specified index.
        `append(data: Any)`: Append data to the end of the list.
        `appendleft(data: Any)`: Append data to the beginning of the list.
        `remove(index: int)`: Remove data at the specified index.
        `pop()`: Remove data from the end of the list.
        `popleft()`: Remove data from the beginning of the list.
        `get(index: int)`: Get data at the specified index.
        `index(data: Any)`: Get the index of the specified data.
        `clear()`: Clear the list.
    '''

    def __init__(self, circular: bool = False):
        super().__init__(SinglyLinkedNode, circular)

    def _link(self, node1: SinglyLinkedNode, node2: SinglyLinkedNode):
        '''
        Link two nodes.
        Link two nodes.

        Args:
            node1 (SinglyLinkedNode): The first node.
            node2 (SinglyLinkedNode): The second node.
        '''

        node1.next = node2
