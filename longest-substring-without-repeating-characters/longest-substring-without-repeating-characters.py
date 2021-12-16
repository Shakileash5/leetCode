class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def soltwo():
            left = 0
            right = 0
            longest = 0
            currLongest = 0
            hashMap = {}
            size = len(s)
            
            while(left<size):
                if s[left] not in hashMap:
                    currLongest = left - right + 1
                    longest = max(currLongest,longest)
                    hashMap[s[left]] = left
                    left += 1
                else:
                    right = hashMap[s[left]] + 1
                    del hashMap[s[left]]
                    keys = list(hashMap.keys())
                    for key in keys:
                        if hashMap[key] < right:
                            del hashMap[key]
                #print(hashMap,right,left,currLongest)   
            return longest
                    
        
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
        return soltwo()