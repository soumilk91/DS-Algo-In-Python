"""
Author: Soumil Ramesh Kulkarni
Date: 02/06/2024

Question:
Given a string that might contain duplicate characters, find all the possible distinct subsets of that string.
{
"s": "aab"
}
["", "a", "aa", "aab", "ab", "b"]

"""


def _helper(s, index, slate, results):
    # Base Case
    if index == len(s):
        temp = slate[:]
        if "".join(sorted(temp)) not in results:
            results[("".join(sorted(temp)))] = 1
        return

    # Recursive Case
    # Inclusion
    slate.append(s[index])
    _helper(s, index + 1, slate, results)
    slate.pop()

    # Exclusion
    _helper(s, index + 1, slate, results)


def get_distinct_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    results = {}
    return_list = []
    _helper(s, 0, [], results)
    for i in results.keys():
        return_list.append(i)
    return return_list
