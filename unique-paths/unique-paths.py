class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import numpy as np
        res = np.ones(shape=(m,n))
        for i in range(1,m):
            for j in range(1,n):
                res[i][j] = res[i-1][j]+res[i][j-1]
        return int(res[-1][-1])