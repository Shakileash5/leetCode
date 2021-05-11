class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        
        def recur(n):
            
            if n==1:
                return 0
            
            if n%2 == 0:
                return recur(n//2)+1
            else:
                return 1+ min(recur(n+1),recur(n-1))
        
        """ while n>1:
            if n%2 == 0:
                n = n//2
            else:
                n-=1
            count+=1"""
        return recur(n)