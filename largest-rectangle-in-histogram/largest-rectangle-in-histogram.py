class Solution:
    def solutionTwo(self,height):
        monotoneStack = []
        maxRect = 0
        size = len(height)
        height.append(0)
        for i in range(size+1):
            count = 1
            minVal = 10000
            while monotoneStack and height[i]<height[monotoneStack[-1]]:
                val = height[monotoneStack.pop()]
                min_ = min(val,minVal)
                if monotoneStack == []:
                    count = i
                else:
                    count = i - monotoneStack[-1] -1
                total = count*min_
                maxRect = max(maxRect,total)
                count+=1
                
            monotoneStack.append(i)
        return maxRect
                
                
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        def solOne():
            monoStack = []
            maxRect = 0
            size = len(heights)
            heights.append(0)
            for i in range(size+1):
                count = 1
                minVal = 100000
                print("gr",heights)
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
        
        return self.solutionTwo(heights)
        