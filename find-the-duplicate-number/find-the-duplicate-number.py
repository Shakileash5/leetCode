class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        #summation = ((size-1)*size)//2
        #print(summation)
        #arrSum = sum(nums)
        #res = arrSum - summation
        
        nums.sort()
        left = 0
        right = 0
        
        while(left<=right):
            if right >= size:
                break
            count = 0
            while(right<size and nums[left] == nums[right]):
                right+=1
                count+=1
            
            if count>=2 :
                return nums[left]
            left = right
        
        return -1