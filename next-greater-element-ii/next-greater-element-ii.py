class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        size = len(nums)
        
        stack = []
        res = [-1]*size
        
        for i in range(2*size-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[i%size]:
                stack.pop()
            if stack:
                res[i%size] = nums[stack[-1]]
            
            stack.append(i%size)
            
        #res = res[::-1]
        #print(res)
        #print(res1,stack)
        #stack = []        
        return res