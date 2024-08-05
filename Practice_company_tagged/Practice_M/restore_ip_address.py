"""
Question:
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255
(inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1"
are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s.
You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.



Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
"""

class Solution(object):
    # method to check if a part of the string is within the range 0-255,
    # returns True if part is within range 0-255 else False
    def valid(self, s, start, length):
        return length == 1 or (
            s[start] != "0"
            and (length < 3 or s[start : start + length] <= "255")
        )

    # main helper method to solve the problem by backtracking
    def helper(self, s, startIndex, dots, ans):
        remainingLength = len(s) - startIndex
        remainingNumberOfIntegers = 4 - len(dots)
        if (
            remainingLength > remainingNumberOfIntegers * 3
            or remainingLength < remainingNumberOfIntegers
        ):
            return
        if len(dots) == 3:
            if self.valid(s, startIndex, remainingLength):
                temp = ""
                last = 0
                for dot in dots:
                    temp += s[last : last + dot] + "."
                    last += dot
                temp += s[startIndex:]
                ans.append(temp)
            return
        for curPos in range(1, min(4, remainingLength + 1)):
            dots.append(curPos)
            if self.valid(s, startIndex, curPos):
                self.helper(s, startIndex + curPos, dots, ans)
            dots.pop()

    # main method called by leetcode
    def restoreIpAddresses(self, s):
        answer = []
        self.helper(s, 0, [], answer)
        return answer