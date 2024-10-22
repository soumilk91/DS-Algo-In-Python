"""
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be
idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to
be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.



Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval,
neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.
"""

from collections import Counter
from typing import *
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks)

        # Find the maximum frequency
        max_freq = max(task_counts.values())

        # Count how many tasks have the maximum frequency
        max_count = sum(1 for count in task_counts.values() if count == max_freq)

        # Calculate the minimum intervals required
        part_count = max_freq - 1
        part_length = n + 1
        empty_slots = part_count * part_length
        available_slots = empty_slots + max_count

        # The result is either the total number of slots needed or just the length of the tasks
        return max(len(tasks), available_slots)
