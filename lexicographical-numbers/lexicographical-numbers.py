class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = list(range(1,n+1))
        #print(nums)
        nums.sort(key = lambda x: str(x))
        #print(nums)
        return nums