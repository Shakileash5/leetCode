class Solution:
    def rotateArr(self,arr):
        rowSize = len(arr)
        colSize = len(arr[0])
        
        for i in range(rowSize//2):
            queue = []
            for col in range(i,rowSize-i):
                queue.append(arr[i][col])
            #print(queue)
            flag = 0
            for row in range(i,rowSize-i):
                if flag==0:
                    flag =1
                else:
                    queue.append(arr[row][col])
                arr[row][col] = queue.pop(0)
                #print("fea",row,queue)
            #print(arr,queue)
            flag = 0
            for col in range(rowSize-i-2,i-1,-1):
                queue.append(arr[row][col])
                arr[row][col] = queue.pop(0)
            #print(arr,queue)  
            
            for row in range(rowSize-i-2,i-1,-1):
                #print(arr[row][col],row,col)
                queue.append(arr[row][col])
                arr[row][col] = queue.pop(0)
            #print(arr,queue) 
            
            for col in range(i+1,rowSize-i-1):
                arr[row][col] = queue.pop(0)
            #print("completed",arr,queue) 
        #print(arr)
        return
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        toRotate = size//2
        
        queue = []
        self.rotateArr(matrix)
        """for i in range(toRotate):
            #print("iteration:: ",i)
            #print(i,size-i,matrix[i][i:size-i])
            queue=[]
            for col in range(i,size-i):
                queue.append(matrix[i][col])
            #print(queue,matrix)
            for row in range(i,size-i):
                if row !=  i:
                    queue.append(matrix[row][size-1-i])
                matrix[row][size-1-i] = queue.pop(0)
            #print(queue,matrix)    
            for col in range(size-1-i,i-1,-1):
                if col != size-1-i:
                    queue.append(matrix[size-1-i][col])
                    matrix[size-1-i][col] = queue.pop(0)
            #print(queue,matrix)
            for row in range(size-1-i,i-1,-1):
                if row != size-1-i:
                    queue.append(matrix[row][i])
                    matrix[row][i] = queue.pop(0)
            #print(queue,matrix)
            for col in range(i+1,size-1-i):
                matrix[i][col] = queue.pop(0)
            #print(queue)
            #print(matrix)"""
        return