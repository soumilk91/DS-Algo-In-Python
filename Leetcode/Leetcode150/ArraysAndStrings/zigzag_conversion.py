"""
Author: Soumil Ramesh KUlkarni
Date: 03.24.2024

Question:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        row_arr = [""]* numRows
        row_index = 1
        going_up = True

        for ch in s:
            row_arr[row_index - 1] += ch
            if row_index == numRows:
                going_up = False
            elif row_index == 1:
                going_up = True

            if going_up:
                row_index += 1
            else:
                row_index -= 1
        return "".join(row_arr)