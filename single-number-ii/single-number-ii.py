class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        singleNumbers = set()
        hashNums = {}
        
        for i in nums:
            keys = hashNums.keys()
            if i not in keys:
                singleNumbers.add(i)
                hashNums[i] = 1
            elif i in keys:
                if i in singleNumbers:
                    singleNumbers.remove(i)
        singleNumbers = list(singleNumbers)
        
        return singleNumbers[0]