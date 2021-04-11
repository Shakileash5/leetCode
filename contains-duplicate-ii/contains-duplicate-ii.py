class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hashMap = {}
        size = len(nums)
        
        for i in range(size):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
            else:
                idxI = hashMap[nums[i]]
                val = abs(idxI-i)
                if val<=k:
                    return True
                else:
                    hashMap[nums[i]] = i
        
        return False