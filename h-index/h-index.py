class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        hashMap = {}
        size = len(citations)
        
        
        for i in range(size):
            hashMap[i] = citations[i]
        
        #print(hashMap)
        """for i in range(1,size+1):
            for item in hashMap:
                if hashMap[item]>=i:
                    tempIdx = size - item
                    print(tempIdx,i,item)
                    if i!=hashMap[item] and tempIdx>i:
                        break
                    if tempIdx == i:
                        print(i)
                        print(tempIdx,i,item)
                        return i"""
        left = 0
        right = size 
        
        while(left<right):
            mid = (left+right) // 2
            
            if citations[mid] >= size - mid:
                right = mid
            else:
                left = mid + 1
            
        
        return size - left