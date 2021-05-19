class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        size = len(nums)
        if size < 3:
            return res
        nums.sort()
        closest = 10000
        closestSum = 10000
        for i in range(size):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = size-1
            diff = 10000
            while(left<right):
                temp = [nums[i],nums[left],nums[right]]
                sum_ = sum(temp)
                diff = target - sum_
                if closest>abs(diff):
                    closestSum = sum_
                    closest = abs(diff)
                if sum_>target:
                    right-=1
                    while left<right and nums[right] == temp[2]:
                        right-=1
                elif sum_<target:
                    left+=1
                    while left<right and nums[left] == temp[1]:
                        left+=1
                else:
                    return target
                
                    
                
        
        
        print(closest,closestSum,target)             
        return closestSum
      