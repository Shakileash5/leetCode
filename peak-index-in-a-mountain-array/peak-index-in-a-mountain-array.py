class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        size = len(arr)
        
        def binarySearch(left,right):
            mid = (left+right)//2
            #print(left,right,mid,arr[mid])
            if mid>0 and mid<(size-1) and arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            
            if mid<(size-1) and arr[mid+1]>arr[mid]:
                return binarySearch(mid+1,right)
            else:
                return binarySearch(left,mid-1)
        
        return binarySearch(0,size-1)