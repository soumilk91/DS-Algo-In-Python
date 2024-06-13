"""
Question:
Design a queue-like data structure that moves the most recently used element to the end of the queue.

Implement the MRUQueue class:

MRUQueue(int n) constructs the MRUQueue with n elements: [1,2,3,...,n].
int fetch(int k) moves the kth element (1-indexed) to the end of the queue and returns it.


Example 1:

Input:
["MRUQueue", "fetch", "fetch", "fetch", "fetch"]
[[8], [3], [5], [2], [8]]
Output:
[null, 3, 6, 2, 2]

Explanation:
MRUQueue mRUQueue = new MRUQueue(8); // Initializes the queue to [1,2,3,4,5,6,7,8].
mRUQueue.fetch(3); // Moves the 3rd element (3) to the end of the queue to become [1,2,4,5,6,7,8,3] and returns it.
mRUQueue.fetch(5); // Moves the 5th element (6) to the end of the queue to become [1,2,4,5,7,8,3,6] and returns it.
mRUQueue.fetch(2); // Moves the 2nd element (2) to the end of the queue to become [1,4,5,7,8,3,6,2] and returns it.
mRUQueue.fetch(8); // The 8th element (2) is already at the end of the queue so just return it.
"""


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class MRUQueue:

    def __init__(self, n: int):
        self.head = ListNode(0, None)
        curr = self.head
        for i in range(1, n + 1):
            curr.next = ListNode(i, None)
            curr = curr.next
        self.tail = curr

    def fetch(self, k: int) -> int:
        curr = self.head
        while k > 1:
            curr = curr.next
            k -= 1

        mru = curr.next
        if curr.next.next:
            curr.next = curr.next.next
            self.tail.next = mru
            self.tail = self.tail.next
            mru.next = None
        return mru.val

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)