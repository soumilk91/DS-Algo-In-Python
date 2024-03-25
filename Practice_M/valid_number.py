"""
Author: Soumil Ramesh Kulkarni
Date: 03.24.2024

Question:
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:

Input: s = "0"
Output: true
Example 2:

Input: s = "e"
Output: false
Example 3:

Input: s = "."
Output: false
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_exponent = False
        seen_dot = False

        for index, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in ['+', '-']:
                if index > 0 and s[index - 1] != 'e' and s[index - 1] != 'E':
                    return False
            elif char in ['e', 'E']:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif char == '.':
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False
        return seen_digit