'''
Module for the Graph abstract class.
'''

from abc import ABCMeta, abstractmethod

class Graph(metaclass=ABCMeta):
    '''
    Abstract class for graph representations.

    Methods:
        copy() -> Graph: Create a copy of the graph.
        has_edge(x: int, y: int) -> bool: Check if there is an edge between two vertices.
        neighbors(x: int) -> list: Get the neighbors of a vertex.
        add_edge(x: int, y: int, w: float = 1.0) -> None: Add an edge between two vertices. 
            If the edge already exists, the weight is updated.
        remove_edge(x: int, y: int) -> None: Remove an edge between two vertices.
        add_vertex() -> None: Add an isolated vertex to the graph.
        remove_vertex(x: int) -> None: Remove a vertex from the graph.
    '''

    @abstractmethod
    def copy(self):
        '''
        Create a copy of the graph.

        Returns:
            Graph: A copy of the graph.
        '''

    @abstractmethod
    def has_edge(self, x: int, y: int) -> bool:
        '''
        Check if there is an edge between two vertices.

        Args:
            x (int): The source vertex.
            y (int): The destination vertex.

        Returns:
            out (bool): True if there is an edge between the vertices, False otherwise.
        '''

    @abstractmethod
    def neighbors(self, x: int) -> list:
        '''
        Get the neighbors of a vertex.

        Args:
            x (int): The vertex.

        Returns:
            out (list): The neighbors of the vertex.
        '''

    @abstractmethod
    def add_edge(self, x: int, y: int, w: float = 1.0):
        '''
        Add an edge between two vertices.
        
        Args:
            x (int): The source vertex.
            y (int): The destination vertex.
            w (float): The weight of the edge.
        '''

    @abstractmethod
    def remove_edge(self, x: int, y: int):
        '''
        Remove an edge between two vertices.

        Args:
            x (int): The source vertex.
            y (int): The destination vertex.
        '''

    @abstractmethod
    def add_vertex(self):
        '''
        Add an isolated vertex to the graph.
        '''

    @abstractmethod
    def remove_vertex(self, x: int):
        '''
        Remove a vertex from the graph.

        Args:
            x (int): The vertex.
        '''
