class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[None for j in range(n+1)] for i in range(m+1)]
        
        def dfs(idxR,idxC):
            if idxR >= m-1 or idxC >= n-1:
                return 1
            
            if dp[idxR][idxC] == None:
                res = 0
                if idxR+1<m:
                    res += dfs(idxR+1,idxC)
                if idxC+1<n:
                    res += dfs(idxR,idxC+1)
                dp[idxR][idxC] = res
            return dp[idxR][idxC]
        
        return dfs(0,0)