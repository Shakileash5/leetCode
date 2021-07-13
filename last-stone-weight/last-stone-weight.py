import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #heapq.heapify(stones)
        if len(stones)<=1:
            return stones[0]
        
        arr = []
        for i in range(len(stones)):
            heapq.heappush(arr,-1*stones[i])
        
        while(True):
            if len(arr)>=2:
                heavyStone = -1*heapq.heappop(arr)
                secondHeavyStone = -1*heapq.heappop(arr)
                if heavyStone != secondHeavyStone:
                    heavyStone = heavyStone - secondHeavyStone
                    heapq.heappush(arr,-1*heavyStone)
            if len(arr) == 1:
                return -1*arr[0]
            if len(arr) == 0:
                break
        return 0
            