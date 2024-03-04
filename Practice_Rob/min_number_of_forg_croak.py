"""
Author: Soumil Ramesh Kulkarni
Date: 03.02.2024

Question:
ou are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.

Return the minimum number of different frogs to finish all the croaks in the given string.

A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid "croak" return -1.



Example 1:

Input: croakOfFrogs = "croakcroak"
Output: 1
Explanation: One frog yelling "croak" twice.
Example 2:

Input: croakOfFrogs = "crcoakroak"
Output: 2
Explanation: The minimum number of frogs is two.
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".
Example 3:

Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
"""


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = k = max_frog_croak = present_frog_croak = 0
        # need to know, at particular point,
        # what are the max frog are croaking,

        for i, v in enumerate(croakOfFrogs):
            if v == 'c':
                c += 1
                # c gives a signal for a frog
                present_frog_croak += 1
            elif v == 'r':
                r += 1
            elif v == 'o':
                o += 1
            elif v == 'a':
                a += 1
            else:
                k += 1
                # frog stop croaking
                present_frog_croak -= 1

            max_frog_croak = max(max_frog_croak, present_frog_croak)
            # if any inoder occurs;
            if c < r or r < o or o < a or a < k:
                return -1

        # if all good, else -1
        if present_frog_croak == 0 and c == r and r == o and o == a and a == k:
            return max_frog_croak
        return -1
