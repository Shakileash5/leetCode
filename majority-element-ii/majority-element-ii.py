class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = {}
        res = set()
        threshold = len(nums)//3
        
        for val in nums:
            count = 0
            if val not in hashMap:
                hashMap[val] = 1
                count = 1
            else:
                hashMap[val] += 1
                count = hashMap[val]
            if count>threshold:
                res.add(val)
        
        return res
            