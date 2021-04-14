class Solution:
    def addDigits(self, num: int) -> int:
        
        def sumOfDigits(n):
            sumD = 0    
            while n!=0 :
                rem = n%10
                n //= 10
                sumD += rem
            
            return sumD
        
        numRes = num
        while numRes>=10:
            numRes = sumOfDigits(numRes)
        
        return numRes