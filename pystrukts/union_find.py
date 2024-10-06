'''
Union-Find Disjoint Set module.

This module implements a Union-Find Disjoint Set data structure.
'''

class UnionFind:
    '''
    Union-Find Disjoint Set Class.

    Attributes:
        parents (list): The parent nodes of the elements.
        ranks (list): The ranks of the elements.
        sizes (list): The sizes of the sets.
        numdisjoint (int): The number of disjoint sets.

    Methods:
        `find(x: int)`: Find the parent of the element.
        `union(a: int, b: int)`: Union two elements.
        `size(x: int)`: Get the size of the set containing the element.
    '''

    def __init__(self, n):
        '''
        Initialize the UFDS.

        Args:
            n (int): The number of elements.
        '''

        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.numdisjoint = n

    def find(self, x):
        '''
        Find the parent of the element.

        Args:
            x (int): The element.

        Returns:
            int: The parent of the element.
        '''

        x_parent = x
        children = []
        while x_parent != self.parents[x_parent]:
            children.append(x_parent)
            x_parent = self.parents[x_parent]
        for c in children:
            self.parents[c] = x_parent
        return x_parent

    def union(self, a, b):
        '''
        Union two elements.

        Args:
            a (int): The first element.
            b (int): The second element.
        '''

        a_parent = self.find(a)
        b_parent = self.find(b)

        if a_parent == b_parent:
            return

        if self.ranks[a_parent] < self.ranks[b_parent]:
            self.parents[a_parent] = b_parent
            self.sizes[b_parent] += self.sizes[a_parent]

        elif self.ranks[b_parent] < self.ranks[a_parent]:
            self.parents[b_parent] = a_parent
            self.sizes[a_parent] += self.sizes[b_parent]

        else:
            self.parents[b_parent] = a_parent
            self.ranks[a_parent] += 1
            self.sizes[a_parent] += self.sizes[b_parent]

        self.numdisjoint -= 1

    def size(self, x):
        '''
        Get the size of the set containing the element.

        Args:
            x (int): The element.

        Returns:
            int: The size of the set containing the element.
        '''

        return self.sizes[self.find(x)]
