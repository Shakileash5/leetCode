class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSqDigits(num):
            sum = 0
            while(num>0):
                sum += (num%10)**2
                num //= 10
            return sum
        num = n
        hashMap = {}
        while(num!=1):
            hashMap[num] = 1
            num = sumOfSqDigits(num)
            if num in hashMap:
                return False
        return True
        
        