"""
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.



Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
"""

from typing import *
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.wordsList = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.wordsList.append(word)
            # print(current.wordsList)
        current.endOfWord = True

    def searchPrefix(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]
        print(current.wordsList)
        return len(current.wordsList)


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trieClient = Trie()
        for word in words:
            trieClient.addWord(word)
        return trieClient.searchPrefix(pref)
