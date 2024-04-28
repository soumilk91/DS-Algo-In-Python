"""
Author: Soumil Ramesh Kulkarni
Date: 04.27.2024

Question:

Given the array of integers nums, you will choose two different indices i and j of that array.
Return the maximum value of (nums[i]-1)*(nums[j]-1).


Example 1:

Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, t
hat is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12

"""

from typing import *
import heapq


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # approach 1: find 2 max numbers in 2 loops. T = O(n). S = O(1)
        # approach 2: sort and then get the last 2 max elements. T = O(n lg n). S = O(1)
        # approach 3: build min heap of size 2. T = O(n lg n). S = O(1)
        # python gives only min heap feature. heaq.heappush(list, item). heapq.heappop(list)

        heap = [-1]
        for num in nums:
            if num > heap[0]:
                if len(heap) == 2:
                    heapq.heappop(heap)
                heapq.heappush(heap, num)

        return (heap[0] - 1) * (heap[1] - 1)