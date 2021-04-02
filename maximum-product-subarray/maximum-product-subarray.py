class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        size = len(nums)
        if size == 1:
            return nums[0]
        
        maxSoFar = -2**31
        maxEnding = 1
        
        for i in range(size):
            maxEnding = maxEnding*nums[i]
            if maxEnding>maxSoFar:
                maxSoFar = maxEnding
            if maxEnding == 0:
                maxEnding = 1
                
        maxTemp = maxSoFar
        maxEnding = 1
        for i in range(size-1,-1,-1):
            maxEnding = maxEnding*nums[i]
            
            if maxEnding>maxSoFar:
                maxSoFar = maxEnding
            if maxEnding == 0:
                maxEnding = 1
        
        return maxSoFar
                