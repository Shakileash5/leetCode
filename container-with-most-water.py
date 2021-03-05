# https://leetcode.com/problems/container-with-most-water/
# Problem Description

# Solution

#BruteForce
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxSum = 0
        size = len(height)        
        for i in range(size):
            for j in range(i+1,size):
                area = (j-i)*min(height[i],height[j])
                maxSum = max(area,maxSum)
        return maxSum

#Optimized
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxSum = 0
        leftHigh = 0
        rightHigh = len(height)-1
        while rightHigh>leftHigh:
            area = (rightHigh-leftHigh)*min(height[leftHigh],height[rightHigh])
            maxSum = max(area,maxSum)
            if height[leftHigh]>height[rightHigh]:
                rightHigh-=1
            else:
                leftHigh+=1
        return maxSum