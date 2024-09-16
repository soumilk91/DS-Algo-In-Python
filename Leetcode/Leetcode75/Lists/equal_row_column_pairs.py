"""
Author: Soumil Ramesh Kulkarni
Date: 03.16.2024

Question:
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).



Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
"""

from collections import Counter
from typing import *
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        resultCount = 0
        n = len(grid)

        # Keep Track of all the Rows in tuples
        rowCounter = Counter(tuple(row) for row in grid)
        print(rowCounter)

        # Add the freq of each column in map
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            resultCount += rowCounter[tuple(col)]
        return resultCount
