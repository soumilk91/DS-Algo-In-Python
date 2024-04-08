"""
Author: Soumil Ramesh Kulkarni
Date: 03.31.2024

Question:
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number
sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""


class Solution:
    def sortedSquares(self, nums) :
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums

    def sortedSuwares_heap(self, nums):
        heap = []
        import heapq
        for num in nums:
            heapq.heappush(heap, num**num)
        result = []
        while heap:
            result.append(heapq.heappop(heap))
        return result


obj = Solution()
print(obj.sortedSquares([-4,-1,0,3,10]))
print(obj.sortedSuwares_heap([-4,-1,0,3,10]))