class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxSum = 0
        maxProfit = 0
        size = len(prices)
        for i in range(size-1,0,-1):
            #maxVal = max(maxVal,prices[i])
            #tempProfit = maxVal - prices[i]
            #maxProfit = max(maxProfit,tempProfit)
            if prices[i]>prices[i-1]:
                maxSum += prices[i]-prices[i-1]
            
        return maxSum
            
            