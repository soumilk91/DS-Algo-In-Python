"""
Author: Soumil Ramesh Kulkarni
Date: 04.01.2024

Question:
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def combine_helper(remain, comb, nex):
            if remain == 0:
                result.append(comb[:])

            else:
                for i in range(nex, n + 1):
                    comb.append(i)

                    combine_helper(remain - 1, comb, i + 1)

                    comb.pop()

        combine_helper(k, [], 1)
        return result
