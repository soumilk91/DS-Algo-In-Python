"""
Author: Soumil Ramesh Kulkarni
Date: 01/28/2024

Question:
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.

Eg:
Input: s = "the sky is blue"
Output: "blue is sky the"


Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.


Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        temp_list = s.split(" ")
        return_list = []
        num = len(temp_list) - 1
        while num >= 0:
            if temp_list[num] != "":
                return_list.append(temp_list[num])
            num -= 1
        return " ".join(return_list)
