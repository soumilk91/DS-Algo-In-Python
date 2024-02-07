"""
Author: Soumil Ramesh Kulkarni
Date: 02.06/2024

Question:
Generate ALL possible subsets of a given set.
The set is given in the form of a string s containing distinct lowercase characters 'a' - 'z'.

{
"s": "xy"
}
output:
["", "x", "y", "xy"]

Notes:
Any set is a subset of itself.
Empty set is a subset of any set.
Output contains ALL possible subsets of given string.
Order of strings in the output does not matter. E.g. s = "a", arrays ["", "a"] and ["a", ""] both will be accepted.
Order of characters in any subset must be same as in the input string.
For s = "xy", array ["", "x", "y", "xy"] will be accepted, but ["", "x", "y", "yx"] will not be accepted.

"""

def _helper(string, index, slate, results):
    # Base Case
    if index == len(string):
        results.append("".join(slate[:]))
        return

    # Recursive Cases

    # Include
    slate.append(string[index])
    _helper(string, index + 1, slate, results)
    slate.pop()

    # Exclude
    _helper(string, index + 1, slate, results)


def generate_all_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    return_list = []
    _helper(s, 0, [], return_list)
    return return_list
