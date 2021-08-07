class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        nums.sort()
        hashMap = {}
        res = set()
        
        def binarySearch(left,right,target):
            
            while(left<=right):
                mid = (left+right)//2
                
                if nums[mid] == target:
                    return mid
                if nums[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
            return -1
        
        #print(nums)
        for i in range(size):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1,size):
                target = 0 - (nums[i]+nums[j])
                idx = binarySearch(j+1,size-1,target)
                if idx == -1:
                    continue
                #print(idx,i,j,target)
                #if [nums[i],nums[j],nums[idx]] not in res:
                res.add((nums[i],nums[j],nums[idx]))
        return res
                