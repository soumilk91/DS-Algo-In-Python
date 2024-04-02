"""
Author: Soumil Ramesh Kulkarni
Date: 04.01.2024

Question:
Given an integer array nums that may contain duplicates, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        level0    []
        level1    [1]          [2]
        level2    [1,2]        [2,2]
        level3    [1,2,2]
        """
        nums = sorted(nums)
        res = []
        self.backtracking(res,0,[],nums)
        return res
    def backtracking(self,res,start,subset,nums):
        res.append(list(subset))
        for i in range(start,len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            self.backtracking(res,i+1,subset,nums)
            subset.pop()