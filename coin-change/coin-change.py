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
        
        def recur(idx,amount,memo):
            if idx>=size:
                print(amount)
                if ammount == 0:
                    return 0
                return float('inf')
            if amount == 0:
                return 0
            
            if (idx,amount) not in memo:
                minCoin = float('inf')
                for i in range(idx,size):
                    #print("here",i,amount)
                    if (amount - coins[i])>=0:
                        #print("inside")
                        res = recur(i,amount - coins[i],memo) + 1
                        #print(amount,idx,res)
                        minCoin = min(minCoin,res)
                memo[(idx,amount)] = minCoin
                return memo[(idx,amount)]
            else:
                return memo[(idx,amount)]
        #return dpSol(size,amount)
        memo = {}
        res  = recur(0,amount,memo)
        return -1 if res >= float('inf') else res