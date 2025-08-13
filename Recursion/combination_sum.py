"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

"""
from typing import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.helper(candidates, target, 0, [], result)
        return result

    def helper(self, candidates, target, index, slate, result):
        # Base Case
        if target == 0:
            result.append(slate[:])
            return

        # Pruning Case
        if target < 0 or index == len(candidates):
            return

        # Recursive Cases
        # Include the same index
        slate.append(candidates[index])
        self.helper(candidates, target - candidates[index], index, slate, result)  # Allow duplicates
        slate.pop()

        # Exclude
        self.helper(candidates, target, index + 1, slate, result)

