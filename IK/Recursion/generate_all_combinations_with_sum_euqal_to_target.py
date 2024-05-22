"""
Author: Soumil Ramesh Kulkarni
Date: 02/06/2024

Question:
Given an integer array, generate all the unique combinations of the array numbers that sum up to a given target value.

{
"arr": [1, 2, 3],
"target": 3
}
Output:
[
[3],
[1, 2]
]
"""

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

def _helper(arr, target, index, slate, results):
    # Base Case
    if target == 0 and slate[:] not in results:
        results.append(slate[:])
        return

    # Backtracking Case/ Pruning
    if target < 0 or index == len(arr):
        return

    # Recursive Case
    # Include
    slate.append(arr[index])
    _helper(arr, target - arr[index], index + 1, slate, results)
    slate.pop()

    # Exculde
    _helper(arr, target, index + 1, slate, results)