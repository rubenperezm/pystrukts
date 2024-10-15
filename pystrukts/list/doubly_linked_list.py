'''
Doubly Linked List Module.

This module implements a Doubly Linked List and Node data structures.
'''

from dataclasses import dataclass
from typing import Any
from .linked_list import LinkedList

@dataclass
class DoublyLinkedNode:
    '''
    DoublyLinkedNode Class.

    Attributes:
        data (Any): The data stored in the node.
        prev (DoublyLinkedNode): The previous node in the list.
        next (DoublyLinkedNode): The next node in the list.

    Methods:
        `__str__()`: Return the string representation of the node.
    '''

    data: Any = None
    prev: 'DoublyLinkedNode' = None
    next: 'DoublyLinkedNode' = None

    def __str__(self):
        return f"DoublyLinkedNode({self.data}){' <-> ' + str(self.next) if self.next else ''}"

@dataclass
class DoublyLinkedList(LinkedList[DoublyLinkedNode]):
    '''
    DoublyLinkedList Class.

    Attributes:
        __head (DoublyLinkedNode): The head of the list.
        __tail (DoublyLinkedNode): The tail of the list.
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
        super().__init__(DoublyLinkedNode, circular)

    def _link(self, node1: DoublyLinkedNode, node2: DoublyLinkedNode):
        '''
        Link two nodes.
        Link two nodes.

        Args:
            node1 (DoublyLinkedNode): The first node.
            node2 (DoublyLinkedNode): The second node.
        '''

        node1.next = node2
        if node2:
            node2.prev = node1
    