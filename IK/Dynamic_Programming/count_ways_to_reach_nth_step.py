"""
Author: Soumil Ramesh Kulkarni
Date: 03.29.2024

Question:
There is a staircase with n steps. A person standing at the 0-th step wants to reach the n-th one.
They are capable of jumping up by certain numbers of steps at a time.

Given how the person can jump, count the number of ways they can reach the top.

Example One
{
"steps": [1, 2],
"n": 1
}
Output:

1
The person can jump up by either 1 or 2 steps at a time. The only way to reach step 1 from step 0 is to jump up one step once.

Example Two
{
"steps": [1, 2],
"n": 2
}
Output:

2
There are two distinct ways to reach step 2: {1, 1}, {2}.

Example Three
{
"steps": [2, 3],
"n": 7
}
Output:

3
There are three distinct ways to reach step 7 from step 0: {2, 2, 3}, {2, 3, 2}, {3, 2, 2}.
"""


def count_ways_to_climb(steps, n):
    """
    Args:
     steps(list_int32)
     n(int32)
    Returns:
     int64
    """
    # Write your code here.
    cache = [0] * (n+1)
    cache[0] = 1
    for i in range(1, n+1):
        for step in steps:
            if i - step >= 0:
                cache[i] += cache[i - step]
    return cache[n]
