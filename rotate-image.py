# https://leetcode.com/problems/rotate-image/
# Problem Description

# Solution
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        toRotate = size//2
        
        queue = []
        
        for i in range(toRotate):
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
            #print(matrix)
        return