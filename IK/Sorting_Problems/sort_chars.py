"""
Author: Soumil Ramesh Kulkarni
Date: 04.03.2024

Question:
Given a list of characters, sort it in the non-decreasing order based on ASCII values of characters.

Example
{
"arr": ["a", "s", "d", "f", "g", "*", "&", "!", "z", "y"]
}
Output:

["!", "&", "*", "a", "d", "f", "g", "s", "y", "z"]
"""


def sort_array(arr):
    """
    Args:
     arr(list_char)
    Returns:
     list_char
    """
    # Write your code here.
    return_list = []
    for char in arr:
        return_list.append(ord(char))
    return_list.sort()
    ret = []
    for value in return_list:
        ret.append(chr(value))
    return ret

