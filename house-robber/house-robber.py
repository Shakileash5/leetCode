class Solution:
    
    def recur(self,nums,idx,dp):
        if idx >= len(nums):
            return 0
        
        if dp[idx] == None:
            dontRob = self.recur(nums,idx+1,dp)
            robHouse = self.recur(nums,idx+2,dp) + nums[idx]
            dp[idx] = max(dontRob,robHouse)
        
        return dp[idx]
    
    def rob(self, nums: List[int]) -> int:
        dp = [None]*(len(nums))
        return self.recur(nums,0,dp)