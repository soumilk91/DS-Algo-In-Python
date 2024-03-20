"""
Author: Soumil Ramesh Kulkarni
Date: 03.19.2024

Question:
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

Example 1:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Example 2:
Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        queue = [(root, False)]
        delete_set = set(to_delete)
        result = []
        while queue:
            node, hasParent = queue.pop(0)
            # New root Found
            if not hasParent and node.val not in to_delete:
                result.append(node)

            hasParent = not node.val in to_delete

            if node.left:
                queue.append((node.left, hasParent))
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                queue.append((node.right, hasParent))
                if node.right.val in to_delete:
                    node.right = None
        return result