class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        sizeRow = len(mat)
        sizeCol = len(mat[0])
        
        res = []
        hashMap = {}
        
        for i in range(sizeRow):
            for j in range(sizeCol):
                if i+j not in hashMap:
                    hashMap[i+j] = [mat[i][j]]
                else:
                    hashMap[i+j].append(mat[i][j])
        #print(hashMap,sizeRow,sizeCol)        
        for val in range(sizeRow+sizeCol-1):
            if val%2 == 0:    
                res.extend(hashMap[val][::-1])
            else:
                res.extend(hashMap[val])
                
        return res
                
                
                        
        