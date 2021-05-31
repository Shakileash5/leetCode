class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashQueue = {}
        self.size = 0

    def get(self, key: int) -> int:
        keys = list(self.hashQueue.keys())
        #print(keys,key,"get")
        if key in keys:
            val = self.hashQueue[key]
            del self.hashQueue[key]
            self.hashQueue[key] = val
            #print("get",self.hashQueue)
            return val
        else:
            return -1    

    def put(self, key: int, value: int) -> None:
        #print(self.size,self.hashQueue)
        if key not in self.hashQueue.keys():
            if self.size<self.capacity:
                self.hashQueue[key] = value
                self.size+=1
            else:
                keys = list(self.hashQueue.keys())
                del self.hashQueue[keys[0]]
                self.hashQueue[key] = value
        else:
            del self.hashQueue[key]
            self.hashQueue[key] = value
        #print(self.hashQueue)
        return
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)