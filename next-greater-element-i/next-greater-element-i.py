class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        size1 = len(nums1)
        size2 = len(nums2)
        
        stack  = []
        hashMap = {}
        res = []
        
        for i in range(size2-1,-1,-1):
            
            while stack and stack[-1]<=nums2[i]:
                ele = stack.pop()
                
            hashMap[nums2[i]] = [i,stack[-1] if stack else -1]
            stack.append(nums2[i])
            
        print(stack)
        for i in range(size1):
            res.append(hashMap[nums1[i]][1])    
            
            
        return res