"""
Author: Soumil Ramesh Kulkarni
Date: 05.16.2024

Question:

Given a sequence of matrices, find the most efficient way to multiply these matrices together.
The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.

We have many options to multiply a chain of matrices because matrix multiplication is associative. In other words,
no matter how we parenthesize the product, the result will be the same. For example, if we had four matrices A, B, C, and D,
we would have:

(ABC)D = (AB)(CD) = A(BCD) = ....

However, the order in which we parenthesize the product affects the number of simple arithmetic operations needed to
compute the product, or the efficiency. For example, suppose A is a 10 × 30 matrix, B is a 30 × 5 matrix, and C is a 5 × 60 matrix.
Then,

(AB)C = (10 × 30 × 5) + (10 × 5 × 60) = 1500 + 3000 = 4500 operations

A(BC) = (30 × 5 × 60) + (10 × 30 × 60) = 9000 + 18000 = 27000 operations.

Clearly, the first parenthesization requires less number of operations.

Given an array matrix_sizes, which represents the chain of matrices such that the i-th matrix matrix_sizes[i] is of
dimension matrix_sizes[i - 1] x matrix_sizes[i], we need to write a function that should return the minimum number of multiplications needed to multiply the chain. Length of the chain of matrices is n and thus the size of matrix_sizes is n + 1.

Example
{
"matrix_sizes": [10, 30, 5, 60]
}
Output:

4500
"""

def  minimum_multiplication_cost(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[0]*n for i in range(n)]
    for d in range(1, n-1):
        for i in range(1, n-d):
            j = i + d
            p = matrix_sizes[i-1]*matrix_sizes[j]
            dp[i][j] = min([dp[i][k] + dp[k+1][j] + p*matrix_sizes[k] for k in range(i, j)])
    return dp[1][n-1]
