class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alphaStore = set()
        start = 0
        end = 0
        n = len(s)
        maxSubString = 1
        if s == "":
            return 0
        while end<n:
            if s[end] in alphaStore:
                alphaStore.remove(s[start])
                start +=1         
            else:
                alphaStore.add(s[end])
                maxSubString = max(end - start +1 ,maxSubString)
                end+=1   
        
        def solutionWithHash():
            alphaBet={}
            left = 0
            right = 0
            size = len(s)
            max_ = 0
            if size>0:
                alphaBet[s[0]] = 1
                right+=1
                max_= 1
            
            while right<size:
                if alphaBet.get(s[right],0):
                    while left<right and alphaBet[s[right]] == 1:
                        alphaBet[s[left]] = 0
                        left+=1
                else:
                    alphaBet[s[right]] = 1
                    #print(s[left:right+1])
                    max_= max(max_,(right-left+1))
                    right+=1
                    
            return(max_)
        #print(solutionWithHash())
        
        #return maxSubString
        return solutionWithHash()