"""
Question:

Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree.
The formatted layout matrix should be constructed using the following rules:

The height of the tree is height and the number of rows m should be equal to height + 1.
The number of columns n should be equal to 2height+1 - 1.
Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and
its right child at res[r+1][c+2height-r-1].
Continue this process until all the nodes in the tree have been placed.
Any empty cells should contain the empty string "".
Return the constructed matrix res.

Example 1:
Input: root = [1,2]
Output:
[["","1",""],
 ["2","",""]]

Example 2:
Input: root = [1,2,3,null,4]
Output:
[["","","","1","","",""],
 ["","2","","","","3",""],
 ["","","4","","","",""]]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 28 ms, 92.33%. Time: O(N). Space: O(H)
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_depth(node):
            if not node: return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1

        def insert_value(node, lo, hi, depth=0):
            if not node: return
            mid = (lo + hi) // 2
            output[depth][mid] = str(node.val)
            insert_value(node.left, lo, mid, depth + 1)
            insert_value(node.right, mid, hi, depth + 1)

        depth = get_depth(root)
        output = [[""] * (2 ** depth - 1) for _ in range(depth)]

        insert_value(root, 0, 2 ** depth - 1)
        return output
