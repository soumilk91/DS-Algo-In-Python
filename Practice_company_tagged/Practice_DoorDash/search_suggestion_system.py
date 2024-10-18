"""
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix
return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.



Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
"""

from typing import *
class TrieNode:
    def __init__(self):
        self.children = {}
        self.products = []
        self.num = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        runner = self.root
        for char in word:
            if char not in runner.children:
                runner.children[char] = TrieNode()
            runner = runner.children[char]
            if runner.num < 3:
                runner.products.append(word)
                runner.num += 1

    def searchWords(self, prefix):
        runner = self.root
        for char in prefix:
            if char not in runner.children:
                return []
            runner = runner.children[char]
        return runner.products


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        sortedProducts = products.sort()
        trieClient = Trie()
        for product in products:
            trieClient.addWord(product)

        prefix = ""
        result = []
        for char in searchWord:
            prefix += char
            temp_list = trieClient.searchWords(prefix)
            result.append(temp_list)
        return result

