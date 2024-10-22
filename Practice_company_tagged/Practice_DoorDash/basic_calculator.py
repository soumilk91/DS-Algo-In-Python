"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        number = 0
        sign = 1  # 1 for positive, -1 for negative

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)  # Accumulate the digit
            elif char in "+-":
                result += number * sign
                number = 0  # Reset the number
                if char == "-":  # Reset the sign
                    sign = -1
                else:
                    sign = 1
            elif char == '(':
                # Push the result and sign to the stack, then reset them
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * number
                number = 0
                # Pop the sign and previous result
                result *= stack.pop()  # stack.pop() is the sign before the parentheses
                result += stack.pop()  # stack.pop() is the result before the parentheses
            # Ignore spaces

        result += sign * number  # Add the last number to the result
        return result