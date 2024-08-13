"""
Author: Soumil Ramesh Kulkarni
Date: 08/13/2024

Question:
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with searchWord. If there are more than three products with a common
prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
"""

from typing import *
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = list()
        self.n = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children: node.children[c] = TrieNode()
            node = node.children[c]
            if node.n < 3:
                node.words.append(word)
                node.n += 1

    def find_word_by_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return ''
            node = node.children[c]
        return node.words


class Solution:
    def suggestedProducts(self, A: List[str], searchWord: str) -> List[List[str]]:
        A.sort()
        trie = Trie()
        for word in A:
            trie.add_word(word)
        ans, cur = [], ''
        for c in searchWord:
            cur += c
            ans.append(trie.find_word_by_prefix(cur))
            # print(ans)
        return ans