"""
Author: Soumil Ramesh Kulkarni
Date: 01/28/2024

Question:
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

eg:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].


Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
"""


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_dict = {}
        nums2_dict = {}
        for i in nums1:
            nums1_dict[i] = 1
        for j in nums2:
            nums2_dict[j] = 1

        return_list = []
        return_nums1 = []
        for i in nums1:
            if i not in nums2_dict:
                return_nums1.append(i)

        return_list.append(list(set(return_nums1)))

        return_nums2 = []
        for j in nums2:
            if j not in nums1_dict:
                return_nums2.append(j)
        return_list.append(list(set(return_nums2)))

        return return_list
