class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        if nums==[]:
            return res
        nums = sorted(nums)
        size = len(nums)
        res = set()
        
        for i in range(size):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,size):
                left = j+1
                right = size-1
                while(left<right):
                    pairs = [nums[i],nums[j],nums[left],nums[right]]
                    sum_ = sum(pairs)
                    if sum_<target:
                        left+=1
                        while left<right and nums[left] == pairs[2]:
                            left+=1
                    elif sum_>target:
                        right-=1
                        while left<right and nums[right] == pairs[3]:
                            right-=1
                    else:
                        res.add(tuple(pairs))
                        while left<right and nums[left] == pairs[2]:
                            left+=1
                        while left<right and nums[right] == pairs[3]:
                            right-=1
                        
        
        return res