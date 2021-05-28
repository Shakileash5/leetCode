class Solution:
    def localMaxMin(self,prices):
        maxProfit = 0
        buy = prices[0]
        size = len(prices)
        
        for i in range(1,size):
            if buy>prices[i]:
                buy = prices[i]
            else:
                maxProfit = max(maxProfit,prices[i]-buy)
        #print(maxProfit)
        return maxProfit
        
    def maxProfit(self, prices: List[int]) -> int:
        def recur(arr,idx,val,maxVal):
            if arr == []:
                return
            if len(arr) == 1:
                if val>arr[0]:
                    return -1
                else:
                    return arr[0]
                
            if arr[idx]>maxVal[0] and val<arr[idx]:
                maxVal[0] = arr[idx]
                
            if idx == len(arr)-1:
                #print("here",val,maxVal,arr)
                return maxVal[0]
            
            #print("iteration",idx)
            recur(arr,idx+1,val,maxVal)
            return maxVal[0]
        
        def solutionOne():
            size = len(prices)
            minVal = prices[0]
            maxProfit = -1
            for i in range(size):
                minVal = min(prices[i],minVal)
                tempProfit = prices[i] - minVal
                maxProfit = max(maxProfit,tempProfit)
            return maxProfit
        
        return self.localMaxMin(prices)
        