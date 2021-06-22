class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        size = len(nums)
        res  = []
        def backtrack(idx,tempArr):
            if idx >= size:
                #print(tempArr)
                if len(tempArr)>=2 and tempArr not in res:
                    res.append(tempArr)
                return
            if tempArr == [] or tempArr[-1] <= nums[idx]:
                backtrack(idx+1,tempArr+[nums[idx]])
                backtrack(idx+1,tempArr)
            else:
                backtrack(idx+1,tempArr)
            
            return
        
        backtrack(0,[])
        return res