class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashMap = {}
        hashMap[0] = 1
        sum_ = 0
        count = 0
        
        for val in nums:
            sum_ += val
            if sum_ - goal in hashMap:
                count += hashMap[sum_-goal]
            hashMap[sum_] = hashMap.get(sum_,0)+1
        
        return count