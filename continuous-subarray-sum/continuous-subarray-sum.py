class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        size = len(nums)
        
        if size<2:
            return False
        
        left = 0
        right = 2
        prefixArr = set()
        sum_ = 0
        rem_ = 0
        for i in range(size):
            sum_ += nums[i]
            #print(sum_,sum_%k)
            rem = sum_%k
            if rem in prefixArr:
                return True
            prefixArr.add(rem_)
            rem_ = sum_%k
            #print(prefixArr)
        
        """sum_ = prefixArr[1]
        print(prefixArr)
        
        while(right<size):
            print(left,right,sum_)
            if sum_%k == 0:
                return True
            if sum_<k:
                sum_ = prefixArr[right] - prefixArr[left-1]
                right += 1
                
            elif sum_>k:
                sum_ -= prefixArr[left]
                left += 1
                if left-right<2:
                    sum_ = prefixArr[right] - prefixArr[left-1]
                    right += 1"""
        
        return False
                
            