import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.heap1 = []
        self.heap2 = []

    def addNum(self, num: int) -> None:
        if len(self.heap1) == len(self.heap2):
            val = heapq.heappush(self.heap1,num)
            heapq.heappush(self.heap2,-1*heapq.heappop(self.heap1))
        else:
            val = heapq.heappush(self.heap2,-1*num)
            heapq.heappush(self.heap1,-1*heapq.heappop(self.heap2))
            
        return

    def findMedian(self) -> float:
        if len(self.heap1) == len(self.heap2):
            return -1*(-1*self.heap1[0] + self.heap2[0])/2.0
        
        return -1*self.heap2[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()