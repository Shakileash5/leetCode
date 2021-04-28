class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {}
        sizeNum1 = len(nums1)
        sizeNum2 = len(nums2)
        res = []
        
        for i in range(sizeNum1):
            
            hashMap[nums1[i]] = 1
        
        keys = hashMap.keys()
        
        for j in range(sizeNum2):
            if nums2[j] in keys and nums2[j] not in res:
                res.append(nums2[j])
        
        return res