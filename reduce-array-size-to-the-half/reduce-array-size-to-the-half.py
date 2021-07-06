import heapq

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        size = len(arr)
        heapArr = []
        hashMap = {}
        for i in range(size):
            if arr[i] not in hashMap:
                hashMap[arr[i]] = 1
            else:
                hashMap[arr[i]] += 1
        
        #print(hashMap)
        for key in hashMap:
            heapq.heappush(heapArr,-1*hashMap[key])
        
        k = 0
        count = 0
        #print(size//2)
        #print(heapArr)
        while k<(size//2):
            k += -1*heapq.heappop(heapArr)
            count += 1
            #print(k)
        #heapq.heapify(heapArr)
        #print(heapArr,k)
        
        return count