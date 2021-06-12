class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        size = len(nums)
        toChange = None
        prev = None
        '''prev = nums[0]
        for i in range(1,size):
            
            if nums[i-1]>nums[i]:
                #print(nums[i])
                if toChange == None:
                    toChange = nums[i]
                    if i>=2:
                        if i!= size-1 and nums[i]<prev:
                            if i+1 == size-1 or i+1<size:
                                if nums[i-1]>nums[i+1]:
                                    return False
                else:
                    print("second")
                    return False'''
        dipfixedonce=False
        for i in range(1,len(nums)):
                # pre1/pre2 will be wrong if depends on whether we remove index i or i-1 in our previous dip fix, but we won't need them if we found 2nd case of dip
                pre1,pre2=nums[i-1], nums[i-2] if i>=2 else -sys.maxsize-1
                if nums[i]<nums[i-1]:
                    if dipfixedonce or pre2>nums[i] and pre1>(nums[i+1] if i<len(nums)-1 else sys.maxsize):
                        return False
                    dipfixedonce=True
        return True