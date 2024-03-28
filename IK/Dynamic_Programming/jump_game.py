"""
Author: Soumil Ramesh Kulkarni
Date: 03.26.2024

Question:
Given a list of maximum jump lengths from different houses, determine if you can reach the last house in one or more
jumps starting from the first one.

Maximum jump length of 2 from a house, for example, means that you can either jump to the next house or to the one after next.

Example One
{
"maximum_jump_lengths": [2, 3, 1, 0, 4, 7]
}
Output:

1
You can reach the last house in the following way:

Example one

Example Two
{
"maximum_jump_lengths": [3, 1, 1, 0, 2, 4]
}
Output:

0
"""


def can_reach_last_house(maximum_jump_lengths):
    """
    Args:
     maximum_jump_lengths(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    num_houses = len(maximum_jump_lengths)
    last_index = num_houses-1
    for index in range(num_houses-1, -1, -1):
        if (index + maximum_jump_lengths[index]) >= last_index:
            last_index = index
    return last_index == 0