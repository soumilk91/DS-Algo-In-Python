"""
Author: Soumil Ramesh Kulkarni
Date: 01/19/2024

Question: Given a seven-digit phone number, return all the character combinations that can be generated according to the following mapping:

character mapping to number on the keypad on any phone
mapping_dict = {'2':['a','b','c'], '3':['d','e','f'], '4':['g', 'h', 'i'],
        '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'],
        '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']
    }

Eg: {
"phone_number": "1234567"
}

Output:
[
"adgjmp",
"adgjmq",
"adgjmr",
"adgjms",
"adgjnp",
...
"cfilns",
"cfilop",
"cfiloq",
"cfilor",
"cfilos"
]
"""

from typing import *
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        result = []
        self.helper(digits, mapping, 0, [], result)
        return result

    def helper(self, digits, mapping, index, slate, result):
        # Base Case
        if index == len(digits):
            result.append("".join(slate[:]))
            return

        # Recursive Case
        if digits[index] not in mapping:
            self.helper(digits, mapping, index + 1, slate, result)
        else:
            for char in mapping[digits[index]]:
                slate.append(char)
                self.helper(digits, mapping, index + 1, slate, result)
                slate.pop()