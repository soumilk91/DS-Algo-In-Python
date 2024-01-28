"""
Author: Soumil Ramesh Kulkarni
Date: 01/25/2024

Question: Write a function for Selection Sort
"""
"""
Approach: 
-> Locate the smallest item and put it in the first Place 
-> locate the second smallest item and put in the second Place 
-> Repeate this Process on the entire Array 
"""

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def selectionSort(array):
    for outer in range(len(array)):
        minvalue = array[outer]
        swap_index = outer
        for inner in range(outer+1, len(array)):
            if array[inner] <= minvalue:
                minvalue = array[inner]
                swap_index = inner
        array[outer], array[swap_index] = array[swap_index], array[outer]
    return array

print(selectionSort([5,2,1,9,6]))
print(selectionSort([5,2,1,9,6,6]))
print(selectionSort([]))
