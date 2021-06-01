class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        hashMap = {}
        res = []
    
        for name in names:
            
            if name not in hashMap:
                hashMap[name] = 1
                res.append(name)
            else:
                val = str(hashMap[name])
                nameChange = name + '('+val+')'
                #print(hashMap)
                val = int(val)
                while nameChange in hashMap:
                    val+=1
                    nameChange = name + '('+str(val)+')'
                
                hashMap[name]+=abs(hashMap[name]-val)
                hashMap[nameChange] = 1
                #print(hashMap)
                res.append(nameChange)
        
        return res