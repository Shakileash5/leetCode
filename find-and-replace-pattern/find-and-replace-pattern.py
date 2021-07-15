class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        sizePattern = len(pattern)
        res = []
        
        def isMatch(word):
            size = len(word)
            hashMap = {}
            visited = set()
            for i in range(sizePattern):
                if pattern[i] not in hashMap:
                    if word[i] in visited:
                        return False
                    hashMap[pattern[i]] = word[i]
                    visited.add(word[i])
                else:
                    if hashMap[pattern[i]] != word[i]:
                        return False
            
            return True
        
        #print(isMatch('mea'))
        for word in words:
            if isMatch(word):
                res.append(word)
        
        return res