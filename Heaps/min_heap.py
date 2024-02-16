"""
Author: Soumil Ramesh Kulkarni
Date: 02/12/2024

Question: Implement a min Heap Data Structure without using internal libraries.
"""
import sys


class MinHeap:

    # Initialize the list for Storing the binary heap
    def __init__(self):
        self.nodes = []

    # Return the len of the current Heap List
    def __len__(self):
        return len(self.nodes)

    # Return the index of the left child of a given node
    # Formula = (2 * node_index ) + 1
    def __return_left_child_index(self, node_index):
        return 2 * node_index + 1

    # Return the index of the Right child of the given Node
    # Formula = (2 * node_index) + 2
    def __return_right_child_index(self, node_index):
        return 2 * node_index + 2

    # Return the index of the Parent Node for any Given Node
    # Formula = Floor value of ( node_index - 1 ) // 2
    def __return_parent_node_index(self, node_index):
        return (node_index - 1) // 2

    # Return True if any given Node has a left Child
    # if left_child index < len (self.nodes)
    def __has_left_child(self, node_index):
        return self.__return_left_child_index(node_index) < self.__len__()

    # Return True if any given node has right Child
    # if right_child_index > len(self.nodes)
    def __has_right_child(self, node_index):
        return self.__return_right_child_index(node_index) < self.__len__()

    # Return True is parent_node_index >=0
    def __has_parent_node(self, node_index):
        return self.__return_parent_node_index(node_index) >= 0

    # Function to Get the Left Child
    def left_child(self, node_index):
        if not self.__has_left_child(node_index):
            return -sys.maxsize
        return self.nodes[self.__return_left_child_index(node_index)]

    # Function to get the Right Child
    def right_child(self, node_index):
        if not self.__has_right_child(node_index):
            return -sys.maxsize
        return self.nodes[self.__return_right_child_index(node_index)]

    # Function to get the Parent Node
    def parent_node(self, node_index):
        if not self.__has_parent_node(node_index):
            return -sys.maxsize
        return self.nodes[self.__return_parent_node_index(node_index)]

    # Swap Elements
    def _swap(self, first_index, second_index):
        if first_index >= len(self.nodes) or second_index >= len(self.nodes):
            print("Either of the Given Index is not Valid")
            return
        # Swap Elements
        self.nodes[first_index], self.nodes[second_index] = self.nodes[second_index], self.nodes[first_index]

    # Move the Last Element in the Heap to the Correct Position
    def _heapfy_up(self, child=None):
        if not child:
            child = len(self.nodes) - 1
        parent = self.__return_parent_node_index(child)
        # Check if Smaller than Parent and if yes, Swap, Keep doing this unitl parent value <= child value
        if self.__return_parent_node_index(child) and  self.nodes[child] < self.parent_node(parent):
            #Swap child and Parent
            self._swap(child, parent)
            self._heapfy_up(child=parent)
        return self.nodes

    # Add Elements to the Min Heap
    def add(self, value):
        self.nodes.append(value)
        self._heapfy_up()

    # Move the elements from the Last Position of the Heap to the correct index after deletion
    def _heapfy_down(self, index=0):
        # Move root to the Right Index in the Heap
        if index >= len(self.nodes) or not self.__has_left_child(index):
            return self.nodes

        #Check if greater than left ot right
        smaller_child_index = self.__return_left_child_index(index)
        if self.__has_right_child(index) and self.right_child(index) < self.left_child(index):
            smaller_child_index = self.__return_right_child_index(index)

        if self.nodes[index] < self.nodes[smaller_child_index]:
            return self.nodes

        if self.nodes[index] >= self.nodes[smaller_child_index]:
            #Swap
            self._swap(index, smaller_child_index)
            return self._heapfy_down(index=smaller_child_index)


    def poll(self):
        # Swap the last Element with root
        # Shrink the Size by 1
        # Heapify Down
        if self.__len__() == 0:
            print("Heap Empty ... Nothing to Delete")
            return None

        removed_node = self.nodes[0]
        self.nodes[0] = self.nodes[len(self.nodes) - 1]
        # Shrink The Size by 1
        self.nodes.pop()

        self._heapfy_down(index=0)
        return removed_node