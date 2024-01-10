"""
Author: Soumil Ramesh Kulkarni
Date: 01/09/2024

Question: Basic Implementation of Stack Data Structure
Basic Operations to be implemented:
-> push
-> pop
-> isempty
-> peek

Stacks can be implemented using lists or linked Lists. We are going to use lists for our implementation
"""

class StackBasicFunctions:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if not self.stack:
            return True
        else:
            return False

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def print_stack(self):
        print(self.stack)

# Now Lets Test Our Implementation

stackObject = StackBasicFunctions()
if stackObject.is_empty():
    print("Stack is Empty")
stackObject.push(1)
stackObject.push(2)
if not stackObject.is_empty():
    print("Stack is Not Empty")
print(stackObject.peek())
stackObject.pop()
print(stackObject.peek())
stackObject.print_stack()




