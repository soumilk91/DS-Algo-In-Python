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
        num = 0
        pre_op = '+'
        stack = []
        s += '+'

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == ' ':
                pass
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == "*":
                    operant = stack.pop()
                    stack.append((operant * num))
                elif pre_op == '/':
                    operant = stack.pop()
                    stack.append(math.trunc(operant / num))
                num = 0
                pre_op = c
        return sum(stack)