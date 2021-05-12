class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sizeSub = len(s)
        sizeStr = len(t)
        j = 0
        for i in range(sizeSub):
            subChar = s[i]
            while(j<sizeStr and subChar!=t[j]):
                j+=1
            if j>=sizeStr:
                return False
            else:
                j+=1
            
        return True