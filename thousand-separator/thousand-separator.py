class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        size = len(n)
        div = size//3
        div = div
        i = size-1
        count = 1
        while i>=0:
            if count==3 and i!=0 and div>0:
                n = n[:i]+'.'+n[i:]
                div-=1
                count = 0
            
            count+=1
            i-=1
        
        print( n)
        return n