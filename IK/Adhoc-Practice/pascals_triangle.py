"""
Author: Soumil Rmaesh Kulkarni
Date: 05.15.2024

Question:

Pascal’s triangle is a triangular array of the binomial coefficients.
Write a function that takes an integer value n as input and returns a two-dimensional array representing pascal’s triangle.

pascalTriangleArray is a two-dimensional array of size n * n, where
pascalTriangleArray[i][j] = BinomialCoefficient(i, j); if j <= i,
pascalTriangleArray[i][j] = 0; if j > i

Example
{
"n": 4
}
Output:

[
[1],
[1, 1],
[1, 2, 1],
[1, 3, 3, 1]
]
"""


def find_pascal_triangle(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    if n == 0:
        return []

    if n == 1:
        return [[1]]

    if n == 2:
        return [[1], [1, 1]]

    res = [[1], [1, 1]]

    for i in range(3, n + 1):
        prev = res[-1]
        next = [1] * (len(prev) + 1)

        for j in range(1, len(prev)):
            next[j] = (prev[j - 1] + prev[j]) % (10 ** 9 + 7)

        res.append(next)

    return res
