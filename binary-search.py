def binary(nums,left,right,target):
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        if left == right:
            return -1
        if nums[mid]<target:
            return binary(nums,mid+1,right,target)
        else:
            return binary(nums,left,right-1,target)


def binaryPivot(nums,left,right):
            mid = (left+right)//2
            print(left,right,mid,nums[mid])
            if left == right or left>right:
                if nums[left-1]<nums[left] and nums[left]>nums[left+1]:
                    return left
                if nums[right-1]<nums[right] and nums[right]>nums[right+1]:
                    return right
                return -1
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                print(mid)
                return mid
            if nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]:
                print(mid)
                return mid-1   
            if nums[left]<nums[mid] and nums[mid]>nums[right]:
                print("left")
                return binaryPivot(nums,mid+1,right)
            else :
                print("right")
                return binaryPivot(nums,left,mid-1)

print("output",binaryPivot([12,13,14,3,4,5,6,7,9,10,11],0,10))
#t = binaryPivot([12,13,14,3,4,5,6,7,9,10,11],0,10)
#print(binary([12,13,14,3,4,5,6,7,9,10,11][:t+1],0,t-1,10))
#print(binary([12,13,14,3,4,5,6,7,9,10,11][t+1:],0,8,10))