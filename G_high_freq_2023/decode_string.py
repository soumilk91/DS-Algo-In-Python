"""
Author: Soumil Ramesh Kulkarni
Date: 03.25.2024

Question:
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers,
k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_string = ''
        curr_num = 0
        for i in s:
            if i.isdigit():
                curr_num = curr_num * 10 + int(i)
            elif i == '[':
                stack.append(curr_num)
                stack.append(curr_string)
                curr_num = 0
                curr_string = ''
            elif i == ']':
                prev_str = stack.pop()
                prev_num = stack.pop()
                curr_string = prev_str + curr_string * prev_num
            else:
                curr_string += i
        while stack:
            curr_string += stack.pop() + curr_string
        return curr_string
