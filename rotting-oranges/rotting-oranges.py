class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        sizeRow = len(grid)
        sizeCol = len(grid[0])
        
        allFreshOranges = 0
        totalMinutes = -1
        cordsOfRotten = []
        
        for i in range(sizeRow):
            for j in range(sizeCol):
                if grid[i][j] == 1:
                    allFreshOranges += 1
                elif grid[i][j] == 2:
                    cordsOfRotten.append([i,j])
        
        if allFreshOranges == 0:
            return 0
        elif len(cordsOfRotten) == 0:
            return -1
        
        def isValid(x,y):
            if x<0 or y<0 or x>=sizeRow or y>=sizeCol:
                return False
            return True
        
        level = len(cordsOfRotten)
        while(cordsOfRotten):
            coords = cordsOfRotten.pop(0)
            didAffect = 0
            level -= 1
            for x,y in [(coords[0]+1,coords[1]),(coords[0]-1,coords[1]),(coords[0],coords[1]+1),(coords[0],coords[1]-1)]:
                if isValid(x,y) and grid[x][y] == 1:
                    grid[x][y] = 2
                    cordsOfRotten.append([x,y])
                    didAffect = 1
                    allFreshOranges -= 1
            
            if level == 0:
                totalMinutes += 1
                level = len(cordsOfRotten)
        #print(res)
        if allFreshOranges > 0:
            return -1
        if totalMinutes == -1:
            return 0
        return totalMinutes 