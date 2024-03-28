"""
Author: Soumil Ramesh Kulkarni
Date: 03.26.2024

Question:
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537

"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        # Initialize The table
        table = [0,0,1]
        for i in range(2, n+1):
            trib_number = table[i] + table[i-1] + table[i-2]
            table.append(trib_number)
        print(table)
        return table[-1]