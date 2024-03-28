"""
Author: Soumil Ramesh Kulkarni
Date: 03.26.2024

Question:

"""


def maximum_stolen_value(values):
    """
    Args:
     values(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    n = len(values)

    # Only one house given
    if n == 1:
        return values[0]

    # Only 2 Houses Given
    if n == 2:
        return max(values[0], values[1])

    table = [-1] * n
    # Initialize
    table[0] = values[0]
    table[1] = max(values[0], values[1])

    for i in range(2, n):
        table[i] = max(table[i - 1], table[i - 2] + values[i])
    return table[n - 1]
