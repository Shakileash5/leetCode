class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        size = len(candidates)
        self.res = set()
        
        def backtrack(i,temp):
            for j in range(i,size):
                if sum(temp)< target:
                    if j>i and candidates[j] == candidates[j-1]:
                        continue
                    temp.append(candidates[j])
                    backtrack(j+1,temp)
                    if sum(temp) == target:
                        if temp not in res:    
                            res.append(sorted(temp[:]))
                    temp.pop()
        
        def backtrackSolTwo(idx,sum_,temp):
            if sum_==0:
                #print(temp)
                temp.sort()
                self.res.add(tuple(temp))
                #print(self.res)
                #if temp not in self.res:
                #    self.res.append(temp)
                return
            for i in range(idx,size):
                if sum_ - candidates[i] >= 0:
                    if i>idx and candidates[i] == candidates[i-1]:
                        continue
                    backtrackSolTwo(i+1,sum_-candidates[i],temp+[candidates[i]])
            return
        candidates.sort()
        backtrackSolTwo(0,target,[])
        #
        #backtrack(0,[])
        return self.res
                
        