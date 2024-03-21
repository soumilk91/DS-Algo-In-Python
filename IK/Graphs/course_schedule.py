"""
Author: Soumil Ramesh Kulkarni
Date: 03.04.2024

Question:
here are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first
if you want to take course ai.

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


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a graph
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        # Fill up the prereqs as adjlist in the above graph
        for prereq in prerequisites:
            subject = prereq.pop(0)
            for pre in prereq:
                graph[subject].append(pre)
        print(graph)

        # Now DFS on the created graph to check if there is a loop,
        # if yes, then we cannot finish all the courses
        visited = [False] * numCourses
        instack = [False] * numCourses

        for i in range(numCourses):
            if self.dfs(i, graph, visited, instack):
                return False
        return True

    def dfs(self, node, graph, visited, instack):
        # if the node is already in the stack, we have a cycle
        if instack[node]:
            return True
        if visited[node]:
            return False
        # Mark current node as visited and part of the current recursion stack
        visited[node] = True
        instack[node] = True
        for neighbor in graph[node]:
            if self.dfs(neighbor, graph, visited, instack):
                return True
        # Remove Node from the Stack
        instack[node] = False
        return False
