class Solution:
    def rowMajor(self,idx,sizeR,sizeC):
        row = idx//sizeC
        col = idx%sizeC
        if sizeR == 1:
            return 0,idx
        return row,col
    
    def binarySearch(self,left,right,target,matrix):
        if left>right:
            return False
        
        mid = (left+right)//2
        row,col = self.rowMajor(mid,len(matrix),len(matrix[0]))
        #print(row,col,mid)
        if matrix[row][col] == target:
            return True
        if matrix[row][col]<target:
            return self.binarySearch(mid+1,right,target,matrix)
        else :
            return self.binarySearch(left,mid-1,target,matrix)
        return
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        sizeR = len(matrix)
        sizeC = len(matrix[0])
        #print(sizeC)
        def rowMajor(x):
            i = x//sizeC 
            j = x%sizeC 
            
            if sizeR == 1:
                return 0,x
            return i,j
        
        
        """def binarySearch(target,left,right):
            
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
        """
        #return binarySearch(target,0,sizeR*sizeC-1)
        return self.binarySearch(0,sizeR*sizeC-1,target,matrix)
        #print(self.rowMajor(0,1,2))