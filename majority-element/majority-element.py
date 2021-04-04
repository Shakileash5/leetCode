class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        rejected = {}
        
        size = len(nums)
        
        for i in range(size):
            if nums[i] not in rejected.keys():
                count = nums.count(nums[i])
                if count>(size//2):
                    return nums[i]
                else:
                    rejected[nums[i]] = True
                
        
        return 0
                    