# https://leetcode.com/problems/combination-sum-ii/
# Problem Description

# Solution
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        size = len(candidates)
        res = []
        
        def backtrack(i,candidates,temp,res):
            for j in range(i,size):
                if sum(temp)<target:
                    if i>j and candidates[i] == candidates[i-1]:
                        continue
                    temp.append(candidates[j])
                    backtrack(j+1,candidates,temp,res)
                    if sum(temp) == target:
                        #t = sorted(temp)
                        if temp not in res:    
                            res.append(sorted(temp[:]))
                    temp.pop()
        candidates.sort()
        backtrack(0,candidates,[],res)
        return res
                

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        size = len(candidates)
        res = []
        
        def backtrack(i,sumList,temp):
            if sumList> target:
                return
            if sumList == target:
                        #t = sorted(temp)
                        if temp not in res:    
                            res.append(sorted(temp[:]))
                        return
            for j in range(i,size):
                
                    if j>i and candidates[j] == candidates[j-1]:
                        continue
                    #temp.append(candidates[j])
                    backtrack(j+1,sumList+candidates[j],temp+[candidates[j]])
                    #temp.pop()
        candidates.sort()
        backtrack(0,0,[])
        return res
                
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        size = len(candidates)
        res = []
        
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
        candidates.sort()
        backtrack(0,[])
        return res
                
        