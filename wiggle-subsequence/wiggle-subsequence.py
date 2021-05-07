class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        size = len(nums)
        res = 1
        val = nums[0]
        turn = -1
        for i in range(1,size):
            if turn==1:
                if val<nums[i]:
                    turn = 0
                    res+=1
            elif turn==0 :
                if val>nums[i]:
                    turn = 1
                    res+=1 
            else:
                if nums[i]>val:
                    turn = 0
                    res+=1
                elif nums[i]<val:
                    turn = 1
                    res+=1
            val = nums[i]
        return res
                
                