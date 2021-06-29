class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        sizeR = len(grid)
        sizeC = len(grid[0])
        
        
        def isValid(x,y):
            if x<0 or y<0 or x>=sizeR or y>=sizeC:
                return False
            return True
        
        def dfs(idxR,idxC,visited,isBorder):
            if visited[idxR][idxC]:
                return
            
            visited[idxR][idxC] = True
            
            if idxR == 0 or idxC == 0 or idxR==(sizeR-1) or idxC==(sizeC-1):
                isBorder[0] = True
            for x,y in [(idxR+1,idxC),(idxR-1,idxC),(idxR,idxC+1),(idxR,idxC-1)]:
                if isValid(x,y) and grid[x][y] == 0:
                    dfs(x,y,visited,isBorder)
            return False
        
        
        visited = [[False for j in range(sizeC)] for i in range(sizeR)]
        count = 0
        for i in range(sizeR):
            for j in range(sizeC):
                if grid[i][j] == 0 and visited[i][j] == False: 
                    isBorder = [False]
                    dfs(i,j,visited,isBorder) 
                    if isBorder[0] == False:
                        count += 1
        return count
                    