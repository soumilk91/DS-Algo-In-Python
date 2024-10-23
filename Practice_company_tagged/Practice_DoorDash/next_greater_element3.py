"""
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.



Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Convert number to a list of digits
        digits = list(str(n))
        length = len(digits)

        # Step 1: Find the pivot (first decreasing element from the right)
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        # If no pivot is found, the digits are in descending order
        if i == -1:
            return -1

        # Step 2: Find the smallest digit larger than the pivot
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1

        # Step 3: Swap the pivot and the next larger digit
        digits[i], digits[j] = digits[j], digits[i]

        # Step 4: Reverse the digits to the right of the pivot
        digits = digits[:i + 1] + digits[i + 1:][::-1]

        # Convert the digits back to an integer
        result = int(''.join(digits))

        # Step 5: Check if the result fits in 32-bit integer
        return result if result <= 2 ** 31 - 1 else -1
