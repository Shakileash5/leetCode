class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        size1 = len(word1)
        size2 = len(word2)
        hashMap1 = {}
        hashMap2 = {}
        notCommon = []
        count = [0]*26
        
        """for i in range(size1):
            if word1[i] not in hashMap1:
                hashMap1[word1[i]] = [i]
            else:
                hashMap1[word1[i]].append(i)
            count[ord(word1[i])-ord('a')] += 1
            
        for i in range(size2):
            if word2[i] not in hashMap2:
                hashMap2[word2[i]] = [i]
            else:
                hashMap2[word2[i]].append(i)
            count[ord(word2[i])-ord('a')] -= 1"""
        
        @cache
        def lcs(idx1,idx2):
            if idx1>=size1 or idx2 >= size2:
                return 0 
            max_ = 0
            res = 0
            if word1[idx1] == word2[idx2]:
                max_ = lcs(idx1+1,idx2+1) + 1
            else:
                res = max(lcs(idx1+1,idx2) , lcs(idx1,idx2+1)) 
            
            return max(res,max_)
            
        common = lcs(0,0)
        #print(common)
        res = (size1 - common) + (size2 - common)
        return res