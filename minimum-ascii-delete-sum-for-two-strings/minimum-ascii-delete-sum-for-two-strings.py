class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        size1 = len(s1)
        size2 = len(s2)
        subStrMax = ''
        dp = [[None for i in range(size2)] for j in range(size1)]
        
        def lcs(idx1,idx2,subStr):
            if idx1>=size1 or idx2>=size2:
                #print(subStr,"so")
                return [0,'']
            if dp[idx1][idx2] == None:    
                if s1[idx1] != s2[idx2]:
                    moveS1 = lcs(idx1+1,idx2,subStr)
                    moveS2 = lcs(idx1,idx2+1,subStr)
                    if moveS1[0]>moveS2[0]:
                        dp[idx1][idx2] = moveS1
                        return moveS1
                    dp[idx1][idx2] = moveS2
                    return moveS2
                else:
                    res = lcs(idx1+1,idx2+1,subStr+s1[idx1])
                    dp[idx1][idx2] = [res[0]+ ord(s1[idx1]),res[1]+s1[idx1]] 
                    return dp[idx1][idx2]
            else:
                return dp[idx1][idx2]
        
        res = lcs(0,0,"")
        sum1 = 0
        sum2 = 0
        for i in range(size1):
            sum1 += ord(s1[i])
        
        sum1 -= res[0]
        
        for j in range(size2):
            sum2 += ord(s2[j])
        sum2 -= res[0]
        
        return sum1 + sum2