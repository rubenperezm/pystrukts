import pytest
from pystrukts.tree import Trie, TrieNode

def test_trie_node_initialization():
    node = TrieNode()

    assert node.children == {}
    assert node.is_end_of_word == False

def test_trie_insert():
    trie = Trie()
    trie.insert("hello")

    assert trie.root.children['h'].children['e'].children['l'].children['l'].children['o'].is_end_of_word == True

def test_trie_search():
    trie = Trie()
    trie.insert("hello")

    assert trie.search("hello") == True
    assert trie.search("world") == False
    assert trie.search("hell") == False

def test_trie_delete():
    trie = Trie()
    trie.insert("hello")
    trie.insert("helloworld")

    trie.delete("hello")

    assert trie.search("hello") == False
    assert trie.search("helloworld") == True

    trie.delete("helloworld")
    assert trie.search("world") == False
    assert trie.root.children == {}

def test_trie_delete_empty():
    trie = Trie()
    trie.delete("hello")

    assert trie.root.children == {}

def test_trie_startswith():
    trie = Trie()
    trie.insert("hello")

    assert trie.startswith("hell") == True
    assert trie.startswith("world") == False
    assert trie.startswith("hello") == True