class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        size = len(arr)
        memo = {}
        
        def recur(idx,tempArr):
            if idx>=size:
                #print(tempArr)
                return 0
            if len(tempArr)<2 or (idx,tempArr[-1],tempArr[-2]) not in memo:
                last = None
                lastBefore = None
                if len(tempArr)<2:
                    res = max(recur(idx+1,tempArr+[arr[idx]])+1,recur(idx+1,tempArr))
                    if tempArr==[]:
                        last = None
                    else:
                        last = tempArr[-1]
                else:
                    last = tempArr[-1]
                    lastBefore = tempArr[-2]
                    if tempArr[-1] + tempArr[-2] == arr[idx]:
                        res = max(recur(idx+1,tempArr+[arr[idx]])+1,recur(idx+1,tempArr))
                    else:
                        res = recur(idx+1,tempArr)

                memo[(idx,last,lastBefore)] = res
                return res
            else:
                if tempArr!=[]:
                        if len(tempArr)>=2:
                            last = tempArr[-1]
                            lastBefore = tempArr[-2]
                        else:
                            last = tempArr[-1]
                            lastBefore = None
                else:
                        last = None
                        lastBefore = None
                return memo[(idx,last,lastBefore)]
        #res = recur(0,[])
        #if res <= 2:
        #    return 0
        #return res
        
        def binarySearch(arr,size):
            max_ = 0
            for i in range(size):
                for j in range(i+1,size):
                    a = arr[i]
                    b = arr[j]
                    c = a + b
                    
                    idx = bisect.bisect_left(arr,c)
                    if idx >= size or arr[idx] != c:
                        continue
                    a = b
                    b = c
                    count = 3
                    while(True):
                        c = a + b
                        idx = bisect.bisect_left(arr,c)
                        if idx >= size or arr[idx] != c:
                            break
                        count += 1
                        a = b
                        b = c
                    max_ = max(max_,count)
            return max_
                    
        return binarySearch(arr,size)
        
        
                
                    