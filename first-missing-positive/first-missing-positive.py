class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        size = len(nums)
        
        if size==0:
            return 1
        newset = set(nums)
        
        def naive():
            for i in range(1,size+1):
                if i not in newset:
                    return i
        
        for i in range(size):
            idx = nums[i] - 1
            while idx>=0 and idx<size and nums[i] != nums[idx]:
                nums[i],nums[idx] = nums[idx],nums[i]
                idx = nums[i] - 1
        
        for i in range(size):
            if nums[i] != i+1:
                return i+1
        return size+1
        
            
            