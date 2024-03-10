"""
Author: Soumil Ramesh Kulkarni
Date: 03.09.2024

Question:
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

class Solution:
    def dailyTemperatures_using_stacks(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temperature in enumerate(temperatures):
            # Pop until the current day's temp is not
            # warmer than temperature at the top of stack

            while stack and temperatures[stack[-1]] < temperature:
                prev_day = stack.pop()
                result[prev_day] = index - prev_day
            stack.append(index)
        return result


# Brute Force using 2 loops
class Solution_bruteForce:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        return result
