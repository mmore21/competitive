"""
Problem: 146 - LRU Cache
Difficulty: Medium
URL: https://leetcode.com/problems/lru-cache/
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.eviction = []
        self.cache = {}
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.eviction.remove(key)
            self.eviction.insert(0, key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.eviction.remove(key)
            self.eviction.insert(0, key)
        else:
            if len(self.cache) == self.capacity:
                evicted = self.eviction.pop()
                self.cache.pop(evicted)
                self.cache[key] = value
                self.eviction.insert(0, key)
            else:
                self.cache[key] = value
                self.eviction.insert(0, key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)