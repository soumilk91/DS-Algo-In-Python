"""
Author: Soumil Ramesh Kulkarni
Date: 05.07.2024

Question:
You are given two strings s and t of equal length n. You can perform the following operation on the string s:

Remove a suffix of s of length l where 0 < l < n and append it at the start of s.
For example, let s = 'abcd' then in one operation you can remove the suffix 'cd' and append it in front of s making s = 'cdab'.
You are also given an integer k. Return the number of ways in which s can be transformed into t in exactly k operations.

Since the answer can be large, return it modulo 109 + 7.



Example 1:

Input: s = "abcd", t = "cdab", k = 2
Output: 2
Explanation:
First way:
In first operation, choose suffix from index = 3, so resulting s = "dabc".
In second operation, choose suffix from index = 3, so resulting s = "cdab".

Second way:
In first operation, choose suffix from index = 1, so resulting s = "bcda".
In second operation, choose suffix from index = 1, so resulting s = "cdab".
Example 2:

Input: s = "ababab", t = "ababab", k = 1
Output: 2
Explanation:
First way:
Choose suffix from index = 2, so resulting s = "ababab".

Second way:
Choose suffix from index = 4, so resulting s = "ababab".
"""

class Solution:
    def kmp(self, s, t):
        pi, res = [0 for i in range(len(t))], []
        for i in range(1, len(t)):
            j = pi[i-1]
            while j > 0 and t[j] != t[i]: j = pi[j-1]
            pi[i] = 0 if j == 0 and t[0] != t[i] else j + 1
        m, n, j = len(s), len(t), 0
        for i in range(m):
            while j >= n or j > 0 and s[i] != t[j]: j = pi[j-1]
            if s[i] == t[j]: j += 1
            if j == n: res.append(i - n + 1)
        return res
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        n, M = len(s), 10**9 + 7
        pos = self.kmp((s+s)[:-1], t)
        f_k = [0, 0]
        f_k[1] = (pow(n-1, k, M) - (-1)**k + M) * pow(n, M-2, M) % M
        f_k[0] = (f_k[1] + (-1)**k + M) % M
        return sum(f_k[not not p] for p in pos) % M