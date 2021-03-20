class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        size = len(s)
        #print(size)
        
        
        res = []
        
        def isValid(data):
            for i in data:
                #print(i)
                if i == '':
                    return False
                if 0<=int(i)<=255:
                    if len(i)>1 and i[0] == '0':
                        return False
                    flag = 1
                else:
                    return False
            return True
        
        if size == 12:
            if isValid([s[:3],s[3:6],s[6:9],s[9:]]):
                temp = s[:3]+"."+s[3:6]+'.'+ s[6:9]+'.'+s[9:]
                return [temp]
            return []
        
        def backtrack(temp,idx):
            
            if len(temp)==4:
                #print(temp,idx,isValid(temp))
                if idx<size:
                    return
                elif idx==size:
                    print(temp,isValid(temp),"here")
                    if isValid(temp):
                        res.append('.'.join(temp))
                    return
                else:
                    return
            
            for i in range(1,4):
                #print("temp",temp,idx,i)
                backtrack(temp+[s[idx:idx+i]],idx+i)
            
            return
        
        backtrack([],0)
        #print(res)
        
        return res