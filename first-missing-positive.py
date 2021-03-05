# https://leetcode.com/problems/first-missing-positive/
# Problem Description

# Solution

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums.sort()
        size = len(nums)
        mini = 0
        gap = 0
        
        if size==0 or nums[0]>1:
            return 1
        
        for i in range(1,size):
            if nums[i-1]+1 != 0 and nums[i-1]+1 != nums[i]:
                print(nums[i-1]+1)
                if nums[i-1]+1 < 0 and nums[i]!=1:
                    return 1
                if nums[i-1]+1 < 0 and nums[i]!=1:
                    continue
                return nums[i-1]+1
        
        print("atlast")
        if nums[-1]<1:
            return 1
        return nums[-1]+1
            
#solution
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        size = len(nums)
        
        if size==0:
            return 1
        newset = set(nums)
        
        for i in range(1,size+1):
            if i not in newset:
                return i
        
        return size+1
        
            
            