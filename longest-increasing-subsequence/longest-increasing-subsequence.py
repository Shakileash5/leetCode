class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        size = len(nums)
        maxLength = [-1]
        dp = [1]*(size)
        
        @cache
        def dfsRecurWithCache(idx,temp):
            if idx <= (size-1):
                maxLength[0] = max(maxLength[0],len(temp)) 
                #return
            
            for i in range(idx+1,size):
                if nums[i]>int(temp[-1]):
                    dfsRecur(i,temp+str(nums[i]))
                if (i+1)<=(size-1) and nums[i+1]>int(temp[-1]):
                    dfsRecur(i+1,temp+str(nums[i+1]))
        
        
        def dfsRecur(idx,temp):
            #print(idx,size-1,idx<=(size-1),temp)
            if idx <= (size-1):
                #print(idx,temp,len(temp))
                maxLength[0] = max(maxLength[0],len(temp)) 
                #return
            
            for i in range(idx+1,size):
                #print(i,nums[i],nums[i+1],temp[-1],nums[i]>temp[-1])
                if nums[i]>temp[-1]:
                    #print("inside",i,temp+[nums[i]])
                    dfsRecur(i,temp+[nums[i]])
                    #print("returned")
                if (i+1)<=(size-1) and nums[i+1]>temp[-1]:
                    dfsRecur(i+1,temp+[nums[i+1]])
                
                #dp[i] = max(dp[i],len(temp))
                
            return
        
        #for i in range(size):
        #    dfsRecur(i,[nums[i]])
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,size):
                if nums[i]<nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
        
        #print(dp)
            
        return max(dp)