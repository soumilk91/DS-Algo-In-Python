"""
Author: Soumil Ramesh Kulkarni
Date: 01/19/2024

Question: Given a list of a integers and target, Generate all unique COMBINATIONS of the list that sum upto the target
eg: [1,2,3]
output: [[1,2], [3]]
"""

from typing import *
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.helper(candidates, target, 0, [], result)
        return result

    def helper(self, candidates, target, index, slate, result):
        # Base Case: Target is reached
        if target == 0:
            result.append(slate[:])
            return

        # Base Case: Target is exceeded or no more candidates
        if target < 0 or index == len(candidates):
            return

        # Recursive Case:
        # Option 1: Include the current candidate and stay on the same index (since candidates can be reused)
        slate.append(candidates[index])
        self.helper(candidates, target - candidates[index], index, slate, result)
        slate.pop()

        # Option 2: Exclude the current candidate and move to the next index
        self.helper(candidates, target, index + 1, slate, result)
