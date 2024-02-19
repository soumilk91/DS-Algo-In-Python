"""
Author: Soumil Ramesh Kulkarni
Date: 02/18/2024

Question:
Given two integers n and k, find all the possible unique combinations of k numbers in range 1 to n.

Example One
{
"n": 5,
"k": 2
}
Output:

[
[1, 2],
[1, 3],
[1, 4],
[1, 5],
[2, 3],
[2, 4],
[2, 5],
[3, 4],
[3, 5],
[4, 5]
]
Example Two
{
"n": 6,
"k": 6
}
Output:

[
[1, 2, 3, 4, 5, 6]
]
"""


def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result = []

    def helper(remain, slate, current_number):
        if remain == 0:
            result.append(slate[:])

        else:
            for i in range(current_number, n + 1):
                slate.append(i)
                helper(remain - 1, slate, i + 1)
                slate.pop()

    helper(k, [], 1)
    return result

