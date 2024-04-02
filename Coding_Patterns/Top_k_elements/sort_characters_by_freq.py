"""
Author: Soumil Ramesh Kulkarni
Date: 04.01.2024

Question:
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a
character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.



Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        compare_dict = {}
        for char in s:
            if char not in compare_dict:
                compare_dict[char] = 1
            else:
                compare_dict[char] += 1
        result = ""

        heap = []
        for key, value in compare_dict.items():
            heapq.heappush(heap, (-value, key))

        while heap:
            multiple, char = heapq.heappop(heap)
            temp = char * (-multiple)
            result += str(temp)
        return result
