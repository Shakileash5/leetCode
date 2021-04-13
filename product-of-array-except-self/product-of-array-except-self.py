class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        totalProduct = 1
        flag = 0
        for i in nums:
            if  i == 0:
                flag += 1
                continue
            totalProduct *=i

        print(totalProduct,flag)
        for i in range(len(nums)):
            if flag>1:
                nums[i] = 0
            else:
                if nums[i] == 0:
                    if flag == len(nums):
                        nums[i] = 0
                    else:

                        nums[i] = totalProduct
                else:
                    if flag > 0:
                        nums[i] = 0
                    else:

                        nums[i] = totalProduct//nums[i]
        
        return nums