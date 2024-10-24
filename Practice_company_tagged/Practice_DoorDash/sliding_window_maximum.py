"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the
array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

from typing import *
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        index_deque = deque()  # Deque to store indices of elements in the current window
        max_in_windows = []  # List to store the maximums for each window

        for current_index in range(len(nums)):
            # Remove indices of elements that are outside the current window
            if index_deque and index_deque[0] < current_index - k + 1:
                index_deque.popleft()

            # Remove elements from the back of the deque that are smaller than the current element
            while index_deque and nums[index_deque[-1]] < nums[current_index]:
                index_deque.pop()

            # Add the current element's index to the deque
            index_deque.append(current_index)

            # Start adding the maximum values to the result once we have the first full window
            if current_index >= k - 1:
                max_in_windows.append(
                    nums[index_deque[0]])  # The element at the front of deque is the max of the current window

        return max_in_windows
