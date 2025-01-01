from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        # Initialize the capacity and the OrderedDict
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed key to the end to mark it as recently used
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Move the key to the end as it is being updated
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Pop the first (least recently used) key-value pair
            self.cache.popitem(last=False)
