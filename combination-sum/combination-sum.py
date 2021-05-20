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
        
        def backtrackSolTwo(idx,sum_,temp):
            if sum_ == 0:
                if temp not in res:
                    res.append(temp)
                #print(temp)
                return
            for i in range(idx,size):
                if sum_ - candidates[i] >= 0:
                    backtrackSolTwo(i,sum_-candidates[i],temp+[candidates[i]])
            return
        
        
        #backtrack(0,candidates,res,[])
        #backtrackRewind(0,[])
        backtrackSolTwo(0,target,[])
        #print(res)
        return res