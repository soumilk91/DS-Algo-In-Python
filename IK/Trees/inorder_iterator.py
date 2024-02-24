"""
Author: Soumil Ramesh Kulkarni
Date: 02.24.2024

Question:
Design and implement an iterator for the in-order traversal of a binary tree.

Given the root node of a tree of positive numbers, and a sequence of operations on the iterator, calculate return values of all those operations.

Iterator has two operations:

has_next() should return 1 if one or more elements remain in the in-order traversal of the tree, otherwise it should return 0.
next() should return the next value in the in-order traversal of the tree if it exists, otherwise a special value of 0.
Execute operations one by one and return all their return values in a list.

Both operations must take constant time on average and use O(height of the tree) of extra memory.

Example

"operations": ["next", "has_next", "next", "next", "has_next", "has_next", "next"]
Output:

[100, 1, 200, 300, 0, 0, 0]
In-order traversal for the given tree is [100, 200, 300].

1st operation next() returns the first element, 100.

2nd operation has_next() returns 1 because traversal isn't over and there are more elements.

3rd operation, next() returns the second element, 200.

4th operation, next() returns the last element, 300.

5th operation has_next() returns 0; the in-order traversal is over.

6th operation has_next() returns 0; it's still over.

7th operation next() return 0, since there is no next element.
"""


#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


from collections import deque


class TreeIterator:
    def __init__(self):
        self.inorder_traversal = deque([])

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        self.inorder_traversal.append(root.value)
        self.traverse(root.right)

    def has_next(self):
        if not self.inorder_traversal:
            return 0
        else:
            return 1

    def next(self):
        if not self.inorder_traversal:
            return 0
        else:
            return self.inorder_traversal.popleft()


def implement_tree_iterator(root, operations):
    """
    Args:
     root(BinaryTreeNode_int32)
     operations(list_str)
    Returns:
     list_int32
    """
    # Write your code here.
    result = []
    iter = TreeIterator()
    # Treverse inorder on the entire Tree
    iter.traverse(root)

    # Loop over all the Operations
    for operation in operations:
        if operation == "next":
            result.append(iter.next())
        else:
            result.append(iter.has_next())
    return result


