class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        res = []
        for i in range(0,len(nums)):
            idx = abs(nums[i])-1
            
            if nums[idx]>0:
                nums[idx] = - nums[idx]
                #print(idx,nums)
        #print(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res