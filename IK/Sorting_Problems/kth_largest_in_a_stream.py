"""
Author: Soumil Ramesh Kulkarni
Date: 02/13/2024

Question:
Given an initial list along with another list of numbers to be appended with the initial list and an integer k,
return an array consisting of the k-th largest element after adding each element from the first list to the second list.
Eg:
{
"k": 2,
"initial_stream": [4, 6],
"append_stream": [5, 2, 20]
}
Output: [5, 5, 6]

Append	Stream	Sorted Stream	2nd largest
5	[4, 6, 5]	[4, 5, 6]	5
2	[4, 6, 5, 2]	[2, 4, 5, 6]	5
20	[4, 6, 5, 2, 20]	[2, 4, 5, 6, 20]	6
"""

# Brute Force

def kth_largest(k, initial_stream, append_stream):
    """
    Args:
     k(int32)
     initial_stream(list_int32)
     append_stream(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.

    # create a max heap
    return_list = []

    for j in append_stream:
        initial_stream.append(i)
        initial_stream.sort()
        return_list.append(initial_stream[-k])

    return return_list

import heapq
def kth_largest_using_max_heap(k, initial_stream, append_stream):
    """
    Args:
     k(int32)
     initial_stream(list_int32)
     append_stream(list_int32)
    Returns:
     list_int32
    """
    return_list = []
    heap = []

    # Insert all the elements in the initial stream into the max heap
    for initial in initial_stream:
        heapq.heappush(heap, -1*initial)

    # Now loop Over the appendstream and everytime you push an element form the stream into the max heap,
    # Run a for loop for k times to remove max elements from the heap.
    # Put all the elements back in the heap

    temp_list = []
    for append in append_stream:
        heapq.heappush(heap, -1*append)
        for j in range(k):
            temp_list.append(heapq.heappop(heap))
        return_list.append(-1* temp_list[len(temp_list) - 1])

        while temp_list:
            heapq.heappush(heap, temp_list.pop())
    return return_list


import heapq

def kth_largest_using_min_heap(k, initial_stream, append_stream):
    min_heap = []

    for num in initial_stream:
        heapq.heappush(min_heap, num)

        # Make sure that the heap size does not exceed k.
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Remove the element smaller than the k largest elements.

    result = []

    for num in append_stream:
        heapq.heappush(min_heap, num)

        # Make sure that the heap size does not exceed k.
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Remove the element smaller than the k largest elements.

        # Adding the current k-th largest element.
        result.append(min_heap[0])

    return result

