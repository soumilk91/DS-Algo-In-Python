"""
Author: Soumil Ramesh Kulkarni
Date: 01/09/2024

Question: Design a stack which in addition to push and pop have a function min, which return the minimum value present in the stack.
          All 3 operations should have a run time complexity of O(1)

Approach:
-> We will use 2 stacks in our design
-> One Normal stack and the other stack to maintain the minimum element seen in the stack.
-> Any time we push, if the element is less or equal to the top of the min stack, we push in both stacks else we only push in the original stack
-> Any time we pop, if the top of both the stacks is the same, we pop both else we pop only the original stack
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def top(self, min_stack=False):
        if min_stack:
            if self.min_stack:
                return self.min_stack[-1]
        else:
            if self.stack:
                return self.stack[-1]

    def push(self, data):
        if not self.stack:
            self.stack.append(data)
            self.min_stack.append(data)
        elif data <= self.top(min_stack=True):
            self.stack.append(data)
            self.min_stack.append(data)
        else:
            self.stack.append(data)

    def pop(self):
        if self.stack:
            if self.top() == self.top(min_stack=True):
                self.stack.pop()
                self.min_stack.pop()
            else:
                self.stack.pop()

    def get_min(self):
        if self.stack:
            return self.top(min_stack=True)
        else:
            print("Stack is Empty")
            return 0

# Let's test Our Code

stackObject = MinStack()
stackObject.push(5)
stackObject.push(6)
stackObject.push(7)
stackObject.push(4)
stackObject.push(4)
stackObject.push(2)
print(stackObject.get_min())
stackObject.pop()
stackObject.pop()
print(stackObject.get_min())
stackObject.pop()
stackObject.get_min()
print(stackObject.top())
print(stackObject.get_min())

