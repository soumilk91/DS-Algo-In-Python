"""
Author: Soumil Ramesh Kulkarni
Date: 05.07.2024

Question:
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.



Example 1:

Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"
Example 2:

Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.
Example 3:

Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
"""


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0
        current = set()
        for i in range(len(word)):
            if word[i] in 'aeiou':
                current.add(word[i])

                for j in range(i + 1, len(word)):
                    if word[j] in 'aeiou':
                        current.add(word[j])
                    else:
                        break

                    if len(current) == 5:
                        count += 1

            current = set()

        return count