import heapq
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        size = len(nums)
        @cache
        def recur(idx):
            if idx >= size-1:
                #print("fe")
                if idx == size-1:
                    return nums[idx]
                else:
                    return -1
            max_ = float('-inf')
            for i in range(1,k+1):
                if idx+i <= size-1:
                    res = recur(idx+i)+nums[idx]
                    #if res >-1:
                    max_ = max(max_,res)
            return max_
        
        if len(nums) == 1:
            return nums[0]
        heap = []
        # remember heap in python is min heap, so you have to turn the number in nums to negative number so the current largest number will be put on the top of the heap, and you can use heap[0] to achieve it.
        heapq.heappush(heap, (-nums[0], 0))
        for i in range(1, len(nums) - 1):
            # remove the maximun number which not matches the requirement(before i - k)
            while heap[0][1] < i - k:
                heapq.heappop(heap)
            # the reason why I use - heap[0][0] is , we already turn nums[t] into negative number when we count the max jump in step i - k to i - 1 in the previous steps, so we should turn it to positive right now.
            # them we turn the sum of nums[i] and max(step i - k, step i - 1) to negative again ,and push into heap
            heapq.heappush(heap, (- (nums[i] - heap[0][0]), i))
        # do not forget the last element
        if heap[0][1] < len(nums) - 1 - k:
            heapq.heappop(heap)
        #return recur(0)
        return - heap[0][0] + nums[-1]
        