class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        sizeRow = len(heights)
        sizeCol = len(heights[0])
        marked = [[[None,None] for j in range(sizeCol)] for i in range(sizeRow)]
        res = []
        
        def harvestDown(idxR,idxC,x,y,visited):
            if visited[idxR][idxC] == True:
                return 
            visited[idxR][idxC] = True
            
            if marked[idxR][idxC] != [None,None]:
                if marked[idxR][idxC][0] == True:
                    marked[x][y][0] = True
                if marked[idxR][idxC][1] == True:
                    marked[x][y][1] = True
                if marked[x][y] == [True,True]:
                    return   
            if idxR == 0 or idxC == 0:
                marked[x][y][0] = True
                if marked[x][y] == [True,True]:
                    return
            if idxR == (sizeRow-1) or (idxC == sizeCol-1):
                marked[x][y][1] = True
                if marked[x][y] == [True,True]:
                    return 
            if idxR - 1>=0 and heights[idxR-1][idxC]<=heights[idxR][idxC]:
                harvestDown(idxR-1,idxC,x,y,visited)
                if marked[x][y] == [True,True]:
                    return
            if idxC - 1>=0 and heights[idxR][idxC-1]<=heights[idxR][idxC]: 
                harvestDown(idxR,idxC-1,x,y,visited)
                if marked[x][y] == [True,True]:
                    return
            if idxR + 1<sizeRow and heights[idxR+1][idxC]<=heights[idxR][idxC]:
                harvestDown(idxR+1,idxC,x,y,visited)
                if marked[x][y] == [True,True]:
                    return
            if idxC + 1<sizeCol and heights[idxR][idxC+1]<=heights[idxR][idxC]: 
                harvestDown(idxR,idxC+1,x,y,visited)
                if marked[x][y] == [True,True]:
                    return
            return 
        
        def isValid(idxR,idxC,visited):
            if idxR<0 or idxC<0:
                return False
            if idxR>=sizeRow or idxC>=sizeCol:
                return False
            if visited[idxR][idxC]:
                return False
            return True
        
        def dfs(idxR,idxC,visited):
            visited[idxR][idxC] = 1
            for x,y in [(idxR+1,idxC),(idxR,idxC+1),(idxR-1,idxC),(idxR,idxC-1)]:
                if isValid(x,y,visited) and heights[idxR][idxC]<=heights[x][y]:
                    dfs(x,y,visited)
            return
        
        
        visitedPacific = [[0 for j in range(sizeCol)] for i in range(sizeRow)]
        visitedAtlantic = [[0 for j in range(sizeCol)] for i in range(sizeRow)]
        
        for i in range(sizeRow):
            dfs(i,0,visitedPacific)
        for j in range(sizeCol):
            dfs(0,j,visitedPacific)
            
        for i in range(sizeRow):
            dfs(i,sizeCol-1,visitedAtlantic)
        for j in range(sizeCol):
            dfs(sizeRow-1,j,visitedAtlantic)
            
        for i in range(sizeRow):
            for j in range(sizeCol):
                if visitedAtlantic[i][j] == 1 and visitedPacific[i][j] == 1:
                    res.append([i,j])
                    
        return res
        
        