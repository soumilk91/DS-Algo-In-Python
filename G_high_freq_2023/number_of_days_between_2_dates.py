"""
Author: Soumil Ramesh Kulkarni
Date: 03.25.2024

Question:
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.



Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15

"""

from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1, d2 = date.fromisoformat(date1), date.fromisoformat(date2)
        return abs((d1 - d2).days)
