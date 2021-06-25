class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        sizeRow = len(grid)
        sizeCol = len(grid[0])
        visited = set()
        count = 0
        
        def isValid(x,y):
            if x<0 or y<0 or x>=sizeRow or y>=sizeCol:
                return False
            return True
        
        def dfs(i,j,visited,noOfOnes,isBorder):
            
            visited.add((i,j))
            noOfOnes[0] += 1
            if i == 0 or j == 0 or i == sizeRow-1 or j == sizeCol -1:
                isBorder[0] = True
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if isValid(x,y) and grid[x][y] and (x,y) not in visited:
                    dfs(x,y,visited,noOfOnes,isBorder) 
                    
            return True
        
        for i in range(sizeRow):
            for j in range(sizeCol):
                if grid[i][j] and (i,j) not in visited:
                    noOfOnes = [0]
                    isBorder = [False]
                    dfs(i,j,visited,noOfOnes,isBorder)
                    if isBorder[0] == False:
                        count += noOfOnes[0]
        return count