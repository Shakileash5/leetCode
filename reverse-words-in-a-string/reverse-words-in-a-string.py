class Solution:
    def reverseWords(self, s: str) -> str:
        
        strReverse = s.strip()
        strReverse = strReverse.split(" ")
        #print(strReverse)
        strReverse = [x.strip() for x in strReverse]
        while('' in strReverse):
            strReverse.remove('')
        #print(strReverse)
        strReverse = strReverse[::-1]
        strReverse = " ".join(strReverse)
        return strReverse