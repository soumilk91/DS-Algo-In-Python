"""
Author: Soumil Ramesh Kulkarni
Date: 05.15.2024

Question:
Find the minimum element in an array that has been sorted in ascending order and rotated by an unknown pivot.

Example
{
"arr": [4, 5, 6, 7, 8, 1, 2, 3]
}
Output:

1
The array is sorted in the ascending order and right rotated by pivot 5. The minimum value 1 is at index 5.
"""


def find_minimum(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     int32


    [4, 5, 6, 7, 8, 1, 2, 3]
                 ^

    """
    # Write your code here.

    low = 0
    high = len(arr) - 1
    if len(arr) == 1:
        return arr[0]

    if arr[low] < arr[high]:
        return arr[low]

    while low < high:
        mid = (low + high) // 2

        if arr[mid + 1] < arr[mid]:
            return arr[mid + 1]

        if arr[mid] < arr[mid - 1]:
            return arr[mid]

        if arr[low] < arr[mid]:
            low = mid + 1
        else:
            high = mid - 1