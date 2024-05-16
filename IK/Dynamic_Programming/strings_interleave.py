"""
Author: Soumil Ramesh Kulkarni
Date: 05.16.2024

Question:
You are given three strings: a, b and i, write a function that checks whether i is an interleaving of a and b.
String i is said to be interleaving string a and b, if:

len(i) = len(a) + len(b).
i only contains characters present in a or b.
i contains all characters of a. From a, any character a[index] should be added exactly once in i.
i contains all characters of b. From b, any character b[index] should be added exactly once in i.
Order of all characters in individual strings (a and b) is preserved.

Example One
{
"a": "123",
"b": "456",
"i": "123456"
}
Output:

true
Example Two
{
"a": "AAB",
"b": "AAC",
"i": "AAAABC"
}
Output:

true
"""

def do_strings_interleave(a, b, i):
    """
    Args:
     a(str)
     b(str)
     i(str)
    Returns:
     bool
    """
    # Write your code here.
    n = len(a)
    m = len(b)
    if n == 0:
        return b == i
    elif m == 0:
        return a == i
    k = len(i)
    return helper(a, b, i, n-1, m-1, k-1)


def helper(A, B, I, i, j, k):
    if k+1 != (i+j+2):
        return False
    if k < 0:
        return True
    if i >= 0 and j >= 0 and A[i] == B[j] and A[i] == I[k]:
        return helper(A, B, I, i-1, j, k-1) or helper(A, B, I, i, j-1, k-1)
    if i>=0 and A[i] == I[k]:
        return helper(A, B, I, i-1, j, k-1)
    elif j>=0 and B[j] == I[k]:
        return helper(A, B, I, i, j-1, k-1)
    else:
        return False