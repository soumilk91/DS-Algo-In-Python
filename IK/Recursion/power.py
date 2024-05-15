"""
Author: Soumil Ramesh Kulkarni
Date: 05.15.2024

Question:
Given a base a and an exponent b. Your task is to find ab. The value could be large enough. So, calculate ab % 1000000007.

Example
{
"a": 2,
"b": 10
}
Output:

1024
"""


def calculate_power(a, b):
    """
    Args:
     a(int64)
     b(int64)
    Returns:
     int32
    """
    # Write your code here.
    mod = 1000000007

    if b == 0:  # whether originally 0 or through continous halving
        return 1

    c = b // 2

    if b % 2 == 1:
        answer = calculate_power(a, c) ** 2 * a
    else:
        answer = calculate_power(a, c) ** 2

    return answer % mod