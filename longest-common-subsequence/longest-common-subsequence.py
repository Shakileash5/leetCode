class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        size1 = len(text1)
        size2 = len(text2)
        
        dp = [[None for j in range(size2+1)] for i in range(size1+1)]
        
        def recur(idx1,idx2,tempStr):
            
            if idx1>=size1 or idx2>=size2:
                #print(tempStr)
                return 0
            if dp[idx1][idx2] == None:
                res = 0
                max_ = res
                if text1[idx1] == text2[idx2]:
                    max_ = max(max_,recur(idx1+1,idx2+1,tempStr+text1[idx1])+ 1)
                else:
                    max_ = max(recur(idx1+1,idx2,tempStr),recur(idx1,idx2+1,tempStr))
                dp[idx1][idx2] = max_
                return max_ 
            else:
                return dp[idx1][idx2]
        
        return recur(0,0,'') 
                    