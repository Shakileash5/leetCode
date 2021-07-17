class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        size = len(costs)
        costs.sort(key=lambda x: x[1]-x[0])
        res = 0
        #print(costs)
        for i in range(size//2):
            res += costs[i][1]
        for j in range(size//2,size):
            res += costs[j][0]
        return res