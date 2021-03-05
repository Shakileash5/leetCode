# https://leetcode.com/problems/spiral-matrix/
# Problem Description

# Solution
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        sizeRow = len(matrix)
        sizeCol = len(matrix[0])
        
        visited = set()
        res = []
        
        i,j = 0,0
        print(sizeRow,sizeCol)
        
        def isComplete(i,j):
            flag = 0
            if (i+1,j) not in visited:
                flag = 1
            if (i-1,j) not in visited:
                flag = 1
            if (i,j+1) not in visited:
                flag = 1
            if (i,j-1) not in visited:
                flag = 1
                
            return not flag
            
        
        while True:
            
            while i<sizeRow and j<sizeCol:
                #print(i,j,matrix[i][j])
                if (i,j) in visited:
                    break
                visited.add((i,j))
                res.append(matrix[i][j])
                if j+1==sizeCol or (i,j+1) in visited:
                    #print("broke")
                    break
                j+=1
            
            if len(visited) == (sizeRow*sizeCol):
                break
            if isComplete(i,j) :
                break
            
            i+=1   
            while i<sizeRow:
                #print(i,j)
                #print(matrix[i][j])
                if (i,j) in visited:
                    break
                visited.add((i,j))
                res.append(matrix[i][j])
                if i+1==sizeRow or (i+1,j) in visited:
                    break
                i+=1
                
            if len(visited) == (sizeRow*sizeCol):
                #print("here")
                break
            if isComplete(i,j) :
                #print("here1")
                break
                
            j-=1
            while j<sizeCol and j>=0:
                if (i,j) in visited:
                    break
                visited.add((i,j))
                res.append(matrix[i][j])
                if j-1<0 or (i,j-1) in visited:
                    break
                j-=1
            
            if len(visited) == (sizeRow*sizeCol):
                break
            if isComplete(i,j) :
                break
                
            i-=1
            while i<sizeRow and i>=0:
                if (i,j) in visited:
                    break
                visited.add((i,j))
                res.append(matrix[i][j])
                if i-1<0 or (i-1,j) in visited:
                    break
                i-=1
            if len(visited) == (sizeRow*sizeCol):
                break
            if isComplete(i,j) :
                break
            j+=1
        
        print(res)
        return res
            
            
                
            
            
            