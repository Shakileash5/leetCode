class Solution:
    def maxArea(self, height: List[int]) -> int:
        """maxSum = 0
        leftHigh = 0
        rightHigh = len(height)-1
        while rightHigh>leftHigh:
            area = (rightHigh-leftHigh)*min(height[leftHigh],height[rightHigh])
            maxSum = max(area,maxSum)
            if height[leftHigh]>height[rightHigh]:
                rightHigh-=1
            else:
                leftHigh+=1"""
        
        maxSum = 0
        size = len(height)
        left = 0
        right = size-1
        
        while(left<right):
            area = (right-left)*min(height[left],height[right])
            maxSum = max(maxSum,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        
        return maxSum