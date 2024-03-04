"""
Author: Soumil Ramesh Kulkarni
Date: 02.28.2024

Question:

Given a string s, return true if the s can be palindrome after deleting at most one character from it.



Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""


class Solution:
    def validPalindrome_helper(self, s, start, end, if_deleted):
        while start < end:
            if s[start] != s[end]:
                if if_deleted:
                    return False
                else:
                    return self.validPalindrome_helper(s, start + 1, end, True) or self.validPalindrome_helper(s, start,
                                                                                                               end - 1,
                                                                                                               True)
            else:
                start += 1
                end -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        return self.validPalindrome_helper(s, 0, len(s) - 1, False)

