class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        size = len(nums)
        left = size-2
        right = size-1
        
        def recur(idx,left,right):
            
            if idx>=size:
                if left and right and sum(left) == sum(right) and len(left)+len(right)==size:
                    print(left,right)
                    return True
                return
            
            for i in range(idx,size):
                if recur(i+1,left+[nums[i]],right):
                    return True
            
                if recur(i+1,left,right+[nums[i]]):
                    return True
       #res = recur(0,[],[])
        def solutionTwo():
            nums.sort()
            prefix = [nums[0]]
            for i in range(1,size):
                prefix.append((prefix[i-1]+nums[i]))

            prefixRev = [nums[size-1]]
            idx = 0
            for i in range(size-2,-1,-1):  
                prefixRev.append((prefixRev[idx]+nums[i]))
                idx+=1
            prefixRev = prefixRev[::-1]
            print(nums)
            print(prefix,prefixRev)
            for i in range(size):
                if (i+1)<size:
                    if prefix[i] == prefixRev[i+1]:
                        return True
                else:
                    return False
        
        s = sum(nums)
        if s&1:
            return False
        l = len(nums)
        s = s//2
        dp = [[False for _ in range(s+1)] for _ in range(l+1)]
        for i in range(l+1):
            for j in range(s+1):
                if j==0:
                    dp[i][j]=True
        for i in range(1,l+1):
            for j in range(1,s+1):
                if nums[i-1]<=j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
        
            