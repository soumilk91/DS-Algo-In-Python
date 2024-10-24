"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along
the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent
nodes to child nodes).


Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0

            # Update current path sum
            current_sum += node.val

            # Number of paths with sum equal to targetSum ending at this node
            num_paths = prefix_sums.get(current_sum - sum, 0)

            # Update prefix_sums with current path sum
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

            # Recurse on left and right children
            num_paths += dfs(node.left, current_sum)
            num_paths += dfs(node.right, current_sum)

            # Backtrack: remove current path sum from prefix_sums
            prefix_sums[current_sum] -= 1

            return num_paths

        # Dictionary to store prefix sums and their frequencies
        prefix_sums = {0: 1}

        return dfs(root, 0)