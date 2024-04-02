"""
Author: Soumil Ramesh Kulkarni
Date: 04.01.2024

Question:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.




Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""


class Solution:
    def letterCombinations_helper(self, digits, index, compare_dict, slate, result):
        # Base Case
        if index == len(digits):
            result.append("".join(slate[:]))
            return

        # Recursive Cases
        if digits[index] not in compare_dict:
            # If Number is Either 1 or 0. Do nothing
            self.letterCombinations_helper(digits, index + 1, compare_dict, slate, result)
        else:
            # Else Loop over all the available chars assigned for the number
            temp_list = compare_dict[digits[index]]
            for runner in temp_list:
                slate.append(runner)
                self.letterCombinations_helper(digits, index + 1, compare_dict, slate, result)
                slate.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        combination_dict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                            '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'],
                            '9': ['w', 'x', 'y', 'z']}

        result = []
        start_index = 0
        self.letterCombinations_helper(digits, start_index, combination_dict, [], result)
        if len(result) == 1 and result[0] == "":
            return []
        return result