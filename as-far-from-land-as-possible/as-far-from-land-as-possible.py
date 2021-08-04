class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        sizeRow = len(grid)
        sizeCol = len(grid[0])
        
        res = 0
        queue = []
        visited = set()
        
        # take all the lands and mark visited
        for i in range(sizeRow):
            for j in range(sizeCol):
                if grid[i][j] == 1:
                    queue.append([i,j,0])
                    visited.add((i,j))
        
        while queue:
            i,j,dept = queue.pop(0)
            
            for x,y in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
                if 0<=x<sizeRow and 0<=y<sizeCol and grid[x][y] == 0 and (x,y) not in visited:
                    queue.append([x,y,dept+1])
                    visited.add((x,y))
                    res = max(res,dept+1)
        if res == 0:
            return -1
        
        return res
        