class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        res = []
        for i in range(size):
            idx = abs(nums[i])-1
            
            if nums[idx]>0:
                nums[idx] = -nums[idx]
            else:
                res.append(idx+1)

        return res                