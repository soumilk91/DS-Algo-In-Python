"""
Author: Soumil Ramesh Kulkarni
Date: 05.15.2024

Question:

Calculate Hamming weight of an array of integers.
Hamming weight of an integer is defined as the number of set bits in its binary representation.
Hamming weight of an array is a sum of hamming weights of all numbers in it.

Example
{
"s": [1, 2, 3]
}
Output:

4
Binary representation of 1 is “1”; one set bit.
Binary representation of 2 is “10”; one set bit.
Binary representation of 3 is “11”; two set bits.
1 + 1 + 2 = 4


"""


def calculate_hamming_weight(s):
    """
    Args:
     s(list_int64)
    Returns:
     int32
    """
    # fill a dp up to 16 bits with how many ones are in there
    # num*2=num<<1 num>>1 is num/2 but if it's odd you need to add that +1 at the end
    # We used 16 bits instead of 32 to save space complexity so this is a tradeoff
    dp = [0] * (1 << 16)
    dp[0] = 0
    for i in range(1, len(dp)):
        dp[i] = dp[i >> 1] + (i & 1)

    # We need to calculate how many ones are on the left 16 bits + right 16 bits
    total = 0
    for num in s:
        left = dp[num >> 16]
        right = dp[num & ((1 << 16) - 1)]
        total = total + left + right
    return total