"""
Author: Soumil Ramesh Kulkarni
Date: 02.21.2024

Question:
Given an integer x, return true if x is a
palindrome
, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


class Solution:
    def isPalindrome_convert_string(self, x: int) -> bool:
        str_num = str(x)
        start = 0
        end = len(str_num) - 1
        while end > start:
            if str_num[start] != str_num[end]:
                return False
            start += 1
            end -= 1
        return True

    def isPalindrome(self, x: int) -> bool:
        # Without converting into string
        if x < 0:
            return False
        reversed_number = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_number = (reversed_number * 10) + digit
            temp //= 10
        return reversed_number == x
