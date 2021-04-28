class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0,0]
        for i in range(2, n + 1):
            re = 0
            for j in range(1, i//2 + 1):
                num = max(j * (i - j), j * dp[i - j])
                re = max(re, num)
            dp.append(re)
        return dp[-1]