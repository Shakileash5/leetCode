class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        size = len(prices)
        maxPrice = [-1]
        #dp = [None]*(size)
        
        @lru_cache(None)
        def recur(idx,buySell,temp,bought):
            if idx>(size-1):
                #print(temp,"sum")
                maxPrice[0] = max(maxPrice[-1],temp)
                return 
            
            for i in range(idx,size):
                if buySell == 0:
                    #print(i,prices[i],"buy")
                    recur(i+1,1,temp,prices[i])
                else:
                    if prices[i]>bought:
                        #print(i,prices[i],"sell")
                        recur(i+2,0,temp+(prices[i]-bought),0)
            return
        
        @lru_cache(None)
        def recur2(idx,buySell,bought):
            if idx>(size-1):
                return 0
            
            if buySell == 0:
                priceBoughtNow = recur2(idx+1,1,prices[idx])
                priceIfWaited = recur2(idx+1,0,0)
                return max(priceBoughtNow,priceIfWaited)
            else:
                priceSoldNow = prices[idx] - bought  + recur2(idx+2,0,0)
                priceWaited = recur2(idx+1,buySell,bought)
                return max(priceSoldNow,priceWaited)
            
        
        def recur3(idx,item,bought):
            if idx>=size:
                return 0
            if (idx,item,bought) not in dp:
                if bought == 0:
                    buyNow = recur3(idx+1,prices[idx],1)
                    dontBuy = recur3(idx+1,item,bought)
                    dp[(idx,item,bought)] = max(buyNow,dontBuy)
                    return dp[(idx,item,bought)]
                else:
                    sellNow = recur3(idx+2,None,0) + prices[idx] - item
                    dontSell = recur3(idx+1,item,bought)
                    dp[(idx,item,bought)] = max(sellNow,dontSell)
                    return dp[(idx,item,bought)]
            else:
                return dp[(idx,item,bought)]
        #recur(0,0,0,0)
        
        #print(max(dp))
        #print(maxPrice)
        
        #return recur2(0,0,0)
        dp = {}
        return recur3(0,None,0)