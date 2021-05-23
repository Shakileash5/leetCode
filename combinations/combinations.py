class Solution:
    
    def combinations(self,idx,temp,res,n,k):
        if len(temp) == k:
            if temp not in res:
                res.append(temp)
            return
        for i in range(idx,n+1):
            self.combinations(i+1,temp+[i],res,n,k)
        return
    
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
        #backtrack(1,[],res)
        self.combinations(1,[],res,n,k)
        return res
        