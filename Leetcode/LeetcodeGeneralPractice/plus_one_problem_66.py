"""
Author: Soumil Ramesh Kulkarni
Date: 01/20/2024

Question:
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        given_number = 0
        temp = len(digits) - 1
        for i in digits:
            given_number += i * (10 ** temp)
            temp -= 1
        # print(given_number)
        new_number = given_number + 1
        return_list = []
        while new_number > 0:
            return_list.append(new_number % 10)
            new_number = new_number // 10
        return return_list[::-1]



