class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        size = len(nums)
        min_ = float('inf')
        queue = collections.deque() 
        low = 0
        high = 0
        sum_ = 0
        
        for high in range(size):
            sum_ += nums[high]
            
            if sum_>=k:
                min_ = min(min_,high+1)
            
            while queue and sum_ - queue[0][0]>=k:
                min_ = min(min_,high-queue.popleft()[1])
            while queue and queue[-1][0]>sum_:
                queue.pop()
            queue.append((sum_,high))
            
        return min_ if min_!= float('inf') else -1
                 