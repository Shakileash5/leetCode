class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        size = len(code)
        res = []
        trueK = k
        k = abs(k)
        for i in range(size):
            
            if trueK>0:
                if i+k<size:
                    res.append(sum(code[i+1:i+k+1]))
                else:
                    rem = size - (i + 1)
                    #print(rem)
                    rem = k - rem
                    #print(rem)
                    val = sum(code[i+1:])
                    #print(code[i+1:],code[:rem])
                    val += sum(code[:rem])
                    res.append(val)
            elif trueK<0:
                
                if (i-k)>=0:
                    res.append(sum(code[i-k:i]))
                else:
                    val = sum(code[:i])
                    rem = -(k - i)
                    val += sum(code[rem:])
                    res.append(val)
            else:
                res.append(0)
                
        return res