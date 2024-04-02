"""
Author: Soumil Ramesh Kulkarni
Date: 04.01.2024

Question:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        compare_dict = {}
        for element in nums:
            if element in compare_dict:
                compare_dict[element] += 1
            else:
                compare_dict[element] = 1

        import heapq
        heap = []
        for key in compare_dict:
            heapq.heappush(heap, (-1 * compare_dict[key], key))
        return_list = []
        while k > 0:
            temp = heapq.heappop(heap)
            return_list.append(temp[1])
            k -= 1
        return return_list