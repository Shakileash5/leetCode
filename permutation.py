# https://leetcode.com/problems/permutations/
# Problem Description

# Solution

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        temp = nums[:]
        size = len(nums)
        res = []
        
        def backtrack(temp,l,r):
            if l>=r:
                res.append(temp[:])
                #print(temp)
                #return
            else:
                for i in range(l,r+1):
                    temp[l],temp[i] = temp[i],temp[l]
                    backtrack(temp,l+1,r)
                    temp[l],temp[i] = temp[i],temp[l]
        
        backtrack(temp,0,size-1)
        #print(res)
        return res
            