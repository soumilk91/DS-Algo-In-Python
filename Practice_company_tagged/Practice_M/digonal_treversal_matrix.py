"""
Author: Soumil Ramesh Kulkarni
Date: 04.14.2024

Question:
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
"""

from typing import *
from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        digonal_dict = defaultdict(list)
        ROWS = len(mat)
        COLS = len(mat[0])
        minDigonal = float("inf")
        maxDigonal = float("-inf")
        for row in range(ROWS):
            for col in range(COLS):
                digonal_dict[(row + col)].append(mat[row][col])
                minDigonal = min(minDigonal, row + col)
                maxDigonal = max(maxDigonal, row + col)
        result = []
        for digonal in range(minDigonal, maxDigonal + 1):
            temp = digonal_dict[digonal]
            if digonal % 2 == 0:
                result.extend(temp[::-1])
            else:
                result.extend(temp)
        return result        
