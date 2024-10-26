'''
Fenwick Tree implementation in Python.

This module contains the implementation of Fenwick Trees, as well as two extensions of it:
- Range Update Point Query (RUPQ)
- Range Update Range Query (RURQ)
'''

from typing import List

class FenwickTree:
    '''
    Fenwick Tree implementation in Python.

    Attributes:
    - n: int - the size of the Fenwick Tree
    - ftree: list - the Fenwick Tree itself

    Methods:
    - lsone(s: int) -> int: returns the least significant bit of s
    - query(i: int, j: int) -> int: returns the sum of the elements in the range [i, j]
    - update(i: int, v: int): updates the element at index i with value v
    - select(k: int) -> int: returns the index of the k-th element in the Fenwick Tree
    '''
    def __init__(self, f: List[int]):
        self.n = len(f)
        self.ftree = [0] * (self.n + 1)

        for i in range(1, self.n + 1):
            self.ftree[i] += f[i - 1]
            if i + self._lsone(i) <= self.n:
                self.ftree[i + self._lsone(i)] += self.ftree[i]

    def _lsone(self, s: int) -> int:
        '''
        Returns the least significant bit of s.

        Args:
            s (int): The number to get the least significant bit from.

        Returns:
            out (int): The least significant bit of s.
        '''
        return s & -s

    def query(self, i: int, j: int) -> int:
        '''
        Queries the Fenwick Tree for the sum of the elements in the range [i, j].

        Args:
            i (int): The lower bound of the range.
            j (int): The upper bound of the range.

        Returns:
            s (int): The sum of the elements in the range [i, j].
        '''
        if i > 1:
            return self.query(1, j) - self.query(1, i - 1)

        s = 0
        while j > 0:
            s += self.ftree[j]
            j -= self._lsone(j)

        return s

    def update(self, i: int, v: int):
        '''
        Updates the element at index i with value v.

        Args:
            i (int): The index of the element to update.
            v (int): The new value of the element.
        '''

        while i <= self.n:
            self.ftree[i] += v
            i += self._lsone(i)

    def select(self, k: int) -> int:
        '''
        Returns the index of the k-th element in the Fenwick Tree.

        Args:
            k (int): The index of the element to return.

        Returns:
            i (int): The index of the k-th element in the Fenwick Tree.
        '''

        p = 1
        while p*2 <= self.n:
            p *= 2

        i = 0
        while p > 0:
            if k > self.ftree[i + p]:
                k -= self.ftree[i + p]
                i += p
            p //= 2

        return i + 1

class RUPQ:
    '''
    Range Update Point Query (RUPQ) implementation.

    This class extends the Fenwick Tree to support range updates and point queries.

    Attributes:
    - ftree: FenwickTree - the Fenwick Tree used for the range updates

    Methods:
    - query(i: int) -> int: returns the value of the element at index i
    - update(i: int, j: int, v: int): updates the elements in the range [i, j] with value v
    '''
    def __init__(self, n: int):
        self.ftree = FenwickTree([0] * n)

    def query(self, i: int) -> int:
        '''
        Queries the Fenwick Tree for the value of the element at index i.
        
        Args:
            i (int): The index of the element to query.

        Returns:
            s (int): The value of the element at index i.
        '''

        return self.ftree.query(1, i)

    def update(self, i: int, j: int, v: int):
        '''
        Updates the elements in the range [i, j] with value v.

        Args:
            i (int): The lower bound of the range.
            j (int): The upper bound of the range.
            v (int): The value to update the elements with.
        '''

        self.ftree.update(i, v)
        self.ftree.update(j + 1, -v)

class RURQ:
    '''
    Range Update Range Query (RURQ) implementation.

    This class extends the Fenwick Tree to support range updates and range queries.

    Attributes:
    - f: FenwickTree - the Fenwick Tree used for the range updates
    - r: RUPQ - the RUPQ used for the range queries

    Methods:
    - query(i: int, j: int) -> int: returns the sum of the elements in the range [i, j]
    - update(i: int, j: int, v: int): updates the elements in the range [i, j] with value v
    '''

    def __init__(self, n: int):
        self.ftree = FenwickTree([0] * n)
        self.rupq = RUPQ(n)

    def query(self, i: int, j: int) -> int:
        '''
        Queries the Fenwick Tree for the sum of the elements in the range [i, j].

        Args:
            i (int): The lower bound of the range.
            j (int): The upper bound of the range.

        Returns:
            s (int): The sum of the elements in the range [i, j].
        '''

        if i > 1:
            return self.query(1, j) - self.query(1, i - 1)
        return self.rupq.query(j) * j - self.ftree.query(1, j)

    def update(self, i: int, j: int, v: int):
        '''
        Updates the elements in the range [i, j] with value v.

        Args:
            i (int): The lower bound of the range.
            j (int): The upper bound of the range.
            v (int): The value to update the elements with.
        '''

        self.rupq.update(i, j, v)
        self.ftree.update(i, v * (i - 1))
        self.ftree.update(j + 1, -1 * v * j)
