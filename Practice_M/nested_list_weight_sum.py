"""
Author: Soumil Ramesh Kulkarni
Date: 03.06.2024

Question:
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.



Example 1:


Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
Example 2:


Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.
Example 3:

Input: nestedList = [0]
Output: 0
"""

class Solution:
    def depthSum_helper(self, temp_list, depth):
        total = 0
        for nested in temp_list:
            if nested.getInteger():
                total += nested.getInteger() * depth
            else:
                total += self.depthSum_helper(nested.getList(), depth + 1)
        return total

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return self.depthSum_helper(nestedList, 1)