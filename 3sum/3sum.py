class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        size = len(nums)
        res = []
        nums.sort()
        
        def binarySearch(arr,left,right,target):
            if left>right:
                return False
            mid = (left+right)//2
            
            if arr[mid] == target:
                return True
            if arr[mid]>target:
                return binarySearch(arr,left,mid-1,target)
            else:
                return binarySearch(arr,mid+1,right,target)
        #print(nums)
        for i in range(size):
            if i!=0  and nums[i]==nums[i-1]:
                continue 
            left = i+1
            right = size-1
            while left<right:
                #print(nums[i],nums[left],nums[right])
                toFind = nums[right] + nums[i] + nums[left]
                if toFind<0:
                    left+=1
                    continue
                elif toFind>0:
                    right-=1
                    continue
                
                pairs = [nums[i],nums[left],nums[right]]
                #print(pairs)
                if pairs not in res:
                    res.append(pairs)
                while left<right and nums[left] == pairs[1]:
                    left+=1
                while left<right and nums[right] == pairs[2]:
                    right-=1
                
                
                
        return res