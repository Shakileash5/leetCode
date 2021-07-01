class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        if desiredTotal <= maxChoosableInteger :
            return True
        
        integerList = [x+1 for x in range(maxChoosableInteger)]
        
        @cache
        def recur(integerList,sum_,turn):
            integerList = list(integerList)
            if sum_<=0:
                if sum_ == 0 and turn%2==1:
                    return True
                return False
            val = sum_
            if val in integerList:
                integerList.remove(val)
                if recur(tuple(integerList),sum_-val,turn+1):
                    return True
                integerList.append(val)
                return False
            
            for i in integerList:
                integerList.remove(i)
                if recur(tuple(integerList),sum_-i,turn+1):
                    return True
                integerList.insert(0,i)
            return False
        
        @lru_cache(None)
        def pick(num, left):
            for i, n in enumerate(num):
                # either i win now or another player lose in next turn
                if n>=left or not pick(num[:i] + num[i+1:], left-n):
                    return True
            return False
        
        #
        if maxChoosableInteger*(maxChoosableInteger+1)/2 < desiredTotal:
            return False
        #return recur(tuple(integerList),desiredTotal,0)
        return pick(tuple([i for i in range(1, maxChoosableInteger+1)]), desiredTotal)
                
            