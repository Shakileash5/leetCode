# https://leetcode.com/problems/roman-to-integer/
# Problem Description

# Solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        size = len(nums)
        res = []
        if size == 0 or size == 1 or size == 2:
            return res
        
        for i in range(size):
            
            vI = nums[i]
            for j in range(size):
                if j == i:
                    continue
                vJ = nums[j]
                
                req = 0 - (vI + vJ)
                
                if req in nums:
                    index = nums.index(req)
                    if i != index and j != index:
                        leti = sorted([vI,vJ,req])
                        if leti not in res:
                            #print(i,j,index)
                            res.append(leti)
        print(res)
        return res

#Optimized
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        size = len(nums)
        res = []
        if size == 0 or size == 1 or size == 2:
            return res
        
        nums = sorted(nums)
        res = set()
        
        for i in range(size):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = size-1
            toGet = 0 - nums[i]
            while (left<right):
                
                sumT = nums[left] + nums[right]
                
                if toGet > sumT:
                    left+=1
                    continue
                elif toGet < sumT:
                    right -=1
                    continue
                temp = [nums[i],nums[left],nums[right]]
                
                res.add(tuple(temp))
                while left<right and nums[left] == temp[1]:
                    left+=1
                while left<right and nums[right] == temp[2]:
                    right-=1
        
        return res