class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        knightDirections = [(-1,-2),(1,-2),(2,-1),(-2,-1),(-2,1),(-1,2),(1,2),(2,1)]
        #dp = [[None for j in range(n)] for i in range(n)]
        memo = {}
        
        def dfs(idxR,idxC,kRemain):
            if idxR<0 or idxR>=n or idxC<0 or idxC>=n:
                return 0
            if kRemain == 0:
                return 1
            if (idxR,idxC,kRemain) not in memo:
                noOfWays = 0
                for x,y in knightDirections:
                    noOfWays += dfs(x+idxR,y+idxC,kRemain-1)
                memo[(idxR,idxC,kRemain)] = noOfWays
            return memo[(idxR,idxC,kRemain)]
        
        res = dfs(row,column,k)
        
        #print(res)
        for i in range(k):
            res /= 8
        return res
                