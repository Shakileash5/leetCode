class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(num,temp,size):
            if size == k:
                res.append(temp)
                return
            if num>n:
                return
            
            for i in range(num,n+1):
                backtrack(i+1,temp+[i],size+1)
            return
        
        backtrack(1,[],0)
        return res
            