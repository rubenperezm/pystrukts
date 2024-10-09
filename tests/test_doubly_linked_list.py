import pytest
from pystrukts.list import DoublyLinkedList, DoublyLinkedNode

def test_node_initialization():
    node = DoublyLinkedNode(1)

    assert node.data == 1
    assert node.next is None
    assert node.prev is None

def test_node_initialization_empty():
    node = DoublyLinkedNode()

    assert node.data is None
    assert node.next is None
    assert node.prev is None

def test_node_str():
    node = DoublyLinkedNode(1)

    assert str(node) == "DoublyLinkedNode(1)"

def test_node_str_empty():
    node = DoublyLinkedNode()

    assert str(node) == "DoublyLinkedNode(None)"

def test_node_str_multiple():
    node1 = DoublyLinkedNode(1)
    node2 = DoublyLinkedNode(2, next=node1)

    assert str(node2) == "DoublyLinkedNode(2) <-> DoublyLinkedNode(1)"

def test_list_initialization():
    linked_list = DoublyLinkedList()

    assert len(linked_list) == 0
    assert linked_list.iscircular() == False
    assert linked_list._LinkedList__head is None
    assert linked_list._LinkedList__tail is None

def test_list_str():
    linked_list = DoublyLinkedList()

    assert str(linked_list) == "DoublyLinkedList(None)"

def test_list_iter_for():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    assert [x for x in linked_list] == [1, 2, 3]

def test_list_iter_while():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    iterator = iter(linked_list)
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3

    with pytest.raises(StopIteration):
        next(iterator)

def test_list_append():
    linked_list = DoublyLinkedList()
    linked_list.append(1)

    assert len(linked_list) == 1
    assert linked_list.get(0) == 1

def test_list_append_multiple():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    assert len(linked_list) == 3
    assert linked_list.get(0) == 1
    assert linked_list.get(1) == 2
    assert linked_list.get(2) == 3
    assert linked_list._LinkedList__tail.prev.prev == linked_list._LinkedList__head

def test_list_prepend():
    linked_list = DoublyLinkedList()
    linked_list.appendleft(1)

    assert len(linked_list) == 1
    assert linked_list.get(0) == 1

def test_list_prepend_multiple():
    linked_list = DoublyLinkedList()
    linked_list.appendleft(1)
    linked_list.appendleft(2)
    linked_list.appendleft(3)

    assert len(linked_list) == 3
    assert linked_list.get(0) == 3
    assert linked_list.get(1) == 2
    assert linked_list.get(2) == 1
    assert linked_list._LinkedList__tail.prev.prev == linked_list._LinkedList__head

def test_insert():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(4)
    linked_list.insert(3, 2)

    assert len(linked_list) == 4
    assert linked_list.get(0) == 1
    assert linked_list.get(1) == 2
    assert linked_list.get(2) == 3
    assert linked_list.get(3) == 4
    assert linked_list._LinkedList__tail.prev.prev.prev == linked_list._LinkedList__head

def test_insert_start():
    linked_list = DoublyLinkedList()
    linked_list.append(2)
    linked_list.append(3)
    linked_list.insert(1, 0)

    assert len(linked_list) == 3
    assert linked_list.get(0) == 1
    assert linked_list.get(1) == 2
    assert linked_list.get(2) == 3

def test_insert_end():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.insert(3, 2)

    assert len(linked_list) == 3
    assert linked_list.get(0) == 1
    assert linked_list.get(1) == 2
    assert linked_list.get(2) == 3

def test_insert_negative_index():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.insert(3, -1)

    assert len(linked_list) == 3
    assert linked_list.get(0) == 1
    assert linked_list.get(1) == 2
    assert linked_list.get(2) == 3

def test_insert_out_of_bounds():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)

    with pytest.raises(IndexError): 
        linked_list.insert(3, 5)

def test_pop():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    assert linked_list.pop() == 3
    assert len(linked_list) == 2
    assert linked_list.get(-1) == 2

def test_pop_last():
    linked_list = DoublyLinkedList()
    linked_list.append(1)

    assert linked_list.pop() == 1
    assert len(linked_list) == 0
    assert linked_list._LinkedList__head is None
    assert linked_list._LinkedList__tail is None

def test_pop_empty():
    linked_list = DoublyLinkedList()

    with pytest.raises(IndexError): 
        linked_list.pop()

def test_popleft():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    assert linked_list.popleft() == 1
    assert len(linked_list) == 2
    assert linked_list.get(0) == 2
    assert linked_list._LinkedList__head.data == 2

def test_popleft_last():
    linked_list = DoublyLinkedList()
    linked_list.append(1)

    assert linked_list.popleft() == 1
    assert len(linked_list) == 0
    assert linked_list._LinkedList__head is None
    assert linked_list._LinkedList__tail is None

def test_popleft_empty():
    linked_list = DoublyLinkedList()

    with pytest.raises(IndexError): 
        linked_list.popleft()

def test_remove():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.remove(2)

    assert len(linked_list) == 3
    assert linked_list.get(0) == 1
    assert linked_list.get(1) == 2
    assert linked_list.get(2) == 4
    assert linked_list._LinkedList__tail.prev.prev == linked_list._LinkedList__head

def test_remove_start():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.remove(0)

    assert len(linked_list) == 2
    assert linked_list.get(0) == 2
    assert linked_list.get(1) == 3
    assert linked_list._LinkedList__tail.prev == linked_list._LinkedList__head

def test_remove_end():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.remove(2)

    assert len(linked_list) == 2
    assert linked_list.get(0) == 1
    assert linked_list.get(1) == 2
    assert linked_list._LinkedList__tail.prev == linked_list._LinkedList__head

def test_remove_negative_index():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.remove(-2)

    assert len(linked_list) == 2
    assert linked_list.get(0) == 1
    assert linked_list.get(1) == 3

def test_remove_out_of_bounds():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    with pytest.raises(IndexError): 
        linked_list.remove(5)

    with pytest.raises(IndexError): 
        linked_list.remove(-5)

def test_get():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    assert linked_list.get(0) == 1
    assert linked_list.get(1) == 2
    assert linked_list.get(2) == 3

def test_get_negative_index():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    assert linked_list.get(-1) == 3
    assert linked_list.get(-2) == 2
    assert linked_list.get(-3) == 1

def test_get_out_of_bounds():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    with pytest.raises(IndexError): 
        linked_list.get(5)
    
    with pytest.raises(IndexError): 
        linked_list.get(-5)

def test_index():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    assert linked_list.index(1) == 0
    assert linked_list.index(2) == 1
    assert linked_list.index(3) == 2

def test_index_not_found():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    with pytest.raises(ValueError): 
        linked_list.index(4)

def test_clear():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.clear()

    assert len(linked_list) == 0

def test_is_circular():
    linked_list = DoublyLinkedList(circular=True)

    assert linked_list.iscircular() == True

def test_append_circular():
    linked_list = DoublyLinkedList(circular=True)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    assert linked_list._LinkedList__head.data == 1
    assert linked_list._LinkedList__tail.data == 3
    assert linked_list._LinkedList__tail.next == linked_list._LinkedList__head
    assert linked_list._LinkedList__head.prev == linked_list._LinkedList__tail

def test_appendleft_circular():
    linked_list = DoublyLinkedList(circular=True)
    linked_list.appendleft(1)
    linked_list.appendleft(2)
    linked_list.appendleft(3)

    assert linked_list._LinkedList__head.data == 3
    assert linked_list._LinkedList__tail.data == 1
    assert linked_list._LinkedList__tail.next == linked_list._LinkedList__head
    assert linked_list._LinkedList__head.prev == linked_list._LinkedList__tail

def test_pop_circular():
    linked_list = DoublyLinkedList(circular=True)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    assert linked_list.pop() == 3
    assert linked_list._LinkedList__head.data == 1
    assert linked_list._LinkedList__tail.data == 2
    assert linked_list._LinkedList__tail.next == linked_list._LinkedList__head
    assert linked_list._LinkedList__head.prev == linked_list._LinkedList__tail

def test_popleft_circular():
    linked_list = DoublyLinkedList(circular=True)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    assert linked_list.popleft() == 1
    assert linked_list._LinkedList__head.data == 2
    assert linked_list._LinkedList__tail.data == 3
    assert linked_list._LinkedList__tail.next == linked_list._LinkedList__head
    assert linked_list._LinkedList__head.prev == linked_list._LinkedList__tail