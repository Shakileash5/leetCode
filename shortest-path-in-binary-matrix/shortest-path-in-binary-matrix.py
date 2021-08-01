class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        sizeRow = len(grid)
        sizeCol = len(grid[0])
        
        if grid[0][0] == 1:
            return -1
        
        queue = [(0,0,1)]
        visited = set()
        visited.add((0,0))
        distance = -1
        
        while queue:
            i,j,depth = queue.pop(0)
            #print(queue,visited,i,j,depth)
            if i == sizeRow-1 and j == sizeCol-1:
                distance = depth
                break
            
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j+1),(i-1,j-1),(i+1,j-1),(i-1,j+1)]:
                if 0<=x<sizeRow and 0<=y<sizeCol and grid[x][y] == 0:
                    if (x,y) not in visited:
                        visited.add((x,y))
                        queue.append((x,y,depth+1))
        
        return distance