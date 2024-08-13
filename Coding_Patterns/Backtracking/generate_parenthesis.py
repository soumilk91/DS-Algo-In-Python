"""
Author: Soumil Ramesh Kulkarni
Date: 04.01.2024

Question:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1:
            return []
        result = []
        self.helper(n, n, [], result)
        return result

    def helper(self, left, right, slate, result):
        # Base Case
        if left == right == 0:
            result.append("".join(slate[:]))
            return
        # Pruning
        if right < left or left < 0 or right < 0:
            return

        # recursive Case
        # Left
        slate.append("(")
        self.helper(left - 1, right, slate, result)
        slate.pop()

        # Right
        slate.append(")")
        self.helper(left, right - 1, slate, result)
        slate.pop()
