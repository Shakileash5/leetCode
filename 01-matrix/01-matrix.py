class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        sizeRow = len(mat)
        sizeCol = len(mat[0])
        
        visited = set()
        queue = []
        
        for i in range(sizeRow):
            for j in range(sizeCol):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    queue.append((i,j,0))
        
        res = [[0 for i in range(sizeCol)] for j in range(sizeRow)]
        #print(mat)
        #print(res)
        while queue:
            node = queue.pop(0)
            #print(node)
            res[node[0]][node[1]] = node[2]
            
            for x,y in [(node[0]+1,node[1]),(node[0]-1,node[1]),(node[0],node[1]+1),(node[0],node[1]-1)]:
                if 0<=x<sizeRow and 0<=y<sizeCol and (x,y) not in visited:
                    visited.add((x,y))
                    queue.append((x,y,node[2]+1))
        return res