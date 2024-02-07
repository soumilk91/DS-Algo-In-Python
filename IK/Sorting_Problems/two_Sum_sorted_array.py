"""
Author: Soumil Ramesh Kulkarni
Date: 02/05/2024

Question:
Given an array sorted in non-decreasing order and a target number,
find the indices of the two values from the array that sum up to the given target number.

Eg:
{
"numbers": [1, 2, 3, 5, 10],
"target": 7
}
Output: [1, 3]
In case when no answer exists, return an array of size two with both values equal to -1, i.e., [-1, -1].
In case when multiple answers exist, you may return any of them.
The order of the indices returned does not matter.
A single index cannot be used twice.
"""

def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.

    # Use a 2 pointer approach
    return_list = [-1, -1]
    start = 0
    end = len(numbers) - 1
    while start < end:
        sumation = numbers[start] + numbers[end]
        if sumation == target:
            return [start, end]
        elif sumation < target:
            start += 1
        else:
            end -= 1

    # Return this By Default which means no pair found
    return return_list

