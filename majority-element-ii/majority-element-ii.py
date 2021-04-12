class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        rejected = {}
        
        size = len(nums)
        res = []
        threshold = size//3
        
        for i in nums:
            if i not in rejected.keys():
                count = nums.count(i)
                if count>threshold:
                    res.append(i)
                    #res.pop()
                rejected[i] = True
        
        return res
        