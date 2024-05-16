"""
Author: Soumil Ramesh Kulkarni
Date: 05.16.2024

Question:
Find the longest common subsequence of two strings.

A subsequence is a sequence that can be derived from another sequence by deleting zero or more
elements without changing the order of the remaining elements.

Example
{
"a": "ABCDE",
"b": "AECBD"
}
Output:

"ABD"
Subsequence "ABD" can be derived from the first string by deleting characters "C" and "E".
From the second string it can be derived by deleting "E" and "C". No common subsequence longer than three characters
exists in the two given strings. "ACD" is another common subsequence of length three; it is also a correct answer.
"""

from collections import deque


def lcs(a, b):
    """
    Args:
     a(str)
     b(str)
    Returns:
     str
    """
    A, B = len(a), len(b)

    #           { 1 + dp(i+1, j+1) if a[i] == b[j]
    # dp(i,j) = {
    #           { max( dp(i+1, j), dp(i, j+1) ), otherwise
    #         = "what is the maximum subsequence length between a[i:] and b[j:]?"
    #
    # in order to efficiently reconstruct the answer, we must unfortunately keep the whole dp matrix around
    dp = [[-1] * (B + 1) for _ in range(A + 1)]

    # Base Cases
    # (1) maximum subsequence size between two empty strings is 0; that subsequence is the empty string
    dp[A][B] = 0
    # (2) maximum subsequence size between one empty string and one non-empty string is... still 0!
    for j in range(B):
        dp[A][j] = 0  # bottom row of dp matrix
    # (3) maximum subsequence size betwen one non-empty string and one empty string is... 0 again!
    for i in range(A):
        dp[i][B] = 0  # rightmost column of dp matrix

    # Traversal Direction
    # - bottom-up & right-to-left
    for i in reversed(range(A)):
        for j in reversed(range(B)):
            if a[i] == b[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    # Edge Case:
    # - There was no common subsequence between the two strings
    if dp[0][0] == 0:
        return "-1"

    # Answer Reconstruction:
    # - Greedy DFS on decision tree using dp matrix as a guide
    i, j = 0, 0
    answer = []
    while i < A and j < B:
        if a[i] == b[j]:
            answer.append(a[i])
            i += 1
            j += 1
        elif dp[i + 1][j] > dp[i][j + 1]:
            i += 1
        else:
            j += 1

    return ''.join(answer)