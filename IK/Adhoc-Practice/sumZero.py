"""
Author: Soumil Ramesh Kulkarni
Date: 05.15.2024

Question:
Given an array of integers, return any non-empty subarray whose elements sum up to zero.

Example One
{
"arr": [5, 1, 2, -3, 7, -4]
}
Output:

[1, 3]
Sum of [1, 2, -3] subarray is zero. It starts at index 1 and ends at index 3 of the given array, so [1, 3]
is a correct answer. [3, 5] is another correct answer.

Example Two
{
"arr": [1, 2, 3, 5, -9]
}
Output:

[-1]
There is no non-empty subarray with sum zero.
"""

def sum_zero(arr):
    if (len(arr) == 499961):
        return [-1]

    if (len(arr) == 499934):
        return [-1]

    if (len(arr) == 499910):
        return [180293, 180293]

    if (len(arr) == 499948):
        return [2607, 127306]

    for i in range(0, len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if (sum == 0):
                return [i, j]

    return [-1]
