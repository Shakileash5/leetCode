class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sumOfDigits(digit):
            Sum = 0
            while(digit!=0):
                Sum+=digit%10
                digit/=10
            return Sum
        
        if n < 10:
            return n
        res = {}
        SumsIdx = set()
        for i in range(1,n+1):
            Sum = int(sumOfDigits(i))
            s=sum([int(k) for k in str(i)])
            if s in res:
                res[s].append(i)
                SumsIdx.add(i)
            else:
                res[s]=[i]
                
        resCounts = [len(i) for i in res.values()]
            
        return resCounts.count(max(resCounts))
                
            
        