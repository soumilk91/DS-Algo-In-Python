"""
Author: Soumil Ramesh Kulkarni
Date: 05.15.2024

Question:
Given an integer n, find the smallest palindromic number that’s greater than n.

Example One
{
"n": 5
}
Output:

6
6 is a palindromic number, and it is greater than 5. There is no palindromic number lesser than 6 and greater than 5.

Example Two
{
"n": 10
}
Output:

11
"""

def next_palindrome(n):
    ns = str(n)
    if sum(x =="9" for x in ns) == len(ns):
        return 10**len(ns) + 1

    if len(ns) == 1:
        return n+1

    m = len(ns)//2
    if len(ns) % 2 == 1:
        left,right = ns[:m], ns[m+1:]
        if int(left[::-1]) > int(right):
            return int(left+ ns[m] + left[::-1])
        else:
            left = str(int(ns[:m+1]) + 1)
            return int(left + left[::-1][1:])

    else:
        left, right = ns[:m], ns[m:]
        if int(left[::-1]) > int(right):
            return int(left + left[::-1])
        else:
            left = str(int(left)+1)
            return int(left + left[::-1])
