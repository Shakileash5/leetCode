class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n <= 0 :
            return False
        highestVal = 3**19
        div = highestVal/n
        
        if int(div) == div:
            return True
        return False
        