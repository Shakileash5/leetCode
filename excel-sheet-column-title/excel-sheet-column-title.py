class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        def numToAlpha(nums)->str:
            return chr(nums+65)
        
        if columnNumber<=26:
            columnNumber-=1
            return numToAlpha(columnNumber)
        else:
            res = ''
            orginal = columnNumber
            while(columnNumber>0):
                columnNumber -=1
                rem = columnNumber%26
                res += numToAlpha(rem)
                columnNumber //= 26
            return res[::-1]
            
            