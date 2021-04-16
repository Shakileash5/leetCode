class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashMap = {}
        twoElements = set()
        
        for i in nums:
            if i not in hashMap:
                twoElements.add(i)
                hashMap[i] = 1
            else:
                twoElements.remove(i)
                hashMap[i]+=1
        
        return list(twoElements)