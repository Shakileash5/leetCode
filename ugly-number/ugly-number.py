class Solution:
    def isUgly(self, n: int) -> bool:
        flag = 0
        
        while(n!=1):
            if n == 0:
                return False
            if n%2 == 0:
                n//=2
                continue
            elif n%3== 0:
                n//=3
                continue
            elif n%5 == 0:
                n//=5
                continue
            flag = 1
            break
        
        if flag == 0:
            return True
        return False