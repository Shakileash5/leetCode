class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        hashMap = {}
        size = len(candyType)
        count = 0
        
        for i in range(size):
            if candyType[i] not in hashMap:
                hashMap[candyType[i]] = 1
                count += 1
            else:
                hashMap[candyType[i]] += 1
        
        can = size // 2
        if count>=can:
            return can
        else:
            return count
            