"""
Author: Soumil Ramesh Kulkarni
Date: 02.25.2024

Question:
Given the root of a binary tree, return the vertical order traversal of its nodes' values.
(i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Use Level Order Traversal with a slight modification
        comp_dict = {}
        if not root:
            return []
        queue = [{"node": root, "place": 0}]
        while queue:
            temp = queue.pop(0)
            place = temp["place"]
            node = temp["node"]
            if place in comp_dict:
                comp_dict[place].append(node)
            else:
                comp_dict[place] = [node]
            if node.left:
                queue.append({"node": node.left, "place": place-1})
            if node.right:
                queue.append({"node": node.right, "place": place+1})
        a_list = sorted(comp_dict.keys())
        ret_list = []
        for i in a_list:
            temp = []
            for j in comp_dict[i]:
                temp.append(j.val)
            ret_list.append(temp)
        return ret_list