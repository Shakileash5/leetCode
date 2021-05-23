class Solution:
    def recur(self,grid,idxR,idxC,m,n):
        if idxR>=n or idxC>=m:
            return 0
        if grid[idxR][idxC] == 1:
            return 0
        if idxR==(n-1) and idxC==(m-1):
            return 1
        if self.memoize[idxR][idxC] == None:
            path = self.recur(grid,idxR+1,idxC,m,n)
            pathTwo = self.recur(grid,idxR,idxC+1,m,n)
            self.memoize[idxR][idxC] = path+pathTwo
            return self.memoize[idxR][idxC]
        else:
            return self.memoize[idxR][idxC]
        
    
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        """flag = 0
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
                    res[i][j] = res[i-1][j] + res[i][j-1]"""
        
        path = [[0 for i in range(m)] for j in range(n)]
        if obstacleGrid[0][0] == 0:
            path[0][0] = 1
        for i in range(1,m):
            if obstacleGrid[0][i] == 1:
                break
            path[0][i] = path[0][i-1]
        for i in range(1,n):
            if obstacleGrid[i][0] == 1:
                break
            path[i][0] = path[i-1][0]
        
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j] != 1:
                    path[i][j] = path[i][j-1] + path[i-1][j]
        
        #print(res)
        #print(path)
        #return path[-1][-1]
        self.memoize = [[None for i in range(m)] for j in range(n)]
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        return self.recur(obstacleGrid,0,0,m,n)       
        