class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashQueue = {}

    def get(self, key: int) -> int:
        keys = list(self.hashQueue.keys())
        if self.capacity>0:
            if key in keys:
                value = self.hashQueue[key]
                del self.hashQueue[key]
                self.hashQueue[key] = value
                self.hashQueue[key][1] += 1
                #print(self.hashQueue,"get")
                return value[0]
            else:
                return -1
        else:
            return -1
            

    def put(self, key: int, value: int) -> None:
        keys = list(self.hashQueue.keys())
        #print(self.hashQueue,key,"put")
        if self.capacity>0:
            if key not in keys:
                if len(self.hashQueue)<self.capacity:
                    self.hashQueue[key] = [value,1]
                else:
                    small = [-1,float("inf")]
                    #print("keysHere",keys)
                    for i in keys:
                        if self.hashQueue[i][1]<small[1]:
                            small = [i,self.hashQueue[i][1]]
                    del self.hashQueue[small[0]]
                    self.hashQueue[key] = [value,1]
            else:
                self.hashQueue[key][1] += 1
                self.hashQueue[key][0] = value
            
        #print(self.hashQueue,"after")
        return


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)