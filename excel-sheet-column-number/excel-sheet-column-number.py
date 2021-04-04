class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        ans = 0
        count = 1
        
        for i in columnTitle[::-1]:
            
            ans += (ord(i)-64)*count
            count = count*26
            
            #print(i,ans)
        #print(ans)
        return ans 