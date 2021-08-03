class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        maxArea = 0
        
        stack = []
        heights.append(0)
        for i in range(size+1):
            min_ = 100000
            while stack and heights[stack[-1]]>heights[i]:
                # Maintain monotonicity
                val = heights[stack.pop()]
                min_ = min(min_,val)
                length = i
                if stack != []:
                    length = i - stack[-1] -1
                maxArea = max(maxArea,min_*length)    
            
            stack.append(i)
        
        return maxArea
            