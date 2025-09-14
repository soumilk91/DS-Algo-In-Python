"""
Author: Soumil Ramesh Kulkarni
Date: 02.20.2024

Question:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

from typing import List


class Solution:
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        triplets = []
        numbers.sort()

        for first_index in range(len(numbers) - 2):
            # Skip duplicate values for the first number
            if first_index > 0 and numbers[first_index] == numbers[first_index - 1]:
                continue

            left_index = first_index + 1
            right_index = len(numbers) - 1

            while left_index < right_index:
                current_sum = (
                        numbers[first_index] +
                        numbers[left_index] +
                        numbers[right_index]
                )

                if current_sum == 0:
                    triplets.append([
                        numbers[first_index],
                        numbers[left_index],
                        numbers[right_index]
                    ])

                    left_index += 1
                    right_index -= 1

                    # Skip duplicates on the left side
                    while (left_index < right_index and
                           numbers[left_index] == numbers[left_index - 1]):
                        left_index += 1

                    # Skip duplicates on the right side
                    while (left_index < right_index and
                           numbers[right_index] == numbers[right_index + 1]):
                        right_index -= 1

                elif current_sum < 0:
                    left_index += 1
                else:
                    right_index -= 1

        return triplets
