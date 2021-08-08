class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        hashMap = {}
        hashMap[0] = 1
        sum_ = 0
        
        for val in nums:
            sum_ += val
            if sum_ - k in hashMap:
                count += hashMap[sum_-k]
            hashMap[sum_] = hashMap.get(sum_,0)+1
        
        return count
            