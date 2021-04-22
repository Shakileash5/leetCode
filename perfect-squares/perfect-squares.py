class Solution:
    def numSquares(self, n: int) -> int:
        from math import sqrt
        minVal = [float("inf")]
        def recur(idx,temp,nums):
            if sum(temp) >= n:
                sumVal = sum(temp)
                #print(temp,sumVal)
                if sumVal == n:
                    minVal[0] = min(minVal[0],len(temp))
                return
            
            #for i in range(idx,len(nums)):
            for i in range(idx,len(nums)):
                if (sum(temp)+nums[i])<=n:
                    recur(i,temp+[nums[i]],nums)
                
        perfectNumbers = []
        for i in range(1,n+1):
            sqr = sqrt(i)
            if int(sqr) == sqr:
                perfectNumbers.append(i)
        #for i in range
        #recur(0,[],perfectNumbers)
        dp = [float("inf")]*(n+1)
        dp[0] = 0
        
        for i in range(n+1):
            for squares in perfectNumbers:
                if squares <= i:
                    dp[i] = min(dp[i],1+dp[i-squares])
        #    temp = []
        #print(minVal[0])
        return dp[-1]
        