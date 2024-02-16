"""
Author: Soumil Kulkarni
Date: 02/29/2024

Question: Implement Min heap using heapq function
"""

import heapq

class minHeap:
    def __init__(self):
        self.nodes = []
        heapq.heapify(self.nodes)

    def add_node(self, value):
        heapq.heappush(self.nodes, value)

    def delete_element_from_min_heap(self):
        return_node = None
        if self.nodes:
            return_node = heapq.heappop(self.nodes)
        return return_node

class maxHeap:
    def __init__(self):
        self.nodes = []
        heapq.heapify(self.nodes)

    def add_node(self, value):
        heapq.heappush(self.nodes, -1*value)

    def delete_element_from_max_heap(self):
        return_node = None
        if self.nodes:
            return_node = heapq.heappop(self.nodes)
        return -1 * return_node

temp = maxHeap()
temp.add_node(1)
temp.add_node(5)
temp.add_node(7)
temp.add_node(10)
print(temp.nodes)
temp1= temp.delete_element_from_max_heap()
print(temp1)
print(temp.nodes)