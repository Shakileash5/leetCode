class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        orginal = nums[:]
        nums.sort()
        
        def binarySearch(arr,left,right,toFind):
            if left>right:
                return -1
            
            mid = (left+right)//2
            
            if arr[mid] == toFind:
                return mid
            if arr[mid]>toFind:
                return binarySearch(arr,left,mid-1,toFind)
            else:
                return binarySearch(arr,mid+1,right,toFind)
        #print(nums,orginal)
        for i in range(size):
            subArr = nums[i+1:]
            toFind = target - nums[i]
            res = binarySearch(subArr,0,size-i-2,toFind)
            #print(toFind,subArr,i,res,nums[i])
            if res != -1:
                res = res+i+1
                #print(res,"res")
                if nums[i] == nums[res]:
                    idx1 = orginal.index(nums[i])
                    idx2 = orginal[idx1+1:].index(nums[i]) + idx1 + 1
                    #print(orginal[idx1+1:].index(nums[i]),orginal[idx1+1:])
                    return [idx1,idx2]
                return [orginal.index(nums[i]),orginal.index(nums[res])]
        return [-1,-1]
    