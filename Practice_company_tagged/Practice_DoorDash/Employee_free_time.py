"""
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.



Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
"""


# Definition for an Interval.
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'[{self.start}, {self.end}]'

class Solution:
    def employeeFreeTime(self, schedule):
        # Step 1: Flatten all intervals into one list
        intervals = []
        for employee in schedule:
            for interval in employee:
                intervals.append(interval)

        # Step 2: Sort intervals by start time, and by end time if start times are equal
        intervals.sort(key=lambda x: (x.start, x.end))

        # Step 3: Merge intervals and find gaps between them
        merged_intervals = []
        prev_interval = intervals[0]

        for current_interval in intervals[1:]:
            if prev_interval.end < current_interval.start:
                # There's a gap (free time) between the previous and current intervals
                merged_intervals.append(Interval(prev_interval.end, current_interval.start))
                prev_interval = current_interval
            else:
                # Merge overlapping intervals
                prev_interval.end = max(prev_interval.end, current_interval.end)

        # Return the list of merged intervals (free time)
        return merged_intervals

