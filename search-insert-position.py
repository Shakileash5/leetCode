# https://leetcode.com/problems/search-insert-position/
# Problem Description

# Solution

class Solution:
    def binary(self,nums,left,right,target):
        mid = (left+right)//2
        if nums[mid] == target:
            return [mid]
        if left>right:
            return [-1,left,right]
        if nums[mid]< target:
            return self.binary(nums,mid+1,right,target)
        else:
            return self.binary(nums,left,mid-1,target)
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size==0:
            return [target] 
        index = self.binary(nums,0,size-1,target)
        #print(index)
        
        if index[0] != -1:
            return index[0]
        
        return index[1]
        
        