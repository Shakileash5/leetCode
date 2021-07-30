class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = 0
        nums.sort(reverse= True)
        smallest = nums[0]
        
        for idx, val in enumerate(nums):
            if smallest > val:
                smallest = val
                count += idx
        
        return count