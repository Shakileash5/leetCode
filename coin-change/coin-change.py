class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        size = len(coins)
        res = [100000]
        resCount = 0
        idx = size-1
        #coins.sort()
        #print(coins)
        @cache
        def recur(idx,amountTemp,count):
            if idx>=size:
                return
            if amountTemp<=0:
                if amountTemp == 0:
                    #print(amountTemp,idx,count)
                    res[0] = min(res[0],count)
                return
            
            for i in range(idx,size):
                recur(i,amountTemp-coins[i],count+1)
                if (i+1)<size:
                    recur(i+1,amountTemp-coins[i+1],count+1)
        
        #recur(0,amount,0)
        
        def dpSol(size,amount):
            dp = [0] + [inf] * amount
            for coin in coins:
                for i in range(coin, amount+1):
                    dp[i] = min(dp[i], dp[i-coin]+1)
            return dp[-1] if dp[-1] < inf else -1
        
        #print(resCount,res,amountTemp)
        return dpSol(size,amount)  
        