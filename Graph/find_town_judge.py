"""
Author: Soumil Ramesh Kulkarni
Date: 08.13.2024

Question:
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.



Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
"""

from typing import *
from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Create the Graph
        graph = defaultdict(set)
        for relation in trust:
            graph[relation[0]].add(relation[1])
        # print(graph)
        # Find the Person not Present in the Relations Graph
        person_not_present = None
        for i in range(1, n + 1):
            if i not in graph:
                if person_not_present != None:
                    # There can only be one Person Who does not Trust Anyone
                    return -1
                person_not_present = i
        # Check Relations for each Person, Each Person should Trust our 'person_not_present'
        for person, relations in graph.items():
            if person_not_present not in relations:
                return -1
        return person_not_present
