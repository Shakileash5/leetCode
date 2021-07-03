class Solution:
    
    def robHouses(self,idx,nums,dp):
        #print("d",idx,nums)
        if idx>=len(nums):
            return 0
        if dp[idx] == None:
            dontRob = self.robHouses(idx+1,nums,dp)
            robNow = self.robHouses(idx+2,nums,dp) + nums[idx]
            dp[idx] = max(dontRob,robNow)
            return dp[idx]
        else:
            return dp[idx]
    def robSolver(self,nums):
        size = len(nums)
        dp = [None for i in range(size)]
        @cache
        def robHouse(idx,taken):
            if taken and idx==size-1:
                return 0
            if idx >= size:
                return 0
            if idx == 0:
                rob = robHouse(idx+2,1) + nums[idx]
                dontRob = robHouse(idx+1,taken)
            else:
                rob = robHouse(idx+2,taken) + nums[idx]
                dontRob = robHouse(idx+1,taken)
            return max(rob,dontRob)
        return robHouse(0,0)
    
    def solver(self,nums):
            
            @lru_cache(None)
            def dp(i):
                if(i == 0):
                    return nums[i]
                elif(i == 1):
                    return max(nums[0], nums[1])
                else:
                    return max(nums[i] + dp(i-2), dp(i-1))
                
            return dp(len(nums)-1)
        
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        
        #
        #dp = [None]*(size+1)
        #rob1StHouse = self.robHouses(2,nums[:-1],dp)
        #dontRob1stHouse = self.robHouses(1,nums,dp)
        
        #print(rob1StHouse,dontRob1stHouse)
        #return max(rob1StHouse,dontRob1stHouse)
        #return max(self.solver(nums[:-1]), self.solver(nums[1:])) 
        return self.robSolver(nums)