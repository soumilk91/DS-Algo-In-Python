"""
Author: Soumil Ramesh Kulkanri
Date: 02.24.2024

Question:
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.


Example 1:

Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
"""


import heapq

# Use minHeap
class SmallestInfiniteSet:

    def __init__(self):
        self.min_val = 1
        self.is_val_in_heap = {}
        # self.is_val_in_heap = set()
        self.heap = []

    def popSmallest(self) -> int:
        if not self.heap:
            smallest = self.min_val
            self.min_val += 1
        else:
            smallest = heapq.heappop(self.heap)
            del self.is_val_in_heap[smallest]
            # self.is_val_in_heap.remove(smallest)

        return smallest

    def addBack(self, num: int) -> None:
        if num >= self.min_val or num in self.is_val_in_heap:
            return
        elif num == self.min_val - 1:
            self.min_val -= 1
        else:
            heapq.heappush(self.heap, num)
            self.is_val_in_heap[num] = True
            # self.is_val_in_heap.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)