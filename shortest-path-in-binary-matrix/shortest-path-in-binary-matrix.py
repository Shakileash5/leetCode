class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        sizeRow = len(grid)
        sizeCol = len(grid[0])
        
        minDist = float('inf')
        visited = set()
        visited.add((0,0))
        queue = [[0,0,1]]
        flag = 0
        if grid[0][0] == 1:
            return -1
        while queue:
            i,j,dist = queue.pop(0)
            
            if i == sizeRow-1 and j == sizeCol-1:
                minDist = min(minDist,dist)
                flag = 1
            #print(i,j,dist,grid[i][j])
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i-1,j-1),(i+1,j+1),(i-1,j+1),(i+1,j-1)]:
                if 0<=x<sizeRow and 0<=y<sizeCol and grid[x][y]!=1 and (x,y) not in visited:
                    visited.add((x,y))
                    queue.append([x,y,dist+1])
                    
        return minDist if flag == 1 else -1 
                
            
        
        