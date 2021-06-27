class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        sizeRow = len(grid)
        sizeCol = len(grid[0])
        
        def isValid(x,y):
            if x<0 or y<0 or x>=sizeRow or y>=sizeCol:
                return False
            return True
        
        def dfs(i,j,visited,currColor,border):
            visited[i][j] = True
            
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if isValid(x,y) and grid[x][y] == currColor:
                    if visited[x][y] == False:
                        dfs(x,y,visited,currColor,border)
                else:
                    border.add((i,j))
                    
            return
        
        visited = [[False for j in range(sizeCol)] for i in range(sizeRow)]
        currColor = grid[r0][c0]
        border = set()
        dfs(r0,c0,visited,currColor,border)
        for x,y in border:
            grid[x][y] = color
        return grid