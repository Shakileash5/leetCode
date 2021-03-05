# https://leetcode.com/problems/divide-two-integers/
# Problem Description

# Solution
# TestCase Passed 953/989
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==0 : return 0
        negative = 0
        count = 0
        if dividend<0 and divisor<0:
            dividend = abs(dividend)
            divisor = abs(divisor)
            negative = 0
        
        if dividend>(2**31 - 1):
            return (2**31 - 1)
        if divisor<-(2**31):
            return (2**31 - 1)
        
        
        elif dividend<0 or divisor<0:
            dividend = abs(dividend)
            divisor = abs(divisor)
            negative = 1
        
        
        
        temp = 0
        quotient = 0
        for i in range(31,-1,-1):
            if (temp+(divisor<<i))<=dividend:
                temp+=divisor<<i
                quotient |= 1<<i
                
        
        if negative:
            quotient = int("-" + str(quotient))
        if quotient==2147483648:quotient-=1
        print(quotient)
        return quotient


# Optimized Solution2
class Solution:
    def recur(self,dividendX,divisorY,n,divisor):
        
        if dividendX == 0 or dividendX<divisorY:
            return 0
        if dividendX-divisorY<divisor:
            return n
        
        if divisorY+divisorY > dividendX:
            return n + self.recur(dividendX-divisorY,divisor,1,divisor)
        else:
            return self.recur(dividendX,divisorY+divisorY,n+n,divisor)   
        
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==0 : return 0
        negative = 0
        count = 0
        if dividend<0 and divisor<0:
            dividend = abs(dividend)
            divisor = abs(divisor)
            negative = 0

        elif dividend<0 or divisor<0:
            dividend = abs(dividend)
            divisor = abs(divisor)
            negative = 1
        
        count = self.recur(dividend,divisor,1,divisor)  
        if negative:
            count = int("-" + str(count))
        if count==2147483648:count-=1
        return count
  
    