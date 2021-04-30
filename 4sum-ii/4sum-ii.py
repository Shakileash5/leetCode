class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = set()
        hashTable = {}
        count = 0
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                pairSum = nums1[i] + nums2[j]
                hashTable[pairSum] = hashTable.get(pairSum,0) + 1
        
        for i in range(n):
            for j in range(n):
                if 0 - (nums3[i]+nums4[j]) in hashTable:
                    count+=hashTable[0 - (nums3[i]+nums4[j])]
                    
        
        return count
                            