class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        max_ = 0
        buy = prices[0]
        
        for i in range(1,size):
            if prices[i]<buy:
                buy = prices[i]
            else:
                max_ = max(max_,prices[i]-buy)
        
        return max_