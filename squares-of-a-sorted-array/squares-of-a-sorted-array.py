import bisect
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        idx = bisect.bisect_right(nums,-1)
        res = []
        flag = False
        i = idx + 1
        print(idx)
        if nums[0] < 0:
            if idx<size and nums[idx]>=0:
                i = idx
                idx -= 1
                flag = True
            elif idx == size and nums[idx-1]<0:
                idx -= 1
                flag = False
                
            
        while(flag):
            print(idx,i)
            if abs(nums[idx])>nums[i]:
                #print(nums[i])
                res.append(nums[i]*nums[i])
                i += 1
                if i>=size:
                    break
            else:
                res.append(nums[idx]*nums[idx])
                idx -= 1
                if idx<0:
                    break
        if idx>-1:
            while(idx>=0):
                res.append(nums[idx]*nums[idx])
                idx -= 1
        if i<size:
            while(i<size):
                res.append(nums[i]*nums[i])
                i += 1
                
        return res