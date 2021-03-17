class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = []
        
        def checkSubSet(res,arr):
            #for i in range(len(res)):
            #    if len(res[i]) == len(arr) and res[i] != arr:
            #        for j in range(len(res[i])):
            #            if 
            return
        def backtrack(temp,idx,n,idxArr):
            if len(temp)==n:
                temp.sort()
                if temp not in res:
                    #print(idxArr)
                    res.append(temp)
                    return

            for i in range(idx,size):
                idxArr.append(i)
                backtrack(temp+[nums[i]],i+1,n,idxArr)
                idxArr.pop()
            return 
        
        for i in range(0,size+1):
            backtrack ([],0,i,[])
            
        #backtrack([],0,1)
        #print(res)
        return res