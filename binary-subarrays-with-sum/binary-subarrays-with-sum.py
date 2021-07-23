class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        size = len(nums)        
        count = 0
        hashMap = {}
        hashMap[0] = 1
        sum_ = 0
        for i in range(size):
            sum_ += nums[i]
            if sum_-goal in hashMap:
                count += hashMap[sum_-goal]
            hashMap[sum_] = hashMap.get(sum_,0) + 1
            #print(count,hashMap,sum_)
        
        return count
                