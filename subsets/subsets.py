class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size =len(nums)
        
        def backtrack(idx,temp,res,n):
            if len(temp)==n:
                if temp not in res:
                    res.append(temp)
                return
            for i in range(idx,size):
                if nums[i] not in temp:
                    backtrack(i,temp+[nums[i]],res,n)
            return
        
        res = []
        for i in range(size+1):
            backtrack(0,[],res,i)
        #print(res)
        
        return res
        