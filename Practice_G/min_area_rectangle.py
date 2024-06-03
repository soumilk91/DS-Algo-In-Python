"""
Question:

You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the X and Y axes.
If there is not any such rectangle, return 0.

Answers within 10-5 of the actual answer will be accepted.



Example 1:
Input: points = [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.

Example 2:
Input: points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.

Example 3:
Input: points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.
"""
from typing import *
from math import sqrt
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        ans = float('inf')
        seen = {}
        for i, (x0, y0) in enumerate(points):
            for x1, y1 in points[i+1:]:
                cx = (x0 + x1)/2
                cy = (y0 + y1)/2
                d2 = (x0 - x1)**2 + (y0 - y1)**2
                for xx, yy in seen.get((cx, cy, d2), []):
                    area = sqrt(((x0-xx)**2 + (y0-yy)**2) * ((x1-xx)**2 + (y1-yy)**2))
                    ans = min(ans, area)
                seen.setdefault((cx, cy, d2), []).append((x0, y0))
        return ans if ans < float('inf') else 0