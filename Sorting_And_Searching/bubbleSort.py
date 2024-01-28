"""
Author: Soumil Ramesh Kulkarni
Date: 01/25/2024

Question: Write a function for bubble Sort
"""

"""
Approach: 
-> Keep Swapping at each iteration
"""

# Time Complexity: O(n^2)
# Space Complexity: O(1)
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] >= array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubbleSort([5,2,1,9,6]))
print(bubbleSort([5,2,1,9,6,6]))
print(bubbleSort([]))