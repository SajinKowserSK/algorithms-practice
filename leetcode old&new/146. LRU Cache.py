class LRUCache:

    def __init__(self, capacity: int):
        self.map1 = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map1:
            return -1

        else:
            res = self.map1[key]
            self.map1.move_to_end(key)
            return res

    def put(self, key: int, value: int):
        if key not in self.map1:
            self.map1[key] = value

        else:
            self.map1[key] = value
            self.map1.move_to_end(key)

        if len(self.map1) > self.capacity:
            self.map1.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)