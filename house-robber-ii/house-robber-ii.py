class Solution:
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
        def recur(temp,idx):
            if idx>=size-1:
                sum = 0
                for i in temp:
                    if len(i)!=0:
                        sum+=i[0]
                print("flag::: ",temp,idx,recur.mark,sum,idx!=size-1 )
                if recur.maxi<sum:
                    if idx == size-1 and recur.mark == 0:
                        print("true")
                    else:
                    #recur.mark = idx
                        recur.maxi = max(recur.maxi,sum)
                        print(recur.maxi)
                
                return
            
            
            recur(temp+[nums[idx+2:idx+3]],idx+2)
            recur(temp+[nums[idx+3:idx+4]],idx+3)
            return
        
        #recur.maxi = -1
        #recur.mark = 0
        #recur([[nums[0]]],0)
        #recur.mark = 1
        #recur([[nums[1]]],1)
        
        return max(self.solver(nums[:-1]), self.solver(nums[1:])) 