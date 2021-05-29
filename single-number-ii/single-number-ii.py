class Solution:
    def findDuplicates(self,nums):
        hashMap = {}
        for val in nums:
            if val not in hashMap:
                hashMap[val] = True
            else:
                hashMap[val] = False
        for key in hashMap.keys():
            if hashMap[key] == True:
                return key
        return -1
        
    def singleNumber(self, nums: List[int]) -> int:
        
        def naiveSol():
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
        
        return self.findDuplicates(nums)