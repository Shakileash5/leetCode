class Solution:
    def combinationWithDP(self,nums,target):
        size = len(nums)
        dp = [None for i in range(target+1)]
        
        def recur(sum_):
            if sum_ == target:
                return 1
            if dp[sum_] == None:
                res = 0
                for i in range(size):
                    if sum_+nums[i]<=target:
                        val = recur(sum_+nums[i]) 
                        if val>0:
                            res += val
                dp[sum_] = res
                return dp[sum_]
            else:
                return dp[sum_]
            
        return recur(0)
    
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        size = len(nums)
        count = [0]
        @lru_cache(None)
        def backtrack(idx,temp):
            if temp==target:
                #print("yes",temp)
                count[0]+=1
                return 1
            res = 0
            for i in range(size):
                if temp+nums[i] <=target:
                    #print(temp,nums[i])
                    res+=backtrack(i,temp+nums[i])
                    #print(res,"here")
            #print(res,"hjk")
            return res
        
        
        return self.combinationWithDP(nums,target)