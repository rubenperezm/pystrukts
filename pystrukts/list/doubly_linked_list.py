# pylint: disable=duplicate-code
'''
Doubly Linked List Module.

This module implements a Doubly Linked List and Node data structures.
'''

from dataclasses import dataclass

@dataclass
class DoublyLinkedNode:
    '''
    DoublyLinkedNode Class.

    Attributes:
        data (any): The data stored in the node.
        prev (DoublyLinkedNode): The previous node in the list.
        next (DoublyLinkedNode): The next node in the list.

    Methods:
        `__str__()`: Return the string representation of the node.
    '''

    data: any = None
    prev: 'DoublyLinkedNode' = None
    next: 'DoublyLinkedNode' = None

    def __str__(self):
        return f"DoublyLinkedNode({self.data}){' <-> ' + str(self.next) if self.next else ''}"

@dataclass
class DoublyLinkedList:
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
        `__next__()`: Return the next element in the list.
        `iscircular()`: Check if the list is circular.
        `insert(data: any, index: int)`: Insert data at the specified index.
        `append(data: any)`: Append data to the end of the list.
        `appendleft(data: any)`: Append data to the beginning of the list.
        `remove(index: int)`: Remove data at the specified index.
        `pop()`: Remove data from the end of the list.
        `popleft()`: Remove data from the beginning of the list.
        `get(index: int)`: Get data at the specified index.
        `index(data: any)`: Get the index of the specified data.
        `clear()`: Clear the list.
    '''

    __head: 'DoublyLinkedNode' = None
    __tail: 'DoublyLinkedNode' = None
    __length: int = 0
    __circular: bool = False

    def __init__(self, circular: bool = False):
        '''
        Initialize the DoublyLinkedList.

        Args:
            circular (bool): Whether the list is circular.

        Returns:
            out (DoublyLinkedList): The DoublyLinkedList instance.
        '''

        self.__head = None
        self.__tail = None
        self.__length = 0
        self.__circular = circular

    def __str__(self):
        return f"DoublyLinkedList({self.__head})"

    def __len__(self):
        return self.__length

    def __iter__(self):
        '''
        Return an iterator for the list.

        Returns:
            out (Iterator): The iterator for the list.

        Yields:
            out (any): The data in the list.
        '''

        current_node = self.__head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next

    def iscircular(self):
        '''
        Check if the list is circular.

        Returns:
            out (bool): Whether the list is circular.
        '''

        return self.__circular

    def insert(self, data: any, index: int):
        '''
        Insert data at the specified index.

        Args:
            data (any): The data to be inserted.
            index (int): The index to insert the data.
        
        Raises:
            IndexError: If the index is out of bounds.
        '''

        if index < 0:
            index = self.__length + index + 1

        if index < 0 or index > self.__length:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.appendleft(data)
            return

        if index == self.__length:
            self.append(data)
            return

        new_node = DoublyLinkedNode(data)

        current_node = self.__head
        for _ in range(index - 1):
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next.prev = new_node
        current_node.next = new_node
        new_node.prev = current_node

        self.__length += 1

    def append(self, data: any):
        '''
        Append data to the end of the list.

        Args:
            data (any): The data to be appended.
        '''

        new_node = DoublyLinkedNode(data)

        if self.__length == 0:
            self.__head = new_node
            self.__tail = new_node

        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node

        if self.__circular:
            self.__tail.next = self.__head
            self.__head.prev = self.__tail

        self.__length += 1

    def appendleft(self, data: any):
        '''
        Append data to the beginning of the list.

        Args:
            data (any): The data to be appended.
        '''

        new_node = DoublyLinkedNode(data)

        if self.__length == 0:
            self.__head = new_node
            self.__tail = new_node

        else:
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node

        if self.__circular:
            self.__tail.next = self.__head
            self.__head.prev = self.__tail

        self.__length += 1

    def remove(self, index: int):
        '''
        Remove data at the specified index.

        Args:
            index (int): The index to remove the data.

        Returns:
            out (any): The removed data.

        Raises:
            IndexError: If the index is out of bounds.
        '''

        if index < 0:
            index = self.__length + index

        if index < 0 or index >= self.__length:
            raise IndexError("Index out of bounds")

        if index == 0:
            return self.popleft()

        if index == self.__length - 1:
            return self.pop()

        current_node = self.__head
        for _ in range(index - 1):
            current_node = current_node.next

        removed_node = current_node.next
        current_node.next = removed_node.next
        current_node.next.prev = current_node
        removed_node.next = None
        removed_node.prev = None

        self.__length -= 1

        return removed_node.data

    def pop(self):
        '''
        Extract data from the end of the list.

        Returns:
            out (any): The extracted data.

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
            removed_node = self.__tail
            self.__tail = self.__tail.prev
            self.__tail.next = removed_node.next

            if self.__circular:
                self.__head.prev = self.__tail

        self.__length -= 1

        return removed_node.data

    def popleft(self):
        '''
        Extract data from the beginning of the list.

        Returns:
            out (any): The extracted data.

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
            self.__head.prev = removed_node.prev

            if self.__circular:
                self.__tail.next = self.__head

        self.__length -= 1

        return removed_node.data

    def get(self, index: int):
        '''
        Get data at the specified index.

        Args:
            index (int): The index to get the data.

        Returns:
            out (any): The data at the specified index.

        Raises:
            IndexError: If the index is out of bounds.
        '''

        if index < 0:
            index = self.__length + index

        if index < 0 or index >= self.__length:
            raise IndexError("Index out of bounds")

        if index < self.__length // 2:
            current_node = self.__head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.__tail
            for _ in range(self.__length - index - 1):
                current_node = current_node.prev

        return current_node.data

    def index(self, data: any):
        '''
        Get the index of the first occurrence of the specified data.

        Args:
            data (any): The data to search for.

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
