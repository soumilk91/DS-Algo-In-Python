"""
Author: Soumil Ramesh Kulkarni
Date: 03.06.2024

Question:
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.



Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1 = p2 = 0

        while p1 < len(word) and p2 < len(abbr):
            if abbr[p2].isdigit():
                if abbr[p2] == '0':
                    return False  # Leading Zeros not allowed
                shift = 0
                while p2 < len(abbr) and abbr[p2].isdigit():
                    shift = (shift * 10) + int(abbr[p2])
                    p2 += 1
                p1 += shift
            else:
                if word[p1] != abbr[p2]:
                    return False
                p1 += 1
                p2 += 1
        return p1 == len(word) and p2 == len(abbr)
