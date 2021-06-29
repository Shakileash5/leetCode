class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        size = len(nums)
        idx = 0
        zeros = 0
        start = 0
        end = 0
        max_ = 0
        
        while(end<(size)):
            if nums[end] == 1:
                end += 1
                window = (end-start)
                max_ = max(max_,window)
            elif nums[end] == 0:
                if (zeros)>=k:
                    while(zeros>=k):
                        if nums[start] == 0:
                            zeros -= 1
                        start += 1
                    end += 1
                else:
                    end += 1
                window = (end-start)
                max_ = max(max_,window)
                zeros += 1
            
        return max_
                    
                    
                    
        