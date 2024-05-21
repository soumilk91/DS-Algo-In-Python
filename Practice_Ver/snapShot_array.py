"""
Author: Soumil Ramesh Kulkarni
Date: 05.20.2024

Question:
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id


Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation:
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
"""

class SnapshotArray:

    def __init__(self, length: int):
        self.cur_id = 0
        self.curVals = [0] * length
        self.snapIdArr = [[-1] for _ in range(length)]
        self.arrVal = [[0] for _ in range(length)]
        self.modified = set()

    def set(self, index: int, val: int) -> None:
        if val == self.arrVal[index][-1]:
            if index in self.modified: self.modified.remove(index)
            return
        self.curVals[index] = val
        if index not in self.modified: self.modified.add(index)

    def snap(self) -> int:
        for idx in self.modified:
            self.snapIdArr[idx].append(self.cur_id)
            self.arrVal[idx].append(self.curVals[idx])
        self.modified.clear()
        self.cur_id += 1
        return self.cur_id - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.snapIdArr[index]
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] <= snap_id:
                l = m + 1
            else: r = m
        return self.arrVal[index][l-1]