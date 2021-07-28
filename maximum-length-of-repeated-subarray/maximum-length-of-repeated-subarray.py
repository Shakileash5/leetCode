class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        size1 = len(nums1)
        size2 = len(nums2)
        max_ = 0
        dp = [[0 for j in range(size2+1)] for i in range(size1+1)]
        
        for i in range(1,size1+1):
            for j in range(1,size2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
            max_ = max(max_,max(dp[i]))
        return max_