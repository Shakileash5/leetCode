class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from math import ceil 
        size = len(nums)
        nums.sort()
        breakPoint = ceil(size/2)
        lows = nums[:breakPoint][::-1]
        highs = nums[breakPoint:][::-1]
        print(lows,highs)
        nums.clear()
        for i in range(len(highs)):
            nums.append(lows[i])
            nums.append(highs[i])
        
        print(nums)
        #nums = res
        if len(lows)>len(highs):
            nums.append(lows[-1])
        return None
        