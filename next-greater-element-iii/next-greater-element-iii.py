class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        size = len(nums)
        
        for i in range(size-2,-1,-1):
            if nums[i]<nums[i+1]:
                for j in range(i+1,size):
                    if nums[i]>=nums[j]:
                        j -= 1
                        break
                nums[i],nums[j] = nums[j],nums[i]
                nums = nums[:i+1] + nums[i+1:][::-1]
                nums = int(''.join(nums))
                
                if nums<=2**31-1:
                    return nums
                break
        return -1
                    