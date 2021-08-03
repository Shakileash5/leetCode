class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if matrix==[]:
            return 0
        
        sizeRow = len(matrix)
        sizeCol = len(matrix[0])
        maxRect = 0
        barMap = [0]*(sizeCol+1)
        
        def getMaxArea(heights):
            maxArea = 0
            stack = []
            
            for i in range(sizeCol+1):
                min_ = 100000
                while stack and heights[stack[-1]]>heights[i]:
                    val = heights[stack.pop()]
                    min_ = min(min_,val)
                    length = i
                    if stack != []:
                        length = i - stack[-1] -1
                    maxArea = max(maxArea,length*min_)
            
                stack.append(i)
            
            return maxArea
        
        for i in range(sizeRow):
            for j in range(sizeCol):
                if matrix[i][j] == '1':
                    barMap[j] += 1
                else:
                    barMap[j] = 0
            maxRect = max(maxRect,getMaxArea(barMap))
        
        return maxRect
        
        
        