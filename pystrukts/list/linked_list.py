'''
Base Linked List Module.

This module implements a Linked List data structure.
'''

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Type, TypeVar, Generic, Any

T = TypeVar('T')

@dataclass
class LinkedList(ABC, Generic[T]):
    '''
    LinkedList Class.

    Attributes:
        __head (Type[T]): The head of the list. T is a node class.
        __tail (Type[T]): The tail of the list. T is a node class.
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

    __head: Type[T] = None
    __tail: Type[T] = None
    __length: int = 0
    __circular: bool = False

    def __init__(self, cls: Type[T], circular: bool = False):
        '''
        Initialize the LinkedList.

        Args:
            circular (bool): Whether the list is circular.
        '''

        self.__cls = cls
        self.__head = None
        self.__tail = None
        self.__length = 0
        self.__circular = circular

    def __str__(self):
        return f"{self.__class__.__name__}({self.__head})"

    def __len__(self):
        return self.__length

    def __iter__(self):
        '''
        Return an iterator for the list.

        Returns:
            out (Iterator): The iterator for the list.

        Yields:
            out (Any): The data in the list.
        '''

        current_node = self.__head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next

    @abstractmethod
    def _link(self, node1: T, node2: T):
        '''
        Link two nodes.

        Args:
            node1 (Type[T]): The first node.
            node2 (Type[T]): The second node.
        '''


    def iscircular(self):
        '''
        Check if the list is circular.

        Returns:
            out (bool): Whether the list is circular.
        '''

        return self.__circular

    def _preprocess_index(self, index: int, insert: bool = False):
        '''
        Preprocess the index.

        Args:
            index (int): The index to preprocess.
            insert (bool): Whether the index is for insertion.
        Returns:
            out (int): The preprocessed index.
        
        Raises:
            IndexError: If the index is out of bounds.
        '''

        ins = 1 if insert else 0

        if index < 0:
            index = self.__length + index + ins

        if index < 0 or ((1 - ins + index) > self.__length):
            raise IndexError("Index out of bounds")

        return index

    def insert(self, data: Any, index: int):
        '''
        Insert data at the specified index.

        Args:
            data (Any): The data to be inserted.
            index (int): The index to insert the data.
        
        Raises:
            IndexError: If the index is out of bounds.
        '''

        index = self._preprocess_index(index, insert=True)

        if index == 0:
            self.appendleft(data)
            return

        if index == self.__length:
            self.append(data)
            return

        new_node = self.__cls(data)

        current_node = self.__head
        for _ in range(index - 1):
            current_node = current_node.next

        self._link(new_node, current_node.next)
        self._link(current_node, new_node)

        self.__length += 1

    def append(self, data: Any):
        '''
        Append data to the end of the list.

        Args:
            data (Any): The data to be appended.
        '''

        new_node = self.__cls(data)

        if self.__length == 0:
            self.__head = new_node
            self.__tail = new_node

        else:
            self._link(self.__tail, new_node)
            self.__tail = new_node

        if self.__circular:
            self._link(self.__tail, self.__head)

        self.__length += 1

    def appendleft(self, data: Any):
        '''
        Append data to the beginning of the list.

        Args:
            data (Any): The data to be appended.
        '''

        new_node = self.__cls(data)

        if self.__length == 0:
            self.__head = new_node
            self.__tail = new_node

        else:
            self._link(new_node, self.__head)
            self.__head = new_node

        if self.__circular:
            self._link(self.__tail, self.__head)

        self.__length += 1

    def remove(self, index: int):
        '''
        Remove data at the specified index.

        Args:
            index (int): The index to remove the data.

        Returns:
            out (Any): The removed data.

        Raises:
            IndexError: If the index is out of bounds.
        '''

        index = self._preprocess_index(index)

        if index == 0:
            return self.popleft()

        if index == self.__length - 1:
            return self.pop()

        current_node = self.__head
        for _ in range(index - 1):
            current_node = current_node.next

        removed_node = current_node.next
        self._link(current_node, removed_node.next)
        removed_node.next = None

        self.__length -= 1

        return removed_node.data

    def pop(self):
        '''
        Extract data from the end of the list.

        Returns:
            out (Any): The extracted data.

        Raises:
            IndexError: If the list is empty.
        '''

        if self.__length == 0:
            raise IndexError("Empty list")

        if self.__length == 1:
            removed_node = self.__head
            self.__head = None
            self.__tail = None

        else:
            current_node = self.__head
            while current_node.next != self.__tail:
                current_node = current_node.next

            removed_node = self.__tail
            self._link(current_node, removed_node.next)
            self.__tail = current_node

        self.__length -= 1

        return removed_node.data

    def popleft(self):
        '''
        Extract data from the beginning of the list.

        Returns:
            out (Any): The extracted data.

        Raises:
            IndexError: If the list is empty.
        '''

        if self.__length == 0:
            raise IndexError("Empty list")

        removed_node = self.__head

        if self.__length == 1:
            self.__head = None
            self.__tail = None

        else:
            self.__head = self.__head.next

            if self.__circular:
                self._link(self.__tail, self.__head)

        self.__length -= 1

        return removed_node.data

    def get(self, index: int):
        '''
        Get data at the specified index.

        Args:
            index (int): The index to get the data.

        Returns:
            out (Any): The data at the specified index.

        Raises:
            IndexError: If the index is out of bounds.
        '''

        index = self._preprocess_index(index)

        current_node = self.__head
        for _ in range(index):
            current_node = current_node.next

        return current_node.data

    def index(self, data: Any):
        '''
        Get the index of the first occurrence of the specified data.

        Args:
            data (Any): The data to search for.

        Returns:
            out (int): The index of the specified data.
        
        Raises:
            ValueError: If the data is not found.
        '''

        current_node = self.__head
        for i in range(self.__length):
            if current_node.data == data:
                return i

            current_node = current_node.next

        raise ValueError("Data not found")

    def clear(self):
        '''
        Remove all data from the list.
        '''

        self.__head = None
        self.__tail = None
        self.__length = 0
