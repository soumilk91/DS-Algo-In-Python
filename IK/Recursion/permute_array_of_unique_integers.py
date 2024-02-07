"""
Author: Soumil Ramesh Kulkarni
Date: 02/06/2024

Question:
Given an array of unique numbers, return in any order all its permutations.
{
"arr": [1, 2, 3]
}
[
[1, 2, 3],
[1, 3, 2],
[2, 1, 3],
[2, 3, 1],
[3, 2, 1],
[3, 1, 2]
]
"""


def _helper(arr, index, slate, return_list):
    # Base Case
    if index == len(arr):
        return_list.append(slate[:])
        return

    # Recursive Case
    for temp in range(index, len(arr)):
        # sawp
        arr[temp], arr[index] = arr[index], arr[temp]
        slate.append(arr[index])
        _helper(arr, index + 1, slate, return_list)

        # Swap again and pop
        arr[temp], arr[index] = arr[index], arr[temp]
        slate.pop()


def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    # Root Case
    return_list = []
    _helper(arr, 0, [], return_list)
    return return_list


print(get_permutations([1,2,3]))