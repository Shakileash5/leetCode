class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        sizeRow = len(obstacleGrid)
        sizeCol = len(obstacleGrid[0])
        
        dp = [[None for j in range(sizeCol+1)] for i in range(sizeRow)]
        
        def dfs(idxR,idxC):
            #print(idxR,idxC)
            if idxR>=sizeRow or idxC>=sizeCol:
                return 0
            
            if obstacleGrid[idxR][idxC] == 1:
                #print(idxR,idxC,"d")
                return 0
            
            if idxR==sizeRow-1 and idxC==sizeCol-1:
                return 1
            
            if dp[idxR][idxC] == None:
                res = 0
                res += dfs(idxR+1,idxC)
                res += dfs(idxR,idxC+1)
                dp[idxR][idxC] = res
            return dp[idxR][idxC]
        
        return dfs(0,0)