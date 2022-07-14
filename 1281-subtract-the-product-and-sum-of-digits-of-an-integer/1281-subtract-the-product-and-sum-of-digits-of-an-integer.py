class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        productOfDigits = 1
        sumOfDigits = 0
        count = 0
        while(n>0):
            count += 1
            lastDigit = n%10
            productOfDigits *= lastDigit
            sumOfDigits += lastDigit
            n = n//10
        
        return productOfDigits - sumOfDigits