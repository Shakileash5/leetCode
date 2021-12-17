class Solution:
    def majorityElementTwo(self,nums):
        hashMap = {}
        size = len(nums)
        threshold = size//2
        
        for i in range(size):
            hashMap[nums[i]] = hashMap.get(nums[i],0)+1
            if hashMap[nums[i]]>threshold:
                return nums[i]
        return 0
    
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        size = len(nums)
        res = (None,0)
        
        for i in range(size):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
                if res[1] < 1:
                    res = (nums[i],1)
            else:
                hashMap[nums[i]] += 1
                if res[1] < hashMap[nums[i]]:
                    res = (nums[i],hashMap[nums[i]])
        
        return res[0]
                    