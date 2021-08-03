class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        size = len(nums)
        maxScore = 0
        
        # naive Approach
        # for i in range(k+1):
        #     for j in range(k,size):
        #         subArr = nums[i:j+1]
        #         score = min(subArr)*(j-i+1)
        #         maxScore = max(score,maxScore)
        mins = list(nums)
        for i in range(k-1,-1,-1):
            mins[i] = min(mins[i],mins[i+1])
        for i in range(k+1,size):
            mins[i] = min(mins[i],mins[i-1])
        
        left = 0
        right = size-1
        
        while(left<=k<=right):
            maxScore = max(maxScore,min(mins[left],mins[right])*(right-left+1))
            if mins[left]<=mins[right]:
                left += 1
            else:
                right -= 1
            
            
        return maxScore