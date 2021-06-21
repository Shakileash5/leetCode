class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        size = len(words)
        hashMap = {}
        
        for word in words:
            for j in range(len(word)):
                if word[j] not in hashMap:
                    hashMap[word[j]] = 1
                else:
                    hashMap[word[j]] += 1
        
        keys = list(hashMap.keys())
        sizeKey = len(keys)
        
        for i in range(sizeKey):
            if hashMap[keys[i]]%size != 0 :
                    return False
        
        return True