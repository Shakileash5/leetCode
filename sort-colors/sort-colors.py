class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #nums.sort()
        colors = [0,0,0]
        size = len(nums)
        
        for i in range(size):
            if nums[i] == 0:
                colors[0]+=1
            if nums[i] == 1:
                colors[1]+=1
            if nums[i] == 2:
                colors[2]+=1
        idx = 0
        for i in range(3):
            for j in range(colors[i]):
                nums[idx] = i
                idx+=1
        #print(colors,nums)
        return
                
        