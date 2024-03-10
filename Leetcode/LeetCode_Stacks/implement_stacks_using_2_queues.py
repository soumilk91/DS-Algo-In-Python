"""
Author: Soumil Ramesh Kulkarni
Date: 02.09.2024

Question:
mplement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.


Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
"""

from collections import deque


class MyStack:

    def __init__(self):
        self.queue1 = deque([])
        self.queue2 = deque([])

    def push(self, x: int) -> None:
        if not self.queue1 and not self.queue2:
            self.queue1.append(x)
        elif not self.queue1:
            self.queue2.append(x)
        else:
            self.queue1.append(x)

    def pop(self) -> int:
        if not self.queue1 and not self.queue2:
            return None
        elif not self.queue1:
            while len(self.queue2) != 1:
                self.queue1.append(self.queue2.popleft())
            return self.queue2.popleft()
        else:
            while len(self.queue1) != 1:
                self.queue2.append(self.queue1.popleft())
            return self.queue1.popleft()

    def top(self) -> int:
        if not self.queue1 and not self.queue2:
            return None
        elif not self.queue1:
            return self.queue2[len(self.queue2) - 1]
        else:
            return self.queue1[len(self.queue1) - 1]

    def empty(self) -> bool:
        if not self.queue1 and not self.queue2:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()