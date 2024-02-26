"""
Author: Soumil Ramesh Kulkarni
Date: 02.24.2024

Question:
Given a sequence of enqueue and dequeue operations, return a result of their execution without using a queue implementation from a library. Use two stacks to implement queue.

Operations are given in the form of a linked list, and you need to return the result as a linked list, too. Operations:

A non-negative integer means "enqueue me".
-1 means
If the queue is not empty, dequeue current head and append it to the result.
If the queue is empty, append -1 to the result.
Example One
{
"operations": [1, -1, 2, -1, -1, 3, -1]
}
Output:

[1, 2, -1, 3]
Here is how we would execute the operations and build the result list:

Operation	Queue contents after the operation	Result list after the operation
1	[1]	[]
-1	[]	[1]
2	[2]	[1]
-1	[]	[1, 2]
-1	[]	[1, 2, -1]
3	[3]	[1, 2, -1]
-1	[]	[1, 2, -1, 3]
Example Two
{
"operations": [0, 1, 2, -1, 3]
}
Output:

[0]
The only dequeue operation results in the first enqueued element, 0, to be appended to the result list.
"""


#For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if len(self.stack) == 0 and len(self.helper):
            self.stack.append(x)
        else:
            if len(self.stack) > 0:
                self.helper.append(x)
                while len(self.stack) > 0:
                    self.helper.append(self.stack.pop())
            else:
                self.stack.append(x)
                while len(self.helper) > 0:
                    self.stack.append(self.helper.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack:
            return self.stack.pop()
        elif self.helper:
            return self.helper.pop()
        else:
            return -1

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        temp = self.stack.pop()
        self.stack.append(temp)
        return temp

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack) == 0:
            return True
        return False


def implement_queue(operations):
    """
    Args:
     operations(LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    temp = LinkedListNode(0)
    runner = temp
    object = MyQueue()
    while operations:
        if operations.value < 0:
            runner.next = LinkedListNode(object.pop())
            runner = runner.next
        else:
            object.push(operations.value)
        operations = operations.next
    return temp.next