class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        number = n*n
        count = 0
        i,j = 0,0
        iteration=0
        res = [[0 for j in range(n)] for i in range(n)]
        #print(res)
        
        while count<number:
            
            for k in range(j,n-iteration):
                #print("1st",k,count)
                j = k
                res[i][j] = count+1;
                count+=1
            #print(res)
            for k in range(i+1,n-iteration):
                i = k
                res[i][j] = count+1
                count+=1
            #print(res)
            for k in range(j-1,-1 + iteration,-1):
                j = k
                res[i][j] = count+1
                count+=1
            #print(res)
            for k in range(i-1,-1+1+iteration,-1):
                i = k
                res[i][j] = count+1
                count+=1
            #print(res)
            iteration+=1
            j=j+1
            #print("atlast")
        return res
                
        
        
                
            
        