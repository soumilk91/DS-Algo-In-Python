"""
Author: Soumil Ramesh Kulkarni
Date: 05.16.2024

Question:

Given a string s of length n, find the length of the longest substring that contains exactly two distinct characters.

Example
{
"s": "ecebaaaaca"
}
Output:

6
"aaaaca" is the largest substring with exactly 2 distinct characters.
"""


def get_longest_substring_length_with_exactly_two_distinct_chars(s):
    """
    Args:
     s(str)
    Returns:
     int32
    """
    #sliding window prob

    n = len(s)
    if n < 2: return 0
    if s.count(s[0]) == n: return 0
    res = cur = count_b = a = b = 0
    for c in s:
        cur = cur + 1 if c in (a, b) else count_b + 1
        count_b = count_b + 1 if c == b else 1
        if b != c: a, b = b, c
        res = max(res, cur)
    return res