class Solution:
    def SolutionTwo(self,nums,k):
        size = len(nums)
        hashMap = {}
        for i in range(size):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
            else:
                j = hashMap[nums[i]]
                val = abs(i-j)
                if val<=k:
                    return True
                hashMap[nums[i]] = i
        return False
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        def solutionOne():
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
        
        return self.SolutionTwo(nums,k) 