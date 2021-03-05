# https://leetcode.com/problems/jump-game/
# Problem Description

# Solution Test-Cases 72/75
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxStep = -1
        i = 0
        size = len(nums)
        
        while i<size:
            
            maxStep = -1
            greedStep = -1
            steps = nums[i]
            
            for j in range(1,steps+1):
                
                if i+j>=size-1:
                    return True
                
                greedVal = nums[i+j]
                
                print("greed",greedVal,i,j)
                if greedVal>maxStep or (greedVal==maxStep and maxStep!=-1):
                    print("here")
                    maxStep = greedVal
                    greedStep = j
                    
            print(maxStep,"maxStep")
            if greedStep == -1:
                greedStep = 0
            if (maxStep == 0 and (i+greedStep)>=size-1) or( maxStep == -1 and (i+greedStep)>=size-1):
                return True
            if maxStep == 0 or maxStep == -1:
                return False
            
            
            i += greedStep
            
        return True    

#Optimised Solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        toReach,i = size-1,size-2
        
        while i>=0:
            if i+nums[i]>=toReach:
                toReach = i
            i-=1
            
        return toReach==0      
                
                
                
                
                
                