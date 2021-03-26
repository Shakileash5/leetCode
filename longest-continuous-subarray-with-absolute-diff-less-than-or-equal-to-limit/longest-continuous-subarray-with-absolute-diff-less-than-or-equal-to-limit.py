class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        output = []
        lengthRes = []
        maxLength = -1
        def absPairs(arr, n):
            if abs(min(arr)-max(arr))<=limit:
                return True
            return False
                
        for i in range(len(nums)):
                   #if abs(nums[i]-nums[i]) <= limit:
            arr = []
            arr.append(nums[i])
            output.append(arr[:])
            sizeArr = len(arr)
            lengthRes.append(sizeArr)
            if maxLength<sizeArr:
                maxLength = sizeArr
                        #print(arr)
            for j in range(i+1,len(nums)):
                            
                temp = arr[:]
                temp.append(nums[j])
                            #print("abs",absPairs(arr,len(arr)),arr)
                if absPairs(temp,len(temp)) == False:
                    break
                else:
                    arr.append(nums[j])
                        #print(arr)
            output.append(arr)
            sizeArr = len(arr)
            lengthRes.append(sizeArr)
            if maxLength<sizeArr:
                maxLength = sizeArr'''
        #print(output)
        #length = [ len(i) for i in output ]
        #print(length,lengthRes)
        minq, maxq = deque(), deque()
        i = 0
        res = 0
        for j, n in enumerate(nums):
            while minq and minq[-1] > n: minq.pop()
            while maxq and maxq[-1] < n: maxq.pop()
            minq.append(n)
            maxq.append(n)
            
            while i<len(nums) and minq and maxq and maxq[0]-minq[0] > limit:
                if maxq[0] == nums[i]: maxq.popleft()
                if minq[0] == nums[i]: minq.popleft()
                res = max(res, j-i)
                i+=1
        return max(res, len(nums)-i)
 