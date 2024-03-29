class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        stack = []
        maxWater = 0
        
        left = 0
        right = size - 1
        
        while(left<right):
            area = min(height[left],height[right])*(right-left)
            maxWater = max(maxWater,area)
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        
        return maxWater