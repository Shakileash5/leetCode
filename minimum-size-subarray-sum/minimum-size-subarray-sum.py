class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        start = -1
        end = -1
        size = len(nums)
        minSoFar = size+1
        
        def naiveSolution(minSoFar):
            for i in range(size):
                if nums[i]>=target:
                    return 1
                for j in range(i+1,size):
                    tempVal = sum(nums[i:j+1])
                    if tempVal>=target:
                        minSoFar = min(len(nums[i:j+1]),minSoFar)
            return minSoFar
        
        def twoPointer(minSoFar):
            for i in range(size):
                start = i
                end = size-1
                if nums[start] >= target:
                    return 1
                while start<end:
                    tempArr = nums[start:end+1]
                    tempSum = sum(tempArr)
                    if tempSum>=target:
                        #print(tempArr,tempSum)
                        minSoFar = min(minSoFar,len(tempArr))
                        end-=1
                    elif tempSum<target:
                        break
                    
            return minSoFar    
        
        def towPointerOpt(minSoFar,start,end,target):
            temp = []
            while start<size:
                tempArr = []
                tempSum = -1
                while end<size:
                    tempArr = nums[start:end+1]
                    tempSum = sum(tempArr)
                    if tempSum>=target:
                        break
                    end+=1
                #print("temp",tempArr,tempSum,"poi",start,end)
                while start<=end:
                    if tempSum>=target:
                        minSoFar = min(minSoFar,len(tempArr))
                    else:
                        break
                    if tempSum>target:
                        if nums[start]<nums[end]:
                            start+=1
                        else:
                            end-=1
                    else:
                        break
                    tempArr = nums[start:end+1]
                    tempSum = sum(tempArr)
                    #print(start,end)
                start+=1
            return minSoFar
        
        #minSoFar = naiveSolution(minSoFar)
        #print(minSoFar) 
        #minSoFar = twoPointer(minSoFar)
        minSoFar = towPointerOpt(minSoFar,0,0,target)
        print(minSoFar) 
        
        if minSoFar==(size+1):
            minSoFar = 0
        
        return minSoFar