class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashMap = {}
        stringList = s.split(" ")
        size = len(pattern)
        if len(stringList)<size:
            return False
        
        for i in range(size):
            if pattern[i] not in hashMap:
                if stringList[i] not in hashMap.values():
                    hashMap[pattern[i]] = stringList[i]
                else:
                    return False
            else:
                if hashMap[pattern[i]] !=  stringList[i]:
                    return False
        #print(i)
        if i == len(stringList)-1:
            return True
        
        return False