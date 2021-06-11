class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        sizeStr = len(s)
        sizeWords = len(words)
        count = 0
        hashMap = {}
        
        def isSubSequence(word):
            idxWord = 0
            count = 0
            idx = 0
            size = len(word)
            while(idx<sizeStr and idxWord<size):
                if s[idx] == word[idxWord]:
                    idxWord += 1
                idx += 1
            
            return idxWord == size
        
        for i in range(sizeWords):
            if words[i] not in hashMap:
                res = isSubSequence(words[i])
                hashMap[words[i]] = res
            else:
                res = hashMap[words[i]]
            if res:
                count += 1
                   
        return count