# https://leetcode.com/problems/trapping-rain-water/
# Problem Description

# Solution
class Solution:
    def trap(self, height: List[int]) -> int:
        res = []
        maxLevel = 0
        size = len(height)
        left = 0
        right = size-1
        leftMax = -1
        rightMax = -1
        #height.sort()
        while left<right:
            print(left,right)
            if rightMax==-1 or height[right]>height[rightMax]:
                    rightMax = right
                    print(rightMax,"right")
            if leftMax==-1 or height[left]>height[leftMax]:
                    leftMax = left
                    print(leftMax,"left")
            if height[left]>height[right] or height[left]==height[right]:
                right-=1
                
            else:# height[left]<height[right]:
                left+=1
        print(leftMax,rightMax,"res")        
        for i in range(leftMax+1,rightMax):
            maxLevel+=height[leftMax]-height[i]
            print(maxLevel,"here")
            
        return maxLevel

#Solution TestCases 233/320
class Solution:
    def trap(self, height: List[int]) -> int:
        res = []
        maxLevel = 0
        size = len(height)
        left = 0
        right = 0
        leftMax = -1
        rightMax = -1
        level = 0
        secondLevel = 0
        #height.sort()
        
        while left<size:
            flag=0
            secondLevel = -1
            level = 0
            #print(left,right,"lr")
            while right<size:
                
                level += height[left]-height[right]
                print(level,left,right,"level")
                right = right+1
                if right==size:
                    print("broke")
                    break
                if right>0 and height[right]>height[right-1]:
                    if secondLevel==-1 or height[secondLevel] <height[right]:
                        secondLevel = right
                    print("level two",secondLevel)
                if height[left]<=height[right]:
                    flag=1
                    #level+=height[left]
                    
                    break
            print(right,"h")
            if flag==1:
                maxLevel += level
                print("maxLevel",maxLevel)
                left = right
            else:
                print(left,"what??")
                level = 0
                if secondLevel!=-1:
                    for j in range(secondLevel-1,left,-1):
                        if height[secondLevel] == height[j] or height[secondLevel]<height[j]:
                            break
                        level+=height[secondLevel]- height[j]
                    maxLevel+=level
                    print("\nThe levl",level)
                    left = right
                else:        
                    left+=1
                    right = left
                
            
        return maxLevel

#Solution
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        ctr=0
        for i in range(1,len(height)-1):
            hmin = min(max(height[:i]), max(height[i+1:]))
            if hmin-height[i]>0:
                ctr+=hmin-height[i]
				
        return ctr