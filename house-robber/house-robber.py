class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [None]*(size+3)
        if size == 1:
            return nums[0]
        #@LruCache
        def recur(temp,idx):
            if idx>=size:
                sum = 0
                #print(temp)
                for i in temp:
                    if isinstance(i,int):
                        sum+=i
                    else:
                        if len(i)!=0:
                            sum+=i[0]
                #print(sum,dp)
                recur.maxi = max(recur.maxi,sum)
                
                return recur.maxi
            #if idx+2<size:
            #print("here",temp,[nums[idx+2:idx+1]])
            #if dp[idx+2]:
            #    return dp[idx+2]
            #else:
            dp[idx+2] =  recur(temp+[nums[idx+2:idx+3]],idx+2)
            #if idx+3<size:
            #if dp[idx+3]:
            #    return dp[idx+3]
            #else:
            dp[idx+3] = recur(temp+[nums[idx+3:idx+4]],idx+3)
            #print(dp)
        
        recur.maxi = -1
        #recur([nums[0]],0)
        #recur([nums[1]],1)
        
        res = nums.copy()
        res.extend([0,0,0])
        for i in range(size-1,-1,-1):
            res[i] = res[i]+max(res[i+2],res[i+3])
        
        #print(house1,house2)
        return max(res[0],res[1])