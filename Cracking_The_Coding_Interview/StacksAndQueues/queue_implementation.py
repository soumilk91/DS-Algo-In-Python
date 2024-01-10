"""
Author: Soumil Ramesh Kulkarni
Date: 01/09/2024

Question: Basic Implementation of a Queue Data Structure
Basic Operations to be implemented:
-> enqueue
-> dequeue
-> peek
-> is_empty

Just Like stacks, queues can be implemented using lists and linked Lists. For our implementation, we are going to use lists
"""

class QueueBasicFunctions:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if not self.queue:
            return True
        else:
            return False

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            self.queue.pop(0)

    def peek(self):
        if self.queue:
            return self.queue[0]

    def print_queue(self):
        print(self.queue)


# Now Lets Test our Implementation

queueobject = QueueBasicFunctions()
if queueobject.is_empty():
    print("Queue is Empty")
queueobject.enqueue(1)
queueobject.enqueue(5)
print(queueobject.peek())
queueobject.dequeue()
print(queueobject.peek())
queueobject.dequeue()