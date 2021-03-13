class Solution:
    def jump(self, nums: List[int]) -> int:
        
        size = len(nums)
        toReach,i = size-1,size-2
        greedy = [10000 for _ in range(size-1)] + [0]
        pathCount = 0
        print(greedy)
        while i>=0:
            print(greedy,greedy[i+1:i+nums[i]+1],i+1,i+nums[i]+1)
            if nums[i] != 0:
                greedy[i] = 1+min(greedy[i+1:i+nums[i]+1])
            i-=1
        
        return(greedy[0])
        