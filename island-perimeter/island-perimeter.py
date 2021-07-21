class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        sizeRow = len(grid)
        sizeCol = len(grid[0])
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        perimeter = [0]
        visited = set()
        
        def dfs(idxR,idxC):
            visited.add((idxR,idxC))
            #print(idxR,idxC,perimeter)
            perimeter[0] += 4
            for i,j in dirs:
                x = i+idxR
                y = j+idxC
                if 0<=x<sizeRow and 0<=y<sizeCol and grid[x][y] == 1:
                    perimeter[0] -= 1
                    #print(perimeter,x,y)
                    if (x,y) not in visited:
                        dfs(x,y)
            return
        
        flag = 0
        for i in range(sizeRow):
            for j in range(sizeCol):
                if grid[i][j] == 1:
                    dfs(i,j)
                    flag = 1
                    break
            if flag == 1:
                break
        return perimeter[0]
                    
            