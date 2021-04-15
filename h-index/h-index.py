class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        hashMap = {}
        size = len(citations)
        
        if size == 1:
            if citations[0]>=1:
                return 1
            return 0
        
        for i in range(size):
            hashMap[i] = citations[i]
        
        print(hashMap)
        for i in range(1,size+1):
            for item in hashMap:
                if hashMap[item]>=i:
                    tempIdx = size - item
                    print(tempIdx,i,item)
                    if i!=hashMap[item] and tempIdx>i:
                        break
                    if tempIdx == i:
                        print(i)
                        print(tempIdx,i,item)
                        return i
        return 0