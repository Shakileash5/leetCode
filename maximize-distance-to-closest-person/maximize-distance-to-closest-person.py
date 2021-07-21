class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        size = len(seats)
        max_ = 0
        prev = None
        
        for i in range(size):
            if i == size-1:
                if seats[i] == 0:
                    max_ = max(max_,i-prev)
            if seats[i] == 1:
                if prev == None:
                    max_ = max(max_,i)
                else:
                    max_ = max(max_,(i-prev)//2)
                prev = i
        return max_