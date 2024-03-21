"""
Author: Soumil Ramesh Kulkarni
Date: 02/03/2024

Question:
Given a string brackets that only contains characters '(' and ')', find the length of the longest substring that has
"balanced parentheses".

Eg:
{
"brackets": "((((())(((()"
}
output: 4

{
"balanced": "()()()"
}
output:6
"""


def find_max_length_of_matching_parentheses(brackets):
    """
    Args:
     brackets(str)
    Returns:
     int32
    """
    # Write your code here

    # Base Case
    if not brackets:
        return 0

    max_len = 0
    stack = [-1]

    for index, brace in enumerate(brackets):
        if brace == "(":
            stack.append(index)
        else:
            stack.pop()
            if not stack:
                stack.append(index)
            else:
                current_len = index - stack[len(stack) - 1]
                max_len = max(current_len, max_len)
    return max_len

