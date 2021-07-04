class Solution:
    
    def recur(self,moveTo,n):
        if moveTo >= (n-1):
            #print("happadaw")
            return True
        if self.dp[moveTo] == None:
            for i in range(self.nums[moveTo],0,-1):
                if self.recur(moveTo+i,n):
                    self.dp[moveTo] = True
                    return True
                self.dp[moveTo+i] = False
        else:
            print("hit")
            return self.dp[moveTo]
        self.dp[moveTo] = False
        return False
        
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        moveTo,i = size-1,size-2
        self.nums = nums
        self.dp = [None]*(size+1)
        #while i>=0:
        #    if nums[i]+i >= moveTo:
        #        moveTo = i
        #    i -=1
        #print()
        #return toReach==0       
        #return self.recur(0,size)        
        
        def recur(idx):
            if idx>=size-1:
                return True
            if self.dp[idx] == None:
                for i in range(nums[idx],0,-1):
                    if recur(idx+i):
                        return True
                self.dp[idx] = False
                return False
            else:
                return False
        
        #print()
        moveTo = size-1
        i = size-2
        while i>=0:
            if nums[i]+i>=moveTo:
                moveTo = i
            i -= 1
        
        return moveTo == 0                
                