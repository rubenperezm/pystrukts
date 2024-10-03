import pytest
from pystrukts import MaxHeap

def test_heap_initialization():
    heap = MaxHeap([3, 1, 5, 7, 2])
    assert heap.peek() == 7

def test_empty_heap_initialization():
    heap = MaxHeap()
    assert not heap.data

def test_heap_push():
    heap = MaxHeap([3, 1, 5])
    heap.push(10)
    assert heap.peek() == 10

def test_push_negative_values():
    heap = MaxHeap([-1, 2, -3])
    heap.push(-10)
    assert heap.peek() == 2

def test_heap_pop():
    heap = MaxHeap([10, 20, 15, 2, 5])
    max_value = heap.pop()
    assert max_value == 20
    assert heap.peek() == 15

def test_pop_empty_heap():
    heap = MaxHeap()
    with pytest.raises(IndexError):
        heap.pop()

def test_heap_peek():
    heap = MaxHeap([1, 3, 2])
    assert heap.peek() == 3

def test_peek_empty_heap():
    heap = MaxHeap()
    with pytest.raises(IndexError):
        heap.peek()

def test_heap_str():
    heap = MaxHeap([4, 2, 9])
    assert str(heap) == "MaxHeap([9, 2, 4])"

def test_str_empty_heap():
    heap = MaxHeap()
    assert str(heap) == "MaxHeap([])"
