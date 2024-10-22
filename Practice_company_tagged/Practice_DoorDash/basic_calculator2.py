"""
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
        # Initialize variables
        stack = []
        current_num = 0
        operator = '+'
        n = len(s)

        # Traverse each character in the string
        for i in range(n):
            char = s[i]

            # Build the current number if the character is a digit
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            # If the character is an operator or we've reached the end of the string
            if char in "+-*/" or i == n - 1:
                if operator == '+':
                    stack.append(current_num)
                elif operator == '-':
                    stack.append(-current_num)
                elif operator == '*':
                    stack[-1] = stack[-1] * current_num
                elif operator == '/':
                    # Perform integer division that truncates towards zero
                    stack[-1] = int(stack[-1] / current_num)

                # Update operator and reset current number
                operator = char
                current_num = 0

        # Return the sum of the stack which contains all the final values
        return sum(stack)
