"""
Author: Soumil Ramesh Kulkarni
Date: 03.09.2024

Question:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        close_to_open = {")": "(", "}": "{", "]": "["}

        stack = []

        for brace in s:
            if brace not in close_to_open:
                stack.append(brace)
            else:
                if not stack:
                    return False
                else:
                    temp = stack.pop()
                    if temp != close_to_open[brace]:
                        return False
        if stack:
            return False
        return True
