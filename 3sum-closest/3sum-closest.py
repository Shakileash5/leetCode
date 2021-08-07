class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size<3:
            return -1
        
        closest = 10000
        closestSum = 10000
        nums.sort()
        res = 0
        #print(nums)
        for i in range(size):
            if i != 0 and nums[i]==nums[i-1]:
                continue
            #print("Fea",i)
            left = i + 1
            right = size - 1
            while(left<right):
                sum_ = nums[i]+nums[left]+nums[right]
                
                diff = abs(target-sum_)
                #print(sum_,i,left,right,diff)
                if diff<closest:
                    closest = diff
                    res = sum_
                if sum_>target:
                    te = nums[right]
                    right -= 1
                    while(left<right and nums[right]==te):
                        right -= 1
                elif sum_<target:
                    te = nums[left]
                    left += 1
                    #print('feie')
                    while(left<right and nums[left]==te):
                        left += 1
                else:
                    #print("Vr")
                    return target
                #print("Fe",left,right)
            #print("end")
        return res
                    