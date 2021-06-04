class Solution:
    def productExceptSelfTwo(self,nums):
        product = 1
        zeroFlag = 0
        multipleZeros = 0
        size = len(nums)
        res = []
        
        for i in range(size):
            if nums[i] == 0:
                if zeroFlag == 1:
                    multipleZeros = 1
                zeroFlag = 1
                continue
            product *= nums[i]
        
        for i in range(size):
            if multipleZeros:
                res.append(0)
            else:
                if nums[i] == 0:
                    res.append(product)
                elif zeroFlag == 1:
                    res.append(0)
                else:
                    res.append(product//nums[i])
        
        return res
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        def solutionOne():
            totalProduct = 1
            flag = 0
            for i in nums:
                if  i == 0:
                    flag += 1
                    continue
                totalProduct *=i

            #print(totalProduct,flag)
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
        
        return self.productExceptSelfTwo(nums)