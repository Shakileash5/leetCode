class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        size = len(nums)
        hashMap = {}
        
        for i in range(size):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] += 1
        
        for key in hashMap:
            if hashMap[key] == size//2:
                return key
        
        return -1