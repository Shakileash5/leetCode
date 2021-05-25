class Solution:

    def catlanNumber(self,n,dp):
        if n<=1:
            return 1
        if dp[n] == None:
            res = 0
            for i in range(n):
                res+=self.catlanNumber(i,dp)*self.catlanNumber(n-i-1,dp)
            dp[n] = res
            return dp[n]
        else:
            return dp[n]
    
    
    def numTrees(self, n: int) -> int:
        #@cache
        dp = [None]*n
        def recur(n,dp):
            if n<=1:
                return 1
            if dp[n-1]!=None:
                return dp[n-1]
            res = 0
            for i in range(n):
                res+= recur(i,dp)*recur(n-i-1,dp)
            dp[n-1] = res
            return dp[n-1]
        #fact = factorial(n)
        #re = recur(n,dp)
        #print(re,fact)
        #unique = recur(n)//factorial(n)
        #return re
        dp = [None]*(n+1)
        return self.catlanNumber(n,dp)