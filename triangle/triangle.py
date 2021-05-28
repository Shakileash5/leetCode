class Solution:
    def recurMin(self,row,idx,triangle):
        if row>=len(triangle) or row<len(triangle) and idx>=len(triangle):
            return 0
        
        if self.dp[row][idx] == None:
            res = min(self.recurMin(row+1,idx,triangle),self.recurMin(row+1,idx+1,triangle)) + triangle[row][idx]
            self.dp[row][idx] = res
            return res
        else:
            #print("HIT")
            return self.dp[row][idx]
        
        
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        size = len(triangle)
        #minPath = [None]
        #dp = [[None]*_ for _ in range(1,size+1)]
        
        def recur(size,idx,row,temp,dp):
            #print(row)
            if row == size-1:
                #print(minPath)
                if minPath[0] == None:
                    minPath[0] = sum(temp)
                else:
                    minPath[0] = min(minPath[0],sum(temp))
                return minPath[0]
            if dp[row][idx]!=None:
                return dp[row][idx]
            
            dp[row+1][idx] = recur(size,idx,row+1,temp+[triangle[row+1][idx]],dp)
            dp[row+1][idx+1] = recur(size,idx+1,row+1,temp+[triangle[row+1][idx+1]],dp)
            
            return dp[row][idx]
        #recur(size,0,0,[triangle[0][0]],dp)
        #print(minPath[0])
        #bottomUp Approach
        def iterativeDp():
            dp = triangle[:]
            for i in range(size-2,-1,-1):
                for j in range(len(dp[i])-1,-1,-1):
                    dp[i][j] = min(dp[i][j]+dp[i+1][j],dp[i][j]+dp[i+1][j+1])


            return dp[0][0]
        self.dp = [[None for j in range(len(triangle[-1]))] for i in range(len(triangle))]
        return self.recurMin(0,0,triangle)