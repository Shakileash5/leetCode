class Solution:
    def findNthDigit(self, n: int) -> int:
        
        def solutionOpt(n):
            if n <10:
                return n
            num = n - 10
            ones = num%2
            tows = num//2
            num = 10 + tows
            num = str(num)
            print(num)
            if ones == 0:
                return num[0]
            else:
                return num[1]
        x, y = 9, 1
        while n > x*y:
            n -= (x*y)
            x *= 10
            y += 1
        
        val = int(10**(y-1) + (n/y));
        n %= y
        if n == 0: return (val-1)%10
        return int(str(val)[n-1])
