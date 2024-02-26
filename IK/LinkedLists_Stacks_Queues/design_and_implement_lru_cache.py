"""
Author: Soumil Ramesh Kulkarni
Date: 02.25.2024

Question:

mplement a Least Recently Used (LRU) cache and execute a given sequence of SET(key, value) and GET(key) operations.
Return the results of all the GET operations from the sequence.

Initially the cache is empty. Cache capacity is a part of the input. Keys and values are all positive. GET(key)
returns either the cached value or -1 (cache miss). SET(key, value) adds or updates the value for the key.
If cache is at capacity and a new value needs to be added, remove the least recently used (LRU) value first.

Example
{
"capacity": 2,
"query_type": [1, 1, 0, 1, 0, 1, 0],
"key": [5, 10, 5, 15, 10, 5, 5],
"value": [11, 22, 1, 33, 1, 55, 1]
}
Output:

[11, -1, 55]
query_type of 0 means GET and query_type of 1 means SET.

Here are the operations from the input along with the return values and side effects of their execution:

Operation	Cache after	Returned value	Side effect
SET(5, 11)	[5 -> 11]		5 -> 11 added to cache
SET(10, 22)	[10 -> 22, 5 -> 11]		5 -> 11 became LRU
GET(5)	[5 -> 11, 10 -> 22]	11	10 -> 22 became LRU
SET(15, 33)	[15 -> 33, 5 -> 11]		10 -> 22 got evicted
GET(10)	[15 -> 33, 5 -> 11]	-1	Access order unchanged
SET(5, 55)	[5 -> 55, 15 -> 33]		Key 5 updated, became the
most recently used (MRU)
GET(5)	[5 -> 55, 15 -> 33]	55	No change; key 5 already
was the MRU
Notes
The function accepts four arguments:

The cache capacity,
query_type array with 0 for GET and 1 for SET operation,
key array with the keys for all the operations,
value array with the values for SET operations (value to be ignored for GETs).
The three input arrays all have the same length n and together they represent n operations.
Constraints:

1 <= capacity <= 105
1 <= n <= 105
1 <= any key <= 105
1 <= any value <= 105
"""


class LruCache:
    def __init__(self, capacity):
        self.lru = {}
        self.capacity = capacity
        self.dict = {}
        self.term = 0

    def get(self, key):
        if key in self.lru:
            self.dict[key] = self.term
            self.term += 1
            return self.lru[key]
        else:
            return -1

    def set(self, key, value):
        if (key in self.lru or len(self.lru) < self.capacity):
            self.lru[key] = value
            self.dict[key] = self.term
            self.term += 1
        else:
            max_val = float('inf')
            for k, v in self.dict.items():
                if v < max_val:
                    max_val = v
                    key_to_pop = k
            self.lru.pop(key_to_pop)
            self.dict.pop(key_to_pop)
            self.lru[key] = value
            self.dict[key] = self.term
            self.term += 1


def implement_lru_cache(capacity, query_type, key, value):
    """
    Args:
     capacity(int32)
     query_type(list_int32)
     key(list_int32)
     value(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    result = []
    object = LruCache(capacity)
    for i in range(len(query_type)):
        if query_type[i] == 0:
            result.append(object.get(key[i]))
        else:
            object.set(key[i], value[i])
    return result
