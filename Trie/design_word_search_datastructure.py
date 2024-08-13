"""
Author: Soumil Ramesh Kulkarni
Date: 08/12/2024

Question:
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
word may contain dots '.' where dots can be matched with any letter.
"""
from typing import *
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.endOfWord = True


    def search(self, word: str) -> bool:
        def helper(root, index):
            current = root
            for i in range(index, len(word)):
                ch = word[i]
                if ch == '.':
                    for child in current.children.values():
                        if helper(child, i + 1):
                            return True
                    return False
                else:
                    if ch not in current.children:
                        return False
                    current = current.children[ch]
            return current.endOfWord

        return helper(self.root, 0)