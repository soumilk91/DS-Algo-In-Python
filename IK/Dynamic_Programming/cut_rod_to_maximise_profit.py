"""
Author: Soumil Ramesh Kulkarni
Date: 03.29.2024

Question:
Given the prices for rod pieces of every size between 1 inch and n inches, find the maximum total profit that can
be made by cutting an n inches long rod inch into pieces.

Example
{
"price ": [1, 5, 8, 9]
}
Output:

10
The rod can be cut in the ways given below:

1 + 1 + 1 + 1 inches will cost price[0] + price[0] + price[0] + price[0] = 4
1 + 1 + 2 inches will cost price[0] + price[0] + price[1] = 7
1 + 3 inches will cost price[0] + price[2] = 9
2 + 2 inches will cost price[1] + price[1] = 10
One piece of 4 inches will cost price[3] = 9
The maximum profit is obtained by cutting it into two pieces 2 inches each.


"""


def get_maximum_profit(price):
    """
    Args:
     price(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    n = len(price)
    cut_options = [0] * n

    for i in range(0, n):
        divisions = n // (i + 1)
        remainder = n % (i + 1)
        cut_options[i] = (divisions * price[i])

        if remainder > 0:
            cut_options[i] += price[remainder - 1]

    return max(cut_options)
