"""
Author: Soumil Ramesh Kulkarni
Date: 02/05/2024

Question:
Given an array and a target number, find the indices of the two values from the array that sum up to the given target number.
Eg:
{
"numbers": [5, 3, 10, 45, 1],
"target": 6
}
output: [0, 4]

{
"numbers": [4, 1, 5, 0, -1],
"target": 10
}
output: [-1, -1]

notes:
The function returns an array of size two where the two elements specify the input array indices whose values sum up to the given target number.
In case when no answer exists, return an array of size two with both values equal to -1, i.e., [-1, -1].
In case when multiple answers exist, you may return any of them.
The order of the returned indices does not matter.
A single index cannot be used twice.
"""


def two_sum(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.

    # Since the array is not sorted. Use a dict to check if target-number exists in the list
    # dict contains key=number and value=index at which it is stored in the array
    compare_dict = {}
    for index, number in enumerate(numbers):
        if (target - number) in compare_dict:
            return [index, compare_dict[(target - number)]]
        else:
            compare_dict[number] = index
    # Base Case when no 2 numbers can be added up to the terget
    return [-1, -1]
