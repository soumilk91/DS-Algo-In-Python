"""
Author: Soumil Ramesh Kulkarni
Date: 03.19.2024

Question:
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            pivot_index = left + (right - left) // 2
            pivot_element = matrix[pivot_index // n][pivot_index % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_index - 1
                else:
                    left = pivot_index + 1
        return False