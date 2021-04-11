class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        size = 9
        res = []
        
        def backtrack(idx,temp):
            
            if len(temp)>=k:
                sumTemp = sum(temp)        
                if sumTemp==n:
                    res.append(temp)
        
                return
            
            for i in range(idx,size+1):
                backtrack(i+1,temp+[i])
            
            return
        
        backtrack(1,[])
        #print(res)
        
        return res