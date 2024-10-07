'''
Adjacency list representation of a graph.

This module provides the AdjacencyList class, which
represents an unweighted graph using an adjacency list.
'''

from warnings import warn
from pystrukts.graph import Graph

class AdjacencyList(Graph):
    '''
    Graph representation using adjacency list.

    Attributes:
        num_vertices (int): The number of vertices in the graph.
        directed (bool): True if the graph is directed, False otherwise.
        vertex_list (list): The adjacency list of the graph.

    Methods:
        copy() -> AdjacencyList: Create a copy of the graph.
        _copy_list(vertex_list: list) -> list: Copy the adjacency list.
        _raise_error_if_invalid_vertex(x: int) -> None: Raise an error if the vertex does not exist.
        has_edge(x: int, y: int) -> bool: Check if there is an edge between two vertices.
        neighbors(x: int) -> set: Get the neighbors of a vertex.
        add_edge(x: int, y: int, w: float = None) -> None: Add an edge between two vertices.
        remove_edge(x: int, y: int) -> None: Remove an edge between two vertices.
        add_vertex() -> None: Add an isolated vertex to the graph.
        remove_vertex(x: int) -> None: Remove a vertex from the graph.
    '''

    def __init__(self, num_vertices: int = None, vertex_list: list = None,
                 directed: bool = True) -> None:
        '''
        Initialize the adjacency list.

        Args:
            num_vertices (int): The number of vertices in the graph.
            vertex_list (list): The adjacency list of the graph.
            directed (bool): True if the graph is directed, False otherwise.
        '''
        if not vertex_list and not num_vertices:
            raise ValueError('You must specify either the number of vertices \
                             or the adjacency list.')

        if num_vertices and num_vertices < 0:
            raise ValueError('The number of vertices must be non-negative.')

        if vertex_list and num_vertices:
            warn('The number of vertices will be ignored, as an adjacency list was provided.')

        self.num_vertices = len(vertex_list) if vertex_list else int(num_vertices)
        self.directed = directed
        self._copy_list(vertex_list)

    def copy(self) -> 'AdjacencyList':
        '''
        Create a copy of the graph.

        Returns:
            out (AdjacencyList): The copy of the graph.
        '''

        return AdjacencyList(vertex_list = self.vertex_list, directed = self.directed)

    def _copy_list(self, vertex_list: list) -> list:
        '''
        Copy the adjacency list with floating point values.

        If the graph is undirected and the list is not
        symmetric,the function creates a symmetric list.

        Args:
            vertex_list (list): The list to be copied.
            directed (bool): True if the graph is directed, False otherwise.

        Returns:
            out (list): The list. Each element is a set of vertices.

        Raises:
            ValueError: If a vertex does not exist.
        '''

        self.vertex_list = [set() for _ in range(self.num_vertices)]

        if vertex_list:
            for u in range(self.num_vertices):
                for v in vertex_list[u]:
                    self._raise_error_if_invalid_vertex(v)
                    self.vertex_list[u].add(v)

                    if not self.directed:
                        self.vertex_list[v].add(u)

    def  _raise_error_if_invalid_vertex(self, x: int) -> None:
        '''
        Raise an error if the vertex does not exist.

        Args:
            x (int): The vertex.

        Raises:
            ValueError: If the vertex does not exist.
        '''
        if x >= self.num_vertices or x < 0 or not isinstance(x, int):
            raise ValueError(f'The vertex {x} does not exist.')

    def has_edge(self, x: int, y: int) -> bool:
        '''
        Check if there is an edge between two vertices. 
        If the vertices are the same, the function checks if the vertex has a self-loop.

        Args:
            x (int): The source vertex.
            y (int): The destination vertex.

        Returns:
            out (bool): True if there is an edge between the vertices, False otherwise.

        Raises:
            ValueError: If x or y are not valid vertices.
        '''

        self._raise_error_if_invalid_vertex(x)
        self._raise_error_if_invalid_vertex(y)

        return y in self.vertex_list[x]

    def neighbors(self, x: int) -> set:
        '''
        Get the neighbors of a vertex. 
        If x has a self-loop, the output contains the vertex itself.

        Args:
            x (int): The vertex.

        Returns:
            out (set): The set of neighbors of the vertex.

        Raises:
            ValueError: If x is not a valid vertex.
        '''

        self._raise_error_if_invalid_vertex(x)

        return self.vertex_list[x]

    def add_edge(self, x: int, y: int, w: float = None) -> None:
        '''
        Add an edge between two vertices.

        Args:
            x (int): The source vertex.
            y (int): The destination vertex.
            w (float): The weight. Not used.

        Raises:
            ValueError: If x or y are not valid vertices.
        '''
        if w:
            warn('The weight will be ignored, as the graph is unweighted.')

        self._raise_error_if_invalid_vertex(x)
        self._raise_error_if_invalid_vertex(y)

        self.vertex_list[x].add(y)

        if not self.directed:
            self.vertex_list[y].add(x)

    def remove_edge(self, x: int, y: int) -> None:
        '''
        Remove an edge between two vertices.

        Args:
            x (int): The source vertex.
            y (int): The destination vertex.

        Raises:
            ValueError: If x or y are not valid vertices.
        '''

        self._raise_error_if_invalid_vertex(x)
        self._raise_error_if_invalid_vertex(y)

        self.vertex_list[x].discard(y)

        if not self.directed:
            self.vertex_list[y].discard(x)

    def add_vertex(self) -> None:
        '''
        Add an isolated vertex to the graph.
        '''

        self.num_vertices += 1

        self.vertex_list.append(set())

    def remove_vertex(self, x: int) -> None:
        '''
        Remove a vertex from the graph. The vertices with
        higher indexes are shifted one position to the left.

        Args:
            x (int): The vertex to be removed.

        Raises:
            ValueError: If the vertex does not exist.
        '''

        self._raise_error_if_invalid_vertex(x)

        for u in range(self.num_vertices):
            self.vertex_list[u].discard(x)

        self.vertex_list.pop(x)
        self.num_vertices -= 1

        for u in range(self.num_vertices):
            self.vertex_list[u].discard(x)
            for v in range(x + 1, self.num_vertices + 1):
                if v in self.vertex_list[u]:
                    self.vertex_list[u].discard(v)
                    self.vertex_list[u].add(v - 1)
