class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        start = 0 
        left = 0
        right = 0
        size = len(nums)
        min1 = min2 = 2**31 - 1
        def bruteForce(size,nums):
            for i in range(size):
                for j in range(i+1,size):
                    for k in range(j+1,size):
                        if nums[i] < nums[j] < nums[k]:
                            return True
            return False
    
        for i,val in enumerate(nums):
            if val<min1:
                min1 = val
                start = i
            if min1<val<min2 and start<i:
                min2 = val
                left = i
            if min1<min2<val and left<i:
                return True
        stack = []
        for i in range(size-1,-1,-1):
            
            while stack and stack[-1]<=nums[i]:
                stack.pop()
                
            stack.append(nums[i])
            if len(stack)>2:
                return True

        return False
                
                        