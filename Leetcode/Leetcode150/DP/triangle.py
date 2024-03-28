"""
Author: Soumil Ramesh Kulkarni
Date: 03.26.2024

Question:
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.



Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        table = []
        for i in range(len(triangle)):
            table.append([0] * (i + 1))
        print(table)
        # Base Case, Initialize our table Values
        table[0][0] = triangle[0][0]
        for row in range(1, len(triangle)):
            table[row][0] = table[row - 1][0] + triangle[row][0]
            table[row][-1] = table[row - 1][-1] + triangle[row][-1]
        print(table)
        # Now Fill in all other values
        for row in range(2, len(triangle)):
            for col in range(1, row):
                table[row][col] = triangle[row][col] + min(table[row - 1][col], table[row - 1][col - 1])
        print(table)
        return min(table[-1])
