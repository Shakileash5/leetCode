class Solution:
    def wordBreakTwo(self,s,words):
        size = len(s)
        flag = [False]
        def recur(idx,temp):
            if idx>=size:
                #print(temp)
                flag[0]=True
                return 
            for i in range(idx,size):
                subStr = s[idx:i+1]
                if subStr in words:
                    recur(i+1,temp+[subStr])
            return
        
        #recur(0,[])   
        def bottomUp(idx):
            if idx>=size:
                return True
            if dp[idx] == None:
            
                for i in range(idx,size):
                    subStr = s[idx:i+1]
                    if subStr in words:
                        res = bottomUp(i+1)
                        if res:
                            dp[idx] = True
                            return True
                dp[idx] = False
                return dp[idx]
                        
            else:
                return dp[idx]
        
        dp = [None]*(size+1)
        return bottomUp(0)
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        @cache
        def recur(idx,words):
            if idx>=size:
                sums = len(words)
                #for i in words:
                #    sums+=len(i)
                if sums == size:
                    flag = True
                    return True
                #print(words,"whats")
                return False
            
            for i in range(idx,size):
                string = s[idx:i+1]
                
                if string in wordDict:
                    #print(string,idx,i,words)
                    if i+1>=size:
                        
                        temp = words
                        words+=string
                        sums = len(words)
                        #print(words,"whats")
                        #for k in words:
                         #   sums+=len(k)
                        if sums == size:
                            flag = True
                            return True
                        words = temp
                        
                    #return False
                    if recur(i+1,words+string) == True:
                        return True
            return False
        
        #size = len(s)
        #words = []
        #recur(0,'')
        """wordDict = set(wordDict)
        dp = [True] + [False] * len(s)
        for i in range(len(s)):
            if dp[i]:
                for j in range(i, len(dp)):
                    if s[i:j] in wordDict:
                        dp[j] = True
        #return dp[-1]"""
        return self.wordBreakTwo(s,wordDict)
        
        