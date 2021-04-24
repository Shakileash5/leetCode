class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        monoStack = []
        maxRect = 0
        size = len(heights)
        heights.append(0)
        for i in range(size+1):
            count = 1
            minVal = 100000
            while monoStack and heights[i]<heights[monoStack[-1]]:
                val = heights[monoStack.pop()]
                minVal = min(val,minVal)
                if monoStack == []:
                    count = i
                else:
                    count = i - monoStack[-1]-1
                #print(val,count*val,count)
                maxRect = max(count*minVal,maxRect)
                #print(monoStack,"mono",minVal,count,count*minVal)
                count+=1
            monoStack.append(i)
            #print(monoStack,"out")
        #print("\n")
        
        return maxRect
        