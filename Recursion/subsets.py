"""
Author: Soumil Ramesh Kulkarni
Date: 01/17/2024

Question: Given a set of distinct integers, return all possible subsets ... No duplicates

The only question at each level of the recursive tree we need to ask is INCLUDE / EXCLUDE
eg: Input = [1,2,3]
Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
"""

return_list = []
def _helper(num_list, start_index, slate):
    """
    num_list = input definition
    start_index = input definition
    slate = partial result
    """
    # Base Case
    if start_index == len(num_list):
        return_list.append(slate[:])
        return

    # Recursive Case
    # INCLUDE DECISION

    slate.append(num_list[start_index])
    _helper(num_list, start_index+1, slate)
    slate.pop()

    # EXCLUDE DECISION
    _helper(num_list, start_index+1, slate)

def subsets(numlist):
    # Root Case
    _helper(numlist, 0, [])
    print(return_list)


subsets([1,2,3,4])
