class Solution:
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
        
        size = len(prices)
        maximum = -1
        #for i in range(size-1):
        #    val = recur(prices[i+1:],0,prices[i],[-1])
            #print(i,prices[i],val,prices[i+1:])
        #    if val !=-1:
        #        if (val - prices[i])>maximum:
        #            maximum = val - prices[i]
        #            print("min",maximum)
        #if maximum == -1:
        #    return 0
        
        minVal = prices[0]
        maxProfit = -1
        for i in range(size):
            minVal = min(prices[i],minVal)
            tempProfit = prices[i] - minVal
            maxProfit = max(maxProfit,tempProfit)
            
        return maxProfit