"""
Author: Soumil Ramesh Kulkarni
Date: 03.30.2024

Question:
You are given a 0-indexed array of unique strings words.

A palindrome pair is a pair of integers (i, j) such that:

0 <= i, j < words.length,
i != j, and
words[i] + words[j] (the concatenation of the two strings) is a
palindrome
.
Return an array of all the palindrome pairs of words.

You must write an algorithm with O(sum of words[i].length) runtime complexity.



Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["a","a"]
"""


"""
Brute Force. Nested For Loop

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        pairs = []

        for i, word_1 in enumerate(words):
            for j, word_2 in enumerate(words):
                if i == j:
                    continue
                combined_word = word_1 + word_2
                if combined_word == combined_word[::-1]:
                    pairs.append([i, j])

        return pairs
            
"""

# Using Hashmaps
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        backward, res = {}, []
        for i, word in enumerate(words):
            backward[word[::-1]] = i

        for i, word in enumerate(words):

            if word in backward and backward[word] != i:
                res.append([i, backward[word]])

            if word != "" and "" in backward and word == word[::-1]:
                res.append([i, backward[""]])
                res.append([backward[""], i])

            for j in range(len(word)):
                if word[j:] in backward and word[:j] == word[j - 1::-1]:
                    res.append([backward[word[j:]], i])
                if word[:j] in backward and word[j:] == word[:j - 1:-1]:
                    res.append([i, backward[word[:j]]])

        return res