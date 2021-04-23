class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sumArr = [0]*(len(nums)+1)
        val = 0
        for i in range(len(nums)):
            self.update(i,nums[i],True)

    def update(self, index: int, val: int,init=False) -> None:
        #print(self.nums,index)
        if not init:
            # only update the difference  
            val, self.nums[index] = val - self.nums[index], val
            
        idx = index+1
        while(idx<=len(self.nums)):
            self.sumArr[idx]+=val
            idx = idx + (idx & (-idx))
        
    def getSum(self,index):
        idx = index+1
        sumVal = 0
        
        while(idx>0):
            sumVal += self.sumArr[idx]
            idx = idx - (idx&(-idx))
        return sumVal
    #print(self.sumArr)
    def sumRange(self, left: int, right: int) -> int:
        return self.getSum(right) - self.getSum(left-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)