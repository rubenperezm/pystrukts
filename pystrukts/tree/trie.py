'''
Trie Module.

This module implements a Trie (Prefix Tree) and TrieNode data structures.
'''

from collections import defaultdict
from dataclasses import dataclass

@dataclass
class TrieNode:
    '''
    TrieNode Class.

    Attributes:
        children (defaultdict): The children nodes of the node.
        is_end_of_word (bool): Whether the node is the end of a word.

    Methods:
        `__str__()`: Return the string representation of the node.
    '''

    children: defaultdict
    is_end_of_word: bool

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False

@dataclass
class Trie:
    '''
    Trie Class.

    Attributes:
        root (TrieNode): The root node of the trie.

    Methods:
        `insert(word: str)`: Insert a word into the trie.
        `search(word: str)`: Search for a word in the trie.
        `delete(word: str)`: Delete a word from the trie.
        `startswith(prefix: str)`: Check if the trie contains a prefix.
    '''
    root = TrieNode()

    def insert(self, word: str) -> None:
        '''
        Insert a word into the trie.

        Args:
            word (str): The word to insert.
        '''

        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        '''
        Search for a word in the trie.

        Args:
            word (str): The word to search.

        Returns:
            out (bool): Whether the word is in the trie.
        '''

        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def _delete(self, node: TrieNode, word: str, depth: int) -> bool:
        '''
        Delete a node from the trie. Helper function for `delete`.

        Args:
            node (TrieNode): The current node.
            word (str): The word to delete.
            depth (int): The current depth.

        Returns:
            out (bool): Whether the node should be deleted.
        '''
        if depth == len(word):
            node.is_end_of_word = False
            return len(node.children) == 0

        char = word[depth]
        if char not in node.children:
            return False

        if self._delete(node.children[char], word, depth + 1):
            del node.children[char]
            return len(node.children) == 0

        return False

    def delete(self, word: str) -> None:
        '''
        Delete a word from the trie.

        Args:
            word (str): The word to delete.
        '''
        self._delete(self.root, word, 0)

    def startswith(self, prefix: str) -> bool:
        '''
        Check if the trie contains a prefix.

        Args:
            prefix (str): The prefix to check.

        Returns:
            out (bool): Whether the trie contains the prefix.
        '''
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
