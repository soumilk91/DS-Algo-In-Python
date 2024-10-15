"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.



Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
"""

from collections import deque
from typing import *
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        queue = deque([])
        for num in arr:
            if len(queue) == len(arr):
                break
            queue.append(num)
            if num == 0:
                if len(queue) < len(arr):
                    queue.append(num)
        runner = 0
        while queue:
            arr[runner] = queue.popleft()
            runner += 1

