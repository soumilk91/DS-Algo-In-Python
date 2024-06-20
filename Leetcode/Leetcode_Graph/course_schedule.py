"""
Question:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course
bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

from typing import *


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create the Graph First
        preMap = {i: [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)

        # Create a visited Set to track Loops
        visited = set()

        # DFS Traverse the Graph and check if the loop is not present
        def dfs(crs):
            # Base Case that the course is present in the visited Set
            if crs in visited:
                return False

            # Another Base Case when a particular course does not have any prereqs
            if not preMap[crs]:
                return True

            # Now DFS Recursive Code
            visited.add(crs)
            # Loop over all the Pre-reqs and check if present in the visited Set
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            # remove the course from the visited set since no loop found in the For loop above
            visited.remove(crs)
            # Set the Pre-reqs for this course to null since this course can be completed ..
            # We do not need to check again
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True