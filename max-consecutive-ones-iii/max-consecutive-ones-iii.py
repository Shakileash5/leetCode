class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        size = len(nums)
        countZeros = 0
        low = 0
        max_ = 0
        
        for high in range(size):
            if nums[high] == 0:
                countZeros += 1
            
            while(countZeros>k and low<=high):
                if nums[low] == 0:
                    countZeros -= 1
                low += 1
            
            max_ = max(max_,high-low+1)
        
        return max_