class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxDiff = 0
        size = len(nums)
        if size == 1:
            return 0
        #print(nums)
        for i in range(0,size-1):
            diff = nums[i+1]-nums[i]
            #print(diff,"diff",nums[i])
            if diff > maxDiff:
                #print(i)
                maxDiff = diff
        
        return maxDiff