class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        sizeR = len(grid)
        sizeC = len(grid[0])
        visited = set()
        noOfIsland = 0
        
        def dfs(idxR,idxC):
            if (idxR,idxC) in visited:
                return
            
            visited.add((idxR,idxC))
            if(idxR+1 < sizeR) and grid[idxR+1][idxC] == '1':
                dfs(idxR+1,idxC)
            if(idxR-1 >= 0) and grid[idxR-1][idxC] == '1':
                dfs(idxR-1,idxC)
            if(idxC+1 < sizeC) and grid[idxR][idxC+1] == '1':
                dfs(idxR,idxC+1)
            if(idxC-1 >= 0) and grid[idxR][idxC-1] == '1':
                dfs(idxR,idxC-1)
            
            return
        
        for i in range(sizeR):
            for j in range(sizeC):
                if(grid[i][j] == '1'):
                    if (i,j) not in visited:
                        dfs(i,j)
                        noOfIsland += 1
        return noOfIsland 
            