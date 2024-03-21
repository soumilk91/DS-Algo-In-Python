"""
Author: Soumil Ramesh Kulkarni
Date: 03.21.2024

Question:
Given a string s, return true if a permutation of the string could form a
palindrome
 and false otherwise.



Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true

"""

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if not s or len(s)== 1:
            return True
        compute_dict = {}
        for char in s:
            if char not in compute_dict:
                compute_dict[char] = 1
            else:
                compute_dict[char] += 1
        odd = 0
        for key, value in compute_dict.items():
            if value % 2 != 0:
                odd += 1
                if odd > 1:
                    break
        if len(s) % 2 == 0 and odd == 0:
            return True
        else:
            if odd == 0 or odd == 1:
                return True
            else:
                return False