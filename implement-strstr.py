# https://leetcode.com/problems/implement-strstr/
# Problem Description

# Solution

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        needleIdx = -1
        idx = 0
        needlePos = 0
        size = len(haystack)
        needleSize = len(needle)
        
        if needleSize==0 and size == needleSize:
            return 0
        
        if needleSize == 0 and size != 0:
            return 0
    
        while idx<size:
            
            if haystack[idx] == needle[needlePos]:
                flag = 0
                needleIdx = idx
                #print("idx",idx,needlePos,idx+needleSize-2,size)
                needlePos +=1
                idx1= idx+1
               # print("idx",idx1,needlePos,idx+needleSize-2,size)
                if (idx1+needleSize-2) < size:
                    #print("gere")
                    while needlePos<needleSize:
                        if haystack[idx1] == needle[needlePos]:
                            print(haystack[idx1],idx1,needlePos)
                            idx1+=1
                            needlePos+=1 
                            
                        else:
                            flag = 1
                            break
                    if flag==0:
                        return needleIdx
                needlePos = 0
            idx+=1
            needleIdx = -1
        
        return needleIdx

#optimized
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        needleIdx = -1
        idx = 0
        needlePos = 0
        size = len(haystack)
        needleSize = len(needle)
        
        if needleSize==0 and size == needleSize:
            return 0
        
        if needleSize == 0 and size != 0:
            return 0
        
        if size<needleSize:
            return -1
        
        while idx<size: 
            if haystack[idx:idx+needleSize] == needle:
                return idx
            idx+=1
        
        return needleIdx
        