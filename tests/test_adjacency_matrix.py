import pytest
from pystrukts.graph import AdjacencyMatrix

def test_initilization():
    matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    graph = AdjacencyMatrix(matrix=matrix)
    assert graph.num_vertices == 3
    assert graph.directed == True
    assert graph.matrix == [[0., 1., 2.], [3., 4., 5.], [6., 7., 8.]]

    graph2 = AdjacencyMatrix(matrix=matrix, directed=False)
    assert graph2.num_vertices == 3
    assert graph2.directed == False
    assert graph2.matrix == [[0., 1., 2.], [1., 4., 5.], [2., 5., 8.]] # _copy_upper

    graph3 = AdjacencyMatrix(3)
    assert graph3.num_vertices == 3
    assert graph3.directed == True
    assert graph3.matrix == [[float('inf') for _ in range(3)] for _ in range(3)]

    graph4 = AdjacencyMatrix(3, no_edge_value=0)
    assert graph4.num_vertices == 3
    assert graph4.directed == True
    assert graph4.matrix == [[0 for _ in range(3)] for _ in range(3)]

    # num_vertices ignored
    with pytest.warns(UserWarning):
        graph5 = AdjacencyMatrix(2, matrix = matrix)
        assert graph5.num_vertices == 3
        assert graph5.directed == True
        assert graph5.matrix == matrix

def test_initialization_error():
    with pytest.raises(ValueError):
        graph = AdjacencyMatrix(-1)

    with pytest.raises(ValueError):
        matrix = [[0, 1, 2], [3], [6, 7, 8]]
        graph = AdjacencyMatrix(matrix = matrix)

    with pytest.raises(ValueError):
        graph = AdjacencyMatrix()

def test_copy():
    matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    graph = AdjacencyMatrix(matrix=matrix, no_edge_value=0)
    graph2 = graph.copy()
    assert graph2.num_vertices == 3
    assert graph2.directed == True
    assert graph2.matrix == matrix
    assert graph2.no_edge_value == 0

def test_has_edge():
    matrix = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]

    graph = AdjacencyMatrix(matrix=matrix, no_edge_value=0)
    assert graph.has_edge(0, 0) == False
    assert graph.has_edge(0, 1) == True
    assert graph.has_edge(0, 2) == False
    assert graph.has_edge(1, 0) == False
    assert graph.has_edge(1, 1) == False
    assert graph.has_edge(1, 2) == False
    assert graph.has_edge(2, 0) == True
    assert graph.has_edge(2, 1) == False
    assert graph.has_edge(2, 2) == True

def test_has_edge_error():
    matrix = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]
    graph = AdjacencyMatrix(matrix=matrix)

    with pytest.raises(ValueError):
        graph.has_edge(0, 3)

    with pytest.raises(ValueError):
        graph.has_edge(-1, 0)

def test_neighbors():
    matrix = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]

    graph = AdjacencyMatrix(matrix=matrix, no_edge_value=0)
    assert graph.neighbors(0) == [1]
    assert graph.neighbors(1) == []
    assert graph.neighbors(2) == [0, 2]

def test_neighbors_error():
    matrix = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]
    graph = AdjacencyMatrix(matrix=matrix, no_edge_value=0)

    with pytest.raises(ValueError):
        graph.neighbors(3)

    with pytest.raises(ValueError):
        graph.neighbors(-1)

def test_add_edge():
    matrix = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]

    graph = AdjacencyMatrix(matrix=matrix, no_edge_value=0)

    assert graph.has_edge(0, 2) == False
    graph.add_edge(0, 2)
    assert graph.has_edge(0, 2) == True
    assert graph.matrix == [[0., 1., 1.], [0., 0., 0.], [1., 0., 1.]]

    assert graph.has_edge(1, 2) == False
    graph.add_edge(1, 2, 25)
    assert graph.has_edge(1, 2) == True
    assert graph.matrix == [[0., 1., 1.], [0., 0., 25.], [1., 0., 1.]]

def test_add_edge_undirected():
    matrix = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]

    graph = AdjacencyMatrix(3, directed=False, no_edge_value=0)

    assert graph.has_edge(0, 2) == False
    assert graph.has_edge(2, 0) == False
    graph.add_edge(0, 2)
    assert graph.has_edge(0, 2) == True
    assert graph.has_edge(2, 0) == True
    assert graph.get_edge_weight(0, 2) == 1
    assert graph.get_edge_weight(2, 0) == 1

    assert graph.has_edge(1, 2) == False
    assert graph.has_edge(2, 1) == False
    graph.add_edge(1, 2, 25)
    assert graph.has_edge(1, 2) == True
    assert graph.has_edge(2, 1) == True
    assert graph.get_edge_weight(1, 2) == 25
    assert graph.get_edge_weight(2, 1) == 25

def test_add_edge_error():
    matrix = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]
    graph = AdjacencyMatrix(matrix=matrix, no_edge_value=0)

    with pytest.raises(ValueError):
        graph.add_edge(0, 3)

    with pytest.raises(ValueError):
        graph.add_edge(-1, 0)

def test_remove_edge():
    matrix = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]

    graph = AdjacencyMatrix(matrix=matrix, no_edge_value=0)

    assert graph.has_edge(0, 1) == True
    graph.remove_edge(0, 1)
    assert graph.has_edge(0, 1) == False
    assert graph.matrix == [[0., 0., 0.], [0., 0., 0.], [1., 0., 1.]]

    assert graph.has_edge(2, 0) == True
    graph.remove_edge(2, 0)
    assert graph.has_edge(2, 0) == False
    assert graph.matrix == [[0., 0., 0.], [0., 0., 0.], [0., 0., 1.]]

def test_remove_edge_undirected():
    matrix = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]
    graph = AdjacencyMatrix(matrix=matrix, directed=False, no_edge_value=0)

    assert graph.has_edge(0, 1) == True
    assert graph.has_edge(1, 0) == True
    graph.remove_edge(0, 1)
    assert graph.has_edge(0, 1) == False
    assert graph.has_edge(1, 0) == False
    assert graph.matrix == [[1., 0., 0.], [0., 1., 0.], [0., 0., 0.]]

    graph.remove_edge(0, 0)
    assert graph.matrix == [[0., 0., 0.], [0., 1., 0.], [0., 0., 0.]]

def test_remove_edge_error():
    matrix = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]
    graph = AdjacencyMatrix(matrix=matrix, no_edge_value=0)

    with pytest.raises(ValueError):
        graph.remove_edge(0, 3)

    with pytest.raises(ValueError):
        graph.remove_edge(-1, 0)

def test_add_vertex():
    matrix = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]

    graph = AdjacencyMatrix(matrix=matrix, no_edge_value=0)
    assert graph.num_vertices == 3
    assert graph.matrix == [[0., 1., 0.], [0., 0., 0.], [1., 0., 1.]]

    graph.add_vertex()
    assert graph.num_vertices == 4
    assert graph.matrix == [[0., 1., 0., 0.], [0., 0., 0., 0.], [1., 0., 1., 0.], [0., 0., 0., 0.]]

def test_remove_vertex():
    matrix = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]

    graph = AdjacencyMatrix(matrix=matrix, no_edge_value=0)
    assert graph.num_vertices == 3
    assert graph.matrix == [[0., 1., 0.], [0., 0., 0.], [1., 0., 1.]]

    graph.remove_vertex(1)
    assert graph.num_vertices == 2
    assert graph.matrix == [[0., 0.], [1., 1.]]

    graph.remove_vertex(1)
    assert graph.num_vertices == 1
    assert graph.matrix == [[0.]]

def test_remove_vertex_error():
    matrix = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]
    graph = AdjacencyMatrix(matrix=matrix, no_edge_value=0)

    with pytest.raises(ValueError):
        graph.remove_vertex(3)

    with pytest.raises(ValueError):
        graph.remove_vertex(-1)

def test_get_edge_weight():
    matrix = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]

    graph = AdjacencyMatrix(matrix=matrix, no_edge_value=0)
    assert graph.get_edge_weight(0, 1) == 1
    assert graph.get_edge_weight(1, 0) == 0
    assert graph.get_edge_weight(2, 0) == 1

def test_get_edge_weight_error():
    matrix = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]
    graph = AdjacencyMatrix(matrix=matrix, no_edge_value=0)

    with pytest.raises(ValueError):
        graph.get_edge_weight(0, 3)

    with pytest.raises(ValueError):
        graph.get_edge_weight(-1, 0)
