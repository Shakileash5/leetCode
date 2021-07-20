class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = []
        def backtrack(left,right,temp):
            if left>=right:
                res.append(temp[:])
                return
            
            for i in range(left,right+1):
                temp[i],temp[left] = temp[left],temp[i]
                backtrack(left+1,right,temp)
                temp[i],temp[left] = temp[left],temp[i]
            return
        
        backtrack(0,size-1,nums[:])
        return res