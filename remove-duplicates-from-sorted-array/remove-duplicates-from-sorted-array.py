class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count = 0
        size = len(nums)
        index = 0
        idx = 1
        
        while(idx<len(nums)):
            flag = 0
            while idx<len(nums) and nums[idx] == nums[idx-1]:
                flag = 1
                del nums[idx]
                
            if flag == 0:
                idx+=1
        
        
        
        
        
        """while(index<len(nums)):         
                if(index+1 <len(nums) and nums[index] == nums[index+1]):
                    idt = index
                    while(idt+1 <len(nums) and nums[idt] == nums[idt+1]):
                        del nums[idt]

                index+=1
                idt=0"""
        return len(nums)