class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashQueue = {}

    def get(self, key: int) -> int:
        #print(self.hashQueue,"get",key)
        keys = list(self.hashQueue.keys())
        if key in keys:
            value = self.hashQueue[key]
            del self.hashQueue[key]
            self.hashQueue[key] = value
            return value
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        keys = list(self.hashQueue.keys())
        #print(self.hashQueue,key not in keys,key,"put")
        if key not in keys:
            if len(self.hashQueue)<self.capacity:
                self.hashQueue[key] = value
            else:
                del self.hashQueue[keys[0]]
                self.hashQueue[key] = value
        else:
            del self.hashQueue[key]
            self.hashQueue[key] = value
            
        #print(self.hashQueue,"after")
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)