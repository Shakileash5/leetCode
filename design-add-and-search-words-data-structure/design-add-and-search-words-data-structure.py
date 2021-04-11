class TrieNode:
    def __init__(self):
        self.characters = [None]*26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    
    def _charToInt(self,char):
        return ord(char)-ord('a')
    
    def addWord(self, word: str) -> None:
        tempRoot = self.root
        size = len(word)
        
        for i in range(size):
            idx = self._charToInt(word[i])
            if tempRoot.characters[idx] == None:
                tempRoot.characters[idx] = TrieNode()
            tempRoot = tempRoot.characters[idx]
        
        tempRoot.endOfWord = True
        
        return
    
    def backtrack(self,word,idx,node,size):
        if idx>=size:
            if node!=None and node.endOfWord == True:
                return True
            else:
                return False
        
        if word[idx] == ".":
            for i in node.characters:
                if i != None:
                    if self.backtrack(word,idx+1,i,size) == True:
                        return True
        else:
            charIdx = self._charToInt(word[idx])
            if node.characters[charIdx] != None:
                if self.backtrack(word,idx+1,node.characters[charIdx],size) == True:
                    return True
            else:
                return False
                
        
    
    def search(self, word: str) -> bool:
        tempRoot = self.root
        size = len(word)
        tempRootPro = self.root
        res = self.backtrack(word,0,tempRootPro,size)
        #print(res)
        '''
        for i in range(size):
            idx = self._charToInt(word[i])
            print(idx)
            if tempRoot.characters[idx] == None:
                return False
            tempRoot = tempRoot.characters[idx]
        
        if tempRoot!=None and tempRoot.endOfWord == True:
            return True
        '''
        return res
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)