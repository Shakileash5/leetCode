class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def recur(n):
            if n<=1:
                return 1
            res = 0
            for i in range(n):
                res+= recur(i)*recur(n-i-1)
            
            return res
        #fact = factorial(n)
        re = recur(n)
        #print(re,fact)
        #unique = recur(n)//factorial(n)
        return re