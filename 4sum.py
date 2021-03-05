# https://leetcode.com/problems/4sum/
# Problem Description

# Solution
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        if nums==[]:
            return res
        nums = sorted(nums)
        size = len(nums)
        res = set()
        
        for i in range(size):
            #print("Iterate i",i)
            for j in range(size-1,i,-1):
                
                left = i+1
                right = j-1
                #print("iterate j",j)
                while left<right:
                    
                    sums = nums[i] + nums[left] + nums[right] + nums[j]
                    
                    #print(sums,i,left,right,j)
                    
                    if sums<target:
                        left +=1
                    elif sums>target:
                        right-=1
                    else:# 
                        
                        temp = [nums[i] , nums[left] , nums[right] , nums[j]]
                        if sums == target:
                            res.add(tuple(temp))
                        #print(sums)
                        while left<right and nums[left] == temp[1]:
                            left +=1
                        while left<right and nums[right] == temp[2]:
                            right-=1
        return res