class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(idx,temp,res):
            if len(temp)==k:
                if temp not in res:
                    res.append(temp)
                return
            for i in range(idx,n+1):
                if i not in temp:
                    backtrack(i,temp+[i],res)
            
            return 
        res = []
        backtrack(1,[],res)
        return res
        