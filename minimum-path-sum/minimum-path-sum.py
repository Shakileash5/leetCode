class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        
        """
        res = [[0 for j in range(m)] for i in range(n)]
        res[0][0] = grid[0][0]
        
        for j in range(1,m):
            res[0][j] = res[0][j-1] + grid[0][j]
        
        for i in range(1,n):
            res[i][0] = res[i-1][0] + grid[i][0]
        
        #print(res)
        
        for i in range(1,n):
            for j in range(1,m):
                res[i][j] = min(res[i-1][j],res[i][j-1]) + grid[i][j]
        
        #print(res)"""
        path = [[0 for j in range(m)] for i in range(n)]
        path[0][0] = grid[0][0]
        for i in range(1,n):
            path[i][0] = path[i-1][0] + grid[i][0]
        for j in range(1,m):
            path[0][j] = path[0][j-1] + grid[0][j]
        
        for i in range(1,n):
            for j in range(1,m):
                path[i][j] = min(path[i][j-1],path[i-1][j]) + grid[i][j]
        
        #print(path)
        #return res[-1][-1]
        return path[-1][-1]