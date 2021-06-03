class Solution:
    def backtrackTwo(self,idx,temp,n,sum_,res,k):
        if len(temp)==n:
            #print(temp,sum_)
            if sum_ == k:
                res.append(temp)
            return
        for i in range(idx,10):
            self.backtrackTwo(i+1,temp+[i],n,sum_+i,res,k)
        return
    
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
        
        #backtrack(1,[])
        #print(res)
        self.backtrackTwo(1,[],k,0,res,n)
        return res