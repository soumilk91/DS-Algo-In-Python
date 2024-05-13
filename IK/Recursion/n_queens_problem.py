"""
Author: Soumil Ramesh Kulkarni
Date: 05.12.2024

Question:
Given an integer n, find all possible ways to position n queens on an n×n chessboard so that no
two queens attack each other. A queen in chess can move horizontally, vertically, or diagonally.

Do solve the problem using recursion first even if you see some non-recursive approaches.

Example One
{
"n": 4
}
Output:

[
["--q-",
 "q---",
 "---q",
 "-q--"],

["-q--",
 "---q",
 "q---",
 "--q-"]
]
There are two distinct ways four queens can be positioned on a 4×4 chessboard without attacking each other.
The positions may appear in the output in any order. So the same two positions in different order would be another correct output.

Example Two
{
"n": 2
}
Output:

[
]
No way to position two queens on a 2×2 chessboard without them attacking each other - so empty array.
"""


import math
def find_all_arrangements(n):
    ret = []
    cols  = [i for i in range(n)]
    left_diags = [False] * (2*n-1)
    right_diags = [False] * (2*n-1)
    def helper(a, i, partial, left_diags, right_diags):
        if i >= n:
            ret.append(partial.copy())
            if not (n % 2 == 1 and a[0] == n//2):
                ret.append(list(map(lambda x: n-x-1,partial)))
            return
        for j in range(i, n if i>0 else math.ceil(n/2)):
            if left_diags[i+a[j]] or right_diags[i-a[j]+n-1]:
                continue
            left_diags[i+a[j]], right_diags[i-a[j]+n-1] = True, True
            a[i], a[j] = a[j], a[i]
            partial.append(a[i])
            helper(a, i+1, partial, left_diags, right_diags)
            partial.pop()
            a[i], a[j] = a[j], a[i]
            left_diags[i+a[j]], right_diags[i-a[j]+n-1] = False, False
    helper(cols, 0, [], left_diags, right_diags)
    return list(map(lambda partial: ['-'*row+'q'+'-'*(n-row-1) for row in partial], ret))
