"""
Author: Soumil Ramesh Kulkarni
Date: 08/12/2024

Question:

A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys
in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

Implement the PrefixTree class:

PrefixTree() Initializes the prefix tree object.

void insert(String word) Inserts the string word into the prefix tree.

boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before),
and false otherwise.

boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has
the prefix prefix, and false otherwise.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.endOfWord = True

    def search(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.endOfWord

    def startsWith(self, prefix):
        current = self.root
        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return True

client = PrefixTree()
client.insert('dog')
client.insert('leetcode')
print(client.search('leetcode'))
print(client.search('leet'))
print(client.startsWith('leet'))
print(client.search('dog'))
print(client.root.children)