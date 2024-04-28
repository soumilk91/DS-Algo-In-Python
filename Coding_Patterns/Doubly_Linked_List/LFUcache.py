"""
Author: Soumil Ramesh Kulkarni
Date: 04.10.2024

Question:
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present.
When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting
a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency),
the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache.
The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation).
The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
"""


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity  # stores the capacity
        self.di = {}  # stores keys with their frequencies
        self.lfu = defaultdict(OrderedDict)  # stores frequencies and all keys that have a given frequency
        self.least = 0  # stores the minimum frequence which exists in the cache. We need this for eviction

    def update(self, key, value=None):  # help function which update the frequency of a key
        poz = self.di[key] + 1  # if a key frequency was N then after we visit it, the frequency changes to N + 1
        v = self.lfu[poz - 1].pop(
            key)  # if we update the position of a key in the cache then we should maintain its last value
        if value is not None:  # we call the update function in 2 cases: 1. From get function. In this case we maintain its last value; 2. From put function. In this case we should change the key's value with a new one
            v = value  # 2nd case
        self.lfu[poz][key], self.di[key] = v, poz  # update the key in both dictionaries
        if not self.lfu[
            poz - 1] and self.least == poz - 1:  # if there a no more keys with the Nth frequence, and the Nth frequence was the minimal frequence then we need to increment the minimum frequence
            self.least += 1
        return self.lfu[poz][key]  # this line is used only when the updated function was called from the get function

    def get(self, key: int) -> int:
        return self.update(
            key) if key in self.di else -1  # if we find a key, then we should update its position and return its value, otherwise we return -1

    def put(self, key: int, value: int) -> None:
        if not self.capacity: return  # we need this line for the case when the capacity is 0 as we can't put anything
        if key in self.di:
            self.update(key, value)  # if the key is already in our cache then we only update its value with a new one
        else:  # the key isn't in our cache. Its frequence becomes 1
            if len(self.di) == self.capacity:  # the cache reached its capacity
                del self.di[self.lfu[self.least].popitem(last=False)[
                    0]]  # firstly, we remove the key with the minimum frequence, and then we delete the key from the cache
            self.lfu[1][key] = value  # last 3 lines put the key in the cache
            self.di[key] = 1
            self.least = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)