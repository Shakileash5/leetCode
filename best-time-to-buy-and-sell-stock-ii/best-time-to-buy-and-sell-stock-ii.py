class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        maxProfit = 0
        
        for i in range(size-1,0,-1):
            if prices[i]>prices[i-1]:
                maxProfit += prices[i]-prices[i-1]
        
        return maxProfit