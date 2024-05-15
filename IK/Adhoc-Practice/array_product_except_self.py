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
    # We can do this in O(n) two passes. In one pass, we calculate the total product of all elements.
    # Then, we make another pass to store total_product/nums[i] into the ith position of the return array -> 'prod_array'
    # Using division is not allowed anywhere in the solution.

    # No division, and no auxiliary space outside of returned list

    # Naive solution is to use 2 pointers to repeatedly calculate product for current position
    # Can we improve on this design?
    # we can't cache the repeated subproblems since we can't use auxiliary space.
    # what if we used the array we're building as our auxiliary space?
    # but then we can't divide from it, so we must hold a variable describing products, except no aux space so we can't do that either

    # Let's implement it naively to see if we can make any improvements

    # n = len(nums)
    # prod_array = [1]*n
    # MOD_VALUE = 10**9+7

    # def calculate_product(arr, mult, mult_idx):
    #     for i in range(n):
    #         if i == mult_idx: continue
    #         arr[mult_idx] *= mult[i]
    #         arr[mult_idx] %= MOD_VALUE

    # for i in range(n):
    #     calculate_product(prod_array, nums, i)

    # return prod_array

    # Understanding logic behind optimized solution

    result = [None] * len(nums)

    left_product = 1
    for i in range(len(nums)):
        result[i] = left_product
        left_product = (left_product * nums[i]) % 1000000007

    right_product = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] = (result[i] * right_product) % 1000000007
        right_product = (right_product * nums[i]) % 1000000007

    return result