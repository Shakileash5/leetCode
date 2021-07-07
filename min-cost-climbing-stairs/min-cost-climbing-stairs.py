class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        
        @cache
        def recur(idx):
            if idx>=size:
                return 0
            stepOne = recur(idx+1) 
            stepTwo = recur(idx+2)
            return min(stepOne,stepTwo) + cost[idx]
        
        return min(recur(0),recur(1))