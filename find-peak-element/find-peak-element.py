class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        size = len(nums)
        if size == 1:
            return 0 
        if size <3:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        
        for i in range(0,size):
            print(i-1,i,i+1)
            if i == size-1:
                if nums[i]>nums[i-1]:
                    return i
            if i == 0:
                if nums[i]>nums[i+1]:
                    return i
                
            if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                return i
        return -1