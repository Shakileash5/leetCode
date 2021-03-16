class Solution:
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
        
        return binary(target,0,size-1)
        