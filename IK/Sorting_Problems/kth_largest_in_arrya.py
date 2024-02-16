"""
Author: Soumil Ramesh Kulkarni
Date: 02.15.2024

Question: Given an array of integers, find the k-th largest number in it.
Eg:
{
"numbers": [5, 1, 10, 3, 2],
"k": 2
}
Output: 5

{
"numbers": [4, 1, 2, 2, 3],
"k": 4
}
Output: 2

Constraints:

1 <= array size <= 3 * 105
-109 <= array elements <= 109
1 <= k <= array size
"""


def kth_largest_in_an_array(numbers, k):
    """
    Args:
     numbers(list_int32)
     k(int32)
    Returns:
     int32
    """
    # Write your code here.
    # Use max heaps and keep Removing elements from the root until k !=0
    import heapq
    temp = []
    for i in numbers:
        heapq.heappush(temp, -1 * i)
    element = None
    while k > 0:
        k -= 1
        element = heapq.heappop(temp)
    if element:
        return -1 * element
    else:
        return 0

