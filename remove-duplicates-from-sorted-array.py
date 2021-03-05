# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Problem Description

# Solution
#160/161 testCases
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count = 0
        size = len(nums)
        index = 0
        while(index<len(nums)):         
                if(index+1 <len(nums) and nums[index] == nums[index+1]):
                    idt = index
                    while(idt+1 <len(nums) and nums[idt] == nums[idt+1]):
                        idt +=1
                    passVal = idt - index
                    for i in range(index,len(nums)):
                        if i+passVal<len(nums):
                            nums[i] = nums[i+passVal]  
                    count += passVal
                    i = 0
                    while i<passVal:
                        #print(nums,"here")
                        nums.pop()
                        i+=1
                
                index+=1
                idt=0
        return len(nums)
                
#161/161 testCases
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count = 0
        size = len(nums)
        index = 0
        while(index<len(nums)):         
                if(index+1 <len(nums) and nums[index] == nums[index+1]):
                    idt = index
                    while(idt+1 <len(nums) and nums[idt] == nums[idt+1]):
                        del nums[idt]

                index+=1
                idt=0
        return len(nums)
                