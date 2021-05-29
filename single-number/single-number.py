class Solution:
    def singleNumberTwo(self,nums):
        xor = nums[0]
        size = len(nums)
        for i in range(1,size):
            xor ^= nums[i]
        return(xor)
    
    def singleNumber(self, nums: List[int]) -> int:
        
        singleNumbers = set()
        hashNums = {}
        def naive():
            for i in nums:
                keys = hashNums.keys()
                if i not in keys:
                    singleNumbers.add(i)
                    hashNums[i] = 1
                else:
                    singleNumbers.remove(i)
            singleNumbers = list(singleNumbers)
        
        #return singleNumbers[0]
        return self.singleNumberTwo(nums)