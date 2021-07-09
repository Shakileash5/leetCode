class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        def getFib(x):
            res = [1,1]
            while(res[-1]<x):
                res.append(res[-1]+res[-2])
            return res
        
        fibs = getFib(k)
        size = len(fibs)
        #print(fibs)
        #dp = {}
        def recur(idx,sum_):
            if sum_ == k:
                return 0
            
            if idx>=size:
                #print("outOfBound")
                return float('inf')
            if (idx,sum_) not in dp:   
                pickEle = float('inf')
                if sum_+fibs[idx]<=k:
                    pickEle = recur(idx+1,sum_+fibs[idx]) + 1
                leaveEle = recur(idx+1,sum_)
                dp[(idx,sum_)] = min(pickEle,leaveEle)
            return dp[(idx,sum_)]
        
        #recur(0,0)
        count = 0
        idx = size-1
        while(k>0):
            if fibs[idx]<=k:
                k -= fibs[idx]
                count += 1
            idx -= 1
            
        return count 
        
        