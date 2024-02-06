"""
Author: Soumil Ramesh Kulkarni
Date: 02/04/2024

Question:
Given an array of integers arr of size n and an integer w, find maximum number in all subarrays of arr of length w.

Imagine that n is very large and a sliding window of a smaller size w is moving through arr from left to right.
We need to find the maximum in every position of the sliding window.

Eg:
{
"arr": [1, 3, -1, -3, 5, 3, 6, 7],
"w": 3
}
Output: [3, 3, 5, 5, 6, 7]

Size of arr is 8 and so the size of the output array is n - w + 1 = 8 - 3 + 1 = 6.

Here are all the 6 positions of the sliding window and the corresponding maximum values:

[1 3 -1] -3 5 3 6 7. Maximum is 3.
1 [3 -1 -3] 5 3 6 7. Maximum is 3.
1 3 [-1 -3 5] 3 6 7. Maximum is 5.
1 3 -1 [-3 5 3] 6 7. Maximum is 5.
1 3 -1 -3 [5 3 6] 7. Maximum is 6.
1 3 -1 -3 5 [3 6 7]. Maximum is 7.
Notes
Function must return an array of integers of length n - w + 1. i-th value in the returned array must be the maximum among arr[i], arr[i + 1], ..., arr[i + w - 1].
Constraints:

1 <= n <= 105
-2 * 109 <= arr[i] <= 2 * 109
1 <= w <= n
"""


def max_in_sliding_window(arr, w):
    """
    Args:
     arr(list_int32)
     w(int32)
    Returns:
     list_int32
    """
    # Write your code here
    queue = []
    max_element = []
    for i in range(w):
        queue.append(arr[i])

    start_point = w
    while len(queue) == w:
        max_element.append(max(queue))
        if start_point < len(arr):
            queue.append(arr[start_point])
        start_point += 1
        queue.pop(0)
    return max_element

