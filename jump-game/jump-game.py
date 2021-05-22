class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        moveTo,i = size-1,size-2
        
        while i>=0:
            if nums[i]+i >= moveTo:
                moveTo = i
            i -=1
        
        #return toReach==0  
        return moveTo == 0       
                
                
                
                