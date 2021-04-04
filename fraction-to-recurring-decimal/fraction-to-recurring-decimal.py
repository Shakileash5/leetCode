class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        N,D = numerator,denominator
        neg = True
        if (N < 0 and D < 0) or (N >= 0 and D >= 0): neg = False
        N = abs(N)
        D = abs(D)
        rem = N % D
        q = N // D
        res = [("-" if neg else "") + str(q)]                
        maps = {}        
        print(res,N,D,rem,q)
        if rem == 0:
            return str((-1 if neg else 1) * q)
        else:
            print(res,"start")
            res.append('.')
            while rem != 0:   
                print(res,"here",maps)
                if rem in maps:
                    res.append(')')
                    res.insert(maps[rem] , '(')
                    break;
                else:
                    maps[rem] = len(res)
                    rem *= 10
                    print(rem)
                    res.append(str(rem // D))
                    rem %= D
                    print(rem)
        return "".join(res)
        