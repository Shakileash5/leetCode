# https://leetcode.com/problems/powx-n/
# Problem Description

# Solution TestCases 291/304
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        negative = 0
        res = 1
        
        if n<0:
            negative = 1
            n = abs(n)
        
        for i in range(1,n+1):
            res*=x
        
        if negative == 1:
            res = 1/res
        print(res)
        return res
    
        
#optimized solution
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def recur(x,n):
            if(n == 0):
                return 1
            if(n < 0):
                return 1/recur(x, -n)
            else:
                if n%2 == 0:
                    return recur(x*x,n/2)
                else:
                    return x*recur(x,n-1)
    
        res = recur(x,n)
        return res
    
    
        
            