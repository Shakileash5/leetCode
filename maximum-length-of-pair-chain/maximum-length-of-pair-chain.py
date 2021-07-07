class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        size = len(pairs)
        
        pairs.sort(key=lambda x:x[1])
        print(pairs)
        max_ =  0
        dp = [None for i in range(size+1)]
        
        def recur(idx,lastPair):
            if idx>=size:
                return 0
            
            if dp[idx] == None:
                takePair = 0
                if lastPair == 0:
                    takePair = recur(idx+1,pairs[idx])+1
                    leavePair = recur(idx+1,lastPair)
                else:
                    if pairs[idx][0]>lastPair[1]:
                        takePair = recur(idx+1,pairs[idx])+1
                    leavePair = recur(idx+1,lastPair)
                dp[idx] = max(leavePair,takePair) 
                return dp[idx]
            else:
                return dp[idx]
                
        
        #print()
        return recur(0,0)