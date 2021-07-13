class Node:
    def __init__(self):
        self.characterNodes = [None]*26
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.node = Node()
    
    def charToIdx(self,char):
        return ord(char) - ord('a')
    
    def insertKey(self,key):
        size = len(key)
        rootNode = self.node
        for i in range(size):
            idx = self.charToIdx(key[i])
            if rootNode.characterNodes[idx] == None:
                rootNode.characterNodes[idx] = Node()
            rootNode = rootNode.characterNodes[idx]
        rootNode.endOfWord = True
        return
    
    def searchRemain(self,root,res,key):
        if root.endOfWord:
            res.append(key)
            #print(res)
            
        for i in range(26):
            if root.characterNodes[i] != None:
                self.searchRemain(root.characterNodes[i],res,key+chr(i+ord('a')))
        return
        
    
    def searchKey(self,key):
        res = []
        i = 0
        rootNode = self.node
        while(i<len(key)):
            idx = self.charToIdx(key[i])
            if rootNode.characterNodes[idx] == None:
                return res
            rootNode = rootNode.characterNodes[idx]
            i += 1
        self.searchRemain(rootNode,res,key)
        return res
            
        

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.keys = set()
        self.trieKeys = Trie()

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val
        self.keys.add(key)
        self.trieKeys.insertKey(key)
        
    def sum(self, prefix: str) -> int:
        sum_ = 0
        res = self.trieKeys.searchKey(prefix)
        for key in res:
            sum_ += self.map[key]
        
        #for key in self.keys:
        #    if prefix in key[:len(prefix)]:
        #        sum_ += self.map[key] 
        return sum_

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)