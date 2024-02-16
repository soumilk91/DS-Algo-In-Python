"""
Author: Soumil Ramesh Kulkarni
Date: 02.15.2024

Question:Given a list of numbers, the task is to insert these numbers into a stream and find the median of the stream
after each insertion. If the median is a non-integer, consider it’s floor value.

The median of a sorted array is defined as the middle element when the number of elements is odd and the mean of the
middle two elements when the number of elements is even.

Eg:
{
"stream": [3, 8, 5, 2]
}
Output: [3, 5, 5, 4]
Iteration	Stream	Sorted Stream	Median
1	         [3]	     [3]	      3
2	        [3, 8]	    [3, 8]	    (3 + 8) / 2 => 5
3	       [3, 8, 5]	[3, 5, 8]	    5
4	      [3, 8, 5, 2]	[2, 3, 5, 8]	(3 + 5) / 2 => 4
"""


"""
Asymptotic complexity in terms of `n` = size of the input array:
* Time: O(n * log(n)).
* Auxiliary space: O(n).
* Total space: O(n).
"""

# To store the smaller half of the input numbers.
max_heap = []
# To store the larger half of the input numbers.
min_heap = []

import heapq

def add_new_element(num):
    # Balancing heaps to make sure:
    # - smaller half of input numbers are always in the max heap
    # - larger half of input numbers are always in the min heap
    heapq.heappush(max_heap, -num)
    heapq.heappush(min_heap, -heapq.heappop(max_heap))

    # Maintain size property.
    # 1. len(max_heap) = len(min_heap), when the number of elements is even
    # 2. len(max_heap) = len(min_heap) + 1, when the number of elements is odd
    if len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

def get_current_stream_median():
    # If the number of elements in the stream is even.
    if len(max_heap) == len(min_heap):
        return (-max_heap[0] + min_heap[0]) // 2

    # If the number of elements in the stream is odd.
    return -max_heap[0]

def online_median(stream):
    medians = []

    for num in stream:
        add_new_element(num)
        medians.append(get_current_stream_median())
    return medians
