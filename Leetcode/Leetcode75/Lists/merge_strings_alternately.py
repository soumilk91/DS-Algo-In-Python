"""
Author: Soumil Ramesh Kulkarni
Date: 01/19/2024

Question: You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
Eg:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d

"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        return_string = []
        if len(word1) <= len(word2):
            smallest_length = len(word1)
        else:
            smallest_length = len(word2)

        for i in range (smallest_length):
            return_string.append(word1[i])
            return_string.append(word2[i])
        if len(word1) > smallest_length:
            while smallest_length < len(word1):
                return_string.append(word1[smallest_length])
                smallest_length += 1
        elif len(word2) > smallest_length:
            while smallest_length < len(word2):
                return_string.append(word2[smallest_length])
                smallest_length += 1
        else:
            pass
        return ''.join(return_string)