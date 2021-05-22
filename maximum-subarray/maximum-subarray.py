class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        """maxSum = 0
        size = len(nums)
        start = 0
        end = 0
        max_so_far = -10**5 - 1
        
        for i in range(size):
            maxSum += nums[i]
            if maxSum>max_so_far:
                max_so_far = maxSum
            if maxSum <0:
                maxSum = 0"""
        #return max_so_far    
        sumTill = 0
        maxSoFar = -10**5
        size = len(nums)
        
        for i in range(size):
            sumTill += nums[i]
            if sumTill>maxSoFar:
                maxSoFar = sumTill
            if sumTill<0:
                sumTill = 0
        
        
        #print(maxSoFar)
        return maxSoFar
        