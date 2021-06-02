class Solution:
    def happyNumber(self,n):
        def sumOfSqDigits(num):
            res = 0
            while num:
                rem = num%10
                num//=10
                res+=rem*rem
            return res
        
        hardCp = n
        hashMap = {}
        while n!=1:
            hashMap[n] = 1
            n = sumOfSqDigits(n)
            if n in hashMap:
                return False
        if n == 1:
            return True
        return False
        
    def isHappy(self, n: int) -> bool:
        def sumOfSqDigits(num):
            sum = 0
            while(num>0):
                sum += (num%10)**2
                num //= 10
            return sum
        
        def solutionOne():
            num = n
            hashMap = {}
            while(num!=1):
                hashMap[num] = 1
                num = sumOfSqDigits(num)
                if num in hashMap:
                    return False
            return True
        
        return self.happyNumber(n)
        
        