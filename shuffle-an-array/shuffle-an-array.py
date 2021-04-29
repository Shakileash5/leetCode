import random
class Solution:

    def __init__(self, nums: List[int]):
        self.orginalArr = nums
        self.shifted = nums
        self.size = len(nums)
        
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.orginalArr

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        arr = self.orginalArr.copy()
        for i in range(self.size-1):
            idx = random.randint(i,self.size-1)
            arr[i],arr[idx] = arr[idx],arr[i]
        return arr
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()