"""
Author: Soumil Ramesh Kulkarni
Date: 04.01.2024

Question:
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        permutations = []
        counter = Counter(nums)

        def findAllPermutations(res):
            if len(res) == len(nums):
                permutations.append(res)
                return

            for key in counter:
                if counter[key]:
                    counter[key] -= 1  # decrement visited key
                    findAllPermutations(res + [key])
                    counter[key] += 1  # restore the state of visited key to find the next path

        findAllPermutations([])
        return permutations