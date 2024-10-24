"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
"""

from typing import *
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(row, col, parent, path):
            letter = board[row][col]
            curr_node = parent.children[letter]

            # Check if we found a word
            if curr_node.is_word:
                result.add(path)
                curr_node.is_word = False  # Avoid duplicate entries

            # Mark the cell as visited
            board[row][col] = '#'

            # Explore neighbors
            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] in curr_node.children:
                    backtrack(new_row, new_col, curr_node, path + board[new_row][new_col])

            # Unmark the cell
            board[row][col] = letter
        # Build Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in trie.root.children:
                    backtrack(row, col, trie.root, board[row][col])

        return list(result)