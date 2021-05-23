class Solution:
    
    def findPath(self,idxR,idxC,m,n):
        if (idxR>=m) or (idxC>=n):
            #print(idxR,idxC)
            #print("why god")
            return 0
        if idxR==(m-1) and idxC==(n-1) :
            #print("foundIt")
            return 1
        
        if self.dp[idxR][idxC] == None:
            pathTwo = self.findPath(idxR,idxC+1,m,n) 
            #print("comeDown",idxR,idxC)
            path = self.findPath(idxR+1,idxC,m,n) 
            self.dp[idxR][idxC] = pathTwo+path
            return self.dp[idxR][idxC]
        else:
            return self.dp[idxR][idxC]    
            #return self.findPath(idxR,idxC+1,m,n) + self.findPath(idxR+1,idxC,m,n)
        
    
    
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1 for i in range(n)] for j in range(m)]
        
        #print(paths)
        self.dp = [[None for i in range(n)] for j in range(m)]
        """for i in range(1,m):
            for j in range(1,n):
                #print(i,j,i-1,j-1)
                paths[i][j] = paths[i-1][j] + paths[i][j-1]"""
        
        #print(paths)
        #print()
        #return paths[-1][-1]
        return self.findPath(0,0,m,n)