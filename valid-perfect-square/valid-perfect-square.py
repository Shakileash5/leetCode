class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        def binarySearch(left,right):
            if left>right:
                return False
            
            mid = (left+right)//2
            val = mid**2
            if  val == num:
                return True
            
            if val>num:
                return binarySearch(left,mid-1)
            elif val<num:
                return binarySearch(mid+1,right)
            
        return binarySearch(1,num)
        
                