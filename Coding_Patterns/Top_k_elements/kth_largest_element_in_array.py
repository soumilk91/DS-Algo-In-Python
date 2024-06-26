"""
Author: Soumil Ramesh Kulkarni
Date: 04.01.2024

Question:
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""
import heapq
class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use A max Heap
        heap = []
        for i in nums:
            heapq.heappush(heap, -i)
        # print(heap)
        for i in range(k - 1):
            heapq.heappop(heap)
        return -heapq.heappop(heap)
