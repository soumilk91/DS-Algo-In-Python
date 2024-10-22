"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return
the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
"""

from typing import *
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stack to store indices of the histogram bars
        max_area = 0  # variable to store the maximum area
        n = len(heights)

        for i in range(n):
            # While the current bar is shorter than the bar at the top of the stack
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]  # pop the top of the stack
                width = i if not stack else i - stack[-1] - 1  # calculate the width
                max_area = max(max_area, height * width)  # calculate the area

            # Push the current index to the stack
            stack.append(i)

        # Process remaining bars in the stack
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area
