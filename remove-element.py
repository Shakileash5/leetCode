# https://leetcode.com/problems/remove-element/
# Problem Description

# Solution
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0 
        secondPointer = 0
        index = 0
        size = len(nums)
        for i in range(size):
            
            if nums[i] != val:
                nums[secondPointer] = nums[i]
                secondPointer+=1
            else:
                count+=1
        
        #print(nums,count)
        while count>0:
            nums.pop()
            count-=1
        return len(nums)