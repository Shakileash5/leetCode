import bisect
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        size = len(nums)
        
        flag = 0
        
        stageOne = 0
        stageTwo = 0
        
        stack = []
        
        def twoPointers():
            min1 = 2**31 - 1
            min2 = - 2**31 - 1
            start = -1
            left = -1
            for i in range(size):
                val = nums[i]
                if val<min1:
                    min1 = val
                    start = i
                elif min1<val and min2<val and start<i:
                    min2 = val
                    left = i
                elif min1<val<min2 and start<left<i:
                    #print(min1,min2,val)
                    return True
            return False
        k = float('-inf')
        for i in range(size-1,-1,-1):
            if nums[i]<k:
                return True
            while stack and stack[-1]<nums[i]:
                k = stack.pop()
            stack.append(nums[i])
            
        return False
            