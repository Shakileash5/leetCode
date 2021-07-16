class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        size = len(nums)
        max_ = 0
        min_ = 0
        
        def divideAndConquer(left,right):
            if left == right:
                return nums[left],nums[left]
            if right == left + 1:
                return (max(nums[left],nums[right]),min(nums[left],nums[right]))
            mid = (left+right)//2
            max1,min1 = divideAndConquer(left,mid)
            max2,min2 = divideAndConquer(mid+1,right)
            
            return max(max1,max2),min(min1,min2)
        
        max_,min_ = divideAndConquer(0,size-1)
        if (min_+k)>(max_-k):
            return 0
        return (max_-k) - (min_+k)