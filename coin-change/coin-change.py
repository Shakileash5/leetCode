class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        size = len(coins)
        coins.sort(reverse=True)
        memo = {}
        
        def minCoins(idx,sum_):
            if idx>=size:
                if sum_ == 0:
                    return 0
                return float('inf')
            if sum_ <= 0:
                if sum_ == 0:
                    return 0
                return float('inf')
            
            
            if (idx,sum_) not in memo:
                min_ = float('inf')
                for i in range(idx,size):
                    #print(i,sum_)
                    if sum_-coins[i]>=0:
                        #print(i)
                        res = minCoins(i,sum_-coins[i])+1
                        min_ = min(min_,res) 
                    
                memo[(idx,sum_)] = min_
            
            return memo[(idx,sum_)]
        
        res = minCoins(0,amount)
        if res == float('inf'):
            return -1
        return res
                
                