class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        numsCp = sorted(nums)
        size = len(nums)
        left = 0
        right = size-1
        count = 0
        #print(nums)
        #print(numsCp)
        while(left<right):
            if nums[left] == numsCp[left]:
                left+=1
            if nums[right] == numsCp[right]:
                right-=1
            if nums[left]!=numsCp[left] and nums[right] != numsCp[right]:
                #print(nums[left:right])
                return len(nums[left:right+1])
            
        return count