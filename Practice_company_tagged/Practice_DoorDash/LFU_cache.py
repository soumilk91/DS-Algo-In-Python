"""
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.


"""

from collections import defaultdict, OrderedDict
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_value = {}  # Maps key to (value, freq)
        self.freq_to_keys = defaultdict(OrderedDict)  # Maps freq to an OrderedDict of keys
        self.key_to_freq = {}  # Maps key to its frequency

    def _update_frequency(self, key):
        # Get current frequency of the key
        value, freq = self.key_to_value[key]

        # Remove the key from the current frequency list
        del self.freq_to_keys[freq][key]

        # If the current frequency list is empty and freq is min_freq, increment min_freq
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Update key's frequency
        new_freq = freq + 1
        self.freq_to_keys[new_freq][key] = None  # Add key to new frequency list
        self.key_to_value[key] = (value, new_freq)
        self.key_to_freq[key] = new_freq

    def get(self, key: int) -> int:
        if key not in self.key_to_value:
            return -1

        # Update frequency of the key
        self._update_frequency(key)

        # Return the value
        return self.key_to_value[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_value:
            # If key exists, update its value and frequency
            self.key_to_value[key] = (value, self.key_to_value[key][1])  # Keep the freq unchanged
            self._update_frequency(key)
        else:
            # If the cache is full, remove the LFU key
            if len(self.key_to_value) >= self.capacity:
                # Find the LFU key, which is the first key in freq_to_keys[min_freq]
                lfu_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_value[lfu_key]
                del self.key_to_freq[lfu_key]

            # Insert the new key with frequency 1
            self.key_to_value[key] = (value, 1)
            self.freq_to_keys[1][key] = None
            self.key_to_freq[key] = 1
            self.min_freq = 1  # Reset min_freq to 1 for the new key

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)