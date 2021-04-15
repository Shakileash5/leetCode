class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        actualSum = (size*(size+1))//2
        arrSum = sum(nums)
        num = actualSum - arrSum
        return num