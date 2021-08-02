class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        sizeRow = len(mat)
        sizeCol = len(mat[0])
        
        dp = [[0]*sizeCol for _ in range(sizeRow)]
        res = 0
        
        for i in range(sizeRow):
            for j in range(sizeCol):
                if i==0 and mat[i][j]:
                    dp[i][j] = 1
                elif mat[i][j]:
                    dp[i][j] = dp[i-1][j] + 1
        
        #print(dp)
        for i in range(sizeRow):
            for j in range(sizeCol):
                for k in range(j+1,sizeCol+1):
                    res += min(dp[i][j:k])
                    #print(res,dp[i][j:k])
        return res
                    
                    
        
        