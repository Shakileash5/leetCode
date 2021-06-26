import bisect
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = []
        stack = []
        for i in range(size-1,-1,-1):
            idx = bisect.bisect_left(stack,nums[i])
            res.append(idx)
            stack.insert(idx,nums[i])
            
        #print(stack,res)
        return res[::-1]
        