"""
Author: Soumil Ramesh Kulkarni
Date: 03.30.2024

Question:
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
 of at least one of the chosen numbers is different.

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


class Solution:
    def helper(self, numbers, target, index, slate, results):
        # Base Case
        if target == 0 and slate[:] not in results:
            results.append(slate[:])
            return

        # Pruning Case
        if target < 0 or index == len(numbers):
            return

        # Recursive Cases
        # Reuse the same Index
        slate.append(numbers[index])
        self.helper(numbers, target - numbers[index], index, slate, results)
        slate.pop()

        # Include
        slate.append(numbers[index])
        self.helper(numbers, target - numbers[index], index + 1, slate, results)
        slate.pop()

        # Exclude
        self.helper(numbers, target, index + 1, slate, results)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        self.helper(candidates, target, 0, [], results)
        return results
