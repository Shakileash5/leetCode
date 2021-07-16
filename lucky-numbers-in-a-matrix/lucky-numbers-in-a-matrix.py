class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        sizeRow = len(matrix)
        sizeCol = len(matrix[0])
        minRow = []
        maxCol = [0]*sizeCol
        res = []
        
        for i in range(sizeRow):
            min_ = 10**5+1
            for j in range(sizeCol):
                min_ = min(min_,matrix[i][j])
                maxCol[j] = max(maxCol[j],matrix[i][j])
            minRow.append(min_)
        
        for i in range(sizeRow):
            for j in range(sizeCol):
                if minRow[i] == maxCol[j]:
                    res.append(minRow[i])
        
        return res