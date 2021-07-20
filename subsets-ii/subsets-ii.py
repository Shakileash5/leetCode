class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        size = len(nums)
        res = set()
        def backtrack(idx,temp):
            if idx>=size:
                temp.sort()
                res.add(tuple(temp))
                return
            
            backtrack(idx+1,temp)
            backtrack(idx+1,temp+[nums[idx]])
            return
        
        backtrack(0,[])
        return res