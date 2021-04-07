class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        sizeR = len(grid)
        sizeC = len(grid[0])
        visited = [[0 for _ in range(sizeC)] for i in range(sizeR)]
        noOfIsland = 0
        
        def searchIsland(idxR,idxC):
            if grid[idxR][idxC] == "0":
                return
            visited[idxR][idxC] = 1
            if idxR+1<sizeR and visited[idxR+1][idxC]==0 :
                searchIsland(idxR+1,idxC)
            if idxC+1<sizeC and visited[idxR][idxC+1]==0:
                searchIsland(idxR,idxC+1)
            if idxR-1>=0 and visited[idxR-1][idxC]==0:
                searchIsland(idxR-1,idxC)
            if idxC-1>=0 and visited[idxR][idxC-1]==0:
                searchIsland(idxR,idxC-1)
            return
        
        for i in range(sizeR):
            for j in range(sizeC):
                if grid[i][j]=="1" and visited[i][j] == 0:
                    searchIsland(i,j)
                    noOfIsland+=1
                    
        #searchIsland(0,0)
        print(noOfIsland)
        return noOfIsland
        
        
                