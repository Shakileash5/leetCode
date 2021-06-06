class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        size = len(nums)
        sum_ = (size*(size+1))//2
        sumOrginal = 0
        for val in nums:
            sumOrginal += val
        
        return sum_ - sumOrginal