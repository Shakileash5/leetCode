class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 2
        size = len(nums)
        #startP = -1
        #endP = -1
        freeIndex = 0
        active = nums[0]
        
        for i in range(size):
            if nums[i]!=active:
                active = nums[i]
                count = 2
            if nums[i] == active:
                if count!=0:
                    nums[freeIndex] = nums[i]
                    freeIndex+=1
                    count-=1
                
        while len(nums) != freeIndex:
            nums.pop()
        
        return len(nums)
                
                    
        