class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        size = len(nums)
        min_ = 10000001
        left = 0
        right = size-1
        if size ==2:
            return 1
        partisions = []
        
        for i in range(size-1,-1,-1):
            if nums[i]<min_:
                min_ = nums[i]
                partisions.append(i+1)
        #print(partisions)
        for i in range(len(partisions)-1,-1,-1):
            if max(nums[:partisions[i]])<=min(nums[partisions[i]:]):
                return partisions[i]
        
        return partisions[i]