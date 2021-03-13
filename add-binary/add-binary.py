class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ''
        
        sizeA = len(a)
        sizeB = len(b)
        
        if sizeB>sizeA:
            a,b = b,a
            sizeA,sizeB = sizeB,sizeA
        print(a,b,sizeB)
        tempA = a
        a = a[::-1]
        b = b[::-1]
        for i in range(sizeB):
            print(res)
            if a[i]=='0' and carry==0:
                print("oo")
                res = b[i]+res
            elif a[i]=='0' and carry==1:
                if b[i]=='1':
                    res = '0'+res
                    carry = 1
                else:
                    res = '1'+res
                    carry = 0
            elif a[i]=='1' and carry==0:
                if b[i]=='0':
                    res = '1'+res
                else:
                    res = '0'+res
                    carry = 1
            elif a[i]=='1' and carry==1:
                if b[i]=='0':
                    res = '0'+res
                    carry = 1
                else:
                    res = '1' + res
        print(res,"re",carry,i)
        
        if carry == 1 and i<sizeA:
            st = i
            for i in range(st+1,sizeA):
                print(i,a[i],res)
                if a[i]=='0' and carry==0:
                    print("lo",a[i:][::-1])
                    res=a[i:][::-1]+res
                    break
                elif a[i]=='1' and carry==1:
                    res = '0'+res
                    carry = 1
                elif a[i]=='1' and carry==0:
                    res = '1'+res
                elif a[i]=='0' and carry==1:
                    res = '1'+res
                    carry = 0
        
            print(res,"re",carry,i)
        elif sizeA>i and carry==0:
            res = a[i+1:][::-1]+res
            print("here",a[i+1:][::-1],a,i)
        
        if carry == 1:
            res = '1'+res
        
        print(res,"la")
        return res
                    
                