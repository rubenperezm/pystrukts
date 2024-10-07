import pytest
from pystrukts.graph import AdjacencyList

def test_initilization():
    vertex_list = [[1], [2], [0]]
    graph = AdjacencyList(vertex_list=vertex_list)
    assert graph.num_vertices == 3
    assert graph.directed == True
    assert graph.vertex_list == [{1}, {2}, {0}]

    graph2 = AdjacencyList(vertex_list=vertex_list, directed=False)
    assert graph2.num_vertices == 3
    assert graph2.directed == False
    assert graph2.vertex_list == [{1, 2}, {0, 2}, {0, 1}]

    graph3 = AdjacencyList(3)
    assert graph3.num_vertices == 3
    assert graph3.directed == True
    assert graph3.vertex_list == [set(), set(), set()]

    # num_vertices ignored
    with pytest.warns(UserWarning):
        graph4 = AdjacencyList(2, vertex_list=vertex_list)
        assert graph4.num_vertices == 3
        assert graph4.directed == True
        assert graph4.vertex_list == [{1}, {2}, {0}]

def test_initialization_error():
    with pytest.raises(ValueError):
        graph = AdjacencyList(-1)

    with pytest.raises(ValueError):
        vertex_list = [[0, 1, 2], [3], [6, 7, 8]]
        graph = AdjacencyList(vertex_list=vertex_list)

    with pytest.raises(ValueError):
        graph = AdjacencyList()

def test_copy():
    vertex_list = [[1], [2], [0]]
    graph = AdjacencyList(vertex_list=vertex_list)
    graph2 = graph.copy()
    assert graph2.num_vertices == 3
    assert graph2.directed == True
    assert graph2.vertex_list == [{1}, {2}, {0}]

def test_has_edge():
    vertex_list = [[1], [], [0, 2]]

    graph = AdjacencyList(vertex_list=vertex_list)
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
    vertex_list = [[1], [2], [0]]
    graph = AdjacencyList(vertex_list=vertex_list)

    with pytest.raises(ValueError):
        graph.has_edge(0, 3)

    with pytest.raises(ValueError):
        graph.has_edge(-1, 0)

def test_neighbors():
    vertex_list = [[1], [], [0, 2]]

    graph = AdjacencyList(vertex_list=vertex_list)
    assert graph.neighbors(0) == {1}
    assert graph.neighbors(1) == set()
    assert graph.neighbors(2) == {0, 2}

def test_neighbors_error():
    vertex_list = [[1], [], [0, 2]]
    graph = AdjacencyList(vertex_list=vertex_list)

    with pytest.raises(ValueError):
        graph.neighbors(3)

    with pytest.raises(ValueError):
        graph.neighbors(-1)

    with pytest.raises(ValueError):
        graph.neighbors(1.3)

def test_add_edge():
    vertex_list = [[1], [], [0, 2]]

    graph = AdjacencyList(vertex_list=vertex_list)

    assert graph.has_edge(0, 2) == False
    graph.add_edge(0, 2)
    assert graph.has_edge(0, 2) == True
    assert graph.vertex_list == [{1, 2}, set(), {0, 2}]

    with pytest.warns(UserWarning):
        assert graph.has_edge(1, 2) == False
        graph.add_edge(1, 2, 25)
        assert graph.has_edge(1, 2) == True
        assert graph.vertex_list == [{1, 2}, {2}, {0, 2}]

def test_add_edge_undirected():
    vertex_list = [[1], [], [0, 2]]

    graph = AdjacencyList(3, directed=False)

    assert graph.has_edge(0, 2) == False
    assert graph.has_edge(2, 0) == False
    graph.add_edge(0, 2)
    assert graph.has_edge(0, 2) == True
    assert graph.has_edge(2, 0) == True


    with pytest.warns(UserWarning):
        assert graph.has_edge(1, 2) == False
        assert graph.has_edge(2, 1) == False
        graph.add_edge(1, 2, 25)
        assert graph.has_edge(1, 2) == True
        assert graph.has_edge(2, 1) == True

def test_add_edge_error():
    vertex_list = [[1], [], [0, 2]]
    graph = AdjacencyList(vertex_list=vertex_list)

    with pytest.raises(ValueError):
        graph.add_edge(0, 3)

    with pytest.raises(ValueError):
        graph.add_edge(-1, 0)

def test_remove_edge():
    vertex_list = [[1], [], [0, 2]]

    graph = AdjacencyList(vertex_list=vertex_list)

    assert graph.has_edge(0, 1) == True
    graph.remove_edge(0, 1)
    assert graph.has_edge(0, 1) == False
    assert graph.vertex_list == [set(), set(), {0, 2}]

    assert graph.has_edge(2, 0) == True
    graph.remove_edge(2, 0)
    assert graph.has_edge(2, 0) == False
    assert graph.vertex_list == [set(), set(), {2}]

def test_remove_edge_undirected():
    vertex_list = [[0, 1], [0, 1], []]
    graph = AdjacencyList(vertex_list=vertex_list, directed=False)

    assert graph.has_edge(0, 1) == True
    assert graph.has_edge(1, 0) == True
    graph.remove_edge(0, 1)
    assert graph.has_edge(0, 1) == False
    assert graph.has_edge(1, 0) == False
    assert graph.vertex_list == [{0}, {1}, set()]

    graph.remove_edge(0, 0)
    assert graph.vertex_list == [set(), {1}, set()]

def test_remove_edge_error():
    vertex_list = [[1], [], [0, 2]]
    graph = AdjacencyList(vertex_list=vertex_list)

    with pytest.raises(ValueError):
        graph.remove_edge(0, 3)

    with pytest.raises(ValueError):
        graph.remove_edge(-1, 0)

def test_add_vertex():
    vertex_list = [[1], [], [0, 2]]

    graph = AdjacencyList(vertex_list=vertex_list)
    assert graph.num_vertices == 3
    assert graph.vertex_list == [{1}, set(), {0, 2}]

    graph.add_vertex()
    assert graph.num_vertices == 4
    assert graph.vertex_list == [{1}, set(), {0, 2}, set()]

def test_remove_vertex():
    vertex_list = [[1], [], [0, 2]]

    graph = AdjacencyList(vertex_list=vertex_list)
    assert graph.num_vertices == 3
    assert graph.vertex_list == [{1}, set(), {0, 2}]

    graph.remove_vertex(1)
    assert graph.num_vertices == 2
    assert graph.vertex_list == [set(), {0, 1}]

    graph.remove_vertex(0)
    assert graph.num_vertices == 1
    assert graph.vertex_list == [{0}]

def test_remove_vertex_error():
    vertex_list = [[1], [], [0, 2]]
    graph = AdjacencyList(vertex_list=vertex_list)

    with pytest.raises(ValueError):
        graph.remove_vertex(3)

    with pytest.raises(ValueError):
        graph.remove_vertex(-1)
