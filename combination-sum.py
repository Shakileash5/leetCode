# https://leetcode.com/problems/combination-sum/
# Problem Description

# Solution
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
        backtrack(0,candidates,res,[])
        
        #print(res)
        return res