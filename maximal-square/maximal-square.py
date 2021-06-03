class Solution:
    def maximalSquareTwo(self,matrix):
        sizeR = len(matrix)
        sizeC = len(matrix[0])
        
        dp = [[None for _ in range(sizeC)] for j in range(sizeR)]
        maxRect = 0
        for i in range(sizeR):
            for j in range(sizeC):
                if matrix[i][j] == '1':
                    if maxRect == 0:
                        maxRect = 1
                    if i-1<0 or j-1<0:
                        continue
                    matrix[i][j] = 1 + min(int(matrix[i-1][j]),min(int(matrix[i-1][j-1]),int(matrix[i][j-1])))
                    maxRect = max(maxRect,matrix[i][j])
        return maxRect**2
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        sizeRow = len(matrix)
        sizeColumn = len(matrix[0])
        maxSquare = 0
        
        def isSquare(idxR,idxC,size):
            
            for i in range(idxR,idxR+size):
                for j in range(idxC,idxC+size):
                    if i<sizeRow and j<sizeColumn and matrix[i][j] == '0':
                        return False
                    if i>=sizeRow or j>=sizeColumn:
                        return False
            
            return True
        
        def maxSquareBruteForce(sizeRow,sizeColumn):
            for i in range(sizeRow):
                for j in range(sizeColumn):

                    if matrix[i][j] == '1':
                        tempMax = 1
                        size = 2

                        while(isSquare(i,j,size)):
                            tempMax = size*size
                            size+=1

                        if maxSquare<tempMax:
                            maxSquare = tempMax
            return maxSquare
        """        
        dp = [[0 for _ in range(sizeColumn)] for x in range(sizeRow)]
        for i in range(sizeRow):
            for j in range(sizeColumn):
                if matrix[i][j] == '1':
                    if maxSquare == 0:
                        maxSquare = 1
                    if (i-1)<0 or (j-1)<0:
                        continue
                    matrix[i][j] = 1+min(int(matrix[i-1][j]),int(matrix[i][j-1]),int(matrix[i-1][j-1]))
                    maxSquare = max(maxSquare,matrix[i][j])

                    
        return maxSquare**2"""
        return self.maximalSquareTwo(matrix[:])
                    
        
        