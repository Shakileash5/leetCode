class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashMap = {}
        
        for i in s:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        
        size = len(hashMap)
        count = 0
        #print(hashMap)
        for j in t:
            if j not in hashMap:
                return False
            else:
                hashMap[j] -= 1
                if hashMap[j] == 0:
                    count+=1
        #print(count)
        if count == size:
            return True
        
        return False