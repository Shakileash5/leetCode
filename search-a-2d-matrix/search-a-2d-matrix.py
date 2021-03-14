class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        sizeR = len(matrix)
        sizeC = len(matrix[0])
        print(sizeC)
        def rowMajor(x):
            i = x//sizeC 
            j = x%sizeC 
            
            if sizeR == 1:
                return 0,x
            return i,j
        
        def binarySearch(target,left,right):
            
            mid = (left+right)//2
            i,j = rowMajor(mid)
            print(left,right,mid,i,j)
            
            if left>right:
                return False
            
            if matrix[i][j] == target:
                return True
            
            
            if matrix[i][j] < target:
                return binarySearch(target,mid+1,right)
            else:
                return binarySearch(target,left,mid-1)
        
        return binarySearch(target,0,sizeR*sizeC-1)