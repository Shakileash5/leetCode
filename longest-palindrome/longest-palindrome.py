class Solution:
    def longestPalindrome(self, s: str) -> int:
        size = len(s)
        hashMap = {}
        oddCount = 0
        evenCount = 0
        
        for i in range(size):
            if s[i] not in hashMap:
                hashMap[s[i]] = 1
                oddCount += 1
            else:
                if hashMap[s[i]]%2 == 0:
                    oddCount += 1
                else:
                    oddCount -= 1
                
                hashMap[s[i]] += 1
        
        #print(oddCount)
        if oddCount > 0:
            return size - oddCount + 1
        return size