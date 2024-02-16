"""
Author: Soumil Ramesh Kulkarni
Date: 02/15/2024

Question: Given an integer array and a number k, find the k most frequent elements in the array.
Eg:
{
"arr": [1, 2, 3, 2, 4, 3, 1],
"k": 2
}
Output: [3, 1]

{
"arr": [1, 2, 1, 2, 3, 1],
"k": 1
}
Output: [1]
"""


def find_top_k_frequent_elements(arr, k):
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    compare_dict = {}
    for element in arr:
        if element in compare_dict:
            compare_dict[element] += 1
        else:
            compare_dict[element] = 1

    import heapq
    heap = []
    for key in compare_dict:
        heapq.heappush(heap, (-1 * compare_dict[key], key))

    result = []
    while k > 0:
        temp = heapq.heappop(heap)
        result.append(temp[1])
        k -= 1
    return result
