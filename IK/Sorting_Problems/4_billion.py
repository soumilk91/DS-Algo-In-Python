"""
Author: Soumil Ramesh Kulkarni
Date: 05.11.2024

Question:

Given four billion of 32-bit integers, return any one that’s not among them. Assume you have 1 GiB (10243 bytes) of memory.

Follow up: what if you only have 10 MiB of memory?

Example One
{
"arr": [0, 1, 2, 3]
}
Output:

4
Any number in the [4 .. 232) range is a correct answer.

Example Two
{
"arr": [4294967295, 399999999, 0]
}
Output:

1
Here again 1 is just one of many correct answers.
"""


def find_integer(arr):
    """
    Args:
     arr(list_int64)
    Returns:
     int64
    """
    # Write your code here.
    result = 0
    start = len(arr)

    max_element = max(arr)

    for i in range(start, max_element + 2):
        if i not in arr:
            result = i
            break

    return result

