class Solution:
    def binarySearch(self,left,right,target,nums) -> bool:
        if left>right:
            return False
        mid = (left + right)//2
        if nums[mid] == target:
            return True
        if nums[0]<=nums[mid]:
            if target>=nums[0] and target<nums[mid]:
                return self.binarySearch(left,mid-1,target,nums)
            elif target>=nums[0] and target>nums[mid]:
                return self.binarySearch(mid+1,right,target,nums)
            elif target<nums[0] and target<nums[mid]:
                return self.binarySearch(mid+1,right,target,nums)
        else:
            if target<=nums[-1] and nums[mid]<target:
                return self.binarySearch(mid+1,right,target,nums)
            elif target<=nums[-1] and nums[mid]>target:
                return self.binarySearch(left,mid-1,target,nums)
            elif target>num[-1] and target>nums[mid]:
                return self.binarySearch(left,mid-1,target,nums)
    
    def search(self, nums: List[int], target: int) -> bool:
        
        size = len(nums)
        nums.sort()
        def binary(target,left,right):
            mid = (left+right)//2
            print(left,right,mid)
            if nums[mid] == target:
                return True
            if left>right:
                return False
            else:
                if nums[left]<=nums[mid]:
                    if nums[left]>target or target>nums[mid]:
                        return binary(target,mid+1,right)
                    else:
                        return binary(target,left,mid-1)
                else:
                    if nums[right]<target or target<nums[mid]:
                        print("fr")
                        return binary(target,left,mid-1)
                    else:
                        print("frr")
                        return binary(target,mid+1,right)
        
        #return binary(target,0,size-1)
        return self.binarySearch(0,size-1,target,nums)