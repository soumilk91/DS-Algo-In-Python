"""
Author: Soumil Ramesh Kulkarni
Date: 03.14.2024

Question:
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.



Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
"""


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if not arr:
            return 0
        if len(arr) == 1:
            return arr[0]
        int_25 = int(0.25 * len(arr))

        compare_dict = {}
        for num in arr:
            if num not in compare_dict:
                compare_dict[num] = 1
            else:
                compare_dict[num] += 1
                if compare_dict[num] > int_25:
                    return num
        return 0
