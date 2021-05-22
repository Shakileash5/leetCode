class Solution:
    @cache
    def recur(self,jumpIdx,steps):
        #print(jumpIdx)
        if jumpIdx >= len(self.nums)-1:
            #print(steps)
            return 0 
        #if self.dp[jumpIdx] == None:
        min_ = 100
        for i in range(self.nums[jumpIdx],0,-1):
                #print(jumpIdx,jumpIdx+i)
            min_ = min(self.recur(jumpIdx+i,steps)+1,min_)
            #self.dp[jumpIdx]
        return min_
        #else:
        #    return self.dp[jumpIdx]
            
        return 0
    
    def jump(self, nums: List[int]) -> int:
        
        size = len(nums)
        """toReach,i = size-1,size-2
        greedy = [10000 for _ in range(size-1)] + [0]
        pathCount = 0
        
        while i>=0:
            
            if nums[i] != 0:
                greedy[i] = 1+min(greedy[i+1:i+nums[i]+1])
            i-=1"""
        
        #return(greedy[0])
        self.nums = nums
        self.dp = [None]*(size+1)
        #print()
        return self.recur(0,0)