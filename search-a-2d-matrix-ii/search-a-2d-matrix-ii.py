class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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