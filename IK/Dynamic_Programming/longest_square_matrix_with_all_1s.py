"""
Author: Soumil Ramesh Kulkarni
Date: 05.16.2024

Question:
Given a two-dimensional binary matrix of size n * m, find the largest square submatrix with all 1s.

Example
{
"n": 3,
"m": 3,
"mat": [
[1, 0, 0],
[0, 1, 1],
[0, 1, 1]
]
}
Output:

2
2x2 submatrix at right-bottom has all 1s. That’s the largest one. Length of its side is 2.


"""


def largest_sub_square_matrix(n, m, mat):
    """
    Args:
     n(int32)
     m(int32)
     mat(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    # Create the auxillary matrix
    aux = [[0] * m for _ in range(n)]

    # Initialize the first row and column of the aux
    for r in range(n):
        aux[r][0] = mat[r][0]
    for c in range(m):
        aux[0][c] = mat[0][c]

    # Filling in the remaining aux
    for r in range(1, n):
        for c in range(1, m):
            if mat[r][c] == 1:
                aux[r][c] = min(aux[r - 1][c], aux[r][c - 1], aux[r - 1][c - 1]) + 1

    return max(max(row) for row in aux)
