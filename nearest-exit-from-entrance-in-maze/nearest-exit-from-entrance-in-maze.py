class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        sizeRow = len(maze)
        sizeCol = len(maze[0])
        
        queue = [(entrance[0],entrance[1],0)]
        visited = set()
        visited.add((entrance[0],entrance[1]))
        
        while queue:
            i,j,dist = queue.pop(0)
            #print(i,j)
            if (i == 0 or i == sizeRow-1 or j == 0 or j == sizeCol-1):
                if not (i==entrance[0] and j==entrance[1]):
                    return dist
            
            for x,y in [(i,j+1),(i+1,j),(i-1,j),(i,j-1)]:
                if 0<=x<sizeRow and 0<=y<sizeCol:
                    if maze[x][y] == '.' and (x,y) not in visited:
                        queue.append((x,y,dist+1))
                        visited.add((x,y))
        return -1