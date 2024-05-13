"""
Author: Soumil Ramesh KUlkarni
Date: 05.12.2024

Question:
Given coordinates of a point p and n other points on a two-dimensional surface,
find k points out of n which are the nearest to point p.

Distance is measured by the standard Euclidean method.

Example One
{
"p_x": 1,
"p_y": 1,
"k": 1,
"n_points": [
[0, 0],
[1, 0]
]
}
Output:

[
[1, 0]
]
The distance of point {0, 0} from point p{1, 1} is sqrt(2) and that of point {1, 0} is 1.
We need to choose 1(k) point having the minimum distance from point p. So it is {1, 0}.

Example Two
{
"p_x": 1,
"p_y": 1,
"k": 2,
"n_points": [
[1, 0],
[2, 1],
[0, 1]
]
}
Output:

[
[1, 0],
[2, 1]
]
We can see that there are all the points are at the same distance from point p. So the
answer can be any 2 points. Here {{1, 0}, {0, 1}} and {{2, 1}, {0, 1}} are all equally acceptable answers.
"""

import math
import random
def nearest_neighbours(p_x, p_y, k, n_points):
    """
    Args:
     p_x(int32)
     p_y(int32)
     k(int32)
     n_points(list_list_int32)
    Returns:
     list_list_int32
    """
    # approach -- get all the distance
    # (distance1, start1, end1)....(distancen, startn, endn)
    # 1. sort it and get [:k]
    # 2. do a quick select for kth element and essential [:k]
    # quick select is faster --> O(N)
    # T(N) = T(N/2) + O(cN)
    # T(N) = cn + cn/2 + cn/4 + cn/8... . N

    dis_point_list = []
    for index, point in enumerate(n_points):
        dis_from_point = distance(p_x, p_y, point[0], point[1])
        dis_point_list.append((dis_from_point, index))

    result = []
    quick_select(0, len(n_points) - 1, k - 1, dis_point_list)
    for i in range(k):
        result.append(n_points[dis_point_list[i][1]])
    return result


def quick_select(start, end, index_to_find, array):
    if start >= end:
        return
    rindex = random.randint(start, end)
    # swap with zero
    array[start], array[rindex] = array[rindex], array[start]

    smaller = start - 1
    bigger = start
    while bigger <= end:
        if array[bigger] <= array[start]:
            smaller += 1
            array[bigger], array[smaller] = array[smaller], array[bigger]
        bigger += 1
    # swap start with smaller
    array[smaller], array[start] = array[start], array[smaller]

    if smaller == index_to_find:
        return
    elif smaller < index_to_find:
        return quick_select(smaller, end, index_to_find, array)
    elif smaller > index_to_find:
        return quick_select(start, smaller, index_to_find, array)


def distance(p1_x, p1_y, p2_x, p2_y):
    # sqrt p2_x-p1_x*
    x_diff = p2_x - p1_x
    y_diff = p2_y - p1_y
    return math.sqrt(x_diff * x_diff + y_diff * y_diff)
