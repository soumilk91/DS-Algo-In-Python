"""
Author: Soumil Ramesh Kulkarni
Date: 05.15.2024

Question:

Given an array of positive and negative integers, rearrange the elements so that the positive and negative numbers alternate.
Order of the positive elements should be preserved, same with the negative ones.
Start output with a positive integer if one exists in the input.
Number of positive and negative integers may not be equal and extra positives or negatives have to appear at the end of the output.

Example
{
"array": [2, 3, -4, -9, -1, -7, 1, -5, -6]
}
Output:

[2, -4, 3, -9, 1, -1, -7, -5, -6]
The order of positives in the input: 2, 3, 1.
The order of negatives in the input: -4, -9, -1, -7, -5, -6.
We start with the first positive number, alternate until we run out of (in this case) positives, and dump the
remaining negatives at the end of the output.
"""

from collections import deque


def alternating_positives_and_negatives(array):
    """
    Args:
     array(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    if not array:
        return []
    result = []
    positiveQueue = deque([])
    negativeQueue = deque([])
    for num in array:
        if num < 0:
            negativeQueue.append(num)
        else:
            positiveQueue.append(num)

    while positiveQueue and negativeQueue:
        result.append(positiveQueue.popleft())
        result.append(negativeQueue.popleft())

    while positiveQueue:
        result.append(positiveQueue.popleft())

    while negativeQueue:
        result.append(negativeQueue.popleft())

    return result
