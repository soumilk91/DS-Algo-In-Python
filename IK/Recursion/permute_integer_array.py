"""
Author: Soumil Ramesh Kulkarni
Date: 02/18/2024

Question:
Given an array of numbers with possible duplicates, return all of its permutations in any order.

Example
{
"arr": [1, 2, 2]
}
Output:

[
[1, 2, 2],
[2, 1, 2],
[2, 2, 1]
]

"""


def get_permutation_helper(array, index, slate, result):
    # Base Case
    if index == len(array):
        if slate[:] not in result:
            result.append(slate[:])
        return result

    for i in range(index, len(array)):
        # Swap the element to get it at the 0th index
        array[index], array[i] = array[i], array[index]

        slate.append(array[index])

        # Recurse
        get_permutation_helper(array, index + 1, slate, result)

        # Swap again to get the elements at their original Positions
        array[index], array[i] = array[i], array[index]
        slate.pop()


def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result = []
    get_permutation_helper(arr, 0, [], result)
    return result
