class Node:
    def __init__(self):
        self.characters = [None]*26
        self.endOfWord = False

class TrieNode:
    def __init__(self):
        self.root = Node()
    
    def charToIdx(self,char):
        return ord(char)-ord('a')
    
    def addWord(self,word):
        tempRoot = self.root
        
        for i in range(len(word)):
            idx = self.charToIdx(word[i])
            if tempRoot.characters[idx] == None:
                tempRoot.characters[idx] = Node()
            
            tempRoot = tempRoot.characters[idx]
            if i  == len(word)-1:
                tempRoot.endOfWord = True
            
        #tempRoot.endOdWord = True
    
    def indToChar(self,ind):
        return chr(ord('a')+ind)
    
    def getSuggestions(self,word):
        suggestions = []
        tempRoot = self.root
        k = [3]
        def recur(idx,root,k,temp):
            if k[0]<=0:
                return
            #print(root)
            if root.endOfWord == True:
                suggestions.append(temp)
                k[0] -= 1
            #print(temp,root.endOfWord)
            for i in range(26):
                if root.characters[i] != None:
                    recur(idx,root.characters[i],k,temp+self.indToChar(i))
            return
            
        
        
        for i in range(len(word)):
            idx = self.charToIdx(word[i])
            if tempRoot.characters[idx] == None:
                return []
            tempRoot = tempRoot.characters[idx]
        #print(tempRoot)
        recur(0,tempRoot,k,word)
        return suggestions
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        TrieObj = TrieNode()
        sizeProducts = len(products)
        sizeWord = len(searchWord)
        res = []
        
        for i in range(sizeProducts):
            TrieObj.addWord(products[i])
        
        for i in range(sizeWord):
            res.append(TrieObj.getSuggestions(searchWord[:i+1]))
        
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        