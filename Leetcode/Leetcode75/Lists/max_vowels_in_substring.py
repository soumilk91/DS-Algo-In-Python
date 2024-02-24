"""
Author: Soumil Ramesh Kulkarni
Date: 02.23.2024

Question:
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.



Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

"""

import heapq


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels_dict = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        queue = []
        runner = 0
        max_vowels = 0
        maxHeap = []
        for i in range(k):
            queue.append(s[i])
            runner += 1
            if s[i] in vowels_dict:
                max_vowels += 1
        # print(queue)
        # print(max_vowels)
        heapq.heappush(maxHeap, -max_vowels)
        while runner < len(s):
            temp = queue.pop(0)
            if temp in vowels_dict:
                max_vowels -= 1
            queue.append(s[runner])
            if s[runner] in vowels_dict:
                max_vowels += 1
            # print(queue)
            # print(max_vowels)
            heapq.heappush(maxHeap, -max_vowels)
            runner += 1
        return -heapq.heappop(maxHeap)


