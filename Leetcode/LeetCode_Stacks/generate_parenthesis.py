"""
Author: Soumil Ramesh Kulkarni
Date: 03.09.2024

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
    def generateParenthesis_helper(self, n, opening_bracket, closing_bracket, slate, result):
        # Backtrack
        if closing_bracket > opening_bracket or opening_bracket > n or closing_bracket > n:
            return

        # Base Case
        if len(slate) == 2 * n and opening_bracket == n and closing_bracket == n:
            result.append("".join(slate[:]))
            return

        # Recursive Case
        if opening_bracket < n:
            slate.append("(")
            self.generateParenthesis_helper(n, opening_bracket + 1, closing_bracket, slate, result)
            slate.pop()

        if closing_bracket < n:
            slate.append(")")
            self.generateParenthesis_helper(n, opening_bracket, closing_bracket + 1, slate, result)
            slate.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generateParenthesis_helper(n, 0, 0, [], result)
        return result