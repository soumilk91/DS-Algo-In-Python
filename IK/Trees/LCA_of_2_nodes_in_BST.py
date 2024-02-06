# Date: 02/05/2024
# Find the LCA of two given nodes from the binary Tree
"""
Approach:

Follow the steps to implement the above approach:

-> Create a hash table or a map to store the parent pointers of each node in the binary tree.
-> Traverse the binary tree and populate the hash table or the map with the parent pointers for each node.
-> Starting from the first node, traverse up the tree and add each ancestor to a set or a list.
-> Starting from the second node, traverse up the tree and check if each ancestor is already in the set or the list.
    The first ancestor that is already in the set or the list is the lowest common ancestor.
-> If no common ancestor is found, return null or any other value that indicates the absence of a common ancestor.
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def build_parent_map(root):
    parent_dict = {}
    parent_dict[root] = None
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            parent_dict[node.left] = node
            queue.append(node.left)
        if node.right:
            parent_dict[node.right] = node
            queue.append(node.right)
    return parent_dict


def lca(root, a, b):
    """
    Args:
     root(BinaryTreeNode_int32)
     a(BinaryTreeNode_int32)
     b(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.

    # Prepare the parent dict
    parent_dict = build_parent_map(root)

    # Treverse Level Order again to locate the given 2 nodes
    p, q = None, None
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node == a:
            p = node
        if node == b:
            q = node
        if p is not None and q is not None:
            break
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    # Create a dict of all parents (ancistors) of p
    ancistors = {}
    while p:
        ancistors[p] = 1
        p = parent_dict[p]

    # Now while finding all the parents of q, the first node present in the parents of p is the LCA
    while q:
        if q in ancistors:
            return q.value
        q = parent_dict[q]
    return -1