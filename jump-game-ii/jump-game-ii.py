class Solution:
    def recur(self,jumpIdx,steps):
        if jumpIdx >= len(self.nums)-1:
            return 0 
        if self.dp[jumpIdx] == None:
            min_ = 100
            for i in range(self.nums[jumpIdx],0,-1):
                min_ = min(self.recur(jumpIdx+i,steps)+1,min_)
            self.dp[jumpIdx] = min_
            return min_
        else:
            return self.dp[jumpIdx]
            
        return 0
    
    def jump(self, nums: List[int]) -> int:
        
        size = len(nums)
        def greedy():
            toReach,i = size-1,size-2
            greedy = [10000 for _ in range(size-1)] + [0]
            pathCount = 0

            while i>=0:

                if nums[i] != 0:
                    greedy[i] = 1+min(greedy[i+1:i+nums[i]+1])
                i-=1
        
        #return(greedy[0])
        self.nums = nums
        self.dp = [None]*(size+1)
        #print()
        def recur(idx):
            if idx>=size-1:
                return 0
            
            if self.dp[idx] == None:
                min_ = float('inf')
                for i in range(nums[idx],0,-1):
                    min_ = min(min_,recur(idx+i)+1)
                self.dp[idx] = min_
                return min_
            else:
                return self.dp[idx]
        
        #return self.recur(0,0)
        return recur(0)