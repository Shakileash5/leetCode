class Solution:
    def mySqrt(self, x: int) -> int:
        
        def binary(num,left,right):
            mid = (left+right)//2
            midSq = mid**2
            midSqL = (mid-1)**2
            midSqR = (mid+1)**2
            #print(mid,midSq,midSqL,midSqR,"left",left,right)
            if midSq==num or midSq<num and midSqR>num:
                return mid
            if midSqL<num and midSq>num:
                return mid-1
            
            if midSq>num:
                return binary(num,left,mid-1)
            else:
                return binary(num,mid+1,right)
        
        if x==1:
            return 1
        
        res = binary(x,0,x//2)
        #print(res)
        return res