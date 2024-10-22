"""
Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.



Example 1:
Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 6
Explanation: Given three friends living at (0,0), (0,4), and (2,2).
The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
So return 6.

Example 2:
Input: grid = [[1,1]]
Output: 1
"""

from typing import *
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        def get_sorted_coordinates(coordinate_list):
            return sorted(coordinate_list)

        # Get all the x and y coordinates of houses (1s)
        x_coords, y_coords = [], []

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    x_coords.append(row)
                    y_coords.append(col)

        # The median minimizes the total travel distance
        median_x = get_sorted_coordinates(x_coords)[len(x_coords) // 2]
        median_y = get_sorted_coordinates(y_coords)[len(y_coords) // 2]

        # Calculate the total travel distance to the meeting point (median_x, median_y)
        total_distance = 0
        for x in x_coords:
            total_distance += abs(x - median_x)
        for y in y_coords:
            total_distance += abs(y - median_y)

        return total_distance
