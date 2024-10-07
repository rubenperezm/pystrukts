'''
Adjacency matrix representation of a graph.

This module provides the AdjacencyMatrix class, which represents a graph using an adjacency matrix.
'''

from warnings import warn
from pystrukts.graph import Graph

class AdjacencyMatrix(Graph):
    '''
    Graph representation using adjacency matrix.

    Attributes:
        num_vertices (int): The number of vertices in the graph.
        directed (bool): True if the graph is directed, False otherwise.
        matrix (list): The adjacency matrix of the graph.
        no_edge_value (float): The value used to represent the absence of an edge.

    Methods:
        copy() -> AdjacencyMatrix: Create a copy of the graph.
        _copy_matrix(matrix: list, directed: bool) -> list: Copy the adjacency matrix.
        _raise_error_if_invalid_vertex(x: int) -> None: Raise an error if the vertex does not exist.
        has_edge(x: int, y: int) -> bool: Check if there is an edge between two vertices.
        neighbors(x: int) -> list: Get the neighbors of a vertex.
        add_edge(x: int, y: int, w: float = 1.0) -> None: Add an edge between two vertices.
            If the edge already exists, the weight is updated.
        remove_edge(x: int, y: int) -> None: Remove an edge between two vertices.
        add_vertex() -> None: Add an isolated vertex to the graph.
        remove_vertex(x: int) -> None: Remove a vertex from the graph.
        get_edge_weight(x: int, y: int) -> float: Get the weight of an edge.
        set_edge_weight(x: int, y: int, w: float) -> None: Set the weight of an edge.
    '''

    def __init__(self, num_vertices: int = None, directed: bool = True,
                 matrix: list = None, no_edge_value: float = float('inf')) -> None:
        '''
        Initialize the adjacency matrix.

        Args:
            num_vertices (int): The number of vertices in the graph.
            directed (bool): True if the graph is directed, False otherwise.
            matrix (list): The adjacency matrix of the graph.
            no_edge_value (float): The value used to represent the absence of an edge.

        Raises:
            ValueError: No adjacency matrix or number of vertices provided.
        '''

        if not matrix and not num_vertices:
            raise ValueError('You must specify either the number of vertices \
                             or the adjacency matrix.')

        if num_vertices and num_vertices < 0:
            raise ValueError('The number of vertices must be a non-negative integer.')

        if matrix and num_vertices:
            warn('The number of vertices will be ignored, as an adjacency matrix was provided.')

        self.directed = directed
        self.no_edge_value = no_edge_value

        if matrix is not None:
            for row in matrix:
                if len(row) != len(matrix):
                    raise ValueError('The number of columns in the matrix must be \
                                      equal to the number of vertices.')

            self.num_vertices = len(matrix)
            self.matrix = self._copy_matrix(matrix)
        else:
            self.num_vertices = int(num_vertices)
            self.matrix = [[no_edge_value for _ in range(num_vertices)]
                           for _ in range(num_vertices)]

    def copy(self) -> 'AdjacencyMatrix':
        '''
        Create a copy of the graph.

        Returns:
            out (AdjacencyMatrix): The copy of the graph.
        '''

        return AdjacencyMatrix(directed = self.directed,
                               matrix = self.matrix, no_edge_value = self.no_edge_value)

    def _copy_matrix(self, matrix: list) -> list:
        '''
        Copy the adjacency matrix with floating point values. 
        If the graph is undirected, the matrix is made symmetric by copying the upper triangle.


        Args:
            matrix (list): The matrix to be copied.

        Returns:
            out (list): The matrix.
        '''

        if not self.directed:
            return [[matrix[i][j] if i <= j else matrix[j][i]
                 for j in range(self.num_vertices)] for i in range(self.num_vertices)]
        return [[float(matrix[i][j]) for j in range(self.num_vertices)]
                for i in range(self.num_vertices)]

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

        return self.matrix[x][y] != self.no_edge_value

    def neighbors(self, x: int) -> list:
        '''
        Get the neighbors of a vertex. 
        If x has a self-loop, the output contains the vertex itself.

        Args:
            x (int): The vertex.

        Returns:
            out (list): The list of neighbors of the vertex.

        Raises:
            ValueError: If x is not a valid vertex.
        '''

        self._raise_error_if_invalid_vertex(x)

        return [i for i in range(self.num_vertices) if self.matrix[x][i] != self.no_edge_value]

    def add_edge(self, x: int, y: int, w: float = 1.0) -> None:
        '''
        Add an edge between two vertices. If the edge already exists, the weight is updated.

        Args:
            x (int): The source vertex.
            y (int): The destination vertex.
            w (float): The weight of the edge.

        Raises:
            ValueError: If x or y are not valid vertices.
        '''

        self._raise_error_if_invalid_vertex(x)
        self._raise_error_if_invalid_vertex(y)

        self.matrix[x][y] = float(w)

        if not self.directed:
            self.matrix[y][x] = float(w)

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

        self.matrix[x][y] = self.no_edge_value

        if not self.directed:
            self.matrix[y][x] = self.no_edge_value

    def add_vertex(self) -> None:
        '''
        Add an isolated vertex to the graph.
        '''

        self.num_vertices += 1

        for row in self.matrix:
            row.append(self.no_edge_value)

        self.matrix.append([self.no_edge_value for _ in range(self.num_vertices)])

    def remove_vertex(self, x: int) -> None:
        '''
        Remove a vertex from the graph.

        Args:
            x (int): The vertex to be removed.

        Raises:
            ValueError: If the vertex does not exist.
        '''

        self._raise_error_if_invalid_vertex(x)

        self.num_vertices -= 1

        for row in self.matrix:
            del row[x]

        del self.matrix[x]

    def get_edge_weight(self, x: int, y: int) -> float:
        '''
        Get the weight of an edge.

        Args:
            x (int): The source vertex.
            y (int): The destination vertex.

        Returns:
            out (float): The weight of the edge.

        Raises:
            ValueError: If x or y are not valid vertices.
        '''

        self._raise_error_if_invalid_vertex(x)
        self._raise_error_if_invalid_vertex(y)

        return self.matrix[x][y]
