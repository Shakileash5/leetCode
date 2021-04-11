class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        res = []
        
        def backtrack(i,candidates,res,tem=[]):
            for j in range(i,size):
                if sum(tem)<target:
                    tem.append(candidates[j])
                    backtrack(j,candidates,res,tem)
                    if sum(tem) == target:
                        res.append(tem[:])
                    tem.pop()
        
        def backtrackRewind(idx,temp):
            if sum(temp)>=target:
                if sum(temp) == target:
                    res.append(temp[:])
                return
            for i in range(idx,size):
                backtrackRewind(i,temp+[candidates[i]])
            
            return
        
        #backtrack(0,candidates,res,[])
        backtrackRewind(0,[])
        
        #print(res)
        return res