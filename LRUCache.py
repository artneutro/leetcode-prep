class LRUCache:

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.priority = []

    def get(self, key: int) -> int:
        if key in self.cache :
            self.priority.remove(key)
            self.priority.append(key)
            return self.cache[key]
        else :
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        if key in self.priority :
            self.priority.remove(key)
            self.priority.append(key)
        else :
            self.priority.append(key)
        if len(self.cache) > self.capacity :
            key = self.priority.pop(0)
            del self.cache[key]

