class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = {}
        for i,char in enumerate(s):
            if char not in hashMap.keys():
                hashMap[char] = [1,i]
            else:
                hashMap[char][0]+=1
        
        for key in hashMap.keys():
            if hashMap[key][0] == 1:
                return hashMap[key][1]
        
        return -1
        