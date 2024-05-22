"""
Author: Soumil Ramesh Kulkarni
Date: 05.15.2024

Question:

Given an array of numbers, return an array of the same size where i-th element is the product of all elements except the i-th one.

Calculate the products modulo 109 + 7.

Using division is not allowed anywhere in the solution. Using more than constant auxiliary space is not allowed.

Example
{
"nums": [1, 2, 3, 4, 5]
}
Output:

[120, 60, 40, 30, 24]
[(2 * 3 * 4 * 5), (1 * 3 * 4 * 5), (1 * 2 * 4 * 5), (1 * 2 * 3 * 5), (1 * 2 * 3 * 4)] = [120, 60, 40, 30, 24]
"""


def get_product_array(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    result = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix = (prefix * nums[i]) % 1000000007
    print(result)

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] = (result[i] * postfix) % 1000000007
        postfix = (postfix * nums[i]) % 1000000007
    print(result)
    return result