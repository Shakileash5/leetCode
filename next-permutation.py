# https://leetcode.com/problems/next-permutation/
# Problem Description

# Solution
class Solution:
    def nextMaxim(self,nums,ind,curr):
        index = 0
        maxi = -1
        
        for i in range(ind,len(nums)):
            if nums[i]>curr:
                if maxi == -1:
                    maxi = curr
                    index = i
                else:
                    maxi = min(nums[i],maxi)
                    index = i
        return index
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        flag = False
        while i>=0:
            
            if nums[i]<nums[i+1]:
                flag = True
                break
            i-=1
        
        if flag == False:
            nums.sort()
        
        else:
            m = self.nextMaxim(nums,i,nums[i])
            nums[i],nums[m] = nums[m],nums[i]
            nums[i+1:] = nums[i+1:][::-1]
        return             
        