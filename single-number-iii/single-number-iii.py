class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashMap = {}
        res = []
        size = len(nums)
        
        for i in range(size):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] += 1
        
        for key,val in hashMap.items():
            if val == 1:
                res.append(key)
        
        return res