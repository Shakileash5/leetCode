class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        size = len(s)
        if size == 1:
            if s in wordDict:
                return True
            else:
                return False
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
        
        words = []
        
        return recur(0,'')
        
        