# https://leetcode.com/problems/maximum-subarray/
# Problem Description

# Solution
# kaden's algorithm
# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = 0
        size = len(nums)
        start = 0
        end = 0
        max_so_far = -10**5 - 1
        
        for i in range(size):
            maxSum += nums[i]
            if maxSum>max_so_far:
                max_so_far = maxSum
            if maxSum <0:
                maxSum = 0
            
        
        print(max_so_far)
        return max_so_far
        