class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binaryPivot(nums,left,right):
            mid = (left+right)//2
            #print(left,right,mid,nums[mid])
            if left == right or left>right:
                if nums[left-1]<nums[left] and nums[left]>nums[left+1]:
                    return left
                
                return -1
            if  nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                #print(mid)
                return mid
            if nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]:
                #print(mid)
                return mid-1   
            if nums[left]<nums[mid] and nums[mid]>nums[right]:
                #print("left")
                return binaryPivot(nums,mid+1,right)
            else :
                #print("right")
                return binaryPivot(nums,left,mid-1)
        
        size = len(nums)
        
        pivot = binaryPivot(nums,0,size-1)
        #print("pivot",pivot)
        if pivot+1<size:
            if nums[pivot+1]<nums[pivot]:
                return nums[pivot+1]
        return nums[0]
        