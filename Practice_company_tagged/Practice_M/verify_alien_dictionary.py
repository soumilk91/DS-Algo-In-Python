"""
Author: Soumil Ramesh Kulkarni
Date: 04.15.2024

Question:
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the
given words are sorted lexicographically in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to
lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is
less than any other character (More info).
"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        compare_dict = {}
        for index, char in enumerate(order):
            compare_dict[char] = index

        for i in range(1, len(words)):
            pre = words[i - 1]
            curr = words[i]
            flag = 0
            for j in range(min(len(pre), len(curr))):
                if compare_dict[pre[j]] < compare_dict[curr[j]]:
                    flag = 1
                    break
                elif compare_dict[pre[j]] > compare_dict[curr[j]]:
                    return False

            if not flag and len(pre) > len(curr):
                return False
        return True