class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        size = len(nums)
        prefixSum = []
        prefixSumRev = []
        sum_ = 0
        if size == 1:
            return 0
        
        for i in range(size):
            sum_ += nums[i]
            prefixSum.append(sum_)
        
        sum_ = 0
        
        for i in range(size-1,-1,-1):
            sum_ += nums[i]
            prefixSumRev.append(sum_)
        
        #print(prefixSum,prefixSumRev[::-1])
        prefixSumRev = prefixSumRev[::-1]
        
        for i in range(size):
            if i == 0:
                if i+1<size and prefixSumRev[i+1] == 0:
                    return i
            if i == size-1:
                if i-1>=0 and prefixSum[i-1] == 0:
                    return  i
            
            if i-1>=0 and i+1<size and prefixSum[i-1] == prefixSumRev[i+1]:
                return i
        
        return -1
        
        