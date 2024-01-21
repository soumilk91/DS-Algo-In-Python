"""
Author: Soumil Ramesh Kulkarni
Date: 01/19/2024

Question: Given a list of a integers and target, Generate all unique COMBINATIONS of the list that sum upto the target
eg: [1,2,3]
output: [[1,2], [3]]
"""


def _helper(arr, target, index, slate, results):
    # Base Case
    if target == 0 and slate[:] not in results:
        results.append(slate[:])
        return

    # Backtracking Case/ Pruning
    if target <= 0 or index == len(arr):
        return

    # Recursive Case
    # Include
    slate.append(arr[index])
    _helper(arr, target - arr[index], index + 1, slate, results)
    slate.pop()

    # Exculde
    _helper(arr, target, index + 1, slate, results)


def generate_all_combinations(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    results = []
    _helper(arr, target, 0, [], results)
    return results


print(generate_all_combinations([1,2,3], 3))