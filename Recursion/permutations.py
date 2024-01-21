"""
Author: Soumil Ramesh Kulkarni
Date: 01/17/2024

Question: Given a list of distinct integers, return all the possible permutations.
eg: input = [1,2,3]
Output = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
"""

result_list = []
def _helper(numlist, start_index, slate):
    #Base Case
    if start_index == len(numlist):
        if slate[:] not in result_list:
            result_list.append(slate[:])
        return

    #Recursive Case
    for temp in range(start_index, len(numlist)):
        # Swap The elements in the list to the first Position in the subproblem
        numlist[temp], numlist[start_index] = numlist[start_index], numlist[temp]
        slate.append(numlist[start_index])

        # Call the Recursive Function
        _helper(numlist, start_index+1, slate)

        # Pop the element from the slate and swap the elements back to their original places
        slate.pop()
        numlist[temp], numlist[start_index] = numlist[start_index], numlist[temp]


def permutations(numlist):
    _helper(numlist, 0, [])

permutations([1,2,2])
print(result_list)