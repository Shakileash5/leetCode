class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowSize = len(matrix)
        colSize = len(matrix[0])
        res = []
        iterations = (rowSize+colSize)//2
        
        for i in range(iterations):
            row = i
            flag = 0
            for col in range(i,colSize-i):
                res.append(matrix[row][col])
                flag = 1
            if flag == 0:
                break
            #print(res,"1")
            flag = 0
            for row in range(row+1,rowSize-i):
                res.append(matrix[row][col])
                flag = 1
            if flag == 0:
                break
            #print(res,"2")
            flag = 0
            for col in range(col-1,i-1,-1):
                res.append(matrix[row][col])
                flag = 1
            if flag == 0:
                break
            #print(res,"3")
            flag = 0
            for row in range(row-1,i,-1):
                res.append(matrix[row][col])
                flag = 1
            if flag == 0:
                break
            #print(res,'4')
            
        return res