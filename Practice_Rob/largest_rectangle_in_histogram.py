"""
Author: Soumil Ramesh Kulkarni
Date: 03.02.2024

Question:
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        heights.append(0)

        for index, height in enumerate(heights):
            start = index

            while start and stack[-1][1] > height:
                i, h = stack.pop()
                maxArea = max(maxArea, (index - i) * h)
                start = i
            stack.append((start, height))

        return maxArea