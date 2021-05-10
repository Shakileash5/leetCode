class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        monotoneStack = []
        res = []
        size = len(T)
        
        for i in range(size-1,-1,-1):
            
            while monotoneStack and T[monotoneStack[-1]]<=T[i]:
                idx = monotoneStack.pop()
                #print(monotoneStack,"afterPop")
            if monotoneStack:
                res.insert(0,monotoneStack[-1]-i)
            else:
                res.insert(0,0)
            monotoneStack.append(i)
            #print(T[i],"val",monotoneStack,res)
            
        return res