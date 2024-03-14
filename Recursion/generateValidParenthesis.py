"""
Author: Soumil Ramesh Kulkarni
Date: 01/17/2024

Question: Given 'n' pairs for paranthesis, Write a function to generate all Well formed parenthesis
This is a Backtracking Example
Eg: n = 3
output: ['((()))', '(()())', '(())()', '()(())', '()()()']
"""


class Solution:
    def generateParenthesis_helper(self, left, right, slate, result):
        # Backtraking Case
        if right < left or left < 0 or right < 0:
            return

        # Base Case
        if left == right == 0:
            result.append("".join(slate[:]))
            return

        # Recursive Case
        # Left
        slate.append("(")
        self.generateParenthesis_helper(left - 1, right, slate, result)
        slate.pop()

        # Right
        slate.append(")")
        self.generateParenthesis_helper(left, right - 1, slate, result)
        slate.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generateParenthesis_helper(n, n, [], result)
        return result
