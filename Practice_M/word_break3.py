"""
Author: Soumil Ramesh Kulkarni
Date: 04.15.2024

Question:
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each
word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
"""

from typing import *
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = {}

        def wordbr(s):
            if s not in cache:
                result = []
                for w in wordDict:
                    if s[:len(w)] == w:
                        if len(s) == len(w):
                            result.append(w)
                        else:
                            for word in wordbr(s[len(w):]):
                                result.append(w + " " + word)
                cache[s] = result
            return cache[s]

        return wordbr(s)