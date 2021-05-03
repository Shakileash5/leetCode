import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        maxHeap = []
        size1 = len(nums1)
        size2 = len(nums2)
        
        for i in range(size1):
            for j in range(size2):
                val = nums1[i] + nums2[j]
                if len(maxHeap)<k:
                    heapq.heappush(maxHeap,(-val,nums1[i],nums2[j]))
                else:
                    top = maxHeap[0]
                    if -top[0]>=val:
                        #maxHeap[0] = (-val,nums1[i],nums2[j])
                        #heapq.heapify(maxHeap)
                        heapq.heappop(maxHeap)
                        heapq.heappush(maxHeap,(-val,nums1[i],nums2[j]))
        #print(maxHeap)
        res = []
        for sumVal,val1,val2 in maxHeap:
            res.append([val1,val2])
        return res