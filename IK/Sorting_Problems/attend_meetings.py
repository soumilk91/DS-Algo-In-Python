"""
Author: Soumil Ramesh Kulkarni
Date: 02.14.2024

Question:
Given a list of meeting intervals where each interval consists of a start and an end time,
check if a person can attend all the given meetings such that only one meeting can be attended at a time.

Eg:
{
"intervals": [
[1, 5],
[5, 8],
[10, 15]
]
}
Output: 1
As the above intervals are non-overlapping intervals, it means a person can attend all these meetings.

{
"intervals": [
[1, 5],
[4, 8]
]
}
Output: 0
Time 4 - 5 is overlapping in the first and second intervals.
"""


def can_attend_all_meetings(intervals):
    # Sorting in ascending order of start time of an interval.
    # If start time is same for two intervals then sort in ascending order of end time of intervals.
    intervals.sort()
    for i in range(len(intervals) - 1):
        end_time_current_interval = intervals[i][1]
        start_time_next_interval = intervals[i + 1][0]
        # If overlap found, return 0.
        if end_time_current_interval > start_time_next_interval:
            return 0
    return 1