class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        sizeRow = len(grid)
        sizeCol = len(grid[0])
        maxArea = 0
        visited = [[False for j in range(sizeCol)] for i in range(sizeRow)]
        
        def isValid(x,y):
            if x<0 or y<0 or x>=sizeRow or y>=sizeCol:
                return False
            return True
        
        def dfs(i,j,visited,count):
            visited[i][j] = True
            count[0] += 1
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if isValid(x,y) and grid[x][y] and visited[x][y] == False:
                    dfs(x,y,visited,count)
        
        for i in range(sizeRow):
            for j in range(sizeCol):
                if grid[i][j] and visited[i][j] == False:
                    count = [0]
                    dfs(i,j,visited,count)
                    maxArea = max(maxArea,count[0])
        return maxArea