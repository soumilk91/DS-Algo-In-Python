"""
Author: Soumil Ramesh Kulkarni
Date: 04.01.2024

Question:
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.



Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
"""


class Solution:
    def letterCasePermutation_helper(self, s, index, slate, result):
        # Base Case
        if index == len(s):
            result.append("".join(slate[:]))
            return

        # Capital Letter
        if s[index].isdigit():
            slate.append(s[index])
            self.letterCasePermutation_helper(s, index + 1, slate, result)
            slate.pop()
        else:
            # Lower
            slate.append(s[index].lower())
            self.letterCasePermutation_helper(s, index + 1, slate, result)
            slate.pop()

            # Upper
            slate.append(s[index].upper())
            self.letterCasePermutation_helper(s, index + 1, slate, result)
            slate.pop()

    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        self.letterCasePermutation_helper(s, 0, [], result)
        return result