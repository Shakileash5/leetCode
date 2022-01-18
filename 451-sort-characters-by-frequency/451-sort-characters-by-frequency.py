class Solution:
    

    def frequencySort(self, s: str) -> str:
        hashMap = {}
        size = len(s)
        
        for i in range(size):
            if s[i] not in hashMap:
                hashMap[s[i]] = 1
            else:
                hashMap[s[i]] += 1
        
        resList = list(hashMap.items())
        def compare(e):
            return (e[1],e[0])
        resList = sorted(resList, key=compare,reverse=True)
        res = ""
        
        for i in range(len(resList)):
            res += resList[i][0]*resList[i][1]
        
        return res