"""
Question:
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]
"""
from typing import *

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        self.helper(candidates, target, 0, [], result)
        return result

    def helper(self, candidates, target, index, slate, result):
        # Base Case
        if target == 0:
            temp = tuple(sorted(slate[:]))
            if temp not in result:
                result.add(temp)
            return

            # Pruning Case
        if target < 0 or index == len(candidates):
            return

            # Recursive Cases
        # Include
        slate.append(candidates[index])
        self.helper(candidates, target - candidates[index], index + 1, slate, result)
        slate.pop()

        # Exclude
        self.helper(candidates, target, index + 1, slate, result)
