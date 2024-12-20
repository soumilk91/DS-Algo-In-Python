"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
"""

from typing import *
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        result = []
        indexFirst = 0
        indexSecond = 0
        while indexFirst < len(firstList) and indexSecond < len(secondList):
            left = max(firstList[indexFirst][0], secondList[indexSecond][0])
            right = min(firstList[indexFirst][1], secondList[indexSecond][1])
            if left <= right:
                result.append([left, right])
            if firstList[indexFirst][1] < secondList[indexSecond][1]:
                indexFirst += 1
            else:
                indexSecond += 1
        return result
