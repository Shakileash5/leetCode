class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        flag = 0
        print(n,m)
        res = [[0 for j in range(m)] for i in range(n)]
        
        if obstacleGrid[0][0] == 0:
            res[0][0] = 1
        
        for j in range(1,m):
            if obstacleGrid[0][j] == 0:
                res[0][j] = res[0][j-1]
        for i in range(1,n):
            if obstacleGrid[i][0] == 0:
                res[i][0] = res[i-1][0]
                
        
        print(res)
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j] == 0:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        
        #print(res)
        return res[-1][-1]
                
        