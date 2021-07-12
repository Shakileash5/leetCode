class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 1000000007
        dp = [[[None for c in range(maxMove+1)] for j in range(n+1)] for i in range(m+1)]
        
        def dfs(idxR,idxC,movesLeft):
            if movesLeft<0:
                return 0
            if idxR<0 or idxR>=m or idxC<0 or idxC>=n:
                return 1
            
            #visited.add((idxR,idxC))
            if dp[idxR][idxC][movesLeft] == None:
                noOfWays = 0
                for x,y in [(idxR+1,idxC),(idxR-1,idxC),(idxR,idxC+1),(idxR,idxC-1)]:
                    #if (x,y) not in visited:
                    noOfWays += dfs(x,y,movesLeft-1)%mod
                dp[idxR][idxC][movesLeft] = noOfWays%mod
            return dp[idxR][idxC][movesLeft]
        
        #print()
        return dfs(startRow,startColumn,maxMove)