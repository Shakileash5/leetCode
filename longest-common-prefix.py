# https://leetcode.com/problems/longest-common-prefix/submissions/
# Problem Description

# Solution

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        i,j,k = 0,0,0
        size = len(strs)
        #print(size,strs)
        if size == 0:
            return res
        if len(strs[0]) == 0:
                return res
        size1 = len(strs[0])
        while True:
            flag = 0
            if i>=size1:
                break
            r = strs[0][i]
            #print(j,size,strs[j])
            if i>=len(strs[j]) or r != strs[j][i]:
                flag = 1
                break
            if j==(size-1):
                i+=1
                j = 0
                res +=r
            else:
                j+=1
                
        #print(res)
        return res