"""
Author: Soumil Ramesh Kulkarni
Date: 03.22.2024

Question:
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.



Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.

"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        A = list(str(num))
        ans = A[:]
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                A[i], A[j] = A[j], A[i]
                if A > ans: ans = A[:]
                A[i], A[j] = A[j], A[i]

        return int("".join(ans))
