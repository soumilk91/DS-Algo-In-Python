"""
Author: Soumil Ramesh Kulkarni
Date: 04.15.2024

Question:
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.



Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
Example 2:

Input: strings = ["a"]
Output: [["a"]]

"""


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_hash(string):
            key = []
            for a, b in zip(string, string[1:]):
                key.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
            return ''.join(key)

        compare_dict = {}
        for string in strings:
            hashkey = get_hash(string)
            if hashkey not in compare_dict:
                compare_dict[hashkey] = [string]
            else:
                compare_dict[hashkey].append(string)

        return list(compare_dict.values())

