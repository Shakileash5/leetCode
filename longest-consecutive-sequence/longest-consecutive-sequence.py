class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = {}
        res = 0
        
        for n in nums:
            hashMap[n] = 1
        
        for key in hashMap:
            count = 0
            if key-1 not in hashMap:
                val = key
                while val in hashMap:
                    count += 1
                    val += 1
                res = max(res,count)
        return res