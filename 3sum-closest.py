# https://leetcode.com/problems/3sum-closest/
# Problem Description

# Solution
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        size = len(nums)
        if size < 3:
            return res
        nums = sorted(nums)
        #print(nums)
        lastClose = nums[0] + nums[1] + nums[len(nums)-1]

        for i in range(size-2):
            left = i+1
            right = size-1
            
            print(i,"in T")
            while left<right:
                
                close = nums[left] + nums[right] + nums[i]
                
                print(close,left,right)
                
                #close = abs(target - sums)
                temp = [nums[i],nums[left],nums[right]]
                if abs(target - close)<abs(target - lastClose):
                    lastClose = close
                     
                if close<target :
                    left+=1
                    while left<right and nums[left] == nums[left-1]:
                        left+=1        
                elif close>target:
                    right-=1
                    while left<right and nums[right] == nums[right+1]:
                        right-=1
                else:
                    return target

        print(close,lastClose,target)             
        return lastClose
      

t = [-1,2,10,-4]
obj = Solution()
print(obj.threeSumClosest(t,1))