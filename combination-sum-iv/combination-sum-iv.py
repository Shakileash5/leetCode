class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        size = len(nums)
        count = [0]
        @functools.lru_cache(None)
        def backtrack(idx,temp):
            if temp==target:
                #print("yes",temp)
                count[0]+=1
                return 1
            res = 0
            for i in range(size):
                if temp+nums[i] <=target:
                    res+=backtrack(i,temp+nums[i])
            #print(res,"hjk")
            return res
        
        
        return backtrack(0,0)