"""
Link to the Problem: https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
Author: Soumil Ramesh Kulkarni
Date: 02.19.2024

Question:
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters_in_ransomNote = {}
        for i in ransomNote:
            if i not in letters_in_ransomNote:
                letters_in_ransomNote[i] = 1
            else:
                letters_in_ransomNote[i] += 1

        letters_magazine = {}
        for i in magazine:
            if i not in letters_magazine:
                letters_magazine[i] = 1
            else:
                letters_magazine[i] += 1

        for letter in letters_in_ransomNote:
            if letter not in letters_magazine:
                return False
            if letters_in_ransomNote[letter] > letters_magazine[letter]:
                return False
        return True

