# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Problem Description

# Solution

class Solution:
    def binaryPivot(self,nums,left,right):
            mid = (left+right)//2
            print(left,right,mid,nums[mid])
            if left == right or left>right:
                if nums[left-1]<nums[left] and nums[left]>nums[left+1]:
                    return left
                
                return -1
            if  nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                print(mid)
                return mid
            if nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]:
                print(mid)
                return mid-1   
            if nums[left]<nums[mid] and nums[mid]>nums[right]:
                print("left")
                return self.binaryPivot(nums,mid+1,right)
            else :
                print("right")
                return self.binaryPivot(nums,left,mid-1)
            
    def binary(self,nums,left,right,target):
        mid = (left+right)//2
        if nums[mid] == target:
            print(mid,"mid")
            return mid
        if left == right:
            return -1
        if nums[mid]<target:
            return self.binary(nums,mid+1,right,target)
        else:
            return self.binary(nums,left,right-1,target)
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        pivot = 0
        flag= 0
        pivot = self.binaryPivot(nums,0,len(nums))
        print(pivot,nums[:pivot+1],nums[pivot+1:])
        if pivot == -1:
            pivot = len(nums)-1
            flag = 1
        if nums[0]<=target:
            print("indise 1st")
            idx = self.binary(nums[:pivot+1],0,len(nums[:pivot+1])-1,target)
        elif flag!=1:
            idx = self.binary(nums[pivot+1:],0,len(nums[pivot+1:])-1,target)
            print(idx)
            if idx == -1:
                return -1
            idx = idx+pivot+1
        else:
            return -1
        print(idx+pivot+1,idx,pivot)
        if idx == -1:
            return -1
        return idx

# optimised solution

class Solution:
    def binaryPivot(self,nums,left,right):
            mid = (left+right)//2
            print(left,right,mid,nums[mid])
            if left == right or left>right:
                if nums[left-1]<nums[left] and nums[left]>nums[left+1]:
                    return left
                
                return -1
            if  nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                print(mid)
                return mid
            if nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]:
                print(mid)
                return mid-1   
            if nums[left]<nums[mid] and nums[mid]>nums[right]:
                print("left")
                return self.binaryPivot(nums,mid+1,right)
            else :
                print("right")
                return self.binaryPivot(nums,left,mid-1)
            
    def binary(self,nums,left,right,target):
        mid = (left+right)//2
        if nums[mid] == target:
            print(mid,"mid")
            return mid
        if left == right:
            return -1
        if nums[mid]<target:
            return self.binary(nums,mid+1,right,target)
        else:
            return self.binary(nums,left,right-1,target)
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        pivot = 0
        flag= 0
        #pivot = self.binaryPivot(nums,0,len(nums))
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            
            if nums[mid] == target:
                return mid
            else:
                if nums[l] <= nums[mid]:
                    if target>nums[mid] or target<nums[l]:
                        l = mid+1
                    else:
                        r = mid-1
                else:
                    if target<nums[mid] or target>nums[r]:
                        r = mid -1
                    else:
                        l = mid+1
            
        return -1