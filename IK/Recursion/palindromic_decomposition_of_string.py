"""
Author: Soumil Ramesh Kulkarni
Date: 05.12.2024

Question:
Find all palindromic decompositions of a given string s.

A palindromic decomposition of string is a decomposition of the string into substrings,
such that all those substrings are valid palindromes.

Example
{
"s": "abracadabra"
}
Output:

["a|b|r|a|c|ada|b|r|a", "a|b|r|aca|d|a|b|r|a", "a|b|r|a|c|a|d|a|b|r|a"]
Notes
Any string is its own substring.
Output should include ALL possible palindromic decompositions of the given string.
Order of decompositions in the output does not matter.
To separate substrings in the decomposed string, use | as a separator.
Order of characters in a decomposition must remain the same as in the given string. For example,
for s = "ab", return ["a|b"] and not ["b|a"].
Strings in the output must not contain whitespace. For example, ["a |b"] or ["a| b"] is incorrect.
Constraints:

1 <= length of s <= 20
s only contains lowercase English letters.
"""


def is_palindrome(string, left, right):
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


def helper(result, string, pos, partial):
    n = len(string)
    # if at the end add the partial to result container
    if pos == n:
        result.append(partial)
        return

    # Try to add s[pos, i] if it is a palindrome
    for i in range(pos, n):
        # backtracking step
        if is_palindrome(string, pos, i):
            if pos == 0:
                # We are adding s[0, i] so do not put '|' before it. Passing down a new partial
                helper(result, string, i + 1, string[pos:i + 1])
            else:
                helper(result, string, i + 1, partial + "|" + s[pos:i + 1])


def generate_palindromic_decompositions(s):
    res = []
    helper(res, s, 0, "")
    return res