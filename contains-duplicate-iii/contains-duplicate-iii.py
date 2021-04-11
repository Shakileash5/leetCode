class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        size = len(nums)
        hashMap = []
        for ind, num in enumerate(nums):
            hashMap.append([num,ind])
        hashMap = sorted(hashMap,key=lambda x: x[0])
        for i in range(len(hashMap)):
            for j in range(i+1,len(hashMap)):
                if abs(hashMap[i][0] - hashMap[j][0]) > t:
                    break
                elif abs(hashMap[i][1]-hashMap[j][1]) <= k:
                    return True
        return False
                
        
        