class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        windowSize = len(p)
        size = len(s)
        
        hashMap = {}
        for i in p:
            if i not in hashMap:
                hashMap[i] = [1,0]
            else:
                hashMap[i][0] +=1
                
        subStr = s[:windowSize]
        hashMapUtil = {}
        lst = []
        res = []
        idx = 0
        lst = list(p)
        tmp = sorted(subStr)
        #print(tmp)
        lst.sort()
        for i in tmp:
            if i in hashMap:
                hashMap[i][1]+=1
                #print(i,lst)
                if i in lst:
                    lst.remove(i)
                    
        print(lst,hashMap,"what")
        if lst == []:
            res.append(0)
        for i in range(1,size-windowSize+1):
            r = subStr[0]
            l = s[i+windowSize-1]
            subStr = subStr[1:]+l
            if r in hashMap:
                hashMap[r][1]-=1
                k = 0
                #print(hashMap[r][0]-hashMap[r][1],"index",r,l,hashMap[r])
                if k<(hashMap[r][0]-hashMap[r][1]):
                    lst.append(r)
                    k+=1
            if l in hashMap:
                hashMap[l][1]+=1
                #print(hashMap,lst,"here",l,subStr)
                if hashMap[l][0]>=hashMap[l][1]:
                    lst.remove(l)
                
            if lst == []:
                res.append(i)
            #print(lst,subStr,hashMap,r,l)
        
        return res