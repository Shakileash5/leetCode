class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        size = len(nums)
        memo = [None for i in range(size+1)]
        
        def recur(idx,lastNum):
            if idx >= size:
                return 0
              
            moveSequence = recur(idx+1,lastNum)
            takeElement = 0
            if lastNum<nums[idx]:
                if memo[idx] == None:
                    memo[idx] = recur(idx+1,nums[idx]) + 1
                takeElement = memo[idx]
            return max(moveSequence,takeElement)
                
        return recur(0,float('-inf'))