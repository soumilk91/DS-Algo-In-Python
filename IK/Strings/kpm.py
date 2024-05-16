"""
Author: Soumil Ramesh Kulkarni
Date: 05.16.2024

Question:
Given a text and a pattern, find all occurrences of the pattern in the text. Return start indices of all
occurrences in the ascending order.

The problem is named after the string-searching algorithm called KMP (Knuth Morris Pratt).

Example
{
"text": "Ourbusinessisourbusinessnoneofyourbusiness",
"pattern": "business"
}
Output:

[3, 16, 34]
"""


def match_pattern_in_text(text, pattern):
    """
    Args:
     text(str)
     pattern(str)
    Returns:
     list_int32
    """
    # Write your code here.
    def pattern_prep(pattern):
        L = len(pattern)
        result = [0] * L
        first = 0
        last = 1
        while last < L:
            if pattern[last] == pattern[first]:
                first += 1
                result[last] = first
                last += 1
            else:
                result[last] = result[first]
                last += 1
        return result

    def find_matches(text, pattern, prep):
        results = []
        T = len(text)
        P = len(pattern)
        t = 0
        p = 0
        while t < T:
            char = text[t]
            pchar = pattern[p]
            if char == pchar:
                t += 1
                p += 1
                if p == P:
                    results.append(t - p)
                    p = prep[p - 1]
            elif p == 0:
                t += 1
            else:
                p = prep[p - 1]

        if len(results) == 0:
            return [-1]
        return results

    prep = pattern_prep(pattern)
    results = find_matches(text, pattern, prep)

    return results