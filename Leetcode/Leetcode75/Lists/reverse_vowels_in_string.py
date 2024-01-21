"""
Author: Soumil Ramesh Kulkarni
Date: 01/19/2024

Question:
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_dict = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'A':1, 'E':1, 'I':1, 'O':1,'U':1}
        start = 0
        end = len(s) -1
        s = list(s)
        while start < end:
            if s[start] in vowels_dict and s[end] in vowels_dict:
                #Swap
                s[start],s[end] = s[end], s[start]
                start += 1
                end -= 1
            elif s[start] in vowels_dict and s[end] not in vowels_dict:
                end -= 1
            elif s[start] not in vowels_dict and s[end] in vowels_dict:
                start += 1
            else:
                start +=1
                end -= 1
        return "".join(s)
