class Solution:
    def binaryPivot(self,nums,left,right):
            mid = (left+right)//2
            print(left,right,mid,nums[mid])
            if left == right or left>right:
                if nums[left-1]<nums[left] and nums[left]>nums[left+1]:
                    return left
                
                return -1
            if  nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                print(mid)
                return mid
            if nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]:
                print(mid)
                return mid-1   
            if nums[left]<nums[mid] and nums[mid]>nums[right]:
                print("left")
                return self.binaryPivot(nums,mid+1,right)
            else :
                print("right")
                return self.binaryPivot(nums,left,mid-1)
            
    def binary(self,nums,left,right,target):
        mid = (left+right)//2
        if nums[mid] == target:
            print(mid,"mid")
            return mid
        if left == right:
            return -1
        if nums[mid]<target:
            return self.binary(nums,mid+1,right,target)
        else:
            return self.binary(nums,left,right-1,target)
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        pivot = 0
        flag= 0
        #pivot = self.binaryPivot(nums,0,len(nums))
        l,r = 0,len(nums)-1
        leftEle = nums[0]
        rightEle = nums[r]
        if target>rightEle and target<leftEle:
            return -1
        
        while(l<=r):
            mid = (l+r)//2
            #print(l,r,mid)
            if nums[mid] == target:
                return mid
            else:
                if nums[mid]>=leftEle:
                    if target>=leftEle and target<nums[mid]:
                        r = mid-1
                    elif target>=leftEle and target>nums[mid]:
                        l = mid + 1
                    elif target<=rightEle:
                        l = mid+1
                elif nums[mid]<=rightEle:
                    if target<=rightEle and target>nums[mid]:
                        l = mid+1
                    elif target<=rightEle and target<nums[mid]:
                        r = mid - 1
                    elif target>=leftEle :
                        r = mid - 1
                else:
                    return -1
            
        return -1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """while l<=r:
            mid = (l+r)//2
            
            if nums[mid] == target:
                return mid
            else:
                if nums[l] <= nums[mid]:
                    if target>nums[mid] or target<nums[l]:
                        l = mid+1
                    else:
                        r = mid-1
                else:
                    if target<nums[mid] or target>nums[r]:
                        r = mid -1
                    else:
                        l = mid+1"""