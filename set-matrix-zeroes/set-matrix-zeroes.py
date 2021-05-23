class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        sizeR = len(matrix)
        sizeC = len(matrix[0])
        setR = set()
        setC = set()
        
        """for i in range(sizeR):
            for j in range(sizeC):
                if matrix[i][j] == 0:
                    setR.add(i)
                    setC.add(j)
        for i in range(sizeR):
            for j in range(sizeC):
                if i in setR:
                    matrix[i][j] = 0
                elif j in setC:
                    matrix[i][j] = 0"""
        #print(setR,setC,matrix)
        for i in range(sizeR):
            for j in range(sizeC):
                if matrix[i][j] == 0:
                    setR.add(i)
                    setC.add(j)
        
        for i in range(sizeR):
            for j in range(sizeC):
                if i in setR or j in setC:
                    matrix[i][j] = 0
        
        return
        