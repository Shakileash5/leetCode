class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        size = len(s)
        
        def divideAndConquere(string,k):
            
            countMap = {}
            size = len(string)
            for i in range(size):
                if string[i] not in countMap.keys():
                    #print(i,size,string)
                    #print(string[i])
                    countMap[string[i]] = 1
                else:
                    #print(i,size,string,"sec")
                    countMap[string[i]]+=1
            #print(countMap)
            for i in range(size):
                if countMap[string[i]]<k:
                    #print("comeHere",i,string)
                    left = divideAndConquere(string[:i],k)
                    right = divideAndConquere(string[i+1:],k)
                    return max(left,right)
            return size
        
        return divideAndConquere(s,k)
        