class Solution:
    def minSteps(self, n: int) -> int:
        
        def recur(tempStr,buffer):
            if len(tempStr) == n:
                #print(tempStr)
                return 0
            elif len(tempStr)>n:
                return 1e9
            
            resCp = float('inf')
            res = float('inf')
            #print(tempStr)
            if len(buffer)<len(tempStr):     
                res = recur(tempStr+buffer,buffer) + 1
                resCp = recur(tempStr,tempStr) + 1
            else:
                res = recur(tempStr+buffer,buffer) + 1
            #print(res,resCp)
            return min(res,resCp)
           
        if n == 1:
            return 0
        return 1 + recur('A','A')