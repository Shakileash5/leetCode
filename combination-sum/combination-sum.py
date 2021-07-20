class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        res = []
        
        def getCombinations(idx,sum_,temp):
            if sum_ == target:
                res.append(temp)
                return
            if idx>=size:
                return
            
            for i in range(idx,size):
                if sum_+candidates[i]<=target:
                    getCombinations(i,sum_+candidates[i],temp+[candidates[i]])
            return
        
        getCombinations(0,0,[])
        return res