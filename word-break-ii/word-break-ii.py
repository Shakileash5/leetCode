class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        size = len(s)
        res = []
        
        def recur(idx,sentense):
            if idx>=size:
                res.append(" ".join(sentense))
                return 
            #print(idx,sentense)
            for i in range(idx+1,size+1):
                subStr =  s[idx:i]
                if subStr in wordDict:
                    #print(idx,sentense)
                    recur(i,sentense+[subStr]) 
            return
        
        recur(0,[])
        return res