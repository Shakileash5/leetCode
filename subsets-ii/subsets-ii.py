class Solution:
    def backtrack(self,idx,temp,res,nums):
        if idx>=len(nums):
            temp.sort()
            if temp not in res:
                res.append(temp)
            return
        
        #self.backtrack(idx+1,temp,res,nums)
        for i in range(idx,len(nums)):
            self.backtrack(i+1,temp,res,nums)
            self.backtrack(i+1,temp+[nums[idx]],res,nums)
        return
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = []
        def backtrack(temp,idx,n):
            if len(temp)==n:
                temp.sort()
                if temp not in res:
                    #print(idxArr)
                    res.append(temp)
                    return

            for i in range(idx,size):
                backtrack(temp+[nums[i]],i+1,n)
            return 
        
        #for i in range(0,size+1):
        #    backtrack ([],0,i)
            
        #backtrack([],0,1)
        #print(res)
        #for i in range(0,size+1):
        self.backtrack(0,[],res,nums)
        return res