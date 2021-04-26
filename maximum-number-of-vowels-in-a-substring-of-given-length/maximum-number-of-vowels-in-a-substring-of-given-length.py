class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        maxVowels = -1
        idx = 0
        size = len(s)
        count = 0
        vowels = ["a","e","i","o","u"]
        
        for i in range(0,k):
            if s[i] in vowels:
                count+=1
        
        #print(idx,count)
        maxVowels = max(count,maxVowels)
        idx = 1
        
        while(idx<=(size-k+1)):
            if idx-1 >= 0 and s[idx-1] in vowels:
                count-=1
            if (idx+k-1)<size and s[idx+k-1] in vowels:
                count+=1
            maxVowels = max(count,maxVowels)
            #print(count,idx-1,idx,idx+k,s[idx:idx+k])
            idx+=1
        #print(maxVowels)
        return maxVowels
        
            
            
                
                