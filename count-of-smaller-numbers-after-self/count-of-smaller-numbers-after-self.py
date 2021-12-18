class Solution:
    
    def getInsertPos(self,arr,val):
        if arr == []:
            return 0
        left = 0
        right = len(arr) - 1
        
        while(left+1<right):
            mid = (left+right)//2
            if arr[mid] == val:
                right = mid
            if val > arr[mid]:
                left = mid
            else:
                right = mid
        if arr[right]<val:
            return right + 1
        if arr[left]<val:
            return left + 1
        return 0
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        stack = []
        size = len(nums)
        def getInsertPos(arr,target):
            if arr == []:
                return 0
            
            left = 0
            right = len(arr)-1
            while(left+1<right):
                mid = (left+right)//2
                if arr[mid] == target:
                    right = mid
                if arr[mid]<target:
                    left = mid
                else:
                    right = mid
            
            if arr[right]<target:
                return right + 1
            if arr[left]<target:
                return left + 1
            return 0
        
        for i in range(size-1,-1,-1):
            pos = self.getInsertPos(stack,nums[i])
            res.append(pos)
            stack.insert(pos,nums[i])
            #print(nums[i],pos,stack)
        return res[::-1]