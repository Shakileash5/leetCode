class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        left = 0
        right = size - 1
        idx = 0
        
        while(idx<=right):
            if nums[idx] == 0:
                nums[idx],nums[left] = nums[left],nums[idx]
                left += 1
                idx += 1
            elif nums[idx] == 1:
                idx += 1
            else:
                nums[idx],nums[right] = nums[right],nums[idx]
                right -= 1
                #idx += 1
        
        return