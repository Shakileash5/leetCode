class Solution:
    def localMaxMin(self,prices):
        maxProfit = 0
        sell = prices[-1]
        size = len(prices)
        for i in range(size-1,0,-1):
            if prices[i]>prices[i-1]:
                maxProfit += prices[i]-prices[i-1]
        return maxProfit
    
    def maxProfit(self, prices: List[int]) -> int:
        
        """maxSum = 0
        size = len(prices)
        for i in range(size-1,0,-1):
            if prices[i]>prices[i-1]:
                maxSum += prices[i]-prices[i-1]
            
        return maxSum"""
        return self.localMaxMin(prices)
            
            