class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        size = len(nums)
        maxSum = float("-inf")
        sum_0 = sum(nums)
        rollingSum = sum(i*val for i,val in enumerate(nums))
        
        for i in range(size):
            maxSum = max(maxSum,rollingSum)
            rollingSum += size*nums[i] - sum_0 
        
        return maxSum