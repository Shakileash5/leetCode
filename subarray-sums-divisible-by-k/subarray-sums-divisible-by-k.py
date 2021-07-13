class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        count = 0
        hashmap = {0:1}
        sum_ = 0
        
        for i in range(len(A)):
            sum_ += A[i]
            rem = sum_ % K
            
            if rem < 0:
                rem += K
            
            if rem in hashmap:
                count += hashmap[rem]
                hashmap[rem] += 1
            else:
                hashmap[rem] = 1
        
        return count