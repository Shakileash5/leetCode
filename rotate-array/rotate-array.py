class Solution:
    def rotateTwo(self,nums,k):
        def reverse(arr,left,right):
            while left<right:
                arr[left],arr[right] = arr[right],arr[left]
                left+=1
                right-=1
            return
        size = len(nums)
        k = k%size
        reverse(nums,0,size-1)
        reverse(nums,0,k-1)
        reverse(nums,k,size-1)
        return
        
        
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverseArray(arr,start,end):
            while(start<end):
                arr[start],arr[end] = arr[end],arr[start]
                start+=1
                end-=1
            return
        
        def rotateOne():
            size = len(nums)
            k = k%size

            reverseArray(nums,0,size-1)
            reverseArray(nums,0,k-1)
            reverseArray(nums,k,size-1)
        
        self.rotateTwo(nums,k)
        return
