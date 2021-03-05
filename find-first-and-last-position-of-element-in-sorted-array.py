# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Problem Description

# Solution

class Solution:
    def binary(self,nums,left,right,target):
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        if left>right:
            return -1
        if nums[mid]< target:
            return self.binary(nums,mid+1,right,target)
        else:
            return self.binary(nums,left,mid-1,target)
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        size = len(nums)
        if size==0:
            return [-1,-1] 
        index = self.binary(nums,0,size-1,target)
        
        print(index)
        
        leftIndex = -1
        rightIndex = -1
        
        if index!=-1:
            leftIndex = index-1
            while leftIndex>=0 and nums[leftIndex] == target:
                leftIndex-=1
                
            rightIndex = index+1
            while rightIndex<size and nums[rightIndex] == target:
                rightIndex+=1
            leftIndex+=1
            rightIndex-=1
            
        #print(leftIndex,rightIndex)
        
        return [leftIndex,rightIndex]