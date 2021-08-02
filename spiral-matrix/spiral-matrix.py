class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sizeRow = len(matrix)
        sizeCol = len(matrix[0])
        res = []
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        seen = [[False for j in range(sizeCol)] for i in range(sizeRow)]
        
        id_ = 0
        idxR,idxC = 0,0
        
        for i in range(sizeRow*sizeCol):
            res.append(matrix[idxR][idxC])
            seen[idxR][idxC] = True
            x,y = idxR+dirs[id_][0],idxC+dirs[id_][1]
            
            if 0<=x<sizeRow and 0<=y<sizeCol and seen[x][y]==False:
                idxR,idxC = x,y
            else:
                id_ = (id_+1)%4
                idxR,idxC = idxR+dirs[id_][0],idxC+dirs[id_][1]
            #print(idxR,idxC)
        return res
                