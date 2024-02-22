"""
Author: Soumil Ramesh Kulkarni
Date: 02.20.2024

Question:
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_sentence = s.split(" ")
        temp = len(split_sentence) - 1
        while temp >= 0:
            len_of_word = len(split_sentence[temp])
            if len_of_word > 0:
                return len_of_word
            else:
                temp = temp - 1

