"""
Author: Soumil Ramesh Kulkarni
Date: 02.24.2024

Question:
Skip List is a probabilistic data structure that allows O (log(n)) search complexity as well as O (log(n)) insertion complexity within an ordered sequence of n elements.

Implement it using only linked lists.

Skip list has three operations:

insert(value) inserts a value in a skip list, does not return anything.
is_present(value) returns true if given value is present in the skip list and false otherwise.
remove(value) removes a value from a skip list, does not return anything.
Execute the given sequence of operations and return values returned by is_present operations.

Each operation will be given as two numbers:

[0, value] means insert(value),
[1, value] means is_present(value), and
[2, value] means remove(value).
Example
{
"operations": [
[0, 5],
[0, 10],
[0, 1],
[1, 0],
[2, 0],
[1, 1],
[2, 1],
[2, 10],
[0, 10],
[1, 10]
]
}
Output:

[0, 1, 1]
First 3 operations are to insert 5, 10 and 1 in the skip list. So the skip list contains values [1, 5, 10].

4th operation is to search for 0. As 0 is not present in the skip list, the return value will be false.

5th operation is to remove value 0. Now skip list contains [1, 5, 10].

6th operation is to search for 1. As 1 is present in the skip list, the return value will be true.

7th operation is to remove value 1. Now skip list contains [5, 10].

8th operation is to remove value 10. Now skip list contains [5].

9th operation is to insert value 10. Now skip list contains [5, 10].

10th operation is to search for 10. As 10 is present in the skip list, the return value will be true.
"""

import random

class ListNode:
    __slots__ = ('val', 'next', 'down')

    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None


class Skiplist:
    def __init__(self):
        # sentinel nodes to keep code simple
        node = ListNode(float('-inf'))
        node.next = ListNode(float('inf'))
        self.levels = [node]

    def search(self, target: int) -> bool:
        level = self.levels[-1]
        while level:
            node = level
            while node.next.val < target:
                node = node.next
            if node.next.val == target:
                return True
            level = node.down
        return False

    def add(self, num: int) -> None:
        stack = []
        level = self.levels[-1]
        while level:
            node = level
            while node.next.val < num:
                node = node.next
            stack.append(node)
            level = node.down

        heads = True
        down = None
        while stack and heads:
            prev = stack.pop()
            node = ListNode(num)
            node.next = prev.next
            node.down = down
            prev.next = node
            down = node
            # flip a coin to stop or continue with the next level
            heads = random.randint(0, 1)

        # add a new level if we got to the top with heads
        if not stack and heads:
            node = ListNode(float('-inf'))
            node.next = ListNode(num)
            node.down = self.levels[-1]
            node.next.next = ListNode(float('inf'))
            node.next.down = down
            self.levels.append(node)

    def erase(self, num: int) -> bool:
        stack = []
        level = self.levels[-1]
        while level:
            node = level
            while node.next.val < num:
                node = node.next
            if node.next.val == num:
                stack.append(node)
            level = node.down

        if not stack:
            return False

        for node in stack:
            node.next = node.next.next

        # remove the top level if it's empty
        while len(self.levels) > 1 and self.levels[-1].next.next is None:
            self.levels.pop()

        return True

def implement_skip_list(operations):
    """
    Args:
     operations(list_list_int32)
    Returns:
     list_bool
    """
    # Write your code here.
    result = []
    object = Skiplist()
    for operation in operations:
        if operation[0] == 0:
            object.add(operation[1])
        if operation[0] == 1:
            result.append(object.search(operation[1]))
        if operation[0] == 2:
            object.erase(operation[1])
    return result