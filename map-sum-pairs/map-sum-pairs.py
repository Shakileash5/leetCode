class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.keys = set()

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val
        self.keys.add(key)
        
    def sum(self, prefix: str) -> int:
        sum_ = 0
        for key in self.keys:
            if prefix in key[:len(prefix)]:
                sum_ += self.map[key] 
        return sum_

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)