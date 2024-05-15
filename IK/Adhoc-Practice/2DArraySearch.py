"""
Author: Soumil Ramesh Kulkarni
Date: 05.15.2024

Question:

You are given a sorted two-dimensional integer array numbers of size r * c, where all the numbers are in
non-decreasing order from left to right and top to bottom. i.e. numbers[i][j] <= numbers[i + 1][j] and
numbers[i][j] <= numbers[i][j + 1] for all i = 0, 1, ..., (r - 2) and j = 0, 1, ..., (c - 2).

Check if a given number x exists in numbers or not. Given an numbers, you have to answer q such queries.

Example One
{
"numbers": [
[1, 2, 3, 12],
[4, 5, 6, 45],
[7, 8, 9, 78]
],
"queries": [6, 7, 23]
}
Output:

[1, 1, 0]
Given number x = 6 is present at numbers[1][2] and x = 7 is present at numbers[2][0]. Hence, 1 returned for them,
while x = 23 is not present in numbers, hence 0 returned.

Example Two
{
"numbers": [
[3, 4],
[5, 10]
],
"queries" = [12, 32]
}
Output:

[0, 0]
Given number x = 12 and x = 32 are not present in numbers. Hence, 0 returned for both of the queries.
"""


def search(numbers, queries):
    """
    Args:
     numbers(list_list_int32)
     queries(list_int32)
    Returns:
     list_bool
    """
    # Write your code here.

    querieSet = set(queries)
    resSet = set()
    for i in range(len(numbers)):
        for j in range(len(numbers[0])):
            if numbers[i][j] in querieSet:
                resSet.add(numbers[i][j])

    res = []
    for q in queries:
        if q in resSet:
            res.append(True)
        else:
            res.append(False)

    return res
