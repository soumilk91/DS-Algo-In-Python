"""
Author: Soumil Ramesh Kulkarni
Date: 05.16.2024

Question:
Find the longest substring that repeats at least twice in the given string.

Example
{
"s": "efabcdhefhabcdiefi"
}
Output:

"abcd"
"abcd" repeats twice, "ef" repeats three times, some shorter substrings like "a" repeat, too. "abcd" is the longest of them all.
"""

from collections import deque

def get_longest_repeated_substring(s):
    arr = [ord(c) - ord('a') for c in s]
    mod = (1 << 63) - 1
    a, n = 26, len(s)
    def search(l):
        aL = pow(a, l, mod)
        h = 0
        for i in range(l):
            h = (h * a + arr[i]) % mod
        seen = {h}
        for i in range(l, n):
            h = (h * a - arr[i - l] * aL + arr[i]) % mod
            if h in seen:
                return i - l + 1
            seen.add(h)
        return -1
    left, right = 0, n - 1
    idx = 0
    while left < right:
        mid = (left + right + 1) // 2
        i = search(mid)
        if i != -1:
            left = mid
            idx = i
        else:
            right = mid - 1
    return s[idx:idx + left]