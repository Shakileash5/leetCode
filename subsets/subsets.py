class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = []
        
        def backtrack(idx,temp):
            if idx>=size:
                res.append(temp)
                return 
            
            backtrack(idx+1,temp)
            backtrack(idx+1,temp+[nums[idx]])
            return
        
        backtrack(0,[])
        return res