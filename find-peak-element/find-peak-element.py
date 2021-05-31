class Solution:
    def binarySearch(self,left,right,nums):
        mid = (left+right)//2
        
        if mid == 0 and nums[mid+1]<nums[mid]:
            return mid
        elif mid == len(nums)-1 and nums[mid-1]<nums[mid]:
            return mid
        
        if nums[mid-1]<nums[mid]>nums[mid+1]:
            return mid
        if nums[mid+1]>nums[mid]:
            return self.binarySearch(mid+1,right,nums)
        if nums[mid-1]>nums[mid]:
            return self.binarySearch(left,mid-1,nums)
    
    def findPeakElement(self, nums: List[int]) -> int:
        
        size = len(nums)
        if size == 1:
            return 0 
        if size <3:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        def naive():
            for i in range(0,size):
                if i == size-1:
                    if nums[i]>nums[i-1]:
                        return i
                if i == 0:
                    if nums[i]>nums[i+1]:
                        return i

                if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                    return i
            return -1
        
        return self.binarySearch(0,size-1,nums)