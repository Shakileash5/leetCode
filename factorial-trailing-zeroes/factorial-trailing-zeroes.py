class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(num):
            if num ==0:
                return 1
            return num*(factorial(num-1))
        #print(factorial(n))
        count = 2
        ans = n//5
        while(n//5**count):
            ans += n//(5**count)
            count+=1
        return ans