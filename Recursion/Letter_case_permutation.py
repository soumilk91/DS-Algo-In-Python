"""
Author: Soumil Ramesh Kulkarni
Date: 01/17/2024

Question: Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.
        Return a list of all possible strings

Eg:
string: "a1b2"
output: "a1b2", "A1b2", "a1B2", "A1B2"

string: "3z4"
output: "3z4", "3Z4"

string: "12345"
output: "12345"


"""

from typing import *
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        self.helper(s, 0, [], result)
        return result

    def helper(self, s, index, slate, result):
        # Base Case
        if index == len(s):
            result.append("".join(slate[:]))
            return

            # Recursive Cases
        if s[index].isdigit():
            slate.append(s[index])
            self.helper(s, index + 1, slate, result)
            slate.pop()
        else:
            # Capital
            slate.append(s[index].upper())
            self.helper(s, index + 1, slate, result)
            slate.pop()

            # Lower
            slate.append(s[index].lower())
            self.helper(s, index + 1, slate, result)
            slate.pop()
