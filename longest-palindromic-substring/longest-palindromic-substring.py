class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        maxLen = [0,""]
        if size == 1:
            return s
        
        memo = [[None for j in range(size+2)] for i in range(size+2)]
        
        def isPali(s,left,right):
            
            if left+1 == right:
                return s[left] == s[right]
            if left == right:
                return True
            
            if memo[left][right] == None:
                memo[left][right] = False
                if s[left] == s[right]:
                    memo[left][right] = isPali(s,left+1,right-1)   
            
            return memo[left][right]
        
        #print(isPali(s,0,size-3))
        def naive(): 
            for i in range(size):
                for j in range(i+1,size+1):
                    #print("c",s[i:j])
                    if isPali(s,i,j-1):
                        if maxLen[0]<(j-i):
                            maxLen = [j-i,s[i:j]]
        
        start = 0
        end = 0
        store = (0,0,0)
        
        for i in range(1,len(s)):
            start = i-1
            end = i+1
            
            while start>=0 and end<len(s) and s[start] == s[end] :
                if end - start + 1 > store[0]:
                    store = (end - start + 1,start,end)  
                start -=1
                end +=1
            
            start = i-1
            end = i
            
            while start>=0 and end<len(s) and s[start] == s[end] :
                if end - start + 1 > store[0]:
                    store = (end - start + 1,start,end)
                
                start -=1
                end +=1
        
        #print(store)
        
        return s[store[1]:store[2]+1]