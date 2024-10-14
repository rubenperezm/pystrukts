'''
MaxHeap Module.

This module implements a MaxHeap data structure using a list and the heapq library.
It provides methods for inserting, extracting, and peeking at the maximum value in the heap.
'''

from dataclasses import field, dataclass
from typing import Any
import heapq

@dataclass
class MaxHeap:
    '''
    MaxHeap Class.

    Attributes:
        data (list): The internal list that stores the heap's elements.

    Methods:
        `__post_init__()`: Creates the heap from the data.
        `__str__()`: Return the string representation of the heap.
        `push(value: Any)`: Insert a value in the heap.
        `pop()`: Extract the maximum value from the heap.
        `peek()`: Peek the maximum value in the heap.
    '''

    data: list = field(default_factory=list)

    def __post_init__(self):
        '''
        Creates the heap from the data.
        '''
        self.data = [-value for value in self.data]
        heapq.heapify(self.data)

    def __str__(self):
        return f"MaxHeap({[-val for val in self.data]})"

    def push(self, value: Any):
        '''
        Insert a value in the heap.

        Args:
            value (Any): The value to be inserted.
        
        Raises:
            TypeError: If the value is not comparable.
        '''

        heapq.heappush(self.data, -value)

    def pop(self):
        '''
        Extract the maximum value from the heap.

        Returns:
            out (Any): The maximum value in the heap.

        Raises:
            IndexError: If the heap is empty.
        '''
        return -heapq.heappop(self.data)

    def peek(self):
        '''
        Peek the maximum value in the heap.

        Returns:
            out (Any): The maximum value in the heap or `None` if the heap is empty.
        '''
        return -self.data[0]
