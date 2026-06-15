"""
Author: Soumil Ramesh Kulkarni
Date: 03.21.2024

Question:
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5

"""
class Solution:
    def calculate(self, s: str) -> int:
        operation = "+"
        stack = []
        number = 0
        for index, char in enumerate(s):
            if char.isdigit():
                number = (number * 10) + int(char)
            if char in "+-*/" or index == len(s) - 1:
                if operation == "+":
                    stack.append(number)
                elif operation == "-":
                    stack.append(-number)
                elif operation == "*":
                    stack[-1] *= number
                else:
                    stack[-1] = int(stack[-1] / number)
                operation = char
                number = 0
        return sum(stack)