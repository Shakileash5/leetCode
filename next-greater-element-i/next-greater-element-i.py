class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        size1 = len(nums1)
        size2 = len(nums2)
        
        stack = []
        hashMap = {}
        res = []
        
        for i in range(size2-1,-1,-1):
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            if stack:
                hashMap[nums2[i]] = stack[-1]
            else:
                hashMap[nums2[i]] = -1 
            stack.append(nums2[i])
        
        for i in range(size1):
            res.append(hashMap[nums1[i]])
        
        return res
            
            