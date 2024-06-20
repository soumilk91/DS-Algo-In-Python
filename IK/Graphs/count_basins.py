"""
Author: Soumil Ramesh Kulkanri
Date: 05.11.2024

Question:
Given the altitudes of the regions on a surface, determine the basins where water would collect if
poured onto that surface.

Region whose four neighbors (right, left, up and down) are all higher in altitude is called a sink.
All the water would collect in sinks. If a region is not a sink, it is guaranteed to have a single lowest
neighbor where water will drain to. All regions that drain to a particular sink–directly or indirectly–collectively
form one basin. Partition the surface into the basins and return their sizes in the non-decreasing order.

Example One
{
"matrix": [
[1, 5, 2],
[2, 4, 7],
[3, 6, 9]
]
}
Output:

[2, 7]
There are two basins, one consists of two cells and the other consists of seven. They are labeled with A’s and B’s here:
B B A
B B A
B B B

The sink of basin A is cell (0, 2). The sink of basin B is cell (0, 0).

Example Two
{
"matrix": [
[0, 2, 1, 3],
[2, 1, 0, 4],
[3, 3, 3, 3],
[5, 5, 2, 1]
]
}
Output:

[4, 5, 7]
There are three basins. They are labeled with A, B and C here:
B B C C
B C C C
B C C A
B A A A

The sinks of basins A, B and C are (3, 3), (0, 0) and (1, 2) respectively.
"""


def find_basins(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    nrows = len(matrix)
    ncols = len(matrix[0])

    basins = [[-1] * ncols for _ in range(nrows)]

    def get_ngb(r, c):
        minrow = r
        mincol = c

        if basins[r][c] == -1:
            if 0 <= r - 1 and matrix[r - 1][c] < matrix[minrow][mincol]:
                minrow = r - 1
                mincol = c
            if 0 <= c - 1 and matrix[r][c - 1] < matrix[minrow][mincol]:
                minrow = r
                mincol = c - 1
            if c + 1 < ncols and matrix[r][c + 1] < matrix[minrow][mincol]:
                minrow = r
                mincol = c + 1
            if r + 1 < nrows and matrix[r + 1][c] < matrix[minrow][mincol]:
                minrow = r + 1
                mincol = c

            if minrow == r and mincol == c:
                basins[r][c] = cnt[0]
            else:
                basins[r][c] = get_ngb(minrow, mincol)

        return basins[r][c]

    def count_sort(arr):
        maxelem = max(arr)
        minelem = min(arr)
        range_elem = maxelem
        cnt_arr = [0] * (range_elem + 1)
        out = [0] * len(arr)

        for i in range(len(arr)):
            cnt_arr[arr[i]] += 1

        for i in range(1, len(cnt_arr)):
            cnt_arr[i] += cnt_arr[i - 1]

        for i in range(len(arr) - 1, -1, -1):
            out[cnt_arr[arr[i]] - 1] = arr[i]
            cnt_arr[arr[i]] -= 1

        return out

    cnt = [0]

    for r in range(nrows):
        for c in range(ncols):

            val = get_ngb(r, c)
            if val == cnt[0]:
                cnt[0] += 1

    basin_cnt = [0] * cnt[0]

    for r in range(nrows):
        for c in range(ncols):
            basin_cnt[basins[r][c]] += 1

    return count_sort(basin_cnt)