from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        else:
            val = self.cache.pop(key)
            self.cache[key] = val
            return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache.pop(key)

        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value
