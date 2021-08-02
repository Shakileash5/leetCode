class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        id_ = 0
        
        matrix = [[0 for i in range(n)] for j in range(n)]
        idxR = 0
        idxC = 0
        
        for i in range(1,n*n+1):
            matrix[idxR][idxC] = i
            x,y = idxR+dirs[id_][0],idxC+dirs[id_][1]
            
            if 0<=x<n and 0<=y<n and matrix[x][y] == 0:
                idxR,idxC = x,y
            else:
                id_ = (id_+1)%4
                idxR,idxC = idxR+dirs[id_][0],idxC+dirs[id_][1]
        
        return matrix