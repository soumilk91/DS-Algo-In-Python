"""
Author: Soumil Ramesh Kulkarni
Date: 01/25/2024

Question: Write a Function for insertion Sort
"""

"""
Approach: 
-> divide the array into 2 parts sorted and unsorted divided by hole 
-> Keep shifting elements from unsorted part to the sorted part 
"""

def insertionSort(array):
    for i in range(1, len(array)):
        value = array[i]
        hole = i

        while (hole > 0 and array[hole-1] > value):
            array[hole] = array[hole - 1]
            hole -= 1
        array[hole] = value
    return array

print(insertionSort([5,2,1,9,6]))
print(insertionSort([5,2,1,9,6,6]))
print(insertionSort([]))