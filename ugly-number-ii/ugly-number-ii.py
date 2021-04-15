class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        dp = [0]*(n)
        dp[0]=1
        t2=t3=t5 = 0
        
        for i in range(1, n):
            dp[i] = min(dp[t2] * 2, dp[t3] * 3, dp[t5] * 5)
            #print(dp,dp[t2] * 2, dp[t3] * 3, dp[t5] * 5)
            if dp[i] == dp[t2] * 2:
                t2 += 1

            if dp[i] == dp[t3] * 3:
                t3 += 1

            if dp[i] == dp[t5] * 5:
                t5 += 1

        #print(dp)
        return dp[-1]
                        
                
        