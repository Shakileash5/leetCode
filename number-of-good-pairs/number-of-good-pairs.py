class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        size = len(nums)
        hashMap = {}
        res = 0
        
        def nCr(n,r):
            f = math.factorial
            return f(n) // f(r) // f(n-r)
        
        for i in range(size):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = [i]
            else:
                hashMap[nums[i]].append(i)
        
        for key in hashMap:
            lengthOfNum = len(hashMap[key])
            if lengthOfNum > 1: 
                res += nCr(lengthOfNum ,2)
        
        return res