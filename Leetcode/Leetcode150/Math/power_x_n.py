"""
Author: Soumil Ramesh Kulkarni
Date: 03.16.2024

Question:
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

"""

class Solution:
    def myPow_helper(self, base, exponent):
        if exponent == 0:
            return 1
        elif exponent %2 == 0:
            return self.myPow_helper(base * base, exponent //2)
        else:
            return base * self.myPow_helper(base * base, (exponent - 1) // 2)

    def myPow(self, x: float, n: int) -> float:
        temp = self.myPow_helper(x, abs(n))
        if n > 0:
            return float(temp)
        else:
            return 1/temp