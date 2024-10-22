"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'.
The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "1+1"
Output: 2
Example 2:

Input: s = "6-4/2"
Output: 4
Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
"""

from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        q = deque(s.replace(' ', ''))
        return self.helper(q)

    def helper(self, q):
        stack = []
        num = ''
        sign = '+'

        while q:
            x = q.popleft()
            if x == '(':
                num = self.helper(q)
            if x.isnumeric():
                num += x
            if not x.isnumeric() or not q:
                if sign == '+':
                    stack.append(int(num or 0))
                elif sign == '-':
                    stack.append(-1 * int(num or 0))
                elif sign == '*':
                    stack.append(stack.pop() * int(num))
                elif sign == '/':
                    stack.append(int(stack.pop() / int(num)))
                sign = x
                num = ''
            if x == ')':
                break

        return sum(stack)
