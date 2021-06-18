class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<3:
            return nums[-1]
        else:
            val = None
            count = 0
            for i in range(len(nums)-1,-1,-1):
                if val == None:
                    val = nums[i]
                    count += 1
                elif val != nums[i]:
                    val = nums[i]
                    count += 1
                if count == 3:
                    return nums[i]
            return nums[-1]