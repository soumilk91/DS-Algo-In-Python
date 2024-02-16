"""
Author: Soumil Ramesh Kulkarni
Date: 02/12/2024

Question: Sorting using heap ... Implement a heap Sort algorithm
Space Complexity: O(n)
Time Complexity: O(n logn)
"""

import heapq

def heapSort(input_array):
    print(input_array)
    # Heapify all the elemennts in the given Array
    heapq.heapify(input_array)
    print(input_array)
    sorted_array = []
    # now keep removing min elements from the heap and insert into the sorted_array
    for _ in range(len(input_array)):
        sorted_array.append(heapq.heappop(input_array))
    print(sorted_array)


heapSort([50,1,450,2,4,9,102,102])