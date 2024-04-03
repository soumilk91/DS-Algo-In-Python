"""
Author: Soumil ramesh Kulkarni
Date: 04.02.2024

Question:
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            palindrome[i][i] = True
            ans += 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                palindrome[i][i + 1] = True
                ans += 1

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                if s[i] == s[i + length - 1] and palindrome[i + 1][i + length - 2]:
                    palindrome[i][i + length - 1] = True
                    ans += 1

        return ans