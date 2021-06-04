class Solution:
    def searchMatric2D(self,matrix,target):
        sizeR = len(matrix)
        sizeC = len(matrix[0])
        x = 0
        y = sizeC - 1
        
        while(x<sizeR and y>=0):
            if matrix[x][y]>target:
                y -= 1
            elif matrix[x][y]<target:
                x += 1
            else:
                return True
        return False
        
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def searchMatrixOne():
            sizeR = len(matrix)
            sizeC = len(matrix[0])

            x = 0
            y = sizeC-1

            while(x<sizeR and y>=0):
                if matrix[x][y] == target:
                    return True
                if target>matrix[x][y]:
                    x+=1
                else:
                    y-=1

            return False
        
        return self.searchMatric2D(matrix,target)