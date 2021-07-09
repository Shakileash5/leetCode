class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        size = len(nums)
        oddList = []
        evenList = []
        
        for i in range(size):
            if i%2 == 0:
                if nums[i]%2 != 0:
                    evenList.append(i)
            else:
                if nums[i]%2 == 0:
                    oddList.append(i)
        #print(evenList,oddList)
        while(evenList):
            evenIdx = evenList.pop(0)
            oddIdx = oddList.pop(0)
            nums[evenIdx],nums[oddIdx] = nums[oddIdx],nums[evenIdx]
            
        return nums