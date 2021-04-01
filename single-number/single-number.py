class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        singleNumbers = set()
        hashNums = {}
        #for i in range(10):
        #    hashNums[i] = 0
        
        size = len(nums)
        
        for i in nums:
            keys = hashNums.keys()
            if i not in keys:
                singleNumbers.add(i)
                hashNums[i] = 1
            else:
                singleNumbers.remove(i)
        singleNumbers = list(singleNumbers)
        
        return singleNumbers[0]