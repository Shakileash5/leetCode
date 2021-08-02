class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        sizeRow = len(matrix)
        sizeCol = len(matrix[0])
        
        def rowMajor(idx):
            i = idx // sizeCol
            j = idx % sizeCol
            if sizeRow == 1:
                return 0,idx
            
            return i,j
        
        #print(rowMajor(3))
        left = 0
        right = sizeRow*sizeCol-1
        
        while(left<=right):
            mid = (left+right)//2
            
            i,j = rowMajor(mid)
            #print(i,j,left,right,mid)
            if matrix[i][j] == target:
                return True
            if matrix[i][j]>target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False
        
        