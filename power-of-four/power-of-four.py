class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        tempSafe = n
        if n<1:
            return False
        while(n>1):
            #print(n)
            if n%4 == 0:
                n/=4
            else:
                return False
        
        return True
            