"""
Author: Soumil Ramesh Kulkarni
Date: 01/27/2024

Question:
You have to build a min stack. Min stack should support push, pop methods (as usual stack) as well as one method that returns the minimum element in the entire stack.

You are given an integer array named operations of size n, containing values >= -1.

operations[i] = -1 means you have to perform a pop operation. The pop operation does not return the removed/popped element.
operations[i] = 0 means you need to find the minimum element in the entire stack and add it at the end of the array to be returned.
operations[i] >= 1 means you need to push operations[i] on the stack.

Eg:
{
"operations": [10, 5, 0, -1, 0, -1, 0]
}
[5, 10, -1]
"""


def min_stack(operations):
    """
    Args:
     operations(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    return_list = []
    min_stack = []
    stack = []
    for operation in operations:
        if operation >= 1:
            if not min_stack:
                min_stack.append(operation)
            elif min_stack[len(min_stack) - 1] >= operation:
                min_stack.append(operation)
            stack.append(operation)

        elif operation == -1:
            if min_stack and min_stack[len(min_stack) - 1] == stack[len(stack) - 1]:
                min_stack.pop()
            if stack:
                stack.pop()
        else:
            if min_stack:
                return_list.append(min_stack[len(min_stack) - 1])
            else:
                return_list.append(-1)
    return return_list