class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        size = len(nums)
        nums.sort()
        
        for i in range(size):
            left = i + 1
            right = size - 1
            while(left<right):
                tempArr = (nums[i],nums[left],nums[right])
                tempSum = sum(tempArr)
                
                if tempSum < 0 :
                    left += 1
                    continue
                if tempSum > 0 : 
                    right -= 1;
                    continue
                
                if tempSum == 0:
                    res.add(tempArr)
                
                while left<right and nums[left] == tempArr[1]:
                    left += 1
                
                while left<right and nums[right] == tempArr[2]:
                    right -= 1
        
        return res
                    