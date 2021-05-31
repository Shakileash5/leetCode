class Solution:
    def kadanesMagic(self,nums):
        maxEndingHere = 1
        maxSoFar = -2**10
        size = len(nums)
        for i in range(size):
            maxEndingHere *= nums[i]
            maxSoFar = max(maxSoFar,maxEndingHere)
            if maxEndingHere==0:
                maxEndingHere = 1
        
        maxEndingHere = 1
        for i in range(size-1,-1,-1):
            maxEndingHere *= nums[i]
            maxSoFar = max(maxSoFar,maxEndingHere)
            if maxEndingHere==0:
                maxEndingHere = 1
        
        return maxSoFar
    
    def maxProduct(self, nums: List[int]) -> int:
        
        def kadaneMagicUnknown():
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
        
        return self.kadanesMagic(nums)
                