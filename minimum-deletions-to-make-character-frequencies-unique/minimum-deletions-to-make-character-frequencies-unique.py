class Solution:
    def minDeletions(self, s: str) -> int:
        size = len(s)
        hashMap = {}
        hashMapFreq = {}
        
        for i in range(size):
            if s[i] not in hashMap:
                hashMap[s[i]] = 1
            else:
                hashMap[s[i]] += 1
            
        for key in hashMap:
            if hashMap[key] not in hashMapFreq:
                hashMapFreq[hashMap[key]] = [key]
            else:
                hashMapFreq[hashMap[key]].append(key)
        
        #print(hashMap,hashMapFreq)
        count = 0
        idxKey = 0
        keys = list(hashMapFreq.keys())
        sizeKey = len(keys)
        while (idxKey<sizeKey):
            idx = 0
            key = keys[idxKey]
            values = hashMapFreq[key]
            #print(key,values)
            if len(values)>1:
                sizeVal = len(values)
                while(idx<sizeVal):
                    values.pop(0) 
                    val = key
                    while(val in hashMapFreq):
                        val = val - 1
                        count += 1
                    if val != 0:
                        hashMapFreq[val] = [1]
                    sizeVal -= 1
                    #idx+=1
                    #print(values)
                    if sizeVal == 1:
                        #print("he")
                        break
            idxKey += 1
        
        #print(count)
        return count
                