class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        size = len(nums)
        self.count = 0
        
        @cache
        def recur(idx,tempSum):
            if idx>=(size):
                #print(tempSum)
                if tempSum == target:
                    #print("yes")
                    #self.count+=1
                    return 1
                return 0
            
            for i in range(idx,size):
                return recur(i+1,tempSum+nums[idx]) + recur(i+1,tempSum-nums[idx])
                
            
        
        self.count = recur(0,0)
        return self.count
            