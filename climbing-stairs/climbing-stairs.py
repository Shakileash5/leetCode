class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        fib = [0]*n
        fib[0] = 1
        fib[1] = 2
        
        for i in range(2,n):
            fib[i] = fib[i-1] + fib[i-2]
            
        #print(fib)
        return fib[-1]
        