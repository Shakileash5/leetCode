# https://leetcode.com/problems/two-sum/
# Problem Description

# Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            if (target-nums[i]) in nums[i+1:]:
                return [i,nums.index((target-nums[i]),i+1,n)]
        return [-1,-1]
        