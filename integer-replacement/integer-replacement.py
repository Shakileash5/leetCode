class Solution:
    def integerReplacement(self, n: int) -> int:
        def recur(n):
            
            if n==1:
                return 0
            
            if n%2 == 0:
                return recur(n//2)+1
            else:
                return 1+ min(recur(n+1),recur(n-1))
        
        self.count = float('inf')
        @cache
        def recur2(n,count):
            if n == 1:
                self.count = min(count,self.count)
                return
            if n%2==0:
                return recur2(n//2,count+1)
            else:
                recur2(n+1,count+1)
                recur2(n-1,count+1)
            return
            
        """ while n>1:
            if n%2 == 0:
                n = n//2
            else:
                n-=1
            count+=1"""
        #recur(n)
        recur2(n,0)
        return self.count